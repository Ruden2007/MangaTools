import sys
from typing import Iterable
import time

from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QFont

import keyboard_tools
from data_base import SoundSearch, PersonalBase, FavoriteSounds

from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QLabel, QApplication, QWidget

from my_windows import AddSound
from sqlite import pb
from ui_designer import Ui_MainWindow
from my_widgets import ResultWidget, MainKeyboard


class MangaTools(QMainWindow):
    resized = Signal()

    def __init__(self):
        super(MangaTools, self).__init__()
        self.time = time.time

        self._db = pb
        self.favorites = FavoriteSounds()

        self.add_sound_window = AddSound()
        self.sound_search = SoundSearch()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.widget = QWidget(self)
        self.layout = QVBoxLayout(self.widget)
        self.ui.scrollArea.setWidget(self.widget)
        self.ui.scrollArea.setWidgetResizable(True)

        # Подключаем кнопки
        self.ui.searchButton.clicked.connect(self.start_search)
        self.ui.search_input.returnPressed.connect(self.start_search)
        self.ui.btn_keyboard.clicked.connect(self.show_or_hide_main_keyboard)
        self.ui.btn_add_sound.clicked.connect(self.show_add_sound)
        self.ui.btn_favorite.clicked.connect(self.show_favorites)

        self.main_keyboard = MainKeyboard(self)
        self.ui.body_sounds.addWidget(self.main_keyboard)
        self.main_keyboard.show()
        self.main_keyboard.hide()
        self.main_keyboard_hide = True

        keyboard_tools.connect_keyboard_button(self)

        # noinspection PyUnresolvedReferences
        self.resized.connect(self.resize_widgets)

    # изменение размеров
    # noinspection PyUnresolvedReferences
    def resizeEvent(self, event):
        """Отслеживает изменение размеров окна"""

        self.resized.emit()
        return super(MangaTools, self).resizeEvent(event)

    def resize_widgets(self):
        """Устанавливаем всему виджету экранной
        максимальную ширину, умножаем высоту кнопок
        на их количество и прибавляем значение 6ти
        отступов по 2 единицы между ними"""

        h = self.main_keyboard.ki.btn_a.height()
        self.main_keyboard.setMaximumWidth((h * 5) + (2 * 6))

        font = QFont()
        font.setPixelSize(h / 2.1)
        self.main_keyboard.ki.btn_small.setFont(font)

    # поиск и отображение
    def start_search(self):
        query = self.ui.search_input.text()
        self.searching(query=query)

    def searching(self, query):
        start_time = self.time()
        self.clear_searching_results()
        print(f"clear results time = {self.time() - start_time}")
        start_time2 = self.time()
        results = self.sound_search.search(search_input=query)
        print(f"search results time = {self.time() - start_time2}")
        start_time3 = self.time()
        self.show_results(results=results)
        print(f"show result time = {self.time() - start_time3}")
        print(f"all show result time = {self.time() - start_time}")

    def show_favorites(self):
        self.clear_searching_results()

        ids = self._db.get_favorites()
        result = []

        for db_id in ids:
            result.append(self.sound_search.fetch_from_id(db_id[0]))

        self.show_results(result)

    # noinspection PyTypeChecker
    def clear_searching_results(self):
        """Создаёт новый экземпляр виджета для
        self.ui.scrollArea и переопределяет главный
        виджет для self.ui.scrollArea это сделано для
        ускорения работы так как при удалении каждого
        виджета результатов поиска требуется в 18-19
        раз больше времени чем на удаление всего
        виджета хранящего эти результаты.

        Старый вариант:
        for i in reversed(range(self.layout.count())):
            self.layout.itemAt(i).widget().setParent(None)"""

        self.widget = QWidget(self)
        self.layout = QVBoxLayout(self.widget)
        self.ui.scrollArea.setWidget(self.widget)

    def show_results(self, results: Iterable):
        """Выводит результаты поиска если таковые есть
        иначе выводит надпись, что ничего не найдено"""
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
        """Скрывает либо, показывает экранную
        клавиатуру на вкладке со звуками"""

        if self.main_keyboard_hide:
            self.main_keyboard.show()
            self.main_keyboard_hide = False
            self.resize_widgets()
        else:
            self.main_keyboard.hide()
            self.main_keyboard_hide = True
            self.resize_widgets()

    def keyboard_print(self, text: str):
        """Активируется по нажатию кнопок на клавиатуре
        и вводит текст с этих кнопок в конец строки поискового ввода"""

        self.ui.search_input.setText(self.ui.search_input.text() + text)

    def add_sound_mark(self):
        """Добавляет к японским буквам спец символы
        (заменяет текущую букву на букву со спецсимволом
        из словаря dictionary_file.dict)"""

        text = self.ui.search_input.text()
        try:
            letter = text[-1]
        except IndexError:
            return
        mark_letter = keyboard_tools.add_mark(letter)
        self.ui.search_input.setText(text[:-1] + mark_letter)

    def change_letter_size(self):
        """Заменяет последнюю японскую букву в строке
        поискового ввода на букву нижнего регистра
        (если такая есть в файле dictionary_file.dict)"""

        text = self.ui.search_input.text()
        try:
            letter = text[-1]
        except IndexError:
            return
        letter = keyboard_tools.change_letter_size(letter)
        self.ui.search_input.setText(text[:-1] + letter)

    def backspace(self):
        """Удаляет последнюю букву в строке поискового ввода"""

        text = self.ui.search_input.text()
        try:
            text[-1]
        except IndexError:
            return
        self.ui.search_input.setText(text[:-1])

    def clear_search_input(self):
        """Очищает строку поискового ввода"""

        self.ui.search_input.setText("")

    # Окна
    def show_add_sound(self):
        self.add_sound_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MangaTools()
    window.show()

    sys.exit(app.exec())
