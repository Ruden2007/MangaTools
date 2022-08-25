from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

from my_widgets import TitleBar


class Ui_ErrorSample(object):
    def setupUi(self, ErrorSample):
        if not ErrorSample.objectName():
            ErrorSample.setObjectName(u"ErrorSample")
        ErrorSample.resize(370, 160)
        ErrorSample.setStyleSheet(u"#centralwidget{\n"
"	border-image: url(data/images/background3.jpg);\n"
"}")
        self.centralwidget = QWidget(ErrorSample)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.TitleBar = TitleBar(self.centralwidget)
        self.TitleBar.setObjectName(u"TitleBar")
        self.TitleBar.setContentsMargins(0, 2, 0, 3)
        self.TitleBar.setMaximumSize(QSize(16777215, 25))
        self.TitleBar.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"    border-radius: none;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	color: rgb(255, 255, 255);;\n"
"}\n"
"\n"
"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.horizontalLayout_5 = QHBoxLayout(self.TitleBar)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.title = QWidget(self.TitleBar)
        self.title.setObjectName(u"title")
        self.title.setStyleSheet(u"color: rgb(185, 34, 160);")
        self.horizontalLayout_3 = QHBoxLayout(self.title)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(12, 6, 0, 0)
        self.error_title = QLabel(self.title)
        self.error_title.setObjectName(u"error_title")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.error_title.sizePolicy().hasHeightForWidth())
        self.error_title.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.error_title.setFont(font)
        self.error_title.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.error_title)


        self.horizontalLayout_5.addWidget(self.title)

        self.titlebar_buttons = QWidget(self.TitleBar)
        self.titlebar_buttons.setObjectName(u"titlebar_buttons")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.titlebar_buttons.sizePolicy().hasHeightForWidth())
        self.titlebar_buttons.setSizePolicy(sizePolicy1)
        self.horizontalLayout_4 = QHBoxLayout(self.titlebar_buttons)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 5, 3)
        self.close_btn = QPushButton(self.titlebar_buttons)
        self.close_btn.setObjectName(u"close_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.close_btn.sizePolicy().hasHeightForWidth())
        self.close_btn.setSizePolicy(sizePolicy2)
        self.close_btn.setMaximumSize(QSize(15, 15))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.close_btn.setFont(font1)
        self.close_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.close_btn.setFlat(True)

        self.horizontalLayout_4.addWidget(self.close_btn)


        self.horizontalLayout_5.addWidget(self.titlebar_buttons)


        self.verticalLayout.addWidget(self.TitleBar)

        self.error = QWidget(self.centralwidget)
        self.error.setObjectName(u"error")
        self.error.setStyleSheet(u"color: rgb(185, 34, 160);")
        self.horizontalLayout_2 = QHBoxLayout(self.error)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(15, 0, 15, 0)
        self.error_text = QLabel(self.error)
        self.error_text.setObjectName(u"error_text")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.error_text.sizePolicy().hasHeightForWidth())
        self.error_text.setSizePolicy(sizePolicy3)
        self.error_text.setFont(font)
        self.error_text.setWordWrap(True)

        self.horizontalLayout_2.addWidget(self.error_text)


        self.verticalLayout.addWidget(self.error)

        self.buttons = QWidget(self.centralwidget)
        self.buttons.setObjectName(u"buttons")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.buttons.sizePolicy().hasHeightForWidth())
        self.buttons.setSizePolicy(sizePolicy4)
        self.buttons.setStyleSheet(u"QPushButton{\n"
"	border: 1px solid #8f8f91;\n"
"    border-radius: 8px;\n"
"	background-color: rgba(255, 255, 255, 90);\n"
"	color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border: 1px solid #8f8f91;\n"
"    border-radius: 10px;\n"
"	background-color: rgba(255, 255, 255, 110);\n"
"	color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 1px solid #8f8f91;\n"
"    border-radius: 8px;\n"
"	background-color: rgba(255, 220, 255, 100);\n"
"	color: rgb(255, 255, 255)\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.buttons)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 6, 6, 6)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.ok = QPushButton(self.buttons)
        self.ok.setObjectName(u"ok")
        self.ok.setMinimumSize(QSize(70, 0))
        self.ok.setFont(font)
        self.ok.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.ok)


        self.verticalLayout.addWidget(self.buttons)

        ErrorSample.setCentralWidget(self.centralwidget)

        self.retranslateUi(ErrorSample)

        QMetaObject.connectSlotsByName(ErrorSample)
    # setupUi

    def retranslateUi(self, ErrorSample):
        ErrorSample.setWindowTitle(QCoreApplication.translate("ErrorSample", u"MainWindow", None))
        self.error_title.setText(QCoreApplication.translate("ErrorSample", u"\u041e\u0448\u0438\u0431\u043a\u0430:", None))
        self.close_btn.setText(QCoreApplication.translate("ErrorSample", u"\u00d7", None))
        self.error_text.setText(QCoreApplication.translate("ErrorSample", u"\u041d\u0435\u0438\u0437\u0432\u0435\u0441\u0442\u043d\u0430\u044f \u043e\u0448\u0438\u0431\u043a\u0430!", None))
        self.ok.setText(QCoreApplication.translate("ErrorSample", u"\u041e\u043a", None))
    # retranslateUi

