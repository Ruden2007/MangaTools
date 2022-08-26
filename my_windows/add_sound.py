from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QKeySequence, QShortcut

import keyboard_tools
from Transcription import Transcript, ErrorTranscript
from ui_designer import Ui_AddSound, Ui_ErrorSample
from .add_sound_dialog import AddSoundDialog

import py_win_keyboard_layout

import configparser

dictionary = configparser.ConfigParser()
dictionary.read("./dictionaries/keyboard.dict", "utf-8")


class AddSoundErrors(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Нет границы
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowModality(Qt.ApplicationModal)

        self.ui = Ui_ErrorSample()
        self.ui.setupUi(self)

        self.ui.TitleBar.windowMoved.connect(self.move)
        self.ui.close_btn.clicked.connect(self.close)
        self.ui.ok.clicked.connect(self.close)

    def missing_args(self, necessary_args: str):
        self.ui.error_title.setText("Ошибка!")
        self.ui.error_text.setText("Отсутствуют нужные аргументы!\n"
                                   "Введите хотя бы одно из этих значений:\n"
                                   f"{necessary_args}")

        self.show()

    def warning(self, text: str):
        self.ui.error_title.setText("Предупреждение!")
        self.ui.error_text.setText(text)

        self.show()


class AddSound(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(AddSound, self).__init__(*args, **kwargs)
        self.dialog = AddSoundDialog()
        self.cleared_text = None
        self._pressed = False
        self.Direction = None

        # Фон прозрачный
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        # Нет границы
        self.setWindowFlag(Qt.FramelessWindowHint)

        # Отслеживание мыши
        self.setMouseTracking(True)

        # Клавиатурные сокращения:
        self.return_cleared_text_keys = QShortcut(QKeySequence('Ctrl+Z'), self)
        self.return_cleared_text_keys.activated.connect(self.return_cleared_text)

        self.ui = Ui_AddSound()
        self.ui.setupUi(self)

        # привязываем кнопки к событиям
        self.ui.close_btn.clicked.connect(self.ui.TitleBar.windowClosed.emit)
        self.ui.btn_kana.clicked.connect(self.change_keyboard_keymap)
        self.ui.btn_clear.clicked.connect(self.clear)
        self.ui.btn_spliter.clicked.connect(lambda: self.keyboard_print(self.ui.btn_spliter.text()))
        self.ui.ok.clicked.connect(self.show_dialog)

        # привязываем нажатие на поля ввода к смене раскладки клавиатуры
        self.ui.hir.clicked.connect(lambda: self.set_keymap("hir"))
        self.ui.kat.clicked.connect(lambda: self.set_keymap("kat"))
        self.ui.kun.clicked.connect(lambda: self.set_keymap("kun"))
        self.ui.hep.clicked.connect(lambda: self.set_keymap("hep"))
        self.ui.eng.clicked.connect(lambda: self.set_keymap("eng"))
        self.ui.rus.clicked.connect(lambda: self.set_keymap("rus"))
        self.ui.mean.clicked.connect(lambda: self.set_keymap("mean"))
        self.ui.mean2.clicked.connect(lambda: self.set_keymap("mean2"))

        # кнопки авто-транскрипции
        self.ui.hir_auto.clicked.connect(self.auto_hir)
        self.ui.kat_auto.clicked.connect(self.auto_kat)
        self.ui.hep_auto.clicked.connect(self.auto_hep)
        self.ui.kun_auto.clicked.connect(self.auto_kun)

        # функция привязки всех кнопок на клавиатуре к функции ввода текста
        keyboard_tools.add_sound_keyboard_button_connect(self)

        """Привязываем событие изменения текста к функции смены цвета текста
        для того чтобы текст отображался цвета отличного от placeholder-текста"""
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

        # раскладка по умолчанию
        self.keymap = "hir"

    # авто-транскрипция
    def auto_hir(self):
        """Генерирует автоматическую транскрипцию, если
        отсутствуют нужные аргументы возвращает окно с ошибкой"""

        if self.ui.kat.text():
            transcript_text = Transcript.kat_to_hir(text=self.ui.kat.text())
        else:
            return ErrorTranscript(self).missing_args("катакана.")

        self.ui.hir.setText(transcript_text)

    def auto_kat(self):
        """Генерирует автоматическую транскрипцию, если
        отсутствуют нужные аргументы возвращает окно с ошибкой"""

        if self.ui.hir.text():
            transcript_text = Transcript.hir_to_kat(text=self.ui.hir.text())
        else:
            return ErrorTranscript(self).missing_args("хирагана.")

        self.ui.kat.setText(transcript_text)

    def auto_kun(self):
        """Генерирует автоматическую транскрипцию, если
        отсутствуют нужные аргументы возвращает окно с ошибкой"""

        if self.ui.hir.text():
            transcript_text = Transcript.hir_to_kun(text=self.ui.hir.text())
        elif self.ui.kat.text():
            transcript_text = Transcript.kat_to_kun(text=self.ui.kat.text())
        else:
            return ErrorTranscript(self).missing_args("хирагана, катакана.")

        self.ui.kun.setText(transcript_text)

    def auto_hep(self):
        """Генерирует автоматическую транскрипцию, если
        отсутствуют нужные аргументы возвращает окно с ошибкой"""

        if self.ui.hir.text():
            transcript_text = Transcript.hir_to_hep(text=self.ui.hir.text())
        elif self.ui.kat.text():
            transcript_text = Transcript.kat_to_hep(text=self.ui.kat.text())
        else:
            return ErrorTranscript(self).missing_args("хирагана, катакана.")

        self.ui.hep.setText(transcript_text)

    # клавиатура
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
            keyboard_tools.set_keymap(self=self.ui, keymap="hiragana", keyboard='add_sound')
            py_win_keyboard_layout.change_foreground_window_keyboard_layout((int(
                dictionary['keyboard_layout_hex'].get('jap'), 16
            )))
            self.keymap = keymap
        elif keymap == "kat":
            keyboard_tools.set_keymap(self=self.ui, keymap="katakana", keyboard='add_sound')
            py_win_keyboard_layout.change_foreground_window_keyboard_layout((int(
                dictionary['keyboard_layout_hex'].get('jap'), 16
            )))
            self.keymap = keymap
        elif keymap in ["hep", "rus", "mean", "mean2"]:
            keyboard_tools.set_keymap(self=self.ui, keymap="russian", keyboard='add_sound')
            py_win_keyboard_layout.change_foreground_window_keyboard_layout(int(
                dictionary['keyboard_layout_hex'].get('rus'), 16
            ))
            self.keymap = keymap
        elif keymap in ["kun", "eng"]:
            keyboard_tools.set_keymap(self=self.ui, keymap="english", keyboard='add_sound')
            py_win_keyboard_layout.change_foreground_window_keyboard_layout((int(
                dictionary['keyboard_layout_hex'].get('eng'), 16
            )))
            self.keymap = keymap

    def clear(self):
        """В зависимости от установленной раскладки
        клавиатуры устанавливает соответствующему полю
        ввода значение текста как пустую строку и записывает
        удалённый текст в переменную self.cleared_text
        для возможности вернуть этот текст при
        нажатии клавиш ctrl + z"""

        if self.keymap == "hir":
            self.cleared_text = (self.ui.hir.text(), self.keymap)
            self.ui.hir.setText("")
        elif self.keymap == "kat":
            self.cleared_text = (self.ui.kat.text(), self.keymap)
            self.ui.kat.setText("")
        elif self.keymap == "kun":
            self.cleared_text = (self.ui.kun.text(), self.keymap)
            self.ui.kun.setText("")
        elif self.keymap == "hep":
            self.cleared_text = (self.ui.hep.text(), self.keymap)
            self.ui.hep.setText("")
        elif self.keymap == "eng":
            self.cleared_text = (self.ui.eng.text(), self.keymap)
            self.ui.eng.setText("")
        elif self.keymap == "rus":
            self.cleared_text = (self.ui.rus.text(), self.keymap)
            self.ui.rus.setText("")
        elif self.keymap == "mean":
            self.cleared_text = (self.ui.mean.toPlainText(), self.keymap)
            self.ui.mean.setText("")
        elif self.keymap == "mean2":
            self.cleared_text = (self.ui.mean2.toPlainText(), self.keymap)
            self.ui.mean2.setText("")

    def return_cleared_text(self):
        """Активируется при нажатии клавиш ctrl + z и вводит текст
        self.cleared_text[0] в поле ввода self.cleared_text[1].
        Почему-то не работает после нажатия на другие поля
        ввода хотя текст записанный в self.cleared_text
        остаётся прежним"""

        if self.cleared_text:
            self.set_keymap(keymap=self.cleared_text[1])
            self.keyboard_print(self.cleared_text[0])

    def keyboard_print(self, text: str):
        """Активируется по нажатию кнопок на клавиатуре
           и вводит текст с этих кнопок в конец строки
           выбранной раскладки"""

        if self.keymap == "hir":
            self.ui.hir.setText(self.ui.hir.text() + text)
        elif self.keymap == "kat":
            self.ui.kat.setText(self.ui.kat.text() + text)
        elif self.keymap == "hep":
            self.ui.hep.setText(self.ui.hep.text() + text)
        elif self.keymap == "kun":
            self.ui.kun.setText(self.ui.kun.text() + text)
        elif self.keymap == "eng":
            self.ui.eng.setText(self.ui.eng.text() + text)
        elif self.keymap == "rus":
            self.ui.rus.setText(self.ui.rus.text() + text)
        elif self.keymap == "mean":
            self.ui.mean.setText(self.ui.mean.toPlainText() + text)
        elif self.keymap == "mean2":
            self.ui.mean2.setText(self.ui.mean2.toPlainText() + text)

    # окна
    def show_dialog(self):
        """Открываем окно диалога с выбором: отправлять
         звук на модерацию или сохранить локально"""
        print("show")

        if not any((self.ui.hir.text(), self.ui.kat.text(), self.ui.kun.text(), self.ui.hep.text())):
            return AddSoundErrors(self).missing_args("хирагана, катакана, кунрей, хэпбёрн.")

        if self.ui.hir.text() or self.ui.kat.text():
            necessary_args = []
            if not self.ui.hir.text():
                necessary_args.append("хирагана")
            if not self.ui.kat.text():
                necessary_args.append("катакана")
            if not self.ui.kun.text():
                necessary_args.append("кунрей")
            if not self.ui.hep.text():
                necessary_args.append("хепбёрн")

            if necessary_args:
                count = len(necessary_args)
                return AddSoundErrors(self).warning(
                    text=f'{"Отсутствуют следующие аргументы:" if count > 1 else "Отсутствует следующий аргумент:"}'
                         f'\n{", ".join(necessary_args)}.\nПросто нажмите кнопку "auto" возле '
                         f'{"соответствующих полей" if count > 1 else "соответствующего поля"} чтобы '
                         f'автоматически сгенерировать {"их" if count > 1 else "его"}.')
        data = {
        'kun': self.ui.kun.text(),
        'hep': self.ui.hep.text(),
        'hir': self.ui.hir.text(),
        'kat': self.ui.kat.text(),
        'eng': self.ui.eng.text(),
        'rus': self.ui.rus.text(),
        'mean': self.ui.mean.toPlainText(),
        'mean2': self.ui.mean2.toPlainText()
    }
        self.dialog.add_send_data(data)
        self.dialog.show()

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
