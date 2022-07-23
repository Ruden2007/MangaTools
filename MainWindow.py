import sys

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, Signal)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
                               QLayout, QLineEdit, QMainWindow, QPushButton,
                               QScrollArea, QSizePolicy, QSpacerItem, QTabWidget,
                               QVBoxLayout, QWidget)


'''class TitleBar(QWidget):
    # Сигнал минимизации окна
    windowMinimumed = Signal()
    # увеличить максимальный сигнал окна
    windowMaximumed = Signal()
    # сигнал восстановления окна
    windowNormaled = Signal()
    # сигнал закрытия окна
    windowClosed = Signal()
    # Окно мобильных
    windowMoved = Signal(QPoint)
    # Сигнал Своя Кнопка +++
    signalButtonMy = Signal()

    def __init__(self, *args, **kwargs):
        super(TitleBar, self).__init__(*args, **kwargs)

        # Поддержка настройки фона qss
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.mPos = None
        self.iconSize = 20  # Размер значка по умолчанию

        # Установите цвет фона по умолчанию, иначе он будет прозрачным из-за влияния родительского окна
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(palette.Window, QColor(240, 240, 240))
        self.setPalette(palette)

        # макет
        layout = QHBoxLayout(self, spacing=0)
        layout.setContentsMargins(0, 0, 0, 0)

        # значок окна
        self.iconLabel = QLabel(self)
        #         self.iconLabel.setScaledContents(True)
        layout.addWidget(self.iconLabel)

        # название окна
        self.titleLabel = QLabel(self)
        self.titleLabel.setMargin(2)
        layout.addWidget(self.titleLabel)

        # Средний телескопический бар
        layout.addSpacerItem(QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))

        # Своя Кнопка ++++++++++++++++++++++++++
        self.buttonMy = QPushButton(
            '@', self, clicked=self.showButtonMy, objectName='buttonMy')
        layout.addWidget(self.buttonMy)

        # Свернуть кнопку
        self.buttonMinimum = QPushButton(
            '0', self, clicked=self.windowMinimumed.emit, objectName='buttonMinimum')
        layout.addWidget(self.buttonMinimum)

        # Кнопка Max / restore
        self.buttonMaximum = QPushButton(
            '1', self, clicked=self.showMaximized, objectName='buttonMaximum')
        layout.addWidget(self.buttonMaximum)

        # Кнопка закрытия
        self.buttonClose = QPushButton(
            'r', self, clicked=self.windowClosed.emit, objectName='buttonClose')
        layout.addWidget(self.buttonClose)

        # начальная высота
        self.setHeight()

        # +++ Вызывается по нажатию кнопки buttonMy
        def showButtonMy(self):
            print("Своя Кнопка ")
            self.signalButtonMy.emit()


        def showMaximized(self):
            if self.buttonMaximum.text() == '1':
                # Максимизировать
                self.buttonMaximum.setText('2')
                self.windowMaximumed.emit()
            else:  # Восстановить
                self.buttonMaximum.setText('1')
                self.windowNormaled.emit()


        def setHeight(self, height=20):
            """ Установка высоты строки заголовка """
            self.setMinimumHeight(height)
            self.setMaximumHeight(height)
            # Задайте размер правой кнопки  ?
            self.buttonMinimum.setMinimumSize(height, height)
            self.buttonMinimum.setMaximumSize(height, height)
            self.buttonMaximum.setMinimumSize(height, height)
            self.buttonMaximum.setMaximumSize(height, height)
            self.buttonClose.setMinimumSize(height, height)
            self.buttonClose.setMaximumSize(height, height)

            self.buttonMy.setMinimumSize(height, height)
            self.buttonMy.setMaximumSize(height, height)


        def setTitle(self, title):
            """ Установить заголовок """
            self.titleLabel.setText(title)


        def setIcon(self, icon):
            """ настройки значокa """
            self.iconLabel.setPixmap(icon.pixmap(self.iconSize, self.iconSize))


        def setIconSize(self, size):
            """ Установить размер значка """
            self.iconSize = size


        def enterEvent(self, event):
            self.setCursor(Qt.ArrowCursor)
            super(TitleBar, self).enterEvent(event)


        def mouseDoubleClickEvent(self, event):
            super(TitleBar, self).mouseDoubleClickEvent(event)
            self.showMaximized()


        def mousePressEvent(self, event):
            """ Событие клика мыши """
            if event.button() == Qt.LeftButton:
                self.mPos = event.position().toPoint()
            event.accept()


        def mouseReleaseEvent(self, event):
            """ Событие отказов мыши """
            self.mPos = None
            event.accept()


        def mouseMoveEvent(self, event):
            if event.buttons() == Qt.LeftButton and self.mPos:
                self.windowMoved.emit(self.mapToGlobal(event.position().toPoint() - self.mPos))
            event.accept()

    # Перечислить верхнюю левую, нижнюю правую и четыре неподвижные точки
    Left, Top, Right, Bottom, LeftTop, RightTop, LeftBottom, RightBottom = range(8)'''


class Ui_MainWindow(QWidget):

    def __init__(self, *args, **kwargs):
        super(Ui_MainWindow, self).__init__(*args, **kwargs)
        self.layout = QVBoxLayout(self)

        # инициализация вкладок
        self.tabs = QTabWidget()
        self.main_tab = QWidget()
        self.sounds_tab = QWidget()
        self.translate_tab = QWidget()
        self.clean_tab = QWidget()

        # добавление вкладок
        self.tabs.addTab(self.main_tab, "Главная")
        self.tabs.addTab(self.sounds_tab, "Звуки")
        self.tabs.addTab(self.translate_tab, "Перевод")
        self.tabs.addTab(self.clean_tab, "Клин")

        # добавление вкладок к виджету
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)



    def setupUi(self, MainWindow):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Ui_MainWindow()
    window.show()

    sys.exit(app.exec())
