import sys

from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QFont

import utils
from data_base import SoundSearch

from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QLabel, QApplication, QWidget

from main_window import Ui_MainWindow
from main_keyboard import Ui_main_keyboard
from my_widgets import ResultWidget


class MainKeyboard(QWidget):
    def __init__(self, *args, **kwargs):
        super(MainKeyboard, self).__init__(*args, **kwargs)
        self.ki = Ui_main_keyboard()
        self.ki.setupUi(self)

        self.katakana = False

    def change_kana(self):
        if self.katakana:
            utils.set_keyboard_kana(self, kana="hiragana")
            self.katakana = False
        else:
            utils.set_keyboard_kana(self, kana="katakana")
            self.katakana = True


class MangaTools(QMainWindow):
    resized = Signal()

    def __init__(self):
        super(MangaTools, self).__init__()

        self.sound_search = SoundSearch()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.widget = QWidget(self)
        self.layout = QVBoxLayout(self.widget)
        self.ui.scrollArea.setWidget(self.widget)
        self.ui.scrollArea.setWidgetResizable(True)

        self.ui.searchButton.clicked.connect(self.start_search)
        self.ui.search_input.returnPressed.connect(self.start_search)
        self.ui.btn_keyboard.clicked.connect(self.show_or_hide_main_keyboard)

        self.main_keyboard = MainKeyboard(self)
        self.ui.body_sounds.addWidget(self.main_keyboard)
        self.main_keyboard.show()
        self.main_keyboard.hide()
        self.main_keyboard_hide = True

        utils.connect_keyboard_button(self)

        # noinspection PyUnresolvedReferences
        self.resized.connect(self.resize_widgets)

    # изменение размеров
    # noinspection PyUnresolvedReferences
    def resizeEvent(self, event):
        self.resized.emit()
        return super(MangaTools, self).resizeEvent(event)

    def resize_widgets(self):
        """Устанавливаем всему виджету максимальную ширину, умножаем высоту кнопок на их
           количество и прибавляем значение 6ти отступов по 2 единицы между ними"""
        h = self.main_keyboard.ki.btn_a.height()
        self.main_keyboard.setMaximumWidth((h * 5) + (2 * 6))

        font = QFont()
        font.setPixelSize(h/2.1)
        self.main_keyboard.ki.btn_small.setFont(font)

    # поиск и отображение
    def start_search(self):
        query = self.ui.search_input.text()
        self.searching(query=query)

    def searching(self, query):
        self.clear_searching_results()
        results = self.sound_search.search(search_input=query)
        self.show_results(results=results)

    # noinspection PyTypeChecker
    def clear_searching_results(self):
        for i in reversed(range(self.layout.count())):
            self.layout.itemAt(i).widget().setParent(None)

    def show_results(self, results: list):
        if results:
            for result in results:
                w = ResultWidget(result=result)

                self.layout.addWidget(w)
        else:
            label = QLabel("Ничего не найдено, попробуйте изменить запрос!")
            label.setStyleSheet(u"background-color: rgba(225, 225, 225, 0)")
            label.setAlignment(Qt.AlignCenter)
            font = QFont()
            font.setPixelSize(18)
            label.setFont(font)
            self.layout.addWidget(label)

    # клавиатура
    def show_or_hide_main_keyboard(self):
        if self.main_keyboard_hide:
            self.main_keyboard.show()
            self.main_keyboard_hide = False
            self.resize_widgets()
        else:
            self.main_keyboard.hide()
            self.main_keyboard_hide = True
            self.resize_widgets()

    def keyboard_print(self, text: str):
        self.ui.search_input.setText(self.ui.search_input.text() + text)

    def add_sound_mark(self):
        text = self.ui.search_input.text()
        try:
            letter = text[-1]
        except IndexError:
            return
        mark_letter = utils.add_mark(letter)
        self.ui.search_input.setText(text[:-1] + mark_letter)

    def change_letter_size(self):
        text = self.ui.search_input.text()
        try:
            letter = text[-1]
        except IndexError:
            return
        letter = utils.change_letter_size(letter)
        self.ui.search_input.setText(text[:-1] + letter)

    def backspace(self):
        text = self.ui.search_input.text()
        try:
            text[-1]
        except IndexError:
            return
        self.ui.search_input.setText(text[:-1])

    def clear_search_input(self):
        self.ui.search_input.setText("")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MangaTools()
    window.show()

    sys.exit(app.exec())
