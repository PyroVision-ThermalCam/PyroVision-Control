# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QProgressBar, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QStatusBar, QTabWidget, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 700)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.connectionGroup = QGroupBox(self.centralwidget)
        self.connectionGroup.setObjectName(u"connectionGroup")
        self.horizontalLayout = QHBoxLayout(self.connectionGroup)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_ip = QLabel(self.connectionGroup)
        self.label_ip.setObjectName(u"label_ip")

        self.horizontalLayout.addWidget(self.label_ip)

        self.ipInput = QLineEdit(self.connectionGroup)
        self.ipInput.setObjectName(u"ipInput")
        self.ipInput.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout.addWidget(self.ipInput)

        self.label_port = QLabel(self.connectionGroup)
        self.label_port.setObjectName(u"label_port")

        self.horizontalLayout.addWidget(self.label_port)

        self.portInput = QSpinBox(self.connectionGroup)
        self.portInput.setObjectName(u"portInput")
        self.portInput.setMaximumSize(QSize(80, 16777215))
        self.portInput.setMinimum(1)
        self.portInput.setMaximum(65535)
        self.portInput.setValue(80)

        self.horizontalLayout.addWidget(self.portInput)

        self.label_apikey = QLabel(self.connectionGroup)
        self.label_apikey.setObjectName(u"label_apikey")

        self.horizontalLayout.addWidget(self.label_apikey)

        self.apiKeyInput = QLineEdit(self.connectionGroup)
        self.apiKeyInput.setObjectName(u"apiKeyInput")
        self.apiKeyInput.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout.addWidget(self.apiKeyInput)

        self.connectButton = QPushButton(self.connectionGroup)
        self.connectButton.setObjectName(u"connectButton")

        self.horizontalLayout.addWidget(self.connectButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addWidget(self.connectionGroup)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.liveViewTab = QWidget()
        self.liveViewTab.setObjectName(u"liveViewTab")
        self.verticalLayout_2 = QVBoxLayout(self.liveViewTab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.imageLabel = QLabel(self.liveViewTab)
        self.imageLabel.setObjectName(u"imageLabel")
        self.imageLabel.setMinimumSize(QSize(640, 480))
        self.imageLabel.setStyleSheet(u"QLabel { background-color: black; }")
        self.imageLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.imageLabel)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_fps = QLabel(self.liveViewTab)
        self.label_fps.setObjectName(u"label_fps")

        self.horizontalLayout_2.addWidget(self.label_fps)

        self.fpsSpinbox = QSpinBox(self.liveViewTab)
        self.fpsSpinbox.setObjectName(u"fpsSpinbox")
        self.fpsSpinbox.setMinimum(1)
        self.fpsSpinbox.setMaximum(15)
        self.fpsSpinbox.setValue(8)

        self.horizontalLayout_2.addWidget(self.fpsSpinbox)

        self.streamButton = QPushButton(self.liveViewTab)
        self.streamButton.setObjectName(u"streamButton")
        self.streamButton.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.streamButton)

        self.snapshotButton = QPushButton(self.liveViewTab)
        self.snapshotButton.setObjectName(u"snapshotButton")
        self.snapshotButton.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.snapshotButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.frameCounterLabel = QLabel(self.liveViewTab)
        self.frameCounterLabel.setObjectName(u"frameCounterLabel")

        self.verticalLayout_2.addWidget(self.frameCounterLabel)

        self.tabWidget.addTab(self.liveViewTab, "")
        self.imageCaptureTab = QWidget()
        self.imageCaptureTab.setObjectName(u"imageCaptureTab")
        self.verticalLayout_3 = QVBoxLayout(self.imageCaptureTab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_format = QLabel(self.imageCaptureTab)
        self.label_format.setObjectName(u"label_format")

        self.horizontalLayout_3.addWidget(self.label_format)

        self.formatCombo = QComboBox(self.imageCaptureTab)
        self.formatCombo.addItem("")
        self.formatCombo.addItem("")
        self.formatCombo.addItem("")
        self.formatCombo.setObjectName(u"formatCombo")

        self.horizontalLayout_3.addWidget(self.formatCombo)

        self.label_palette = QLabel(self.imageCaptureTab)
        self.label_palette.setObjectName(u"label_palette")

        self.horizontalLayout_3.addWidget(self.label_palette)

        self.paletteCombo = QComboBox(self.imageCaptureTab)
        self.paletteCombo.addItem("")
        self.paletteCombo.addItem("")
        self.paletteCombo.addItem("")
        self.paletteCombo.setObjectName(u"paletteCombo")

        self.horizontalLayout_3.addWidget(self.paletteCombo)

        self.label_scale = QLabel(self.imageCaptureTab)
        self.label_scale.setObjectName(u"label_scale")

        self.horizontalLayout_3.addWidget(self.label_scale)

        self.scaleCombo = QComboBox(self.imageCaptureTab)
        self.scaleCombo.addItem("")
        self.scaleCombo.addItem("")
        self.scaleCombo.setObjectName(u"scaleCombo")

        self.horizontalLayout_3.addWidget(self.scaleCombo)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.captureButton = QPushButton(self.imageCaptureTab)
        self.captureButton.setObjectName(u"captureButton")
        self.captureButton.setEnabled(False)

        self.horizontalLayout_4.addWidget(self.captureButton)

        self.saveToSdButton = QPushButton(self.imageCaptureTab)
        self.saveToSdButton.setObjectName(u"saveToSdButton")
        self.saveToSdButton.setEnabled(False)

        self.horizontalLayout_4.addWidget(self.saveToSdButton)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.capturedImageLabel = QLabel(self.imageCaptureTab)
        self.capturedImageLabel.setObjectName(u"capturedImageLabel")
        self.capturedImageLabel.setMinimumSize(QSize(640, 480))
        self.capturedImageLabel.setStyleSheet(u"QLabel { background-color: black; }")
        self.capturedImageLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.capturedImageLabel)

        self.tabWidget.addTab(self.imageCaptureTab, "")
        self.telemetryTab = QWidget()
        self.telemetryTab.setObjectName(u"telemetryTab")
        self.verticalLayout_4 = QVBoxLayout(self.telemetryTab)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.autoRefreshCheckbox = QCheckBox(self.telemetryTab)
        self.autoRefreshCheckbox.setObjectName(u"autoRefreshCheckbox")

        self.horizontalLayout_5.addWidget(self.autoRefreshCheckbox)

        self.refreshButton = QPushButton(self.telemetryTab)
        self.refreshButton.setObjectName(u"refreshButton")
        self.refreshButton.setEnabled(False)

        self.horizontalLayout_5.addWidget(self.refreshButton)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.uptimeLabel = QLabel(self.telemetryTab)
        self.uptimeLabel.setObjectName(u"uptimeLabel")

        self.verticalLayout_4.addWidget(self.uptimeLabel)

        self.sensorTempLabel = QLabel(self.telemetryTab)
        self.sensorTempLabel.setObjectName(u"sensorTempLabel")

        self.verticalLayout_4.addWidget(self.sensorTempLabel)

        self.coreTempLabel = QLabel(self.telemetryTab)
        self.coreTempLabel.setObjectName(u"coreTempLabel")

        self.verticalLayout_4.addWidget(self.coreTempLabel)

        self.voltageLabel = QLabel(self.telemetryTab)
        self.voltageLabel.setObjectName(u"voltageLabel")

        self.verticalLayout_4.addWidget(self.voltageLabel)

        self.rssiLabel = QLabel(self.telemetryTab)
        self.rssiLabel.setObjectName(u"rssiLabel")

        self.verticalLayout_4.addWidget(self.rssiLabel)

        self.sdCardLabel = QLabel(self.telemetryTab)
        self.sdCardLabel.setObjectName(u"sdCardLabel")

        self.verticalLayout_4.addWidget(self.sdCardLabel)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.tabWidget.addTab(self.telemetryTab, "")
        self.controlTab = QWidget()
        self.controlTab.setObjectName(u"controlTab")
        self.verticalLayout_5 = QVBoxLayout(self.controlTab)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.timeGroup = QGroupBox(self.controlTab)
        self.timeGroup.setObjectName(u"timeGroup")
        self.horizontalLayout_8 = QHBoxLayout(self.timeGroup)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.syncTimeButton = QPushButton(self.timeGroup)
        self.syncTimeButton.setObjectName(u"syncTimeButton")
        self.syncTimeButton.setEnabled(False)

        self.horizontalLayout_8.addWidget(self.syncTimeButton)

        self.label_timezone = QLabel(self.timeGroup)
        self.label_timezone.setObjectName(u"label_timezone")

        self.horizontalLayout_8.addWidget(self.label_timezone)

        self.timezoneInput = QLineEdit(self.timeGroup)
        self.timezoneInput.setObjectName(u"timezoneInput")

        self.horizontalLayout_8.addWidget(self.timezoneInput)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_6)


        self.verticalLayout_5.addWidget(self.timeGroup)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.tabWidget.addTab(self.controlTab, "")
        self.settingsTab = QWidget()
        self.settingsTab.setObjectName(u"settingsTab")
        self.verticalLayout_7 = QVBoxLayout(self.settingsTab)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.firmwareGroup = QGroupBox(self.settingsTab)
        self.firmwareGroup.setObjectName(u"firmwareGroup")
        self.firmwareGroup.setEnabled(False)
        self.verticalLayout_8 = QVBoxLayout(self.firmwareGroup)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.firmwarePathInput = QLineEdit(self.firmwareGroup)
        self.firmwarePathInput.setObjectName(u"firmwarePathInput")
        self.firmwarePathInput.setReadOnly(True)

        self.horizontalLayout_9.addWidget(self.firmwarePathInput)

        self.selectFirmwareButton = QPushButton(self.firmwareGroup)
        self.selectFirmwareButton.setObjectName(u"selectFirmwareButton")

        self.horizontalLayout_9.addWidget(self.selectFirmwareButton)


        self.verticalLayout_8.addLayout(self.horizontalLayout_9)

        self.uploadFirmwareButton = QPushButton(self.firmwareGroup)
        self.uploadFirmwareButton.setObjectName(u"uploadFirmwareButton")
        self.uploadFirmwareButton.setEnabled(False)

        self.verticalLayout_8.addWidget(self.uploadFirmwareButton)

        self.uploadProgress = QProgressBar(self.firmwareGroup)
        self.uploadProgress.setObjectName(u"uploadProgress")
        self.uploadProgress.setValue(0)

        self.verticalLayout_8.addWidget(self.uploadProgress)


        self.verticalLayout_7.addWidget(self.firmwareGroup)

        self.logGroup = QGroupBox(self.settingsTab)
        self.logGroup.setObjectName(u"logGroup")
        self.verticalLayout_9 = QVBoxLayout(self.logGroup)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.logText = QTextEdit(self.logGroup)
        self.logText.setObjectName(u"logText")
        self.logText.setMaximumSize(QSize(16777215, 200))
        self.logText.setReadOnly(True)

        self.verticalLayout_9.addWidget(self.logText)

        self.clearLogButton = QPushButton(self.logGroup)
        self.clearLogButton.setObjectName(u"clearLogButton")

        self.verticalLayout_9.addWidget(self.clearLogButton)


        self.verticalLayout_7.addWidget(self.logGroup)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_3)

        self.tabWidget.addTab(self.settingsTab, "")

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PyroVision Control", None))
        self.connectionGroup.setTitle(QCoreApplication.translate("MainWindow", u"Connection", None))
        self.label_ip.setText(QCoreApplication.translate("MainWindow", u"IP Address:", None))
        self.ipInput.setText(QCoreApplication.translate("MainWindow", u"192.168.178.55", None))
        self.label_port.setText(QCoreApplication.translate("MainWindow", u"Port:", None))
        self.label_apikey.setText(QCoreApplication.translate("MainWindow", u"API Key:", None))
        self.apiKeyInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Optional", None))
        self.connectButton.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.imageLabel.setText(QCoreApplication.translate("MainWindow", u"No Image", None))
        self.label_fps.setText(QCoreApplication.translate("MainWindow", u"FPS:", None))
        self.streamButton.setText(QCoreApplication.translate("MainWindow", u"Start Stream", None))
        self.snapshotButton.setText(QCoreApplication.translate("MainWindow", u"Save Snapshot", None))
        self.frameCounterLabel.setText(QCoreApplication.translate("MainWindow", u"Frames: 0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.liveViewTab), QCoreApplication.translate("MainWindow", u"Live View", None))
        self.label_format.setText(QCoreApplication.translate("MainWindow", u"Format:", None))
        self.formatCombo.setItemText(0, QCoreApplication.translate("MainWindow", u"jpeg", None))
        self.formatCombo.setItemText(1, QCoreApplication.translate("MainWindow", u"png", None))
        self.formatCombo.setItemText(2, QCoreApplication.translate("MainWindow", u"raw", None))

        self.label_palette.setText(QCoreApplication.translate("MainWindow", u"Palette:", None))
        self.paletteCombo.setItemText(0, QCoreApplication.translate("MainWindow", u"iron", None))
        self.paletteCombo.setItemText(1, QCoreApplication.translate("MainWindow", u"gray", None))
        self.paletteCombo.setItemText(2, QCoreApplication.translate("MainWindow", u"rainbow", None))

        self.label_scale.setText(QCoreApplication.translate("MainWindow", u"Scale:", None))
        self.scaleCombo.setItemText(0, QCoreApplication.translate("MainWindow", u"linear", None))
        self.scaleCombo.setItemText(1, QCoreApplication.translate("MainWindow", u"histogram", None))

        self.captureButton.setText(QCoreApplication.translate("MainWindow", u"Capture Image", None))
        self.saveToSdButton.setText(QCoreApplication.translate("MainWindow", u"Save to SD Card", None))
        self.capturedImageLabel.setText(QCoreApplication.translate("MainWindow", u"No Captured Image", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.imageCaptureTab), QCoreApplication.translate("MainWindow", u"Image Capture", None))
        self.autoRefreshCheckbox.setText(QCoreApplication.translate("MainWindow", u"Auto Refresh", None))
        self.refreshButton.setText(QCoreApplication.translate("MainWindow", u"Refresh Now", None))
        self.uptimeLabel.setText(QCoreApplication.translate("MainWindow", u"Uptime: N/A", None))
        self.sensorTempLabel.setText(QCoreApplication.translate("MainWindow", u"Sensor Temperature: N/A", None))
        self.coreTempLabel.setText(QCoreApplication.translate("MainWindow", u"Core Temperature: N/A", None))
        self.voltageLabel.setText(QCoreApplication.translate("MainWindow", u"Supply Voltage: N/A", None))
        self.rssiLabel.setText(QCoreApplication.translate("MainWindow", u"WiFi RSSI: N/A", None))
        self.sdCardLabel.setText(QCoreApplication.translate("MainWindow", u"SD Card: N/A", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.telemetryTab), QCoreApplication.translate("MainWindow", u"Telemetry", None))
        self.timeGroup.setTitle(QCoreApplication.translate("MainWindow", u"Time Synchronization", None))
        self.syncTimeButton.setText(QCoreApplication.translate("MainWindow", u"Sync Time with PC", None))
        self.label_timezone.setText(QCoreApplication.translate("MainWindow", u"Timezone:", None))
        self.timezoneInput.setText(QCoreApplication.translate("MainWindow", u"Europe/Berlin", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.controlTab), QCoreApplication.translate("MainWindow", u"Control", None))
        self.firmwareGroup.setTitle(QCoreApplication.translate("MainWindow", u"Firmware Update", None))
        self.selectFirmwareButton.setText(QCoreApplication.translate("MainWindow", u"Browse...", None))
        self.uploadFirmwareButton.setText(QCoreApplication.translate("MainWindow", u"Upload Firmware", None))
        self.logGroup.setTitle(QCoreApplication.translate("MainWindow", u"Log", None))
        self.clearLogButton.setText(QCoreApplication.translate("MainWindow", u"Clear Log", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settingsTab), QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi

