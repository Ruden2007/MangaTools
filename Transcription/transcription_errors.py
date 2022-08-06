from PySide6.QtGui import Qt
from PySide6.QtWidgets import QMainWindow

from ui_designer import Ui_ErrorSample


class ErrorTranscript(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Нет границы
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowModality(Qt.ApplicationModal)

        self.ui = Ui_ErrorSample()
        self.ui.setupUi(self)

        self.ui.error_title.setText("Ошибка транскрипции!")

        self.ui.TitleBar.windowMoved.connect(self.move)
        self.ui.close_btn.clicked.connect(self.close)
        self.ui.ok.clicked.connect(self.close)

    def missing_args(self, necessary_args: str):
        """Отображает окно с ошибкой,
        что отсутствуют нужные аргументы"""

        self.ui.error_text.setText("Отсутствуют нужные аргументы!\n"
                                   "Введите хотя бы одно из этих значений:\n"
                                   f"{necessary_args}")

        self.show()
