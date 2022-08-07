from PySide6.QtWidgets import QWidget

import keyboard_tools
from ui_designer.main_keyboard import Ui_main_keyboard


class MainKeyboard(QWidget):
    def __init__(self, *args, **kwargs):
        super(MainKeyboard, self).__init__(*args, **kwargs)
        self.ki = Ui_main_keyboard()
        self.ki.setupUi(self)

        self.katakana = False

    def change_kana(self):
        """Изменяет раскладку экранной клавиатуры
        (заменяет текст внутри кнопок)"""

        if self.katakana:
            keyboard_tools.set_keyboard_kana(self=self.ki, kana="hiragana")
            self.katakana = False
        else:
            keyboard_tools.set_keyboard_kana(self=self.ki, kana="katakana")
            self.katakana = True