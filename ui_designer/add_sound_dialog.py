from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

from my_widgets import TitleBar


class Ui_AddSoundDialog(object):
    def setupUi(self, AddSoundDialog):
        if not AddSoundDialog.objectName():
            AddSoundDialog.setObjectName(u"AddSoundDialog")
        AddSoundDialog.resize(385, 445)
        AddSoundDialog.setMinimumSize(QSize(385, 385))
        AddSoundDialog.setMaximumSize(QSize(385, 16777215))
        AddSoundDialog.setStyleSheet(u"#centralwidget{\n"
"	border-image: url(data/images/background5.png);\n"
"}")
        self.centralwidget = QWidget(AddSoundDialog)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.TitleBar = TitleBar(self.centralwidget)
        self.TitleBar.setObjectName(u"TitleBar")
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
        self.horizontalLayout_5.setContentsMargins(0, 2, 0, 3)
        self.title = QWidget(self.TitleBar)
        self.title.setObjectName(u"title")
        self.title.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.horizontalLayout_3 = QHBoxLayout(self.title)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(12, 6, 0, 0)
        self.dialog_title = QLabel(self.title)
        self.dialog_title.setObjectName(u"dialog_title")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dialog_title.sizePolicy().hasHeightForWidth())
        self.dialog_title.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.dialog_title.setFont(font)
        self.dialog_title.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.dialog_title)


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

        self.text = QWidget(self.centralwidget)
        self.text.setObjectName(u"text")
        self.text.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.horizontalLayout_2 = QHBoxLayout(self.text)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(15, 0, 15, 0)
        self.dialog_text = QLabel(self.text)
        self.dialog_text.setObjectName(u"dialog_text")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.dialog_text.sizePolicy().hasHeightForWidth())
        self.dialog_text.setSizePolicy(sizePolicy3)
        self.dialog_text.setFont(font)
        self.dialog_text.setWordWrap(True)

        self.horizontalLayout_2.addWidget(self.dialog_text)


        self.verticalLayout.addWidget(self.text)

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
        self.horizontalLayout.setContentsMargins(6, 6, 6, 6)
        self.cancel = QPushButton(self.buttons)
        self.cancel.setObjectName(u"cancel")
        self.cancel.setMinimumSize(QSize(70, 0))
        self.cancel.setFont(font)
        self.cancel.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.cancel)

        self.save_local = QPushButton(self.buttons)
        self.save_local.setObjectName(u"save_local")
        self.save_local.setMinimumSize(QSize(160, 0))
        self.save_local.setFont(font)
        self.save_local.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.save_local)

        self.send = QPushButton(self.buttons)
        self.send.setObjectName(u"send")
        self.send.setMinimumSize(QSize(90, 0))
        self.send.setFont(font)
        self.send.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.send)


        self.verticalLayout.addWidget(self.buttons)

        AddSoundDialog.setCentralWidget(self.centralwidget)

        self.retranslateUi(AddSoundDialog)

        QMetaObject.connectSlotsByName(AddSoundDialog)
    # setupUi

    def retranslateUi(self, AddSoundDialog):
        AddSoundDialog.setWindowTitle(QCoreApplication.translate("AddSoundDialog", u"MainWindow", None))
        self.dialog_title.setText(QCoreApplication.translate("AddSoundDialog", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c \u0437\u0432\u0443\u043a \u043d\u0430 \u043c\u043e\u0434\u0435\u0440\u0430\u0446\u0438\u044e?", None))
        self.close_btn.setText(QCoreApplication.translate("AddSoundDialog", u"\u00d7", None))
        self.dialog_text.setText(QCoreApplication.translate("AddSoundDialog", u"<html><head/><body>\n"
"<p>\u0416\u0435\u043b\u0430\u0435\u0442\u0435 \u043e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c \u0437\u0432\u0443\u043a \u043d\u0430 \u043c\u043e\u0434\u0435\u0440\u0430\u0446\u0438\u044e \u0447\u0442\u043e\u0431\u044b \u043e\u043d<br/>\n"
"\u0431\u044b\u043b \u0434\u043e\u0431\u0430\u0432\u043b\u0435\u043d \u0432 \u0431\u0443\u0434\u0443\u0449\u0438\u0445 \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u044f\u0445 \u0431\u0430\u0437\u044b \u0434\u0430\u043d\u043d\u044b\u0445?</p>\n"
"\n"
"<p>\u0415\u0441\u043b\u0438 \u0432\u044b \u0441\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u0435 \u0437\u0432\u0443\u043a \u043b\u043e\u043a\u0430\u043b\u044c\u043d\u043e \u043e\u043d \u0431\u0443\u0434\u0435\u0442<br/>\n"
"\u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0430\u0442\u044c\u0441\u044f \u0432 \u043f\u043e\u0438\u0441\u043a\u0435 \u0441 \u043f\u0440\u0438\u0441\u0442\u0430\u0432\u043a\u043e\u0439 P(Personal Base)<br/>\n"
"\u0432\u043e\u0437\u043b\u0435 id(\u0446\u0438\u0444\u0435\u0440"
                        "\u043a\u0438 \u0432 \u043d\u0430\u0447\u0430\u043b\u0435 \u0441\u0442\u0440\u043e\u043a\u0438). \u041a\u043e\u0433\u0434\u0430 \u0436\u0435 \u044d\u0442\u043e\u0442 \u0437\u0432\u0443\u043a<br/>\n"
"\u0434\u043e\u0431\u0430\u0432\u0438\u0442\u0441\u044f \u0432 \u043e\u0441\u043d\u043e\u0432\u043d\u0443\u044e \u0431\u0430\u0437\u0443 \u0432\u044b \u0441\u043c\u043e\u0436\u0435\u0442\u0435 \u0443\u0434\u0430\u043b\u0438\u0442\u044c \u0437\u0432\u0443\u043a<br/>\n"
"\u0441\u043e\u0445\u0440\u0430\u043d\u0451\u043d\u043d\u044b\u0439 \u043b\u043e\u043a\u0430\u043b\u044c\u043d\u043e \u0432 \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430\u0445(\u0447\u0442\u043e\u0431\u044b<br/>\n"
"\u0438\u0437\u0431\u0435\u0436\u0430\u0442\u044c \u0434\u0443\u0431\u043b\u0438\u043a\u0430\u0442\u043e\u0432 \u043f\u0440\u0438 \u043f\u043e\u0438\u0441\u043a\u0435).</p>\n"
"\n"
"<p>\u0415\u0441\u043b\u0438 \u043d\u0430\u0436\u043c\u0451\u0442\u0435 \"\u043e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c\" \u0437\u0432\u0443\u043a"
                        " \u0441\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u0441\u044f<br/>\n"
"\u0443 \u0432\u0430\u0441 \u043b\u043e\u043a\u0430\u043b\u044c\u043d\u043e \u0438 \u0434\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u043e \u043e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u0441\u044f<br/>\n"
"\u043a\u043e \u043c\u043d\u0435 \u043d\u0430 \u043c\u043e\u0434\u0435\u0440\u0430\u0446\u0438\u044e \u0434\u043b\u044f \u0434\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u044f \u0432<br/>\n"
"\u0431\u0443\u0434\u0443\u0449\u0438\u0445 \u0432\u0435\u0440\u0441\u0438\u044f\u0445 \u0431\u0430\u0437\u0437\u044b \u0434\u0430\u043d\u043d\u044b\u0445.</p>\n"
"\n"
"<p>\u041f\u043e\u0434\u0440\u043e\u0431\u043d\u0435\u0435 \u043c\u043e\u0436\u0435\u0442\u0435 \u0443\u0437\u043d\u0430\u0442\u044c \u0432<br/>\u043f\u0440\u0435\u0434\u044b\u0434\u0443\u0449\u0435\u043c \u043e\u043a\u043d\u0435 \u043d\u0430\u0436\u0430\u0432 \u043a\u043d\u043e\u043f\u043a\u0443 &quot;\u041f\u043e\u043c\u043e\u0449\u044c&quot;.</p>\n"
"\n"
""
                        "<p><span style=\" color:#ff0000;\">\u041f\u0440\u0438\u043c\u0435\u0447\u0430\u043d\u0438\u0435: \u0435\u0441\u043b\u0438 \u0432\u044b \u0438\u0437 \u0420\u043e\u0441\u0441\u0438\u0438 \u043f\u043e\u0436\u0430\u043b\u0443\u0439\u0441\u0442\u0430<br/>\u0441\u043d\u0430\u0447\u0430\u043b\u0430 \u0432\u043a\u043b\u044e\u0447\u0438\u0442\u0435 \u043f\u0440\u043e\u043a\u0441\u0438 \u0441\u0435\u0440\u0432\u0435\u0440 \u0432 \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430\u0445<br/>(\u0414\u0440\u0443\u0433\u043e\u0435-&gt;API-&gt;\u0418\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u044c \u043f\u0440\u043e\u043a\u0441\u0438)!</span></p></body></html>", None))
        self.cancel.setText(QCoreApplication.translate("AddSoundDialog", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.save_local.setText(QCoreApplication.translate("AddSoundDialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043b\u043e\u043a\u0430\u043b\u044c\u043d\u043e", None))
        self.send.setText(QCoreApplication.translate("AddSoundDialog", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c", None))
    # retranslateUi

