import pyperclip
from PySide6.QtCore import Qt
from PySide6.QtGui import QCursor
from PySide6.QtWidgets import QLabel


class DoubleClickToCopyLabel(QLabel):
    def __init__(self, *args, **kwargs):
        super(DoubleClickToCopyLabel, self).__init__(*args, **kwargs)
        self.setCursor(QCursor(Qt.PointingHandCursor))
        self.setStyleSheet("margin-right: 5px;")

    def mouseDoubleClickEvent(self, event):
        pyperclip.copy(self.text())


class ClickToCopyLabel(QLabel):
    def __init__(self, *args, **kwargs):
        super(ClickToCopyLabel, self).__init__(*args, **kwargs)
        self.setCursor(QCursor(Qt.PointingHandCursor))
        self.setStyleSheet("margin-right: 5px;")

    def mousePressEvent(self, event):
        pyperclip.copy(self.text())

