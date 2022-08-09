from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow

import keyboard_tools
from Transcription import Transcript, ErrorTranscript
from ui_designer import Ui_AddSound

import py_win_keyboard_layout

import configparser

dictionary = configparser.ConfigParser()
dictionary.read("./dictionaries/keyboard.dict", "utf-8")


class AddSound(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(AddSound, self).__init__(*args, **kwargs)
        self.cleared_text = None
        self._pressed = False
        self.Direction = None

        # Фон прозрачный
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        # Нет границы
        self.setWindowFlag(Qt.FramelessWindowHint)

        # Отслеживание мыши
        self.setMouseTracking(True)

        self.ui = Ui_AddSound()
        self.ui.setupUi(self)

        self.keymap = "hir"

        # привязываем кнопки к событиям
        self.ui.close_btn.clicked.connect(self.ui.TitleBar.windowClosed.emit)
        self.ui.btn_kana.clicked.connect(self.change_keymap)
        self.ui.btn_clear.clicked.connect(self.clear)
        self.ui.btn_spliter.clicked.connect(lambda: self.keyboard_print(self.ui.btn_spliter.text()))

        self.ui.hir.clicked.connect(lambda: self.set_keymap("hir"))
        self.ui.kat.clicked.connect(lambda: self.set_keymap("kat"))
        self.ui.kun.clicked.connect(lambda: self.set_keymap("kun"))
        self.ui.hep.clicked.connect(lambda: self.set_keymap("hep"))
        self.ui.eng.clicked.connect(lambda: self.set_keymap("eng"))
        self.ui.rus.clicked.connect(lambda: self.set_keymap("rus"))
        self.ui.mean.clicked.connect(lambda: self.set_keymap("mean"))
        self.ui.mean2.clicked.connect(lambda: self.set_keymap("mean2"))

        keyboard_tools.add_sound_keyboard_button_connect(self)

        # кнопки авто-транскрипции
        self.ui.hir_auto.clicked.connect(self.auto_hir)
        self.ui.kat_auto.clicked.connect(self.auto_kat)
        self.ui.hep_auto.clicked.connect(self.auto_hep)
        self.ui.kun_auto.clicked.connect(self.auto_kun)

        # Привязываем событие изменения текста к функции смены цвета текста
        self.ui.hir.textChanged.connect(lambda: self.change_stylesheet(element=self.ui.hir))
        self.ui.kat.textChanged.connect(lambda: self.change_stylesheet(element=self.ui.kat))
        self.ui.kun.textChanged.connect(lambda: self.change_stylesheet(element=self.ui.kun))
        self.ui.hep.textChanged.connect(lambda: self.change_stylesheet(element=self.ui.hep))
        self.ui.eng.textChanged.connect(lambda: self.change_stylesheet(element=self.ui.eng))
        self.ui.rus.textChanged.connect(lambda: self.change_stylesheet(element=self.ui.rus))
        self.ui.mean.textChanged.connect(lambda: self.change_stylesheet_q_text_edit(element=self.ui.mean))
        self.ui.mean2.textChanged.connect(lambda: self.change_stylesheet_q_text_edit(element=self.ui.mean2))

        # слот сигнала
        self.ui.TitleBar.windowClosed.connect(self.close)
        self.ui.TitleBar.windowMoved.connect(self.move)

        self.keymap = "hir"

    # авто-транскрипция
    def auto_hir(self):
        """Генерирует автоматическую транскрипцию, если
        отсутствуют нужные аргументы возвращает окно с ошибкой"""

        if self.ui.kat.text():
            transcript_text = Transcript.kat_to_hir(text=self.ui.kat.text())
        else:
            return ErrorTranscript(self).missing_args("Катакана.")

        self.ui.hir.setText(transcript_text)

    def auto_kat(self):
        """Генерирует автоматическую транскрипцию, если
        отсутствуют нужные аргументы возвращает окно с ошибкой"""

        if self.ui.hir.text():
            transcript_text = Transcript.hir_to_kat(text=self.ui.hir.text())
        else:
            return ErrorTranscript(self).missing_args("Хирагана.")

        self.ui.kat.setText(transcript_text)

    def auto_kun(self):
        """Генерирует автоматическую транскрипцию, если
        отсутствуют нужные аргументы возвращает окно с ошибкой"""

        if self.ui.hir.text():
            transcript_text = Transcript.hir_to_kun(text=self.ui.hir.text())
        elif self.ui.kat.text():
            transcript_text = Transcript.kat_to_kun(text=self.ui.kat.text())
        else:
            return ErrorTranscript(self).missing_args("Хирагана, катакана.")

        self.ui.kun.setText(transcript_text)

    def auto_hep(self):
        """Генерирует автоматическую транскрипцию, если
        отсутствуют нужные аргументы возвращает окно с ошибкой"""

        if self.ui.hir.text():
            transcript_text = Transcript.hir_to_hep(text=self.ui.hir.text())
        elif self.ui.kat.text():
            transcript_text = Transcript.kat_to_hep(text=self.ui.kat.text())
        else:
            return ErrorTranscript(self).missing_args("Хирагана, катакана.")

        self.ui.hep.setText(transcript_text)

    # клавиатура
    def change_keymap(self):
        if self.keymap == "hir":
            self.set_keymap(keymap="kat")
        elif self.keymap == "kat":
            self.set_keymap(keymap="eng")
        elif self.keymap == "eng":
            self.set_keymap(keymap="hir")

    def set_keymap(self, keymap: str):
        """Устанавливает значение переменной раскладки
        значение переданное в переменной keymap если это
        значение hir(хирагана) или kat(катакана)то меняет
        раскладку экранной клавиатуры на соответствующую"""

        if keymap == "hir":
            keyboard_tools.set_keyboard_keymap(self=self.ui, kana="hiragana", keyboard="add_sound")
            py_win_keyboard_layout.change_foreground_window_keyboard_layout((int(
                dictionary['keyboard_layout_hex'].get('jap'), 16
            )))
            self.keymap = keymap
        elif keymap == "kat":
            keyboard_tools.set_keyboard_keymap(self=self.ui, kana="katakana", keyboard="add_sound")
            py_win_keyboard_layout.change_foreground_window_keyboard_layout((int(
                dictionary['keyboard_layout_hex'].get('jap'), 16
            )))
            self.keymap = keymap
        elif keymap in ["hep", "rus", "mean", "mean2"]:
            py_win_keyboard_layout.change_foreground_window_keyboard_layout(int(
                dictionary['keyboard_layout_hex'].get('rus'), 16
            ))
            self.keymap = keymap
        elif keymap in ["kun", "eng"]:
            keyboard_tools.set_keyboard_keymap(self=self.ui, kana="english", keyboard="add_sound")
            py_win_keyboard_layout.change_foreground_window_keyboard_layout((int(
                dictionary['keyboard_layout_hex'].get('eng'), 16
            )))
            self.keymap = keymap
        else:
            print("else")
            self.keymap = keymap

    def clear(self):
        if self.keymap == "hir":
            self.cleared_text = self.ui.kat.text()
            self.ui.hir.setText("")
        elif self.keymap == "kat":
            self.cleared_text = self.ui.kat.text()
            self.ui.kat.setText("")
        elif self.keymap == "kun":
            self.cleared_text = self.ui.kun.text()
            self.ui.kun.setText("")
        elif self.keymap == "hep":
            self.cleared_text = self.ui.hep.text()
            self.ui.hep.setText("")
        elif self.keymap == "eng":
            self.cleared_text = self.ui.eng.text()
            self.ui.eng.setText("")
        elif self.keymap == "rus":
            self.cleared_text = self.ui.rus.text()
            self.ui.rus.setText("")
        elif self.keymap == "mean":
            self.cleared_text = self.ui.mean.toPlainText()
            self.ui.mean.setText("")
        elif self.keymap == "mean2":
            self.cleared_text = self.ui.mean2.toPlainText()
            self.ui.mean2.setText("")

    def keyboard_print(self, text: str):
        """Активируется по нажатию кнопок на клавиатуре
           и вводит текст с этих кнопок в конец строки
           выбранной раскладки"""

        if self.keymap == "hir":
            self.ui.hir.setText(self.ui.hir.text() + text)
        elif self.keymap == "kat":
            self.ui.kat.setText(self.ui.kat.text() + text)
        elif self.keymap == "eng":
            self.ui.eng.setText(self.ui.eng.text() + text)
        elif self.keymap == "rus":
            self.ui.rus.setText(self.ui.rus.text() + text)

    @staticmethod
    def change_stylesheet(element):
        """Заменяет цвет текста если он не пустой(нужно чтобы
        placeholder отображался одного цвета, а после ввода текста
        введённый текст становился другого цвета)"""

        if element.text():
            element.setStyleSheet(u"color: rgba(255, 255, 255, 200)")
        else:
            element.setStyleSheet(u"color: rgba(255, 255, 255, 130)")

    @staticmethod
    def change_stylesheet_q_text_edit(element):
        """Заменяет цвет текста если он не пустой(нужно чтобы placeholder отображался
        другого цвета, а после ввода текста введённый текст становился другого цвета)"""

        if element.toPlainText():
            element.setStyleSheet(u"color: rgba(255, 255, 255, 200)")
        else:
            element.setStyleSheet(u"color: rgba(255, 255, 255, 130)")
