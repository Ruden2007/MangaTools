import pyperclip
from PySide6.QtCore import Qt
from PySide6.QtGui import QCursor
from PySide6.QtWidgets import QLabel


class ClickToCopyLabel(QLabel):
    def __init__(self, text: str, db_id: int, fav: object, *args, **kwargs):
        super(ClickToCopyLabel, self).__init__(*args, **kwargs)
        self.fav = fav

        self.setText(text)

        self.db_id = db_id

        self.setCursor(QCursor(Qt.PointingHandCursor))
        self.setStyleSheet("margin-right: 5px;")

    def mousePressEvent(self, event):
        if self.fav.is_favorite(self.db_id):
            self.fav.update_uses(self.db_id)
        pyperclip.copy(self.text())


class SoundIDLabel(QLabel):
    def __init__(self, text: str, db_id: int, fav: object, *args, **kwargs):
        super(SoundIDLabel, self).__init__(*args, **kwargs)
        self.db_id = db_id
        self.fav = fav

        self.favorite = self.fav.is_favorite(self.db_id)

        if self.favorite:
            self.setText(text + " ☆")
        else:
            self.setText(text)

        self.setCursor(QCursor(Qt.PointingHandCursor))
        self.setStyleSheet("margin-right: 5px;")

    def mouseDoubleClickEvent(self, event):
        if self.favorite:
            self.setText(f'{self.db_id}')
            self.fav.remove_sound(self.db_id)
            self.favorite = False
        else:
            self.setText(f'{self.db_id}' + " ☆")
            self.fav.add_sound(self.db_id)
            self.favorite = True
