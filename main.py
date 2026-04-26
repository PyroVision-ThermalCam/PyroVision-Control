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

from PyroVision import PyroVisionClient, TelemetryData, Camera
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
            await client.Connect()

            # Send stream start command
            await client.SendCommand("start", {
                "fps": self._fps
            })

            # Read stream frames
            async for message in client.Connection:
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
                await client.SendCommand("stop", {})
            except:
                pass
            try:
                await client.Disconnect()
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
        self._client = client
        self.running = False

    def run(self):
        """Run telemetry polling"""
        self.running = True
        while(self.running):
            try:
                telemetry = self._client.GetTelemetry()
                self.telemetry_received.emit({
                    "uptime_s": telemetry.UptimeS,
                    "sensor_temp_c": telemetry.LeptonFpaC,
                    "supply_voltage_v": telemetry.BatteryVoltageMv,
                    "wifi_rssi_dbm": telemetry.WifiRssiDbm,
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
        self._client: Optional[PyroVisionClient] = None
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

        self.ui.pushButton_Connect.clicked.connect(self._on_Connect_Clicked)
        self.ui.pushButton_StartStream.clicked.connect(self._on_Stream_Clicked)
        self.ui.pushButton_SaveSnapshot.clicked.connect(self._on_Save_Snapshot)
        self.ui.pushButton_Capture.clicked.connect(self._on_Capture_Clicked)
        self.ui.pushButton_Refresh.clicked.connect(self._on_RefreshTelemetry)
        self.ui.pushButton_SyncTime.clicked.connect(self._on_SyncTime)
        self.ui.pushButton_UploadFirmware.clicked.connect(self._on_UploadFirmware)
        self.ui.pushButton_ClearLog.clicked.connect(self.ui.textEdit_Log.clear)
        self.ui.comboBox_Palette.currentIndexChanged.connect(self._on_Palette_Changed)
        self.ui.comboBox_Format.currentIndexChanged.connect(self._on_Format_Changed)

        self.statusBar().showMessage("Disconnected")

    def Slot_StreamStopped(self):
        """Handle stream stopped event"""

        self.is_streaming = False
        self.ui.pushButton_StartStream.setText("Start Stream")
        self.ui.pushButton_Snapshot.setEnabled(False)
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

    def _on_Palette_Changed(self, index):
        """Handle palette change"""

        if(not self._client):
            return

        try:
            palette_index = self.ui.comboBox_Palette.currentData()
            self._client.SetPalette(palette_index)
            self.log(f"Palette changed to index {palette_index}")
        except Exception as e:
            QMessageBox.critical(self, "Palette Error", str(e))
            self.log(f"Palette change error: {e}")

    def _on_Format_Changed(self, index):
        """Handle image format change"""

        if(not self._client):
            return

        try:
            format_index = self.ui.comboBox_Format.currentData()
            self._client.SetImageFormat(format_index)
            self.log(f"Image format changed to index {format_index}")
        except Exception as e:
            QMessageBox.critical(self, "Format Error", str(e))
            self.log(f"Image format change error: {e}")

    def _on_Connect_Clicked(self):
        """Toggle connection to the device"""

        if(not self._client):
            ip = self.ui.lineEdit_IP.text()
            port = self.ui.spinBox_Port.value()
            api_key = str()

            try:
                self._client = PyroVisionClient(ip, port, api_key)

                self._info = self._client.GetInfo()

                self.ui.comboBox_Palette.blockSignals(True)
                self.ui.comboBox_Palette.clear()
                for Palette in self._info["palettes"]:
                    self.ui.comboBox_Palette.addItem(Palette["name"], Palette["index"])
                self.ui.comboBox_Palette.blockSignals(False)

                self.ui.comboBox_Format.clear()
                for Format in self._info["image_formats"]:
                    self.ui.comboBox_Format.addItem(Format["name"], Format["index"])

                self._client.GetTelemetry()

                self.ui.pushButton_Connect.setText("Disconnect")
                self.statusBar().showMessage(f"Connected to {ip}:{port}")
                self.log(f"Connected to {ip}:{port}")

                self._EnableControls(True)

            except Exception as e:
                QMessageBox.critical(self, "Connection Error", str(e))
                self._client = None
                self.log(f"Connection failed: {e}")
        else:
            if(self.is_streaming):
                self._on_Stream_Clicked()

            if(self.telemetry_thread and self.telemetry_thread.isRunning()):
                self.toggle_auto_refresh(Qt.Unchecked)

            self._client = None
            self.ui.pushButton_Connect.setText("Connect")
            self.statusBar().showMessage("Disconnected")
            self.log("Disconnected")

            self._EnableControls(False)

    def _EnableControls(self, enabled: bool):
        """Enable or disable control buttons"""

        self.ui.pushButton_StartStream.setEnabled(enabled)
        self.ui.pushButton_Capture.setEnabled(enabled)
        self.ui.pushButton_SaveSnapshot.setEnabled(enabled)
        self.ui.pushButton_Refresh.setEnabled(enabled)
        self.ui.pushButton_SyncTime.setEnabled(enabled)
        self.ui.pushButton_UploadFirmware.setEnabled(enabled and bool(self.ui.lineEdit_FirmwarePath.text()))

    def _on_Stream_Clicked(self):
        """Toggle video stream"""

        if(not self.is_streaming):
            self.log("Start video stream")

            ip = self.ui.lineEdit_IP.text()
            port = self.ui.spinBox_Port.value()
            api_key = str()
            
            self.stream_thread = ImageStreamThread(ip, port, api_key, 9)
            self.stream_thread.Signal_FrameReceived.connect(self.Slot_DisplayFrame)
            self.stream_thread.Signal_ErrorOccurred.connect(self.Slot_StreamError)
            self.stream_thread.Signal_StreamStopped.connect(self.Slot_StreamStopped)
            self.stream_thread.start()

            self.is_streaming = True
            self.ui.pushButton_StartStream.setText("Stop Stream")
            self.ui.pushButton_SaveSnapshot.setEnabled(True)
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

        if(not self._client):
            return

        try:
            image_data = self._client.GetImage()

            pixmap = QPixmap()
            pixmap.loadFromData(image_data)

            if(not pixmap.isNull()):
                scaled_pixmap = pixmap.scaled(
                    self.ui.label_CapturedImage.size(),
                    Qt.KeepAspectRatio,
                    Qt.SmoothTransformation
                )

                self.ui.label_CapturedImage.setPixmap(scaled_pixmap)
                self.log("Captured image")
            else:
                QMessageBox.warning(self, "Error", "Failed to decode image")

        except Exception as e:
            QMessageBox.critical(self, "Capture Error", str(e))
            self.log(f"Capture error: {e}")

    def _on_ToggleAutoRefresh(self, state):
        """Toggle automatic telemetry refresh"""

        if(state == Qt.Checked):
            if(not self._client):
                self.ui.autoRefreshCheckbox.setChecked(False)
                return

            self.telemetry_thread = TelemetryThread(self._client)
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

        if(not self._client):
            return

        try:
            telemetry = self._client.GetTelemetry()

            self.ui.label_CameraUptime_Value.setText(f"{telemetry.UptimeS} s")
            self.ui.label_BatteryVoltage_Value.setText(f"{telemetry.BatteryVoltageMv} mV")
            self.ui.label_BatteryPercentage_Value.setText(f"{telemetry.BatteryPercentage} %")
            self.ui.label_BatteryCharging_Value.setText("Yes" if telemetry.BatteryCharging else "No")
            self.ui.label_WiFiRSSI_Value.setText(f"{telemetry.WifiRssiDbm} dBm")
            self.ui.label_Lepton_FPA_Temperature_Value.setText(f"{telemetry.LeptonFpaC:.1f} °C")
            self.ui.label_Lepton_AUX_Temperature_Value.setText(f"{telemetry.LeptonAuxC:.1f} °C")
            self.ui.label_DeviceTemperature_Value.setText(f"{telemetry.DeviceTemperatureC:.1f} °C")

            self.log("Telemetry refreshed")
        except Exception as e:
            QMessageBox.critical(self, "Telemetry Error", str(e))
            self.log(f"Telemetry error: {e}")

    def _on_UpdateTelemetry(self, data: dict):
        """Update telemetry display"""

        hours = data["uptime_s"] // 3600
        minutes = (data["uptime_s"] % 3600) // 60
        seconds = data["uptime_s"] % 60
        self.ui.label_CameraUptime_Value.setText(f"Uptime: {hours}h {minutes}m {seconds}s")

        self.ui.label_Lepton_FPA_Temperature_Value.setText(f"Lepton FPA Temperature: {data['lepton_fpa_c']:.1f} °C")
        self.ui.label_Lepton_AUX_Temperature_Value.setText(f"Lepton AUX Temperature: {data['lepton_aux_c']:.1f} °C")
        self.ui.label_WiFiRSSI_Value.setText(f"WiFi RSSI: {data['wifi_rssi_dbm']} dBm")

        if(data["sdcard_present"]):
            self.ui.label_SDCard_Value.setText(f"SD Card: Present ({data['sdcard_free_mb']} MB free)")
        else:
            self.ui.sdCardLabel.setText("SD Card: Not present")

    def _on_HandleTelemetryError(self, error: str):
        """Handle telemetry error"""

        self.log(f"Telemetry error: {error}")

    def _on_SyncTime(self):
        """Sync device time with PC"""

        if(not self._client):
            return

        try:
            result = self._client.sync_time(datetime.now())
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
            self.ui.uploadFirmwareButton.setEnabled(self._client is not None)

    def _on_UploadFirmware(self):
        """Upload firmware to device"""

        if(not self._client):
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
                result = self._client.upload_firmware(Path(firmware_path))

                self.log(f"Firmware upload complete: {result}")
                self.statusBar().showMessage("Firmware uploaded successfully")
                QMessageBox.information(self, "Success", "Firmware uploaded. Device will reboot.")

                self._client = None
                self.ui.connectButton.setText("Connect")
                self._EnableControls(False)

            except Exception as e:
                QMessageBox.critical(self, "Upload Error", str(e))
                self.log(f"Firmware upload error: {e}")
                self.statusBar().showMessage("Firmware upload failed")

    def log(self, message: str):
        """Add message to log"""

        timestamp = datetime.now().strftime("%H:%M:%S")
        self.ui.textEdit_Log.append(f"[{timestamp}] {message}")

if (__name__ == "__main__"):
    app = QApplication(sys.argv)
    window = ThermalCameraGUI()
    window.show()
    sys.exit(app.exec())
