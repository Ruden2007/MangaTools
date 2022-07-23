import sys

from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QFont

<<<<<<< HEAD
import keyboard_tools
from Transcription import Transcript, ErrorTranscript
from data_base import SoundSearch

from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QLabel, QApplication, QWidget, QMessageBox

from my_windows import AddSound
from ui_designer import Ui_MainWindow
=======
import utils
from data_base import SoundSearch

from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QLabel, QApplication, QWidget

from main_window import Ui_MainWindow
>>>>>>> 62e99dd (first commit)
from main_keyboard import Ui_main_keyboard
from my_widgets import ResultWidget


class MainKeyboard(QWidget):
    def __init__(self, *args, **kwargs):
        super(MainKeyboard, self).__init__(*args, **kwargs)
        self.ki = Ui_main_keyboard()
        self.ki.setupUi(self)

        self.katakana = False

    def change_kana(self):
<<<<<<< HEAD
        """Изменяет раскладку экранной клавиатуры
        (заменяет текст внутри кнопок)"""

        if self.katakana:
            keyboard_tools.set_keyboard_kana(self=self.ki, kana="hiragana")
            self.katakana = False
        else:
            keyboard_tools.set_keyboard_kana(self=self.ki, kana="katakana")
=======
        if self.katakana:
            utils.set_keyboard_kana(self, kana="hiragana")
            self.katakana = False
        else:
            utils.set_keyboard_kana(self, kana="katakana")
>>>>>>> 62e99dd (first commit)
            self.katakana = True


class MangaTools(QMainWindow):
    resized = Signal()

    def __init__(self):
        super(MangaTools, self).__init__()

<<<<<<< HEAD
        self.add_sound_window = AddSound()
=======
>>>>>>> 62e99dd (first commit)
        self.sound_search = SoundSearch()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.widget = QWidget(self)
        self.layout = QVBoxLayout(self.widget)
        self.ui.scrollArea.setWidget(self.widget)
        self.ui.scrollArea.setWidgetResizable(True)

<<<<<<< HEAD
        # Подключаем кнопки
        self.ui.searchButton.clicked.connect(self.start_search)
        self.ui.search_input.returnPressed.connect(self.start_search)
        self.ui.btn_keyboard.clicked.connect(self.show_or_hide_main_keyboard)
        self.ui.btn_add_sound.clicked.connect(self.show_add_sound)
=======
        self.ui.searchButton.clicked.connect(self.start_search)
        self.ui.search_input.returnPressed.connect(self.start_search)
        self.ui.btn_keyboard.clicked.connect(self.show_or_hide_main_keyboard)
>>>>>>> 62e99dd (first commit)

        self.main_keyboard = MainKeyboard(self)
        self.ui.body_sounds.addWidget(self.main_keyboard)
        self.main_keyboard.show()
        self.main_keyboard.hide()
        self.main_keyboard_hide = True

<<<<<<< HEAD
        keyboard_tools.connect_keyboard_button(self)
=======
        utils.connect_keyboard_button(self)
>>>>>>> 62e99dd (first commit)

        # noinspection PyUnresolvedReferences
        self.resized.connect(self.resize_widgets)

    # изменение размеров
    # noinspection PyUnresolvedReferences
    def resizeEvent(self, event):
<<<<<<< HEAD
        """Отслеживает изменение размеров окна"""

=======
>>>>>>> 62e99dd (first commit)
        self.resized.emit()
        return super(MangaTools, self).resizeEvent(event)

    def resize_widgets(self):
        """Устанавливаем всему виджету максимальную ширину, умножаем высоту кнопок на их
           количество и прибавляем значение 6ти отступов по 2 единицы между ними"""
<<<<<<< HEAD

=======
>>>>>>> 62e99dd (first commit)
        h = self.main_keyboard.ki.btn_a.height()
        self.main_keyboard.setMaximumWidth((h * 5) + (2 * 6))

        font = QFont()
<<<<<<< HEAD
        font.setPixelSize(h / 2.1)
=======
        font.setPixelSize(h/2.1)
>>>>>>> 62e99dd (first commit)
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
<<<<<<< HEAD
        """Выводит результаты поиска если таковые есть
        иначе выводит надпись, что ничего не найдено"""

=======
>>>>>>> 62e99dd (first commit)
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
<<<<<<< HEAD
        """Скрывает либо, показывает экранную
        клавиатуру на вкладке со звуками"""

=======
>>>>>>> 62e99dd (first commit)
        if self.main_keyboard_hide:
            self.main_keyboard.show()
            self.main_keyboard_hide = False
            self.resize_widgets()
        else:
            self.main_keyboard.hide()
            self.main_keyboard_hide = True
            self.resize_widgets()

    def keyboard_print(self, text: str):
<<<<<<< HEAD
        """Активируется по нажатию кнопок на клавиатуре
        и вводит текст с этих кнопок в конец строки поискового ввода"""

        self.ui.search_input.setText(self.ui.search_input.text() + text)

    def add_sound_mark(self):
        """Добавляет к японским буквам спец символы
        (заменяет текущую букву на букву со спецсимволом
        из словаря dictionary_file.dict)"""

=======
        self.ui.search_input.setText(self.ui.search_input.text() + text)

    def add_sound_mark(self):
>>>>>>> 62e99dd (first commit)
        text = self.ui.search_input.text()
        try:
            letter = text[-1]
        except IndexError:
            return
<<<<<<< HEAD
        mark_letter = keyboard_tools.add_mark(letter)
        self.ui.search_input.setText(text[:-1] + mark_letter)

    def change_letter_size(self):
        """Заменяет последнюю японскую букву в строке
        поискового ввода на букву нижнего регистра
        (если такая есть в файле dictionary_file.dict)"""

=======
        mark_letter = utils.add_mark(letter)
        self.ui.search_input.setText(text[:-1] + mark_letter)

    def change_letter_size(self):
>>>>>>> 62e99dd (first commit)
        text = self.ui.search_input.text()
        try:
            letter = text[-1]
        except IndexError:
            return
<<<<<<< HEAD
        letter = keyboard_tools.change_letter_size(letter)
        self.ui.search_input.setText(text[:-1] + letter)

    def backspace(self):
        """Удаляет последнюю букву в строке поискового ввода"""

=======
        letter = utils.change_letter_size(letter)
        self.ui.search_input.setText(text[:-1] + letter)

    def backspace(self):
>>>>>>> 62e99dd (first commit)
        text = self.ui.search_input.text()
        try:
            text[-1]
        except IndexError:
            return
        self.ui.search_input.setText(text[:-1])

    def clear_search_input(self):
<<<<<<< HEAD
        """Очищает строку поискового ввода"""

        self.ui.search_input.setText("")

    # Окна
    def show_add_sound(self):
        self.add_sound_window.show()

=======
        self.ui.search_input.setText("")

>>>>>>> 62e99dd (first commit)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MangaTools()
    window.show()

    sys.exit(app.exec())
