import sys

from PySide6.QtCore import QSize
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QVBoxLayout, QApplication, QMainWindow, QWidget


class AboutApplication(QMainWindow):
    def __init__(self):
        super(AboutApplication, self).__init__()
        self.resize(550, 635)
        self.setMinimumSize(QSize(550, 635))
        self.setMaximumSize(QSize(16777215, 16777215))

        self.webV = QWebEngineView()
        self.webV.load("http://ruden.sytes.net/MangaTools/about/index.html")

        self.widget = QWidget(self)
        self.widget.setContentsMargins(0, 0, 0, 0)
        self.layout = QVBoxLayout(self.widget)
        self.layout.addWidget(self.webV)

        self.setCentralWidget(self.widget)


if __name__ == "__main__":
    app = QApplication([])

    web = AboutApplication()
    web.show()

    sys.exit(app.exec())
