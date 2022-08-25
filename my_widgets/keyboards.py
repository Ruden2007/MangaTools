from PySide6.QtWidgets import QWidget

import keyboard_tools
from ui_designer.main_keyboard import Ui_main_keyboard

import py_win_keyboard_layout

import configparser

dictionary = configparser.ConfigParser()
dictionary.read("./dictionaries/keyboard.dict", "utf-8")


class MainKeyboard(QWidget):
    def __init__(self, *args, **kwargs):
        super(MainKeyboard, self).__init__(*args, **kwargs)
        self.ki = Ui_main_keyboard()
        self.ki.setupUi(self)

        self.keymap = "hir"

    def change_keyboard_keymap(self):
        """В зависимости от текущей раскладки
        клавиатуры устанавливает следующую по счёту по
        нажатию кнопки - смены раскладки на клавиатуре"""

        if self.keymap == "hir":
            self.set_keymap(keymap="kat")
        elif self.keymap == "kat":
            self.set_keymap(keymap="eng")
        elif self.keymap == "eng":
            self.set_keymap(keymap="rus")
        elif self.keymap in ["kun", "eng"]:
            self.set_keymap(keymap="rus")
        elif self.keymap in ["hep", "rus", "mean", "mean2"]:
            self.set_keymap(keymap="hir")

    def set_keymap(self, keymap: str):
        """Устанавливает значение переменной раскладки
        значение переданное в переменной keymap если это
        значение hir(хирагана) или kat(катакана)то меняет
        раскладку экранной клавиатуры на соответствующую"""

        if keymap == "hir":
            keyboard_tools.set_keymap(self=self.ki, keymap="hiragana", keyboard='main')
            py_win_keyboard_layout.change_foreground_window_keyboard_layout((int(
                dictionary['keyboard_layout_hex'].get('jap'), 16
            )))
            self.keymap = keymap
        elif keymap == "kat":
            keyboard_tools.set_keymap(self=self.ki, keymap="katakana", keyboard='main')
            py_win_keyboard_layout.change_foreground_window_keyboard_layout((int(
                dictionary['keyboard_layout_hex'].get('jap'), 16
            )))
            self.keymap = keymap
        elif keymap in ["hep", "rus", "mean", "mean2"]:
            keyboard_tools.set_keymap(self=self.ki, keymap="russian", keyboard='main')
            py_win_keyboard_layout.change_foreground_window_keyboard_layout(int(
                dictionary['keyboard_layout_hex'].get('rus'), 16
            ))
            self.keymap = keymap
        elif keymap in ["kun", "eng"]:
            keyboard_tools.set_keymap(self=self.ki, keymap="english", keyboard='main')
            py_win_keyboard_layout.change_foreground_window_keyboard_layout((int(
                dictionary['keyboard_layout_hex'].get('eng'), 16
            )))
            self.keymap = keymap

    def change_kana(self):
        """Изменяет раскладку экранной клавиатуры
        (заменяет текст внутри кнопок)"""

        if self.keymap == "hiragana":
            keyboard_tools.set_keymap(self=self.ki, keymap="katakana", keyboard="main")
            self.keymap = "katakana"
        elif self.keymap == "katakana":
            keyboard_tools.set_keymap(self=self.ki, keymap="hiragana", keyboard="main")
            self.keymap = "hiragana"
