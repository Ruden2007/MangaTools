from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow

from ui_designer import Ui_AddSoundDialog


class AddSoundDialog(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(AddSoundDialog, self).__init__(*args, **kwargs)
        self.cleared_text = None
        self._pressed = False
        self.Direction = None

        # Фон прозрачный
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        # Нет границы
        self.setWindowFlag(Qt.FramelessWindowHint)

        # Отслеживание мыши
        self.setMouseTracking(True)

        self.ui = Ui_AddSoundDialog()
        self.ui.setupUi(self)

        # слот сигнала
        self.ui.TitleBar.windowClosed.connect(self.close)
        self.ui.TitleBar.windowMoved.connect(self.move)
