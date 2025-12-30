"""
PyroVision GUI Stylesheet
Dark theme with orange/thermal accents matching the project branding

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

STYLESHEET = """
/* Main window and base colors */
QMainWindow {
    background-color: #1e1e1e;
    color: #e0e0e0;
}

QWidget {
    background-color: #1e1e1e;
    color: #e0e0e0;
    font-family: 'Segoe UI', Arial, sans-serif;
    font-size: 9pt;
}

/* Group boxes */
QGroupBox {
    background-color: #252525;
    border: 2px solid #404040;
    border-radius: 6px;
    margin-top: 8px;
    padding-top: 12px;
    font-weight: bold;
    color: #ff8c00;
}

QGroupBox::title {
    subcontrol-origin: margin;
    subcontrol-position: top left;
    padding: 2px 8px;
    color: #ff8c00;
}

/* Buttons */
QPushButton {
    background-color: #3a3a3a;
    color: #e0e0e0;
    border: 1px solid #505050;
    border-radius: 4px;
    padding: 6px 16px;
    min-height: 20px;
}

QPushButton:hover {
    background-color: #4a4a4a;
    border: 1px solid #ff8c00;
}

QPushButton:pressed {
    background-color: #2a2a2a;
}

QPushButton:disabled {
    background-color: #2a2a2a;
    color: #666666;
    border: 1px solid #3a3a3a;
}

QPushButton#connectButton {
    background-color: #ff6600;
    color: #ffffff;
    font-weight: bold;
    border: 1px solid #ff8c00;
}

QPushButton#connectButton:hover {
    background-color: #ff8c00;
}

QPushButton#connectButton:pressed {
    background-color: #cc5200;
}

QPushButton#streamButton,
QPushButton#captureButton {
    background-color: #0066cc;
    color: #ffffff;
    border: 1px solid #0088ff;
}

QPushButton#streamButton:hover,
QPushButton#captureButton:hover {
    background-color: #0088ff;
}

/* Line edits and inputs */
QLineEdit, QSpinBox {
    background-color: #2a2a2a;
    color: #e0e0e0;
    border: 1px solid #505050;
    border-radius: 3px;
    padding: 4px 8px;
    selection-background-color: #ff8c00;
}

QLineEdit:focus, QSpinBox:focus {
    border: 1px solid #ff8c00;
}

QLineEdit:disabled, QSpinBox:disabled {
    background-color: #1e1e1e;
    color: #666666;
}

/* Combo boxes */
QComboBox {
    background-color: #2a2a2a;
    color: #e0e0e0;
    border: 1px solid #505050;
    border-radius: 3px;
    padding: 4px 8px;
    min-width: 80px;
}

QComboBox:hover {
    border: 1px solid #ff8c00;
}

QComboBox::drop-down {
    border: none;
    width: 20px;
}

QComboBox::down-arrow {
    image: none;
    border-left: 4px solid transparent;
    border-right: 4px solid transparent;
    border-top: 6px solid #ff8c00;
    margin-right: 6px;
}

QComboBox QAbstractItemView {
    background-color: #2a2a2a;
    color: #e0e0e0;
    selection-background-color: #ff8c00;
    selection-color: #ffffff;
    border: 1px solid #505050;
}

/* Tab widget */
QTabWidget::pane {
    border: 1px solid #404040;
    background-color: #252525;
    border-radius: 4px;
}

QTabBar::tab {
    background-color: #2a2a2a;
    color: #b0b0b0;
    border: 1px solid #404040;
    border-bottom: none;
    padding: 8px 20px;
    margin-right: 2px;
}

QTabBar::tab:selected {
    background-color: #252525;
    color: #ff8c00;
    border-bottom: 2px solid #ff8c00;
}

QTabBar::tab:hover:!selected {
    background-color: #3a3a3a;
    color: #e0e0e0;
}

/* Labels */
QLabel {
    color: #e0e0e0;
    background-color: transparent;
}

QLabel#imageLabel,
QLabel#capturedImageLabel {
    background-color: #000000;
    border: 2px solid #404040;
    border-radius: 4px;
}

/* Text edit / Log */
QTextEdit, QPlainTextEdit {
    background-color: #1a1a1a;
    color: #d0d0d0;
    border: 1px solid #404040;
    border-radius: 3px;
    font-family: 'Consolas', 'Courier New', monospace;
    font-size: 8pt;
}

/* Sliders */
QSlider::groove:horizontal {
    background-color: #2a2a2a;
    height: 6px;
    border-radius: 3px;
}

QSlider::handle:horizontal {
    background-color: #ff8c00;
    width: 16px;
    height: 16px;
    margin: -5px 0;
    border-radius: 8px;
}

QSlider::handle:horizontal:hover {
    background-color: #ffaa00;
}

QSlider::sub-page:horizontal {
    background-color: #ff8c00;
    border-radius: 3px;
}

/* Checkboxes */
QCheckBox {
    color: #e0e0e0;
    spacing: 6px;
}

QCheckBox::indicator {
    width: 18px;
    height: 18px;
    border: 1px solid #505050;
    border-radius: 3px;
    background-color: #2a2a2a;
}

QCheckBox::indicator:checked {
    background-color: #ff8c00;
    border: 1px solid #ff8c00;
}

QCheckBox::indicator:hover {
    border: 1px solid #ff8c00;
}

/* Progress bar */
QProgressBar {
    background-color: #2a2a2a;
    border: 1px solid #404040;
    border-radius: 4px;
    text-align: center;
    color: #e0e0e0;
    height: 20px;
}

QProgressBar::chunk {
    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                    stop:0 #ff6600, stop:1 #ff8c00);
    border-radius: 3px;
}

/* Status bar */
QStatusBar {
    background-color: #252525;
    color: #b0b0b0;
    border-top: 1px solid #404040;
}

QStatusBar::item {
    border: none;
}

/* Scrollbars */
QScrollBar:vertical {
    background-color: #2a2a2a;
    width: 12px;
    border-radius: 6px;
}

QScrollBar::handle:vertical {
    background-color: #505050;
    border-radius: 6px;
    min-height: 20px;
}

QScrollBar::handle:vertical:hover {
    background-color: #606060;
}

QScrollBar::add-line:vertical,
QScrollBar::sub-line:vertical {
    height: 0px;
}

QScrollBar:horizontal {
    background-color: #2a2a2a;
    height: 12px;
    border-radius: 6px;
}

QScrollBar::handle:horizontal {
    background-color: #505050;
    border-radius: 6px;
    min-width: 20px;
}

QScrollBar::handle:horizontal:hover {
    background-color: #606060;
}

QScrollBar::add-line:horizontal,
QScrollBar::sub-line:horizontal {
    width: 0px;
}

/* Tooltips */
QToolTip {
    background-color: #2a2a2a;
    color: #e0e0e0;
    border: 1px solid #ff8c00;
    border-radius: 3px;
    padding: 4px;
}

/* Menu (if any) */
QMenu {
    background-color: #2a2a2a;
    color: #e0e0e0;
    border: 1px solid #404040;
}

QMenu::item:selected {
    background-color: #ff8c00;
    color: #ffffff;
}
"""