from PySide6.QtCore import Qt, QObject, QMetaObject, Signal, Slot
from PySide6.QtGui import QCursor
from PySide6.QtWidgets import QLineEdit, QWidget, QTextEdit


class CustomLineEdit(QLineEdit):
    clicked = Signal()

    def __init__(self, *args, **kwargs):
        super(CustomLineEdit, self).__init__(*args, **kwargs)

        self.setCursor(QCursor(Qt.IBeamCursor))

    def mousePressEvent(self, event):
        self.clicked.emit()


class CustomTextEdit(QTextEdit):
    clicked = Signal()

    def __init__(self, *args, **kwargs):
        super(CustomTextEdit, self).__init__(*args, **kwargs)

        self.setCursor(QCursor(Qt.IBeamCursor))

    def mousePressEvent(self, event):
        self.clicked.emit()
