from PySide6.QtCore import Qt, Signal, QPoint
from PySide6.QtWidgets import QWidget


class TitleBar(QWidget):
    # сигнал закрытия окна
    windowClosed = Signal()
    # Окно мобильных
    windowMoved = Signal(QPoint)

    def __init__(self, *args, **kwargs):
        super(TitleBar, self).__init__(*args, **kwargs)
        self.mPos = None

    def mousePressEvent(self, event):
        """ Событие клика мыши """
        if event.button() == Qt.LeftButton:
            self.mPos = event.position().toPoint()
        event.accept()

    def mouseReleaseEvent(self, event):
        """ Событие отказов мыши """
        self.mPos = None
        event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton and self.mPos:
            self.windowMoved.emit(self.mapToGlobal(event.position().toPoint() - self.mPos))
        event.accept()
