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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QStatusBar, QTabWidget,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 700)
        icon = QIcon()
        icon.addFile(u":/ressources/Logo_Alpha.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_Connection = QGroupBox(self.centralwidget)
        self.groupBox_Connection.setObjectName(u"groupBox_Connection")
        self.horizontalLayout = QHBoxLayout(self.groupBox_Connection)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_IP = QLabel(self.groupBox_Connection)
        self.label_IP.setObjectName(u"label_IP")

        self.horizontalLayout.addWidget(self.label_IP)

        self.lineEdit_IP = QLineEdit(self.groupBox_Connection)
        self.lineEdit_IP.setObjectName(u"lineEdit_IP")
        self.lineEdit_IP.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout.addWidget(self.lineEdit_IP)

        self.label_Port = QLabel(self.groupBox_Connection)
        self.label_Port.setObjectName(u"label_Port")

        self.horizontalLayout.addWidget(self.label_Port)

        self.spinBox_Port = QSpinBox(self.groupBox_Connection)
        self.spinBox_Port.setObjectName(u"spinBox_Port")
        self.spinBox_Port.setMaximumSize(QSize(80, 16777215))
        self.spinBox_Port.setMinimum(1)
        self.spinBox_Port.setMaximum(65535)
        self.spinBox_Port.setValue(80)

        self.horizontalLayout.addWidget(self.spinBox_Port)

        self.pushButton_Connect = QPushButton(self.groupBox_Connection)
        self.pushButton_Connect.setObjectName(u"pushButton_Connect")

        self.horizontalLayout.addWidget(self.pushButton_Connect)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addWidget(self.groupBox_Connection)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_LiveView = QWidget()
        self.tab_LiveView.setObjectName(u"tab_LiveView")
        self.verticalLayout_2 = QVBoxLayout(self.tab_LiveView)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.imageLabel = QLabel(self.tab_LiveView)
        self.imageLabel.setObjectName(u"imageLabel")
        self.imageLabel.setMinimumSize(QSize(640, 480))
        self.imageLabel.setStyleSheet(u"QLabel { background-color: black; }")
        self.imageLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.imageLabel)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_StartStream = QPushButton(self.tab_LiveView)
        self.pushButton_StartStream.setObjectName(u"pushButton_StartStream")
        self.pushButton_StartStream.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.pushButton_StartStream)

        self.pushButton_SaveSnapshot = QPushButton(self.tab_LiveView)
        self.pushButton_SaveSnapshot.setObjectName(u"pushButton_SaveSnapshot")
        self.pushButton_SaveSnapshot.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.pushButton_SaveSnapshot)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.label_FrameCounter = QLabel(self.tab_LiveView)
        self.label_FrameCounter.setObjectName(u"label_FrameCounter")

        self.verticalLayout_2.addWidget(self.label_FrameCounter)

        self.tabWidget.addTab(self.tab_LiveView, "")
        self.tab_Capture = QWidget()
        self.tab_Capture.setObjectName(u"tab_Capture")
        self.verticalLayout_3 = QVBoxLayout(self.tab_Capture)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_Format = QLabel(self.tab_Capture)
        self.label_Format.setObjectName(u"label_Format")

        self.horizontalLayout_3.addWidget(self.label_Format)

        self.comboBox_Format = QComboBox(self.tab_Capture)
        self.comboBox_Format.setObjectName(u"comboBox_Format")

        self.horizontalLayout_3.addWidget(self.comboBox_Format)

        self.label_Palette = QLabel(self.tab_Capture)
        self.label_Palette.setObjectName(u"label_Palette")

        self.horizontalLayout_3.addWidget(self.label_Palette)

        self.comboBox_Palette = QComboBox(self.tab_Capture)
        self.comboBox_Palette.setObjectName(u"comboBox_Palette")

        self.horizontalLayout_3.addWidget(self.comboBox_Palette)

        self.label_Camera = QLabel(self.tab_Capture)
        self.label_Camera.setObjectName(u"label_Camera")

        self.horizontalLayout_3.addWidget(self.label_Camera)

        self.comboBox_Camera = QComboBox(self.tab_Capture)
        self.comboBox_Camera.addItem("")
        self.comboBox_Camera.addItem("")
        self.comboBox_Camera.setObjectName(u"comboBox_Camera")

        self.horizontalLayout_3.addWidget(self.comboBox_Camera)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton_Capture = QPushButton(self.tab_Capture)
        self.pushButton_Capture.setObjectName(u"pushButton_Capture")
        self.pushButton_Capture.setEnabled(False)

        self.horizontalLayout_4.addWidget(self.pushButton_Capture)

        self.pushButton_Download = QPushButton(self.tab_Capture)
        self.pushButton_Download.setObjectName(u"pushButton_Download")
        self.pushButton_Download.setEnabled(False)

        self.horizontalLayout_4.addWidget(self.pushButton_Download)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.label_CapturedImage = QLabel(self.tab_Capture)
        self.label_CapturedImage.setObjectName(u"label_CapturedImage")
        self.label_CapturedImage.setMinimumSize(QSize(640, 480))
        self.label_CapturedImage.setStyleSheet(u"QLabel { background-color: black; }")
        self.label_CapturedImage.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_CapturedImage)

        self.tabWidget.addTab(self.tab_Capture, "")
        self.tab_Telemetry = QWidget()
        self.tab_Telemetry.setObjectName(u"tab_Telemetry")
        self.verticalLayout_4 = QVBoxLayout(self.tab_Telemetry)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.checkBox_AutoRefresh = QCheckBox(self.tab_Telemetry)
        self.checkBox_AutoRefresh.setObjectName(u"checkBox_AutoRefresh")

        self.horizontalLayout_5.addWidget(self.checkBox_AutoRefresh)

        self.pushButton_Refresh = QPushButton(self.tab_Telemetry)
        self.pushButton_Refresh.setObjectName(u"pushButton_Refresh")
        self.pushButton_Refresh.setEnabled(False)

        self.horizontalLayout_5.addWidget(self.pushButton_Refresh)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_BatteryPercentage_Value = QLabel(self.tab_Telemetry)
        self.label_BatteryPercentage_Value.setObjectName(u"label_BatteryPercentage_Value")

        self.gridLayout.addWidget(self.label_BatteryPercentage_Value, 2, 1, 1, 1)

        self.label_WiFiRSSI_Name = QLabel(self.tab_Telemetry)
        self.label_WiFiRSSI_Name.setObjectName(u"label_WiFiRSSI_Name")

        self.gridLayout.addWidget(self.label_WiFiRSSI_Name, 4, 0, 1, 1)

        self.label_BatteryCharging_Value = QLabel(self.tab_Telemetry)
        self.label_BatteryCharging_Value.setObjectName(u"label_BatteryCharging_Value")

        self.gridLayout.addWidget(self.label_BatteryCharging_Value, 3, 1, 1, 1)

        self.label_Lepton_AUX_Temperature_Name = QLabel(self.tab_Telemetry)
        self.label_Lepton_AUX_Temperature_Name.setObjectName(u"label_Lepton_AUX_Temperature_Name")

        self.gridLayout.addWidget(self.label_Lepton_AUX_Temperature_Name, 6, 0, 1, 1)

        self.label_BatteryPercent_Name = QLabel(self.tab_Telemetry)
        self.label_BatteryPercent_Name.setObjectName(u"label_BatteryPercent_Name")

        self.gridLayout.addWidget(self.label_BatteryPercent_Name, 2, 0, 1, 1)

        self.label_Lepton_AUX_Temperature_Value = QLabel(self.tab_Telemetry)
        self.label_Lepton_AUX_Temperature_Value.setObjectName(u"label_Lepton_AUX_Temperature_Value")

        self.gridLayout.addWidget(self.label_Lepton_AUX_Temperature_Value, 6, 1, 1, 1)

        self.label_BatteryVoltage_Value = QLabel(self.tab_Telemetry)
        self.label_BatteryVoltage_Value.setObjectName(u"label_BatteryVoltage_Value")

        self.gridLayout.addWidget(self.label_BatteryVoltage_Value, 1, 1, 1, 1)

        self.label_Lepton_FPA_Temperature_Name = QLabel(self.tab_Telemetry)
        self.label_Lepton_FPA_Temperature_Name.setObjectName(u"label_Lepton_FPA_Temperature_Name")

        self.gridLayout.addWidget(self.label_Lepton_FPA_Temperature_Name, 5, 0, 1, 1)

        self.label_CameraUptime_Value = QLabel(self.tab_Telemetry)
        self.label_CameraUptime_Value.setObjectName(u"label_CameraUptime_Value")

        self.gridLayout.addWidget(self.label_CameraUptime_Value, 0, 1, 1, 1)

        self.label_WiFiRSSI_Value = QLabel(self.tab_Telemetry)
        self.label_WiFiRSSI_Value.setObjectName(u"label_WiFiRSSI_Value")

        self.gridLayout.addWidget(self.label_WiFiRSSI_Value, 4, 1, 1, 1)

        self.label_BatteryVoltage_Name = QLabel(self.tab_Telemetry)
        self.label_BatteryVoltage_Name.setObjectName(u"label_BatteryVoltage_Name")

        self.gridLayout.addWidget(self.label_BatteryVoltage_Name, 1, 0, 1, 1)

        self.label_BatteryCharging_Name = QLabel(self.tab_Telemetry)
        self.label_BatteryCharging_Name.setObjectName(u"label_BatteryCharging_Name")

        self.gridLayout.addWidget(self.label_BatteryCharging_Name, 3, 0, 1, 1)

        self.label_CameraUptime_Name = QLabel(self.tab_Telemetry)
        self.label_CameraUptime_Name.setObjectName(u"label_CameraUptime_Name")

        self.gridLayout.addWidget(self.label_CameraUptime_Name, 0, 0, 1, 1)

        self.label_Lepton_FPA_Temperature_Value = QLabel(self.tab_Telemetry)
        self.label_Lepton_FPA_Temperature_Value.setObjectName(u"label_Lepton_FPA_Temperature_Value")

        self.gridLayout.addWidget(self.label_Lepton_FPA_Temperature_Value, 5, 1, 1, 1)

        self.label_DeviceTemperature_Name = QLabel(self.tab_Telemetry)
        self.label_DeviceTemperature_Name.setObjectName(u"label_DeviceTemperature_Name")

        self.gridLayout.addWidget(self.label_DeviceTemperature_Name, 7, 0, 1, 1)

        self.label_DeviceTemperature_Value = QLabel(self.tab_Telemetry)
        self.label_DeviceTemperature_Value.setObjectName(u"label_DeviceTemperature_Value")

        self.gridLayout.addWidget(self.label_DeviceTemperature_Value, 7, 1, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.tabWidget.addTab(self.tab_Telemetry, "")
        self.tab_Control = QWidget()
        self.tab_Control.setObjectName(u"tab_Control")
        self.verticalLayout_5 = QVBoxLayout(self.tab_Control)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.groupBox_System = QGroupBox(self.tab_Control)
        self.groupBox_System.setObjectName(u"groupBox_System")
        self.horizontalLayout_8 = QHBoxLayout(self.groupBox_System)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.pushButton_SyncTime = QPushButton(self.groupBox_System)
        self.pushButton_SyncTime.setObjectName(u"pushButton_SyncTime")
        self.pushButton_SyncTime.setEnabled(False)

        self.horizontalLayout_8.addWidget(self.pushButton_SyncTime)

        self.label_timezone = QLabel(self.groupBox_System)
        self.label_timezone.setObjectName(u"label_timezone")

        self.horizontalLayout_8.addWidget(self.label_timezone)

        self.lineEdit_Timezone = QLineEdit(self.groupBox_System)
        self.lineEdit_Timezone.setObjectName(u"lineEdit_Timezone")

        self.horizontalLayout_8.addWidget(self.lineEdit_Timezone)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_6)


        self.verticalLayout_5.addWidget(self.groupBox_System)

        self.groupBox_Lepton = QGroupBox(self.tab_Control)
        self.groupBox_Lepton.setObjectName(u"groupBox_Lepton")

        self.verticalLayout_5.addWidget(self.groupBox_Lepton)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.tabWidget.addTab(self.tab_Control, "")
        self.tab_Settings = QWidget()
        self.tab_Settings.setObjectName(u"tab_Settings")
        self.verticalLayout_7 = QVBoxLayout(self.tab_Settings)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.firmwareGroup = QGroupBox(self.tab_Settings)
        self.firmwareGroup.setObjectName(u"firmwareGroup")
        self.firmwareGroup.setEnabled(False)
        self.verticalLayout_8 = QVBoxLayout(self.firmwareGroup)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.lineEdit_FirmwarePath = QLineEdit(self.firmwareGroup)
        self.lineEdit_FirmwarePath.setObjectName(u"lineEdit_FirmwarePath")
        self.lineEdit_FirmwarePath.setReadOnly(True)

        self.horizontalLayout_9.addWidget(self.lineEdit_FirmwarePath)

        self.pushButton_BrowseFirmware = QPushButton(self.firmwareGroup)
        self.pushButton_BrowseFirmware.setObjectName(u"pushButton_BrowseFirmware")

        self.horizontalLayout_9.addWidget(self.pushButton_BrowseFirmware)


        self.verticalLayout_8.addLayout(self.horizontalLayout_9)

        self.pushButton_UploadFirmware = QPushButton(self.firmwareGroup)
        self.pushButton_UploadFirmware.setObjectName(u"pushButton_UploadFirmware")
        self.pushButton_UploadFirmware.setEnabled(False)

        self.verticalLayout_8.addWidget(self.pushButton_UploadFirmware)

        self.progressBar_UploadFirmware = QProgressBar(self.firmwareGroup)
        self.progressBar_UploadFirmware.setObjectName(u"progressBar_UploadFirmware")
        self.progressBar_UploadFirmware.setValue(0)

        self.verticalLayout_8.addWidget(self.progressBar_UploadFirmware)


        self.verticalLayout_7.addWidget(self.firmwareGroup)

        self.groupBox_Log = QGroupBox(self.tab_Settings)
        self.groupBox_Log.setObjectName(u"groupBox_Log")
        self.verticalLayout_9 = QVBoxLayout(self.groupBox_Log)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.textEdit_Log = QTextEdit(self.groupBox_Log)
        self.textEdit_Log.setObjectName(u"textEdit_Log")
        self.textEdit_Log.setMaximumSize(QSize(16777215, 200))
        self.textEdit_Log.setReadOnly(True)

        self.verticalLayout_9.addWidget(self.textEdit_Log)

        self.pushButton_ClearLog = QPushButton(self.groupBox_Log)
        self.pushButton_ClearLog.setObjectName(u"pushButton_ClearLog")

        self.verticalLayout_9.addWidget(self.pushButton_ClearLog)


        self.verticalLayout_7.addWidget(self.groupBox_Log)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_3)

        self.tabWidget.addTab(self.tab_Settings, "")

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
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PyroVision-Control", None))
        self.groupBox_Connection.setTitle(QCoreApplication.translate("MainWindow", u"Connection", None))
        self.label_IP.setText(QCoreApplication.translate("MainWindow", u"IP Address:", None))
        self.lineEdit_IP.setText(QCoreApplication.translate("MainWindow", u"192.168.178.57", None))
        self.label_Port.setText(QCoreApplication.translate("MainWindow", u"Port:", None))
        self.pushButton_Connect.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.imageLabel.setText(QCoreApplication.translate("MainWindow", u"No Image", None))
        self.pushButton_StartStream.setText(QCoreApplication.translate("MainWindow", u"Start Stream", None))
        self.pushButton_SaveSnapshot.setText(QCoreApplication.translate("MainWindow", u"Save Snapshot", None))
        self.label_FrameCounter.setText(QCoreApplication.translate("MainWindow", u"Frames: 0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_LiveView), QCoreApplication.translate("MainWindow", u"Live View", None))
        self.label_Format.setText(QCoreApplication.translate("MainWindow", u"Format:", None))
        self.label_Palette.setText(QCoreApplication.translate("MainWindow", u"Palette:", None))
        self.label_Camera.setText(QCoreApplication.translate("MainWindow", u"Camera:", None))
        self.comboBox_Camera.setItemText(0, QCoreApplication.translate("MainWindow", u"Thermal", None))
        self.comboBox_Camera.setItemText(1, QCoreApplication.translate("MainWindow", u"RGB", None))

        self.pushButton_Capture.setText(QCoreApplication.translate("MainWindow", u"Capture Image", None))
        self.pushButton_Download.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        self.label_CapturedImage.setText(QCoreApplication.translate("MainWindow", u"No Captured Image", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Capture), QCoreApplication.translate("MainWindow", u"Capture", None))
        self.checkBox_AutoRefresh.setText(QCoreApplication.translate("MainWindow", u"Auto Refresh", None))
        self.pushButton_Refresh.setText(QCoreApplication.translate("MainWindow", u"Refresh Now", None))
        self.label_BatteryPercentage_Value.setText("")
        self.label_WiFiRSSI_Name.setText(QCoreApplication.translate("MainWindow", u"WiFi RSSI:", None))
        self.label_BatteryCharging_Value.setText("")
        self.label_Lepton_AUX_Temperature_Name.setText(QCoreApplication.translate("MainWindow", u"Lepton AUX Temperature:", None))
        self.label_BatteryPercent_Name.setText(QCoreApplication.translate("MainWindow", u"Battery Percent:", None))
        self.label_BatteryVoltage_Value.setText("")
        self.label_Lepton_FPA_Temperature_Name.setText(QCoreApplication.translate("MainWindow", u"Lepton FPA Temperature:", None))
        self.label_CameraUptime_Value.setText("")
        self.label_WiFiRSSI_Value.setText("")
        self.label_BatteryVoltage_Name.setText(QCoreApplication.translate("MainWindow", u"Battery Voltage:", None))
        self.label_BatteryCharging_Name.setText(QCoreApplication.translate("MainWindow", u"Battery Charging:", None))
        self.label_CameraUptime_Name.setText(QCoreApplication.translate("MainWindow", u"Camera uptime:", None))
        self.label_Lepton_FPA_Temperature_Value.setText("")
        self.label_DeviceTemperature_Name.setText(QCoreApplication.translate("MainWindow", u"Device Temperature:", None))
        self.label_DeviceTemperature_Value.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Telemetry), QCoreApplication.translate("MainWindow", u"Telemetry", None))
        self.groupBox_System.setTitle(QCoreApplication.translate("MainWindow", u"System", None))
        self.pushButton_SyncTime.setText(QCoreApplication.translate("MainWindow", u"Sync Time with PC", None))
        self.label_timezone.setText(QCoreApplication.translate("MainWindow", u"Timezone:", None))
        self.lineEdit_Timezone.setText(QCoreApplication.translate("MainWindow", u"Europe/Berlin", None))
        self.groupBox_Lepton.setTitle(QCoreApplication.translate("MainWindow", u"Lepton", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Control), QCoreApplication.translate("MainWindow", u"Control", None))
        self.firmwareGroup.setTitle(QCoreApplication.translate("MainWindow", u"Firmware Update", None))
        self.pushButton_BrowseFirmware.setText(QCoreApplication.translate("MainWindow", u"Browse...", None))
        self.pushButton_UploadFirmware.setText(QCoreApplication.translate("MainWindow", u"Upload Firmware", None))
        self.groupBox_Log.setTitle(QCoreApplication.translate("MainWindow", u"Log", None))
        self.pushButton_ClearLog.setText(QCoreApplication.translate("MainWindow", u"Clear Log", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Settings), QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi

