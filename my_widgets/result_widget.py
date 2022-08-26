from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel

from my_widgets import ClickToCopyLabel, SoundIDLabel


class ResultWidget(QWidget):
    def __init__(self, result: tuple, *args, **kwargs):
        super(ResultWidget, self).__init__(*args, **kwargs)

        self.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        # объявляем заголовок
        self.header = QWidget()
        self.header_layout = QHBoxLayout(self.header)
        self.header_layout.setContentsMargins(0, 0, 0, 0)
        self.header_layout.setSpacing(0)

        # объявляем строки с переводом
        self.translation = QWidget()
        self.translation_layout = QHBoxLayout(self.translation)
        self.translation_layout.setContentsMargins(0, 0, 0, 0)
        self.translation_layout.setSpacing(0)

        # объявляем строки со значением
        self.meaning = QWidget()
        self.meaning_layout = QHBoxLayout(self.meaning)
        self.meaning_layout.setContentsMargins(0, 0, 0, 0)
        self.translation_layout.setSpacing(0)

        # кнопки для заголовка
        self.add_header_button(result)

        # кнопки для перевода
        self.add_translate_result(result[5], label_text="Английский: ", db_id=result[0])
        self.add_translate_result(result[6], label_text="Русский: ", db_id=result[0])

        # добавляем строки для значения
        self.add_meaning(result=result[7], label_text="Значение: ")
        self.add_meaning(result=result[8], label_text="Уточнённое значение: ")

        # добавляем прижим элементов к левому краю
        self.header_layout.addStretch()
        self.translation_layout.addStretch()
        self.meaning_layout.addStretch()

        # добавляем виджеты в основной
        self.layout.addWidget(self.header)
        self.layout.addWidget(self.translation)
        self.layout.addWidget(self.meaning)

    def add_header_button(self, result):
        db_id = result[0]
        clik_to_copy_id = SoundIDLabel(f"{result[0]}", db_id=db_id)
        clik_to_copy_kun = ClickToCopyLabel(f"{result[1]}", db_id=db_id)
        clik_to_copy_hep = ClickToCopyLabel(f"{result[2]}", db_id=db_id)
        clik_to_copy_hir = ClickToCopyLabel(f"{result[3]}", db_id=db_id)
        clik_to_copy_kat = ClickToCopyLabel(f"{result[4]}", db_id=db_id)

        self.header_layout.addWidget(clik_to_copy_id)
        self.header_layout.addWidget(clik_to_copy_kun)
        self.header_layout.addWidget(clik_to_copy_hep)
        self.header_layout.addWidget(clik_to_copy_hir)
        self.header_layout.addWidget(clik_to_copy_kat)

    def add_translate_result(self, result, label_text: str, db_id: int):
        if "," in result:
            split_result = result.split(', ')

            label_eng = QLabel(label_text)
            self.translation_layout.addWidget(label_eng)
            for r in split_result:
                clik_to_copy = ClickToCopyLabel(text=f"{r}", db_id=db_id)

                self.translation_layout.addWidget(clik_to_copy)

        else:
            if result == "":
                pass
            elif result == " ":
                pass
            elif result == "\n":
                pass
            else:
                label_eng = QLabel(label_text)
                self.translation_layout.addWidget(label_eng)

                clik_to_copy = ClickToCopyLabel(f"{result}", db_id=db_id)

                self.translation_layout.addWidget(clik_to_copy)

    def add_meaning(self, result, label_text: str):
        if result == "":
            pass
        elif result == " ":
            pass
        elif result == "\n":
            pass
        else:
            label_mean = QLabel(label_text)
            self.meaning_layout.addWidget(label_mean)

            label2_mean = QLabel(f"{result}")
            self.meaning_layout.addWidget(label2_mean)
