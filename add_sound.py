from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QTextEdit, QVBoxLayout,
    QWidget)

from my_widgets import TitleBar

class Ui_AddSound(object):
    def setupUi(self, AddSound):
        if not AddSound.objectName():
            AddSound.setObjectName(u"AddSound")
        AddSound.resize(375, 585)
        AddSound.setMinimumSize(QSize(375, 585))
        AddSound.setMaximumSize(QSize(375, 585))
        AddSound.setStyleSheet(u"#centralwidget{\n"
"	border-image: url(data/images/background2.jpg);\n"
"}\n"
"\n"
"#main{\n"
"	border-image: None;\n"
"}")
        self.centralwidget = QWidget(AddSound)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(6, 0, 6, 6)
        self.main = QWidget(self.centralwidget)
        self.main.setObjectName(u"main")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main.sizePolicy().hasHeightForWidth())
        self.main.setSizePolicy(sizePolicy)
        self.main.setStyleSheet(u"QLineEdit, QTextEdit{\n"
"	border: 1px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"	background-color: rgba(255, 255, 255, 50);\n"
"	color: rgba(225, 225, 225, 140)\n"
"}\n"
"\n"
"QLineEdit:hover, QTextEdit:hover{\n"
"	border: 1px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"	background-color: rgba(255, 255, 255, 55);\n"
"	color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"QLineEdit:focus, QTextEdit:focus{\n"
"	border: 1px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"	background-color: rgba(255, 220, 255, 50);\n"
"	color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"QPushButton{\n"
"	border: 1px solid #8f8f91;\n"
"    border-radius: 8px;\n"
"	background-color: rgba(255, 255, 255, 50);\n"
"	color: rgb(255, 255, 255);\n"
"	padding-bottom: 2px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border: 1px solid #8f8f91;\n"
"    border-radius: 8px;\n"
"	background-color: rgba(255, 255, 255, 60);\n"
"	color: rgb(255, 255, 255);\n"
"	padding-bottom: 2px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 1px solid #8f8f91;\n"
"    border-radiu"
                        "s: 8px;\n"
"	background-color: rgba(255, 240, 255, 80);\n"
"	color: rgb(255, 255, 255);\n"
"	padding-bottom: 2px;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.main)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.TitleBar = TitleBar(self.main)
        self.TitleBar.setObjectName(u"TitleBar")
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
        self.label_6 = QLabel(self.TitleBar)
        self.label_6.setObjectName(u"label_6")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_5.addWidget(self.label_6)

        self.close_btn = QPushButton(self.TitleBar)
        self.close_btn.setObjectName(u"close_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.close_btn.sizePolicy().hasHeightForWidth())
        self.close_btn.setSizePolicy(sizePolicy1)
        self.close_btn.setMaximumSize(QSize(15, 15))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.close_btn.setFont(font1)
        self.close_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.close_btn.setFlat(True)

        self.horizontalLayout_5.addWidget(self.close_btn)


        self.verticalLayout.addWidget(self.TitleBar)

        self.horizontalWidget = QWidget(self.main)
        self.horizontalWidget.setObjectName(u"horizontalWidget")
        sizePolicy.setHeightForWidth(self.horizontalWidget.sizePolicy().hasHeightForWidth())
        self.horizontalWidget.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 8, 0, 0)
        self.label = QLabel(self.horizontalWidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.hir = QLineEdit(self.horizontalWidget)
        self.hir.setObjectName(u"hir")
        sizePolicy1.setHeightForWidth(self.hir.sizePolicy().hasHeightForWidth())
        self.hir.setSizePolicy(sizePolicy1)
        self.hir.setMinimumSize(QSize(230, 0))
        self.hir.setFont(font)

        self.horizontalLayout.addWidget(self.hir)

        self.hir_auto = QPushButton(self.horizontalWidget)
        self.hir_auto.setObjectName(u"hir_auto")
        self.hir_auto.setMinimumSize(QSize(40, 0))
        self.hir_auto.setMaximumSize(QSize(40, 16777215))
        self.hir_auto.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.hir_auto)


        self.verticalLayout.addWidget(self.horizontalWidget)

        self.horizontalWidget_2 = QWidget(self.main)
        self.horizontalWidget_2.setObjectName(u"horizontalWidget_2")
        sizePolicy.setHeightForWidth(self.horizontalWidget_2.sizePolicy().hasHeightForWidth())
        self.horizontalWidget_2.setSizePolicy(sizePolicy)
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalWidget_2)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.horizontalWidget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.kat = QLineEdit(self.horizontalWidget_2)
        self.kat.setObjectName(u"kat")
        sizePolicy1.setHeightForWidth(self.kat.sizePolicy().hasHeightForWidth())
        self.kat.setSizePolicy(sizePolicy1)
        self.kat.setMinimumSize(QSize(230, 0))
        self.kat.setFont(font)

        self.horizontalLayout_2.addWidget(self.kat)

        self.kat_auto = QPushButton(self.horizontalWidget_2)
        self.kat_auto.setObjectName(u"kat_auto")
        self.kat_auto.setMinimumSize(QSize(40, 0))
        self.kat_auto.setMaximumSize(QSize(40, 16777215))
        self.kat_auto.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.kat_auto)


        self.verticalLayout.addWidget(self.horizontalWidget_2)

        self.horizontalWidget_3 = QWidget(self.main)
        self.horizontalWidget_3.setObjectName(u"horizontalWidget_3")
        sizePolicy.setHeightForWidth(self.horizontalWidget_3.sizePolicy().hasHeightForWidth())
        self.horizontalWidget_3.setSizePolicy(sizePolicy)
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalWidget_3)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.horizontalWidget_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.hep = QLineEdit(self.horizontalWidget_3)
        self.hep.setObjectName(u"hep")
        sizePolicy1.setHeightForWidth(self.hep.sizePolicy().hasHeightForWidth())
        self.hep.setSizePolicy(sizePolicy1)
        self.hep.setMinimumSize(QSize(230, 0))
        self.hep.setFont(font)

        self.horizontalLayout_3.addWidget(self.hep)

        self.hep_auto = QPushButton(self.horizontalWidget_3)
        self.hep_auto.setObjectName(u"hep_auto")
        self.hep_auto.setMinimumSize(QSize(40, 0))
        self.hep_auto.setMaximumSize(QSize(40, 16777215))
        self.hep_auto.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.hep_auto)


        self.verticalLayout.addWidget(self.horizontalWidget_3)

        self.horizontalWidget_4 = QWidget(self.main)
        self.horizontalWidget_4.setObjectName(u"horizontalWidget_4")
        sizePolicy.setHeightForWidth(self.horizontalWidget_4.sizePolicy().hasHeightForWidth())
        self.horizontalWidget_4.setSizePolicy(sizePolicy)
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalWidget_4)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.horizontalWidget_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.kun = QLineEdit(self.horizontalWidget_4)
        self.kun.setObjectName(u"kun")
        sizePolicy1.setHeightForWidth(self.kun.sizePolicy().hasHeightForWidth())
        self.kun.setSizePolicy(sizePolicy1)
        self.kun.setMinimumSize(QSize(230, 0))
        self.kun.setFont(font)

        self.horizontalLayout_4.addWidget(self.kun)

        self.kun_auto = QPushButton(self.horizontalWidget_4)
        self.kun_auto.setObjectName(u"kun_auto")
        self.kun_auto.setMinimumSize(QSize(40, 0))
        self.kun_auto.setMaximumSize(QSize(40, 16777215))
        self.kun_auto.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_4.addWidget(self.kun_auto)


        self.verticalLayout.addWidget(self.horizontalWidget_4)

        self.widget_4 = QWidget(self.main)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.widget_4.setMaximumSize(QSize(16777215, 65))
        self.horizontalLayout_6 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_5 = QLabel(self.widget_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.label_5)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout_6.addLayout(self.verticalLayout_2)

        self.mean = QTextEdit(self.widget_4)
        self.mean.setObjectName(u"mean")
        self.mean.setMinimumSize(QSize(280, 0))
        self.mean.setMaximumSize(QSize(280, 16777215))
        self.mean.setFont(font)

        self.horizontalLayout_6.addWidget(self.mean)


        self.verticalLayout.addWidget(self.widget_4)

        self.widget_5 = QWidget(self.main)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy)
        self.widget_5.setMaximumSize(QSize(16777215, 65))
        self.horizontalLayout_8 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_8.setSpacing(6)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_7 = QLabel(self.widget_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_7.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.label_7)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)


        self.horizontalLayout_8.addLayout(self.verticalLayout_4)

        self.mean2 = QTextEdit(self.widget_5)
        self.mean2.setObjectName(u"mean2")
        self.mean2.setMinimumSize(QSize(280, 0))
        self.mean2.setMaximumSize(QSize(280, 16777215))
        self.mean2.setFont(font)

        self.horizontalLayout_8.addWidget(self.mean2)


        self.verticalLayout.addWidget(self.widget_5)

        self.widget_3 = QWidget(self.main)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setStyleSheet(u"QPushButton{\n"
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
        self.horizontalLayout_9 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.support = QPushButton(self.widget_3)
        self.support.setObjectName(u"support")
        self.support.setFont(font)
        self.support.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_9.addWidget(self.support)

        self.cancel = QPushButton(self.widget_3)
        self.cancel.setObjectName(u"cancel")
        self.cancel.setFont(font)
        self.cancel.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_9.addWidget(self.cancel)

        self.ok = QPushButton(self.widget_3)
        self.ok.setObjectName(u"ok")
        self.ok.setFont(font)
        self.ok.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_9.addWidget(self.ok)


        self.verticalLayout.addWidget(self.widget_3)


        self.gridLayout.addWidget(self.main, 2, 0, 1, 1)

        self.keyboard = QWidget(self.centralwidget)
        self.keyboard.setObjectName(u"keyboard")
        sizePolicy.setHeightForWidth(self.keyboard.sizePolicy().hasHeightForWidth())
        self.keyboard.setSizePolicy(sizePolicy)
        self.keyboard.setStyleSheet(u"QPushButton{\n"
"	border: 1px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"	background-color: rgba(255, 255, 255, 130);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border: 1px solid #8f8f91;\n"
"    border-radius: 8px;\n"
"	background-color: rgba(255, 255, 255, 140);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 1px solid #8f8f91;\n"
"    border-radius: 8px;\n"
"	background-color: rgba(255, 245, 255, 160);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.gridLayout_2 = QGridLayout(self.keyboard)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_ke = QPushButton(self.keyboard)
        self.btn_ke.setObjectName(u"btn_ke")
        sizePolicy1.setHeightForWidth(self.btn_ke.sizePolicy().hasHeightForWidth())
        self.btn_ke.setSizePolicy(sizePolicy1)
        self.btn_ke.setMinimumSize(QSize(35, 35))
        self.btn_ke.setMaximumSize(QSize(35, 35))
        self.btn_ke.setFont(font1)
        self.btn_ke.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btn_ke, 3, 7, 1, 1)

        self.btn_spliter = QPushButton(self.keyboard)
        self.btn_spliter.setObjectName(u"btn_spliter")
        sizePolicy1.setHeightForWidth(self.btn_spliter.sizePolicy().hasHeightForWidth())
        self.btn_spliter.setSizePolicy(sizePolicy1)
        self.btn_spliter.setMinimumSize(QSize(35, 35))
        self.btn_spliter.setMaximumSize(QSize(35, 35))
        self.btn_spliter.setFont(font1)
        self.btn_spliter.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btn_spliter, 6, 6, 1, 1)

        self.btn_ma = QPushButton(self.keyboard)
        self.btn_ma.setObjectName(u"btn_ma")
        sizePolicy1.setHeightForWidth(self.btn_ma.sizePolicy().hasHeightForWidth())
        self.btn_ma.setSizePolicy(sizePolicy1)
        self.btn_ma.setMinimumSize(QSize(35, 35))
        self.btn_ma.setMaximumSize(QSize(35, 16777215))
        self.btn_ma.setFont(font1)
        self.btn_ma.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btn_ma, 0, 2, 1, 1)

        self.btn_n = QPushButton(self.keyboard)
        self.btn_n.setObjectName(u"btn_n")
        sizePolicy1.setHeightForWidth(self.btn_n.sizePolicy().hasHeightForWidth())
        self.btn_n.setSizePolicy(sizePolicy1)
        self.btn_n.setMinimumSize(QSize(35, 35))
        self.btn_n.setMaximumSize(QSize(35, 35))
        self.btn_n.setFont(font1)
        self.btn_n.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btn_n, 6, 7, 1, 1)

        self.btn_na = QPushButton(self.keyboard)
        self.btn_na.setObjectName(u"btn_na")
        sizePolicy1.setHeightForWidth(self.btn_na.sizePolicy().hasHeightForWidth())
        self.btn_na.setSizePolicy(sizePolicy1)
        self.btn_na.setMinimumSize(QSize(35, 35))
        self.btn_na.setMaximumSize(QSize(35, 35))
        self.btn_na.setFont(font1)
        self.btn_na.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btn_na, 0, 4, 1, 1)

        self.btn_ko = QPushButton(self.keyboard)
        self.btn_ko.setObjectName(u"btn_ko")
        sizePolicy1.setHeightForWidth(self.btn_ko.sizePolicy().hasHeightForWidth())
        self.btn_ko.setSizePolicy(sizePolicy1)
        self.btn_ko.setMinimumSize(QSize(35, 35))
        self.btn_ko.setMaximumSize(QSize(35, 35))
        self.btn_ko.setFont(font1)
        self.btn_ko.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btn_ko, 4, 7, 1, 1)

        self.btn_e = QPushButton(self.keyboard)
        self.btn_e.setObjectName(u"btn_e")
        sizePolicy1.setHeightForWidth(self.btn_e.sizePolicy().hasHeightForWidth())
        self.btn_e.setSizePolicy(sizePolicy1)
        self.btn_e.setMinimumSize(QSize(35, 35))
        self.btn_e.setMaximumSize(QSize(35, 35))
        self.btn_e.setFont(font1)
        self.btn_e.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btn_e, 3, 8, 1, 1)

        self.btn_ha = QPushButton(self.keyboard)
        self.btn_ha.setObjectName(u"btn_ha")
        sizePolicy1.setHeightForWidth(self.btn_ha.sizePolicy().hasHeightForWidth())
        self.btn_ha.setSizePolicy(sizePolicy1)
        self.btn_ha.setMinimumSize(QSize(35, 35))
        self.btn_ha.setMaximumSize(QSize(35, 16777215))
        self.btn_ha.setFont(font1)
        self.btn_ha.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btn_ha, 0, 3, 1, 1)

        self.btn_dash = QPushButton(self.keyboard)
        self.btn_dash.setObjectName(u"btn_dash")
        sizePolicy1.setHeightForWidth(self.btn_dash.sizePolicy().hasHeightForWidth())
        self.btn_dash.setSizePolicy(sizePolicy1)
        self.btn_dash.setMinimumSize(QSize(35, 35))
        self.btn_dash.setMaximumSize(QSize(35, 35))
        font2 = QFont()
        font2.setPointSize(18)
        font2.setBold(True)
        self.btn_dash.setFont(font2)
        self.btn_dash.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btn_dash, 6, 4, 1, 1)

        self.btn_kana = QPushButton(self.keyboard)
        self.btn_kana.setObjectName(u"btn_kana")
        sizePolicy1.setHeightForWidth(self.btn_kana.sizePolicy().hasHeightForWidth())
        self.btn_kana.setSizePolicy(sizePolicy1)
        self.btn_kana.setMinimumSize(QSize(35, 35))
        self.btn_kana.setMaximumSize(QSize(35, 35))
        self.btn_kana.setFont(font1)
        self.btn_kana.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btn_kana, 6, 0, 1, 1)

        self.btn_ = QPushButton(self.keyboard)
        self.btn_.setObjectName(u"btn_")
        sizePolicy1.setHeightForWidth(self.btn_.sizePolicy().hasHeightForWidth())
        self.btn_.setSizePolicy(sizePolicy1)
        self.btn_.setMinimumSize(QSize(35, 35))
        self.btn_.setMaximumSize(QSize(35, 35))
        self.btn_.setFont(font1)

        self.gridLayout_2.addWidget(self.btn_, 1, 1, 1, 1)

        self.btn_small = QPushButton(self.keyboard)
        self.btn_small.setObjectName(u"btn_small")
        sizePolicy1.setHeightForWidth(self.btn_small.sizePolicy().hasHeightForWidth())
        self.btn_small.setSizePolicy(sizePolicy1)
        self.btn_small.setMinimumSize(QSize(35, 35))
        self.btn_small.setMaximumSize(QSize(35, 35))
        self.btn_small.setFont(font1)
        self.btn_small.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btn_small, 6, 1, 1, 1)

        self.btn_mark = QPushButton(self.keyboard)
        self.btn_mark.setObjectName(u"btn_mark")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_mark.sizePolicy().hasHeightForWidth())
        self.btn_mark.setSizePolicy(sizePolicy2)
        self.btn_mark.setMinimumSize(QSize(35, 35))
        self.btn_mark.setMaximumSize(QSize(35, 35))
        font3 = QFont()
        font3.setPointSize(20)
        font3.setBold(True)
        self.btn_mark.setFont(font3)
        self.btn_mark.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btn_mark, 6, 2, 1, 1)

        self.btn_so = QPushButton(self.keyboard)
        self.btn_so.setObjectName(u"btn_so")
        sizePolicy1.setHeightForWidth(self.btn_so.sizePolicy().hasHeightForWidth())
        self.btn_so.setSizePolicy(sizePolicy1)
        self.btn_so.setMinimumSize(QSize(35, 35))
        self.btn_so.setMaximumSize(QSize(35, 35))
        self.btn_so.setFont(font1)
        self.btn_so.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btn_so, 4, 6, 1, 1)

        self.btn_u = QPushButton(self.keyboard)
        self.btn_u.setObjectName(u"btn_u")
        sizePolicy1.setHeightForWidth(self.btn_u.sizePolicy().hasHeightForWidth())
        self.btn_u.setSizePolicy(sizePolicy1)
        self.btn_u.setMinimumSize(QSize(35, 35))
        self.btn_u.setMaximumSize(QSize(35, 35))
        self.btn_u.setFont(font1)
        self.btn_u.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btn_u, 2, 8, 1, 1)

        self.btn_nu = QPushButton(self.keyboard)
        self.btn_nu.setObjectName(u"btn_nu")
        sizePolicy1.setHeightForWidth(self.btn_nu.sizePolicy().hasHeightForWidth())
        self.btn_nu.setSizePolicy(sizePolicy1)
        self.btn_nu.setMinimumSize(QSize(35, 35))
        self.btn_nu.setMaximumSize(QSize(35, 35))
        self.btn_nu.setFont(font1)
        self.btn_nu.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btn_nu, 2, 4, 1, 1)

        self.btn_me = QPushButton(self.keyboard)
        self.btn_me.setObjectName(u"btn_me")
        sizePolicy1.setHeightForWidth(self.btn_me.sizePolicy().hasHeightForWidth())
        self.btn_me.setSizePolicy(sizePolicy1)
        self.btn_me.setMinimumSize(QSize(35, 35))
        self.btn_me.setMaximumSize(QSize(35, 16777215))
        self.btn_me.setFont(font1)
        self.btn_me.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btn_me, 3, 2, 1, 1)

        self.btn_ki = QPushButton(self.keyboard)
        self.btn_ki.setObjectName(u"btn_ki")
        sizePolicy1.setHeightForWidth(self.btn_ki.sizePolicy().hasHeightForWidth())
        self.btn_ki.setSizePolicy(sizePolicy1)
        self.btn_ki.setMinimumSize(QSize(35, 35))
        self.btn_ki.setMaximumSize(QSize(35, 35))
        self.btn_ki.setFont(font1)
        self.btn_ki.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btn_ki, 1, 7, 1, 1)

        self.btn_wa = QPushButton(self.keyboard)
        self.btn_wa.setObjectName(u"btn_wa")
        sizePolicy1.setHeightForWidth(self.btn_wa.sizePolicy().hasHeightForWidth())
        self.btn_wa.setSizePolicy(sizePolicy1)
        self.btn_wa.setMinimumSize(QSize(35, 35))
        self.btn_wa.setMaximumSize(QSize(35, 35))
        self.btn_wa.setFont(font1)
        self.btn_wa.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btn_wa, 6, 8, 1, 1)

        self.btn_no = QPushButton(self.keyboard)
        self.btn_no.setObjectName(u"btn_no")
        sizePolicy1.setHeightForWidth(self.btn_no.sizePolicy().hasHeightForWidth())
        self.btn_no.setSizePolicy(sizePolicy1)
        self.btn_no.setMinimumSize(QSize(35, 35))
        self.btn_no.setMaximumSize(QSize(35, 35))
        self.btn_no.setFont(font1)
        self.btn_no.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btn_no, 4, 4, 1, 1)

        self.btn_chi = QPushButton(self.keyboard)
        self.btn_chi.setObjectName(u"btn_chi")
        sizePolicy1.setHeightForWidth(self.btn_chi.sizePolicy().hasHeightForWidth())
        self.btn_chi.setSizePolicy(sizePolicy1)
        self.btn_chi.setMinimumSize(QSize(35, 35))
        self.btn_chi.setMaximumSize(QSize(35, 35))
        self.btn_chi.setFont(font1)
        self.btn_chi.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btn_chi, 1, 5, 1, 1)

        self.btn_ku = QPushButton(self.keyboard)
        self.btn_ku.setObjectName(u"btn_ku")
        sizePolicy1.setHeightForWidth(self.btn_ku.sizePolicy().hasHeightForWidth())
        self.btn_ku.setSizePolicy(sizePolicy1)
        self.btn_ku.setMinimumSize(QSize(35, 35))
        self.btn_ku.setMaximumSize(QSize(35, 35))
        self.btn_ku.setFont(font1)
        self.btn_ku.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btn_ku, 2, 7, 1, 1)

        self.btn_ne = QPushButton(self.keyboard)
        self.btn_ne.setObjectName(u"btn_ne")
        sizePolicy1.setHeightForWidth(self.btn_ne.sizePolicy().hasHeightForWidth())
        self.btn_ne.setSizePolicy(sizePolicy1)
        self.btn_ne.setMinimumSize(QSize(35, 35))
        self.btn_ne.setMaximumSize(QSize(35, 35))
        self.btn_ne.setFont(font1)
        self.btn_ne.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btn_ne, 3, 4, 1, 1)

        self.btn_mo = QPushButton(self.keyboard)
        self.btn_mo.setObjectName(u"btn_mo")
        sizePolicy1.setHeightForWidth(self.btn_mo.sizePolicy().hasHeightForWidth())
        self.btn_mo.setSizePolicy(sizePolicy1)
        self.btn_mo.setMinimumSize(QSize(35, 35))
        self.btn_mo.setMaximumSize(QSize(35, 16777215))
        self.btn_mo.setFont(font1)
        self.btn_mo.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btn_mo, 4, 2, 1, 1)

        self.btn_ru = QPushButton(self.keyboard)
        self.btn_ru.setObjectName(u"btn_ru")
        sizePolicy1.setHeightForWidth(self.btn_ru.sizePolicy().hasHeightForWidth())
        self.btn_ru.setSizePolicy(sizePolicy1)
        self.btn_ru.setMinimumSize(QSize(35, 35))
        self.btn_ru.setMaximumSize(QSize(35, 35))
        self.btn_ru.setFont(font1)
        self.btn_ru.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btn_ru, 2, 0, 1, 1)

        self.btn_hi = QPushButton(self.keyboard)
        self.btn_hi.setObjectName(u"btn_hi")
        sizePolicy1.setHeightForWidth(self.btn_hi.sizePolicy().hasHeightForWidth())
        self.btn_hi.setSizePolicy(sizePolicy1)
        self.btn_hi.setMinimumSize(QSize(35, 35))
        self.btn_hi.setMaximumSize(QSize(35, 16777215))
        self.btn_hi.setFont(font1)
        self.btn_hi.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btn_hi, 1, 3, 1, 1)

        self.btn_te = QPushButton(self.keyboard)
        self.btn_te.setObjectName(u"btn_te")
        sizePolicy1.setHeightForWidth(self.btn_te.sizePolicy().hasHeightForWidth())
        self.btn_te.setSizePolicy(sizePolicy1)
        self.btn_te.setMinimumSize(QSize(35, 35))
        self.btn_te.setMaximumSize(QSize(35, 35))
        self.btn_te.setFont(font1)
        self.btn_te.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btn_te, 3, 5, 1, 1)

        self.btn_sa = QPushButton(self.keyboard)
        self.btn_sa.setObjectName(u"btn_sa")
        sizePolicy1.setHeightForWidth(self.btn_sa.sizePolicy().hasHeightForWidth())
        self.btn_sa.setSizePolicy(sizePolicy1)
        self.btn_sa.setMinimumSize(QSize(35, 35))
        self.btn_sa.setMaximumSize(QSize(35, 35))
        self.btn_sa.setFont(font1)
        self.btn_sa.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btn_sa, 0, 6, 1, 1)

        self.btn_su = QPushButton(self.keyboard)
        self.btn_su.setObjectName(u"btn_su")
        sizePolicy1.setHeightForWidth(self.btn_su.sizePolicy().hasHeightForWidth())
        self.btn_su.setSizePolicy(sizePolicy1)
        self.btn_su.setMinimumSize(QSize(35, 35))
        self.btn_su.setMaximumSize(QSize(35, 35))
        self.btn_su.setFont(font1)
        self.btn_su.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btn_su, 2, 6, 1, 1)

        self.btn_ri = QPushButton(self.keyboard)
        self.btn_ri.setObjectName(u"btn_ri")
        sizePolicy1.setHeightForWidth(self.btn_ri.sizePolicy().hasHeightForWidth())
        self.btn_ri.setSizePolicy(sizePolicy1)
        self.btn_ri.setMinimumSize(QSize(35, 35))
        self.btn_ri.setMaximumSize(QSize(35, 35))
        self.btn_ri.setFont(font1)
        self.btn_ri.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btn_ri, 1, 0, 1, 1)

        self.btn_ta = QPushButton(self.keyboard)
        self.btn_ta.setObjectName(u"btn_ta")
        sizePolicy1.setHeightForWidth(self.btn_ta.sizePolicy().hasHeightForWidth())
        self.btn_ta.setSizePolicy(sizePolicy1)
        self.btn_ta.setMinimumSize(QSize(35, 35))
        self.btn_ta.setMaximumSize(QSize(35, 35))
        self.btn_ta.setFont(font1)
        self.btn_ta.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btn_ta, 0, 5, 1, 1)

        self.btn_ni = QPushButton(self.keyboard)
        self.btn_ni.setObjectName(u"btn_ni")
        sizePolicy1.setHeightForWidth(self.btn_ni.sizePolicy().hasHeightForWidth())
        self.btn_ni.setSizePolicy(sizePolicy1)
        self.btn_ni.setMinimumSize(QSize(35, 35))
        self.btn_ni.setMaximumSize(QSize(35, 35))
        self.btn_ni.setFont(font1)
        self.btn_ni.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btn_ni, 1, 4, 1, 1)

        self.btn_ka = QPushButton(self.keyboard)
        self.btn_ka.setObjectName(u"btn_ka")
        sizePolicy1.setHeightForWidth(self.btn_ka.sizePolicy().hasHeightForWidth())
        self.btn_ka.setSizePolicy(sizePolicy1)
        self.btn_ka.setMinimumSize(QSize(35, 35))
        self.btn_ka.setMaximumSize(QSize(35, 35))
        self.btn_ka.setFont(font1)
        self.btn_ka.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btn_ka, 0, 7, 1, 1)

        self.btn_he = QPushButton(self.keyboard)
        self.btn_he.setObjectName(u"btn_he")
        sizePolicy1.setHeightForWidth(self.btn_he.sizePolicy().hasHeightForWidth())
        self.btn_he.setSizePolicy(sizePolicy1)
        self.btn_he.setMinimumSize(QSize(35, 35))
        self.btn_he.setMaximumSize(QSize(35, 16777215))
        self.btn_he.setFont(font1)
        self.btn_he.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btn_he, 3, 3, 1, 1)

        self.btn_ho = QPushButton(self.keyboard)
        self.btn_ho.setObjectName(u"btn_ho")
        sizePolicy1.setHeightForWidth(self.btn_ho.sizePolicy().hasHeightForWidth())
        self.btn_ho.setSizePolicy(sizePolicy1)
        self.btn_ho.setMinimumSize(QSize(35, 35))
        self.btn_ho.setMaximumSize(QSize(35, 16777215))
        self.btn_ho.setFont(font1)
        self.btn_ho.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btn_ho, 4, 3, 1, 1)

        self.btn_tsu = QPushButton(self.keyboard)
        self.btn_tsu.setObjectName(u"btn_tsu")
        sizePolicy1.setHeightForWidth(self.btn_tsu.sizePolicy().hasHeightForWidth())
        self.btn_tsu.setSizePolicy(sizePolicy1)
        self.btn_tsu.setMinimumSize(QSize(35, 35))
        self.btn_tsu.setMaximumSize(QSize(35, 35))
        self.btn_tsu.setFont(font1)
        self.btn_tsu.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btn_tsu, 2, 5, 1, 1)

        self.btn_ro = QPushButton(self.keyboard)
        self.btn_ro.setObjectName(u"btn_ro")
        sizePolicy1.setHeightForWidth(self.btn_ro.sizePolicy().hasHeightForWidth())
        self.btn_ro.setSizePolicy(sizePolicy1)
        self.btn_ro.setMinimumSize(QSize(35, 35))
        self.btn_ro.setMaximumSize(QSize(35, 35))
        self.btn_ro.setFont(font1)
        self.btn_ro.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btn_ro, 4, 0, 1, 1)

        self.btn_ra = QPushButton(self.keyboard)
        self.btn_ra.setObjectName(u"btn_ra")
        sizePolicy1.setHeightForWidth(self.btn_ra.sizePolicy().hasHeightForWidth())
        self.btn_ra.setSizePolicy(sizePolicy1)
        self.btn_ra.setMinimumSize(QSize(35, 35))
        self.btn_ra.setMaximumSize(QSize(35, 35))
        self.btn_ra.setFont(font1)
        self.btn_ra.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btn_ra, 0, 0, 1, 1)

        self.btn_yo = QPushButton(self.keyboard)
        self.btn_yo.setObjectName(u"btn_yo")
        sizePolicy1.setHeightForWidth(self.btn_yo.sizePolicy().hasHeightForWidth())
        self.btn_yo.setSizePolicy(sizePolicy1)
        self.btn_yo.setMinimumSize(QSize(35, 35))
        self.btn_yo.setMaximumSize(QSize(35, 35))
        self.btn_yo.setFont(font1)
        self.btn_yo.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btn_yo, 4, 1, 1, 1)

        self.btn_shi = QPushButton(self.keyboard)
        self.btn_shi.setObjectName(u"btn_shi")
        sizePolicy1.setHeightForWidth(self.btn_shi.sizePolicy().hasHeightForWidth())
        self.btn_shi.setSizePolicy(sizePolicy1)
        self.btn_shi.setMinimumSize(QSize(35, 35))
        self.btn_shi.setMaximumSize(QSize(35, 35))
        self.btn_shi.setFont(font1)
        self.btn_shi.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btn_shi, 1, 6, 1, 1)

        self.btn_1 = QPushButton(self.keyboard)
        self.btn_1.setObjectName(u"btn_1")
        sizePolicy1.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy1)
        self.btn_1.setMinimumSize(QSize(35, 35))
        self.btn_1.setMaximumSize(QSize(35, 35))
        self.btn_1.setFont(font1)

        self.gridLayout_2.addWidget(self.btn_1, 3, 1, 1, 1)

        self.btn_fu = QPushButton(self.keyboard)
        self.btn_fu.setObjectName(u"btn_fu")
        sizePolicy1.setHeightForWidth(self.btn_fu.sizePolicy().hasHeightForWidth())
        self.btn_fu.setSizePolicy(sizePolicy1)
        self.btn_fu.setMinimumSize(QSize(35, 35))
        self.btn_fu.setMaximumSize(QSize(35, 16777215))
        self.btn_fu.setFont(font1)
        self.btn_fu.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btn_fu, 2, 3, 1, 1)

        self.btn_re = QPushButton(self.keyboard)
        self.btn_re.setObjectName(u"btn_re")
        sizePolicy1.setHeightForWidth(self.btn_re.sizePolicy().hasHeightForWidth())
        self.btn_re.setSizePolicy(sizePolicy1)
        self.btn_re.setMinimumSize(QSize(35, 35))
        self.btn_re.setMaximumSize(QSize(35, 35))
        self.btn_re.setFont(font1)
        self.btn_re.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btn_re, 3, 0, 1, 1)

        self.btn_clear = QPushButton(self.keyboard)
        self.btn_clear.setObjectName(u"btn_clear")
        sizePolicy1.setHeightForWidth(self.btn_clear.sizePolicy().hasHeightForWidth())
        self.btn_clear.setSizePolicy(sizePolicy1)
        self.btn_clear.setMinimumSize(QSize(35, 35))
        self.btn_clear.setMaximumSize(QSize(35, 35))
        self.btn_clear.setFont(font1)
        self.btn_clear.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btn_clear, 6, 5, 1, 1)

        self.btn_o = QPushButton(self.keyboard)
        self.btn_o.setObjectName(u"btn_o")
        sizePolicy1.setHeightForWidth(self.btn_o.sizePolicy().hasHeightForWidth())
        self.btn_o.setSizePolicy(sizePolicy1)
        self.btn_o.setMinimumSize(QSize(35, 35))
        self.btn_o.setMaximumSize(QSize(35, 35))
        self.btn_o.setFont(font1)
        self.btn_o.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btn_o, 4, 8, 1, 1)

        self.btn_mi = QPushButton(self.keyboard)
        self.btn_mi.setObjectName(u"btn_mi")
        sizePolicy1.setHeightForWidth(self.btn_mi.sizePolicy().hasHeightForWidth())
        self.btn_mi.setSizePolicy(sizePolicy1)
        self.btn_mi.setMinimumSize(QSize(35, 35))
        self.btn_mi.setMaximumSize(QSize(35, 16777215))
        self.btn_mi.setFont(font1)
        self.btn_mi.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btn_mi, 1, 2, 1, 1)

        self.btn_i = QPushButton(self.keyboard)
        self.btn_i.setObjectName(u"btn_i")
        sizePolicy1.setHeightForWidth(self.btn_i.sizePolicy().hasHeightForWidth())
        self.btn_i.setSizePolicy(sizePolicy1)
        self.btn_i.setMinimumSize(QSize(35, 35))
        self.btn_i.setMaximumSize(QSize(35, 35))
        self.btn_i.setFont(font1)
        self.btn_i.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btn_i, 1, 8, 1, 1)

        self.btn_mu = QPushButton(self.keyboard)
        self.btn_mu.setObjectName(u"btn_mu")
        sizePolicy1.setHeightForWidth(self.btn_mu.sizePolicy().hasHeightForWidth())
        self.btn_mu.setSizePolicy(sizePolicy1)
        self.btn_mu.setMinimumSize(QSize(35, 35))
        self.btn_mu.setMaximumSize(QSize(35, 16777215))
        self.btn_mu.setFont(font1)
        self.btn_mu.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btn_mu, 2, 2, 1, 1)

        self.btn_backspace = QPushButton(self.keyboard)
        self.btn_backspace.setObjectName(u"btn_backspace")
        sizePolicy1.setHeightForWidth(self.btn_backspace.sizePolicy().hasHeightForWidth())
        self.btn_backspace.setSizePolicy(sizePolicy1)
        self.btn_backspace.setMinimumSize(QSize(35, 35))
        self.btn_backspace.setMaximumSize(QSize(35, 35))
        self.btn_backspace.setFont(font3)
        self.btn_backspace.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btn_backspace, 6, 3, 1, 1)

        self.btn_se = QPushButton(self.keyboard)
        self.btn_se.setObjectName(u"btn_se")
        sizePolicy1.setHeightForWidth(self.btn_se.sizePolicy().hasHeightForWidth())
        self.btn_se.setSizePolicy(sizePolicy1)
        self.btn_se.setMinimumSize(QSize(35, 35))
        self.btn_se.setMaximumSize(QSize(35, 35))
        self.btn_se.setFont(font1)
        self.btn_se.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btn_se, 3, 6, 1, 1)

        self.btn_yu = QPushButton(self.keyboard)
        self.btn_yu.setObjectName(u"btn_yu")
        sizePolicy1.setHeightForWidth(self.btn_yu.sizePolicy().hasHeightForWidth())
        self.btn_yu.setSizePolicy(sizePolicy1)
        self.btn_yu.setMinimumSize(QSize(35, 35))
        self.btn_yu.setMaximumSize(QSize(35, 35))
        self.btn_yu.setFont(font1)
        self.btn_yu.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btn_yu, 2, 1, 1, 1)

        self.btn_a = QPushButton(self.keyboard)
        self.btn_a.setObjectName(u"btn_a")
        sizePolicy1.setHeightForWidth(self.btn_a.sizePolicy().hasHeightForWidth())
        self.btn_a.setSizePolicy(sizePolicy1)
        self.btn_a.setMinimumSize(QSize(35, 35))
        self.btn_a.setMaximumSize(QSize(35, 35))
        self.btn_a.setFont(font1)
        self.btn_a.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btn_a, 0, 8, 1, 1)

        self.btn_ya = QPushButton(self.keyboard)
        self.btn_ya.setObjectName(u"btn_ya")
        sizePolicy1.setHeightForWidth(self.btn_ya.sizePolicy().hasHeightForWidth())
        self.btn_ya.setSizePolicy(sizePolicy1)
        self.btn_ya.setMinimumSize(QSize(35, 35))
        self.btn_ya.setMaximumSize(QSize(35, 35))
        self.btn_ya.setFont(font1)
        self.btn_ya.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btn_ya, 0, 1, 1, 1)

        self.btn_to = QPushButton(self.keyboard)
        self.btn_to.setObjectName(u"btn_to")
        sizePolicy1.setHeightForWidth(self.btn_to.sizePolicy().hasHeightForWidth())
        self.btn_to.setSizePolicy(sizePolicy1)
        self.btn_to.setMinimumSize(QSize(35, 35))
        self.btn_to.setMaximumSize(QSize(35, 35))
        self.btn_to.setFont(font1)
        self.btn_to.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btn_to, 4, 5, 1, 1)

        self.line = QFrame(self.keyboard)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line, 5, 4, 1, 1)


        self.gridLayout.addWidget(self.keyboard, 4, 0, 1, 1)

        AddSound.setCentralWidget(self.centralwidget)

        self.retranslateUi(AddSound)

        QMetaObject.connectSlotsByName(AddSound)
    # setupUi

    def retranslateUi(self, AddSound):
        AddSound.setWindowTitle(QCoreApplication.translate("AddSound", u"MainWindow", None))
        self.label_6.setText(QCoreApplication.translate("AddSound", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f \u0447\u0435\u0440\u0435\u0437 \u0437\u0430\u043f\u044f\u0442\u0443\u044e \u0441 \u043f\u0440\u043e\u0431\u0435\u043b\u043e\u043c(\", \"):", None))
        self.close_btn.setText(QCoreApplication.translate("AddSound", u"\u00d7", None))
        self.label.setText(QCoreApplication.translate("AddSound", u"\u0425\u0438\u0440\u0438\u0433\u0430\u043d\u0430:", None))
        self.hir.setPlaceholderText(QCoreApplication.translate("AddSound", u"\u3042, \u3044, \u3046, \u3048, \u304a", None))
        self.hir_auto.setText(QCoreApplication.translate("AddSound", u"auto", None))
        self.label_2.setText(QCoreApplication.translate("AddSound", u"\u041a\u0430\u0442\u0430\u043a\u0430\u043d\u0430:", None))
        self.kat.setPlaceholderText(QCoreApplication.translate("AddSound", u"\u30a2, \u30a4, \u30a6, \u30a8, \u30aa", None))
        self.kat_auto.setText(QCoreApplication.translate("AddSound", u"auto", None))
        self.label_3.setText(QCoreApplication.translate("AddSound", u"\u0425\u044d\u043f\u0431\u0451\u0440\u043d:", None))
        self.hep.setPlaceholderText(QCoreApplication.translate("AddSound", u"a, i, u, e, o", None))
        self.hep_auto.setText(QCoreApplication.translate("AddSound", u"auto", None))
        self.label_4.setText(QCoreApplication.translate("AddSound", u"\u041a\u0443\u043d\u0440\u0435\u0439:", None))
        self.kun.setPlaceholderText(QCoreApplication.translate("AddSound", u"\u0430, \u0438, \u0443, \u0435, \u043e", None))
        self.kun_auto.setText(QCoreApplication.translate("AddSound", u"auto", None))
        self.label_5.setText(QCoreApplication.translate("AddSound", u"\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435:", None))
        self.label_7.setText(QCoreApplication.translate("AddSound", u"\u0423\u0442\u043e\u0447\u043d\u0451\u043d\u043d\u043e\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435:", None))
        self.support.setText(QCoreApplication.translate("AddSound", u"\u041f\u043e\u043c\u043e\u0449\u044c", None))
        self.cancel.setText(QCoreApplication.translate("AddSound", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.ok.setText(QCoreApplication.translate("AddSound", u"\u041e\u043a", None))
        self.btn_ke.setText(QCoreApplication.translate("AddSound", u"\u3051", None))
        self.btn_spliter.setText(QCoreApplication.translate("AddSound", u", ", None))
        self.btn_ma.setText(QCoreApplication.translate("AddSound", u"\u307e", None))
        self.btn_n.setText(QCoreApplication.translate("AddSound", u"\u3093", None))
        self.btn_na.setText(QCoreApplication.translate("AddSound", u"\u306a", None))
        self.btn_ko.setText(QCoreApplication.translate("AddSound", u"\u3053", None))
        self.btn_e.setText(QCoreApplication.translate("AddSound", u"\u3048", None))
        self.btn_ha.setText(QCoreApplication.translate("AddSound", u"\u306f", None))
        self.btn_dash.setText(QCoreApplication.translate("AddSound", u"\u30fc", None))
        self.btn_kana.setText(QCoreApplication.translate("AddSound", u"\u30a2", None))
        self.btn_.setText("")
        self.btn_small.setText(QCoreApplication.translate("AddSound", u"\u3042\u3041", None))
        self.btn_mark.setText(QCoreApplication.translate("AddSound", u" \u309c\u309b ", None))
        self.btn_so.setText(QCoreApplication.translate("AddSound", u"\u305d", None))
        self.btn_u.setText(QCoreApplication.translate("AddSound", u"\u3046", None))
        self.btn_nu.setText(QCoreApplication.translate("AddSound", u"\u306c", None))
        self.btn_me.setText(QCoreApplication.translate("AddSound", u"\u3081", None))
        self.btn_ki.setText(QCoreApplication.translate("AddSound", u"\u304d", None))
        self.btn_wa.setText(QCoreApplication.translate("AddSound", u"\u308f", None))
        self.btn_no.setText(QCoreApplication.translate("AddSound", u"\u306e", None))
        self.btn_chi.setText(QCoreApplication.translate("AddSound", u"\u3061", None))
        self.btn_ku.setText(QCoreApplication.translate("AddSound", u"\u304f", None))
        self.btn_ne.setText(QCoreApplication.translate("AddSound", u"\u306d", None))
        self.btn_mo.setText(QCoreApplication.translate("AddSound", u"\u3082", None))
        self.btn_ru.setText(QCoreApplication.translate("AddSound", u"\u308b", None))
        self.btn_hi.setText(QCoreApplication.translate("AddSound", u"\u3072", None))
        self.btn_te.setText(QCoreApplication.translate("AddSound", u"\u3066", None))
        self.btn_sa.setText(QCoreApplication.translate("AddSound", u"\u3055", None))
        self.btn_su.setText(QCoreApplication.translate("AddSound", u"\u3059", None))
        self.btn_ri.setText(QCoreApplication.translate("AddSound", u"\u308a", None))
        self.btn_ta.setText(QCoreApplication.translate("AddSound", u"\u305f", None))
        self.btn_ni.setText(QCoreApplication.translate("AddSound", u"\u306b", None))
        self.btn_ka.setText(QCoreApplication.translate("AddSound", u"\u304b", None))
        self.btn_he.setText(QCoreApplication.translate("AddSound", u"\u3078", None))
        self.btn_ho.setText(QCoreApplication.translate("AddSound", u"\u307b", None))
        self.btn_tsu.setText(QCoreApplication.translate("AddSound", u"\u3064", None))
        self.btn_ro.setText(QCoreApplication.translate("AddSound", u"\u308d", None))
        self.btn_ra.setText(QCoreApplication.translate("AddSound", u"\u3089", None))
        self.btn_yo.setText(QCoreApplication.translate("AddSound", u"\u3088", None))
        self.btn_shi.setText(QCoreApplication.translate("AddSound", u"\u3057", None))
        self.btn_1.setText("")
        self.btn_fu.setText(QCoreApplication.translate("AddSound", u"\u3075", None))
        self.btn_re.setText(QCoreApplication.translate("AddSound", u"\u308c", None))
        self.btn_clear.setText(QCoreApplication.translate("AddSound", u"\u00d7", None))
        self.btn_o.setText(QCoreApplication.translate("AddSound", u"\u304a", None))
        self.btn_mi.setText(QCoreApplication.translate("AddSound", u"\u307f", None))
        self.btn_i.setText(QCoreApplication.translate("AddSound", u"\u3044", None))
        self.btn_mu.setText(QCoreApplication.translate("AddSound", u"\u3080", None))
        self.btn_backspace.setText(QCoreApplication.translate("AddSound", u"\u2190", None))
        self.btn_se.setText(QCoreApplication.translate("AddSound", u"\u305b", None))
        self.btn_yu.setText(QCoreApplication.translate("AddSound", u"\u3086", None))
        self.btn_a.setText(QCoreApplication.translate("AddSound", u"\u3042", None))
        self.btn_ya.setText(QCoreApplication.translate("AddSound", u"\u3084", None))
        self.btn_to.setText(QCoreApplication.translate("AddSound", u"\u3068", None))
    # retranslateUi

