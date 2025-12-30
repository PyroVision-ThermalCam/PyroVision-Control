#!/usr/bin/env python3

# You need to run the following command to generate the UI and ressources files
#   pyside6-uic ui/mainwindow.ui -o generated/ui_mainwindow.py
#   pyside6-rcc ressources.qrc -o ressources_rc.py

"""
PyroVision GUI Application
Qt6/PySide6 graphical interface for ESP32 Thermal Camera control

Copyright (C) 2026
This file is part of PyroVision.

PyroVision is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

PyroVision is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with PyroVision. If not, see <https://www.gnu.org/licenses/>.
"""

import sys
import asyncio
import websockets

from pathlib import Path
from typing import Optional
from datetime import datetime

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PySide6.QtCore import Qt, QThread, Signal
from PySide6.QtGui import QPixmap, QIcon
from qasync import QEventLoop

from PyroVision import PyroVisionClient, TelemetryData
from generated.ui_mainwindow import Ui_MainWindow
from style import STYLESHEET

class ImageStreamThread(QThread):
    """Thread for WebSocket image streaming"""

    Signal_FrameReceived = Signal(bytes)
    Signal_ErrorOccurred = Signal(str)
    Signal_StreamStopped = Signal()

    def __init__(self, host: str, port: int, api_key: Optional[str], fps: int = 8):
        super().__init__()
        self._host = host
        self._port = port
        self._api_key = api_key
        self._fps = fps
        self._running = False

    def run(self):
        """Run the image stream"""

        self._running = True
        try:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(self._stream_images())
            loop.close()
        except Exception as e:
            self.Signal_ErrorOccurred.emit(str(e))
        finally:
            self.Signal_StreamStopped.emit()

    async def _stream_images(self):
        """Internal async image streaming"""

        client = PyroVisionClient(self._host, self._port, self._api_key)

        try:
            await client.connect()

            # Send stream start command
            await client.send_command("start", {
                "fps": self._fps
            })

            # Read stream frames
            async for message in client.connection:
                if(not(self._running)):
                    break

                if(isinstance(message, bytes)):
                    self.Signal_FrameReceived.emit(message)
        except websockets.exceptions.ConnectionClosed as e:
            if(self._running):
                self.Signal_ErrorOccurred.emit(f"Connection closed: {e}")
        except Exception as e:
            if(self._running):
                self.Signal_ErrorOccurred.emit(f"Stream error: {e}")
        finally:
            try:
                await client.send_command("stop", {})
            except:
                pass
            try:
                await client.disconnect()
            except:
                pass

    def stop(self):
        """Stop the stream"""

        self.running = False

class TelemetryThread(QThread):
    """Thread for telemetry updates"""

    telemetry_received = Signal(dict)
    error_occurred = Signal(str)

    def __init__(self, client: PyroVisionClient):
        super().__init__()
        self.client = client
        self.running = False

    def run(self):
        """Run telemetry polling"""
        self.running = True
        while(self.running):
            try:
                telemetry = self.client.get_telemetry()
                self.telemetry_received.emit({
                    "uptime_s": telemetry.uptime_s,
                    "sensor_temp_c": telemetry.sensor_temp_c,
                    "core_temp_c": telemetry.core_temp_c,
                    "supply_voltage_v": telemetry.supply_voltage_v,
                    "wifi_rssi_dbm": telemetry.wifi_rssi_dbm,
                    "sdcard_present": telemetry.sdcard_present,
                    "sdcard_free_mb": telemetry.sdcard_free_mb
                })
            except Exception as e:
                self.error_occurred.emit(str(e))

            self.msleep(1000)

    def stop(self):
        """Stop telemetry polling"""

        self.running = False

class ThermalCameraGUI(QMainWindow):
    """Main GUI window for Thermal Camera control"""

    def __init__(self):
        super().__init__()
        self.client: Optional[PyroVisionClient] = None
        self.stream_thread: Optional[ImageStreamThread] = None
        self.telemetry_thread: Optional[TelemetryThread] = None
        self.is_streaming = False
        self.frame_counter = 0

        self.ui = Ui_MainWindow()

        icon_path = Path(__file__).parent / "ressources" / "Logo_Alpha.png"
        if(icon_path.exists()):
            self.setWindowIcon(QIcon(str(icon_path)))

        self.ui.setupUi(self)

        self.setStyleSheet(STYLESHEET)

        self.ui.connectButton.clicked.connect(self._on_Connect_Clicked)
        self.ui.streamButton.clicked.connect(self._on_Stream_Clicked)
        self.ui.snapshotButton.clicked.connect(self._on_Save_Snapshot)
        self.ui.captureButton.clicked.connect(self._on_Capture_Clicked)
        self.ui.refreshButton.clicked.connect(self._on_RefreshTelemetry)
        self.ui.brightnessSlider.valueChanged.connect(
            lambda v: self.ui.brightnessValueLabel.setText(str(v))
        )
        self.ui.syncTimeButton.clicked.connect(self._on_SyncTime)
        self.ui.uploadFirmwareButton.clicked.connect(self._on_UploadFirmware)
        self.ui.clearLogButton.clicked.connect(self.ui.logText.clear)

        self.statusBar().showMessage("Disconnected")

    def Slot_StreamStopped(self):
        """Handle stream stopped event"""

        self.is_streaming = False
        self.ui.streamButton.setText("Start Stream")
        self.ui.snapshotButton.setEnabled(False)
        self.log("Stopped video stream")

    def Slot_DisplayFrame(self, frame_data: bytes):
        """Display a frame in the image label"""

        pixmap = QPixmap()
        pixmap.loadFromData(frame_data)

        if(not(pixmap.isNull())):
            scaled_pixmap = pixmap.scaled(
                self.ui.imageLabel.size(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
            self.ui.imageLabel.setPixmap(scaled_pixmap)

            self.frame_counter += 1
            self.ui.frameCounterLabel.setText(f"Frames: {self.frame_counter}")

    def Slot_StreamError(self, error: str):
        """Handle stream error"""

        self.log(f"Stream error: {error}")
        QMessageBox.warning(self, "Stream Error", error)

    def _on_Connect_Clicked(self):
        """Toggle connection to the device"""

        if(not self.client):
            ip = self.ui.ipInput.text()
            port = self.ui.portInput.value()
            api_key = self.ui.apiKeyInput.text() or None

            try:
                self.client = PyroVisionClient(ip, port, api_key)

                self.client.get_telemetry()

                self.ui.connectButton.setText("Disconnect")
                self.statusBar().showMessage(f"Connected to {ip}:{port}")
                self.log(f"Connected to {ip}:{port}")

                # Enable buttons
                self._EnableControls(True)

            except Exception as e:
                QMessageBox.critical(self, "Connection Error", str(e))
                self.client = None
                self.log(f"Connection failed: {e}")
        else:
            if(self.is_streaming):
                self._on_Stream_Clicked()

            if(self.telemetry_thread and self.telemetry_thread.isRunning()):
                self.toggle_auto_refresh(Qt.Unchecked)

            self.client = None
            self.ui.connectButton.setText("Connect")
            self.statusBar().showMessage("Disconnected")
            self.log("Disconnected")

            self._EnableControls(False)

    def _EnableControls(self, enabled: bool):
        """Enable or disable control buttons"""

        self.ui.streamButton.setEnabled(enabled)
        self.ui.captureButton.setEnabled(enabled)
        self.ui.saveToSdButton.setEnabled(enabled)
        self.ui.refreshButton.setEnabled(enabled)
        self.ui.syncTimeButton.setEnabled(enabled)
        self.ui.uploadFirmwareButton.setEnabled(enabled and bool(self.ui.firmwarePathInput.text()))

    def _on_Stream_Clicked(self):
        """Toggle video stream"""

        if(not self.is_streaming):
            self.log("Start video stream")

            fps = self.ui.fpsSpinbox.value()
            ip = self.ui.ipInput.text()
            port = self.ui.portInput.value()
            api_key = self.ui.apiKeyInput.text() or None
            
            self.stream_thread = ImageStreamThread(ip, port, api_key, fps)
            self.stream_thread.Signal_FrameReceived.connect(self.Slot_DisplayFrame)
            self.stream_thread.Signal_ErrorOccurred.connect(self.Slot_StreamError)
            self.stream_thread.Signal_StreamStopped.connect(self.Slot_StreamStopped)
            self.stream_thread.start()

            self.is_streaming = True
            self.ui.streamButton.setText("Stop Stream")
            self.ui.snapshotButton.setEnabled(True)
            self.frame_counter = 0
        else:
            self.log("Stop video stream")

            if(self.stream_thread):
                self.stream_thread.stop()
                self.stream_thread.wait(3000)

                # Disconnect all signals to prevent memory leaks
                try:
                    self.stream_thread.Signal_FrameReceived.disconnect()
                    self.stream_thread.Signal_ErrorOccurred.disconnect()
                    self.stream_thread.Signal_StreamStopped.disconnect()
                except:
                    pass

                self.stream_thread = None

    def _on_Save_Snapshot(self):
        """Save current frame as snapshot"""

        pixmap = self.ui.imageLabel.pixmap()
        if(pixmap):
            filename, _ = QFileDialog.getSaveFileName(
                self,
                "Save Snapshot",
                f"snapshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg",
                "JPEG Image (*.jpg);;PNG Image (*.png)"
            )

            if(filename):
                if(pixmap.save(filename)):
                    self.log(f"Saved snapshot: {filename}")
                    QMessageBox.information(self, "Success", "Snapshot saved successfully")
                else:
                    QMessageBox.critical(self, "Error", "Failed to save snapshot")

    def _on_Capture_Clicked(self):
        """Capture a single image"""

        if(not self.client):
            return

        try:
            format_type = self.ui.formatCombo.currentText()
            palette = self.ui.paletteCombo.currentText()
            scale = self.ui.scaleCombo.currentText()

            image_data = self.client.get_image(format_type, palette, scale)

            pixmap = QPixmap()
            pixmap.loadFromData(image_data)

            if(not pixmap.isNull()):
                scaled_pixmap = pixmap.scaled(
                    self.ui.capturedImageLabel.size(),
                    Qt.KeepAspectRatio,
                    Qt.SmoothTransformation
                )

                self.ui.capturedImageLabel.setPixmap(scaled_pixmap)
                self.log(f"Captured image ({format_type}, {palette}, {scale})")
            else:
                QMessageBox.warning(self, "Error", "Failed to decode image")

        except Exception as e:
            QMessageBox.critical(self, "Capture Error", str(e))
            self.log(f"Capture error: {e}")

    def _on_ToggleAutoRefresh(self, state):
        """Toggle automatic telemetry refresh"""

        if(state == Qt.Checked):
            if(not self.client):
                self.ui.autoRefreshCheckbox.setChecked(False)
                return

            self.telemetry_thread = TelemetryThread(self.client)
            self.telemetry_thread.telemetry_received.connect(self._on_UpdateTelemetry)
            self.telemetry_thread.error_occurred.connect(self._on_HandleTelemetryError)
            self.telemetry_thread.start()
            self.log("Started auto-refresh telemetry")
        else:
            if self.telemetry_thread and self.telemetry_thread.isRunning():
                self.telemetry_thread.stop()
                self.telemetry_thread.wait()
                self.log("Stopped auto-refresh telemetry")

    def _on_RefreshTelemetry(self):
        """Refresh telemetry once"""

        if(not self.client):
            return

        try:
            telemetry = self.client.get_telemetry()
            self.update_telemetry({
                "uptime_s": telemetry.uptime_s,
                "sensor_temp_c": telemetry.sensor_temp_c,
                "core_temp_c": telemetry.core_temp_c,
                "supply_voltage_v": telemetry.supply_voltage_v,
                "wifi_rssi_dbm": telemetry.wifi_rssi_dbm,
                "sdcard_present": telemetry.sdcard_present,
                "sdcard_free_mb": telemetry.sdcard_free_mb
            })
            self.log("Telemetry refreshed")
        except Exception as e:
            QMessageBox.critical(self, "Telemetry Error", str(e))
            self.log(f"Telemetry error: {e}")

    def _on_UpdateTelemetry(self, data: dict):
        """Update telemetry display"""

        hours = data["uptime_s"] // 3600
        minutes = (data["uptime_s"] % 3600) // 60
        seconds = data["uptime_s"] % 60
        self.ui.uptimeLabel.setText(f"Uptime: {hours}h {minutes}m {seconds}s")

        self.ui.sensorTempLabel.setText(f"Sensor Temperature: {data['sensor_temp_c']:.1f} °C")
        self.ui.coreTempLabel.setText(f"Core Temperature: {data['core_temp_c']:.1f} °C")
        self.ui.voltageLabel.setText(f"Supply Voltage: {data['supply_voltage_v']:.2f} V")
        self.ui.rssiLabel.setText(f"WiFi RSSI: {data['wifi_rssi_dbm']} dBm")

        if(data["sdcard_present"]):
            self.ui.sdCardLabel.setText(f"SD Card: Present ({data['sdcard_free_mb']} MB free)")
        else:
            self.ui.sdCardLabel.setText("SD Card: Not present")

    def _on_HandleTelemetryError(self, error: str):
        """Handle telemetry error"""

        self.log(f"Telemetry error: {error}")

    def _on_SyncTime(self):
        """Sync device time with PC"""

        if(not self.client):
            return

        try:
            result = self.client.sync_time(datetime.now())
            self.log(f"Time synchronized: {result}")
            QMessageBox.information(self, "Success", "Time synchronized successfully")

        except Exception as e:
            QMessageBox.critical(self, "Time Sync Error", str(e))
            self.log(f"Time sync error: {e}")

    def select_firmware(self):
        """Select firmware file"""

        filename, _ = QFileDialog.getOpenFileName(
            self,
            "Select Firmware File",
            "",
            "Binary Files (*.bin);;All Files (*.*)"
        )

        if filename:
            self.ui.firmwarePathInput.setText(filename)
            self.ui.uploadFirmwareButton.setEnabled(self.client is not None)

    def _on_UploadFirmware(self):
        """Upload firmware to device"""

        if(not self.client):
            return

        firmware_path = self.ui.firmwarePathInput.text()
        if(not firmware_path):
            return

        reply = QMessageBox.question(
            self,
            "Confirm Firmware Upload",
            "This will update the device firmware. The device will reboot. Continue?",
            QMessageBox.Yes | QMessageBox.No
        )

        if(reply == QMessageBox.Yes):
            try:
                self.log("Uploading firmware...")
                self.statusBar().showMessage("Uploading firmware...")

                from pathlib import Path
                result = self.client.upload_firmware(Path(firmware_path))

                self.log(f"Firmware upload complete: {result}")
                self.statusBar().showMessage("Firmware uploaded successfully")
                QMessageBox.information(self, "Success", "Firmware uploaded. Device will reboot.")

                self.client = None
                self.ui.connectButton.setText("Connect")
                self._EnableControls(False)

            except Exception as e:
                QMessageBox.critical(self, "Upload Error", str(e))
                self.log(f"Firmware upload error: {e}")
                self.statusBar().showMessage("Firmware upload failed")

    def log(self, message: str):
        """Add message to log"""

        timestamp = datetime.now().strftime("%H:%M:%S")
        self.ui.logText.append(f"[{timestamp}] {message}")

if (__name__ == "__main__"):
    app = QApplication(sys.argv)
    window = ThermalCameraGUI()
    window.show()
    sys.exit(app.exec())
