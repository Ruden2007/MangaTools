from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
                               QLayout, QLineEdit, QMainWindow, QPushButton,
                               QScrollArea, QSizePolicy, QSpacerItem, QTabWidget,
                               QVBoxLayout, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(960, 540)
        MainWindow.setMinimumSize(QSize(640, 360))
        icon = QIcon()
        icon.addFile(u"data/icons/window_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"#centralwidget{border-image: url(data/images/background.jpg)}"
                                 "#sounds_tab{border-image: url(data/images/background.jpg)}"
                                 "#main_tab{border-image: url(data/images/background.jpg)}"
                                 "#translate_tab{border-image: url(data/images/background.jpg)}"
                                 "#clean_tab{border-image: url(data/images/background.jpg)}")

        MainWindow.setLocale(QLocale(QLocale.Russian, QLocale.Ukraine))
        MainWindow.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_8 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.tools_tab = QTabWidget(self.centralwidget)
        self.tools_tab.setObjectName(u"tools_tab")
        self.tools_tab.setAutoFillBackground(False)
        self.tools_tab.setTabPosition(QTabWidget.West)
        self.tools_tab.setTabShape(QTabWidget.Rounded)
        self.tools_tab.setUsesScrollButtons(False)
        self.tools_tab.setDocumentMode(True)
        self.tools_tab.setTabsClosable(False)
        self.tools_tab.setMovable(True)
        self.tools_tab.setTabBarAutoHide(False)
        self.main_tab = QWidget()
        self.main_tab.setObjectName(u"main_tab")
        self.verticalLayout = QVBoxLayout(self.main_tab)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(5, 5, 5, 10)
        self.horizontalSpacer_2 = QSpacerItem(553, 54, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(8)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setSizeConstraint(QLayout.SetFixedSize)
        self.horizontalLayout_10.setContentsMargins(-1, 0, -1, 0)
        self.btn_add_sound_5 = QPushButton(self.main_tab)
        self.btn_add_sound_5.setObjectName(u"btn_add_sound_5")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_add_sound_5.sizePolicy().hasHeightForWidth())
        self.btn_add_sound_5.setSizePolicy(sizePolicy)
        self.btn_add_sound_5.setMinimumSize(QSize(32, 32))
        self.btn_add_sound_5.setMaximumSize(QSize(32, 32))
        self.btn_add_sound_5.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u"data/images/add_sound_ico.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_add_sound_5.setIcon(icon1)
        self.btn_add_sound_5.setIconSize(QSize(32, 32))
        self.btn_add_sound_5.setAutoDefault(False)
        self.btn_add_sound_5.setFlat(True)

        self.horizontalLayout_10.addWidget(self.btn_add_sound_5)

        self.btn_minimize_window_5 = QPushButton(self.main_tab)
        self.btn_minimize_window_5.setObjectName(u"btn_minimize_window_5")
        sizePolicy.setHeightForWidth(self.btn_minimize_window_5.sizePolicy().hasHeightForWidth())
        self.btn_minimize_window_5.setSizePolicy(sizePolicy)
        self.btn_minimize_window_5.setMinimumSize(QSize(32, 32))
        self.btn_minimize_window_5.setMaximumSize(QSize(32, 32))
        self.btn_minimize_window_5.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u"data/images/minimize_window_ico.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize_window_5.setIcon(icon2)
        self.btn_minimize_window_5.setIconSize(QSize(32, 30))
        self.btn_minimize_window_5.setFlat(True)

        self.horizontalLayout_10.addWidget(self.btn_minimize_window_5)

        self.btn_favorite_5 = QPushButton(self.main_tab)
        self.btn_favorite_5.setObjectName(u"btn_favorite_5")
        sizePolicy.setHeightForWidth(self.btn_favorite_5.sizePolicy().hasHeightForWidth())
        self.btn_favorite_5.setSizePolicy(sizePolicy)
        self.btn_favorite_5.setMinimumSize(QSize(32, 32))
        self.btn_favorite_5.setMaximumSize(QSize(32, 32))
        self.btn_favorite_5.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u"data/images/favorite_ico.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_favorite_5.setIcon(icon3)
        self.btn_favorite_5.setIconSize(QSize(32, 32))
        self.btn_favorite_5.setFlat(True)

        self.horizontalLayout_10.addWidget(self.btn_favorite_5)

        self.btn_settings_2 = QPushButton(self.main_tab)
        self.btn_settings_2.setObjectName(u"btn_settings_2")
        sizePolicy.setHeightForWidth(self.btn_settings_2.sizePolicy().hasHeightForWidth())
        self.btn_settings_2.setSizePolicy(sizePolicy)
        self.btn_settings_2.setMinimumSize(QSize(0, 0))
        self.btn_settings_2.setMaximumSize(QSize(32, 32))
        self.btn_settings_2.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u"data/images/settings_ico.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_settings_2.setIcon(icon4)
        self.btn_settings_2.setIconSize(QSize(32, 32))
        self.btn_settings_2.setCheckable(False)
        self.btn_settings_2.setFlat(True)

        self.horizontalLayout_10.addWidget(self.btn_settings_2)

        self.horizontalLayout_9.addLayout(self.horizontalLayout_10)

        self.verticalLayout.addLayout(self.horizontalLayout_9)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        icon5 = QIcon()
        icon5.addFile(u"C:/Users/ruden/.designer/backup/data/images/tyan.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tools_tab.addTab(self.main_tab, icon5, "")
        self.sounds_tab = QWidget()
        self.sounds_tab.setObjectName(u"sounds_tab")
        self.verticalLayout_4 = QVBoxLayout(self.sounds_tab)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.header_layout = QHBoxLayout()
        self.header_layout.setObjectName(u"header_layout")
        self.header_layout.setContentsMargins(5, 5, 5, 10)
        self.search_layout = QHBoxLayout()
        self.search_layout.setSpacing(0)
        self.search_layout.setObjectName(u"search_layout")
        self.search_layout.setContentsMargins(5, 20, -1, 10)
        self.search_input = QLineEdit(self.sounds_tab)
        self.search_input.setObjectName(u"search_input")
        sizePolicy.setHeightForWidth(self.search_input.sizePolicy().hasHeightForWidth())
        self.search_input.setSizePolicy(sizePolicy)
        self.search_input.setMinimumSize(QSize(300, 25))
        self.search_input.setMaximumSize(QSize(300, 25))
        self.search_input.setBaseSize(QSize(0, 0))
        font = QFont()
        font.setPointSize(12)
        self.search_input.setFont(font)
        self.search_input.setFocusPolicy(Qt.StrongFocus)
        self.search_input.setFrame(True)

        self.search_layout.addWidget(self.search_input)

        self.searchButton = QPushButton(self.sounds_tab)
        self.searchButton.setObjectName(u"searchButton")
        self.searchButton.setEnabled(True)
        sizePolicy.setHeightForWidth(self.searchButton.sizePolicy().hasHeightForWidth())
        self.searchButton.setSizePolicy(sizePolicy)
        self.searchButton.setMinimumSize(QSize(50, 26))
        self.searchButton.setMaximumSize(QSize(50, 26))
        font1 = QFont()
        font1.setPointSize(10)
        self.searchButton.setFont(font1)
        self.searchButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.search_layout.addWidget(self.searchButton)

        self.header_layout.addLayout(self.search_layout)

        self.horizontalSpacer = QSpacerItem(553, 54, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.header_layout.addItem(self.horizontalSpacer)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(8)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setSizeConstraint(QLayout.SetFixedSize)
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, 1)
        self.btn_add_sound = QPushButton(self.sounds_tab)
        self.btn_add_sound.setObjectName(u"btn_add_sound")
        sizePolicy.setHeightForWidth(self.btn_add_sound.sizePolicy().hasHeightForWidth())
        self.btn_add_sound.setSizePolicy(sizePolicy)
        self.btn_add_sound.setMinimumSize(QSize(32, 32))
        self.btn_add_sound.setMaximumSize(QSize(32, 32))
        self.btn_add_sound.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_add_sound.setIcon(icon1)
        self.btn_add_sound.setIconSize(QSize(32, 32))
        self.btn_add_sound.setAutoDefault(False)
        self.btn_add_sound.setFlat(True)

        self.horizontalLayout_6.addWidget(self.btn_add_sound)

        self.btn_favorite = QPushButton(self.sounds_tab)
        self.btn_favorite.setObjectName(u"btn_favorite")
        sizePolicy.setHeightForWidth(self.btn_favorite.sizePolicy().hasHeightForWidth())
        self.btn_favorite.setSizePolicy(sizePolicy)
        self.btn_favorite.setMinimumSize(QSize(32, 32))
        self.btn_favorite.setMaximumSize(QSize(32, 32))
        self.btn_favorite.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_favorite.setIcon(icon3)
        self.btn_favorite.setIconSize(QSize(32, 32))
        self.btn_favorite.setFlat(True)

        self.horizontalLayout_6.addWidget(self.btn_favorite)

        self.btn_minimize_window = QPushButton(self.sounds_tab)
        self.btn_minimize_window.setObjectName(u"btn_minimize_window")
        sizePolicy.setHeightForWidth(self.btn_minimize_window.sizePolicy().hasHeightForWidth())
        self.btn_minimize_window.setSizePolicy(sizePolicy)
        self.btn_minimize_window.setMinimumSize(QSize(32, 32))
        self.btn_minimize_window.setMaximumSize(QSize(32, 32))
        self.btn_minimize_window.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_minimize_window.setIcon(icon2)
        self.btn_minimize_window.setIconSize(QSize(32, 30))
        self.btn_minimize_window.setFlat(True)

        self.horizontalLayout_6.addWidget(self.btn_minimize_window)

        self.btn_keyboard = QPushButton(self.sounds_tab)
        self.btn_keyboard.setObjectName(u"btn_keyboard")
        sizePolicy.setHeightForWidth(self.btn_keyboard.sizePolicy().hasHeightForWidth())
        self.btn_keyboard.setSizePolicy(sizePolicy)
        self.btn_keyboard.setMinimumSize(QSize(0, 0))
        self.btn_keyboard.setMaximumSize(QSize(32, 32))
        self.btn_keyboard.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u"data/images/keyboard_ico.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_keyboard.setIcon(icon6)
        self.btn_keyboard.setIconSize(QSize(32, 30))
        self.btn_keyboard.setCheckable(False)
        self.btn_keyboard.setFlat(True)

        self.horizontalLayout_6.addWidget(self.btn_keyboard)

        self.btn_settings = QPushButton(self.sounds_tab)
        self.btn_settings.setObjectName(u"btn_settings")
        sizePolicy.setHeightForWidth(self.btn_settings.sizePolicy().hasHeightForWidth())
        self.btn_settings.setSizePolicy(sizePolicy)
        self.btn_settings.setMinimumSize(QSize(0, 0))
        self.btn_settings.setMaximumSize(QSize(32, 32))
        self.btn_settings.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_settings.setIcon(icon4)
        self.btn_settings.setIconSize(QSize(32, 32))
        self.btn_settings.setCheckable(False)
        self.btn_settings.setFlat(True)

        self.horizontalLayout_6.addWidget(self.btn_settings)

        self.header_layout.addLayout(self.horizontalLayout_6)

        self.verticalLayout_4.addLayout(self.header_layout)

        self.body_sounds = QHBoxLayout()
        self.body_sounds.setSpacing(6)
        self.body_sounds.setObjectName(u"body_sounds")
        self.body_sounds.setContentsMargins(-1, -1, 0, -1)
        self.scrollArea = QScrollArea(self.sounds_tab)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy1)
        self.scrollArea.setAutoFillBackground(False)
        self.scrollArea.setStyleSheet(u"background-color: rgba(255, 255, 255, 100);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 640, 285))
        self.verticalLayout_7 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.body_sounds.addWidget(self.scrollArea)

        self.verticalLayout_4.addLayout(self.body_sounds)

        self.tools_tab.addTab(self.sounds_tab, "")
        self.translate_tab = QWidget()
        self.translate_tab.setObjectName(u"translate_tab")
        self.verticalLayout_3 = QVBoxLayout(self.translate_tab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.translate_tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFrameShape(QFrame.WinPanel)
        self.label_2.setTextFormat(Qt.AutoText)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setWordWrap(False)

        self.verticalLayout_3.addWidget(self.label_2)

        self.tools_tab.addTab(self.translate_tab, "")
        self.clean_tab = QWidget()
        self.clean_tab.setObjectName(u"clean_tab")
        self.verticalLayout_2 = QVBoxLayout(self.clean_tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.clean_tab)
        self.label.setObjectName(u"label")
        self.label.setFrameShape(QFrame.WinPanel)
        self.label.setTextFormat(Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(False)

        self.verticalLayout_2.addWidget(self.label)

        self.tools_tab.addTab(self.clean_tab, "")

        self.horizontalLayout_8.addWidget(self.tools_tab)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tools_tab.setCurrentIndex(0)
        self.btn_add_sound_5.setDefault(False)
        self.btn_favorite_5.setDefault(False)
        self.btn_add_sound.setDefault(False)
        self.btn_favorite.setDefault(False)

        QMetaObject.connectSlotsByName(MainWindow)
        # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MangaTools", None))
        self.btn_add_sound_5.setText("")
        # if QT_CONFIG(shortcut)
        self.btn_add_sound_5.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl++", None))
        # endif // QT_CONFIG(shortcut)
        self.btn_minimize_window_5.setText("")
        # if QT_CONFIG(shortcut)
        self.btn_minimize_window_5.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+M", None))
        # endif // QT_CONFIG(shortcut)
        self.btn_favorite_5.setText("")
        # if QT_CONFIG(shortcut)
        self.btn_favorite_5.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+F", None))
        # endif // QT_CONFIG(shortcut)
        self.btn_settings_2.setText("")
        # if QT_CONFIG(shortcut)
        self.btn_settings_2.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
        # endif // QT_CONFIG(shortcut)
        self.tools_tab.setTabText(self.tools_tab.indexOf(self.main_tab), QCoreApplication.translate("MainWindow",
                                                                                                    u"\u0413\u043b\u0430\u0432\u043d\u0430\u044f",
                                                                                                    None))
        self.search_input.setText("")
        self.searchButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.btn_add_sound.setText("")
        # if QT_CONFIG(shortcut)
        self.btn_add_sound.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl++", None))
        # endif // QT_CONFIG(shortcut)
        self.btn_favorite.setText("")
        # if QT_CONFIG(shortcut)
        self.btn_favorite.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+F", None))
        # endif // QT_CONFIG(shortcut)
        self.btn_minimize_window.setText("")
        # if QT_CONFIG(shortcut)
        self.btn_minimize_window.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+M", None))
        # endif // QT_CONFIG(shortcut)
        # if QT_CONFIG(whatsthis)
        self.btn_keyboard.setWhatsThis(QCoreApplication.translate("MainWindow",
                                                                  u"\u042d\u043a\u0440\u0430\u043d\u043d\u0430\u044f \u043a\u043b\u0430\u0432\u0438\u0430\u0442\u0443\u0440\u0430",
                                                                  None))
        # endif // QT_CONFIG(whatsthis)
        self.btn_keyboard.setText("")
        # if QT_CONFIG(shortcut)
        self.btn_keyboard.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+K", None))
        # endif // QT_CONFIG(shortcut)
        self.btn_settings.setText("")
        # if QT_CONFIG(shortcut)
        self.btn_settings.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
        # endif // QT_CONFIG(shortcut)
        self.tools_tab.setTabText(self.tools_tab.indexOf(self.sounds_tab),
                                  QCoreApplication.translate("MainWindow", u"\u0417\u0432\u0443\u043a\u0438", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow",
                                                        u"<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">\u0411\u0443\u0434\u0435\u0442 \u0434\u043e\u0441\u0442\u0443\u043f\u043d\u043e \u0432 \u043d\u043e\u0432\u044b\u0445 \u0432\u0435\u0440\u0441\u0438\u044f\u0445!</span></p></body></html>",
                                                        None))
        self.tools_tab.setTabText(self.tools_tab.indexOf(self.translate_tab), QCoreApplication.translate("MainWindow",
                                                                                                         u"\u041f\u0435\u0440\u0435\u0432\u043e\u0434",
                                                                                                         None))
        self.label.setText(QCoreApplication.translate("MainWindow",
                                                      u"<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">\u0411\u0443\u0434\u0435\u0442 \u0434\u043e\u0441\u0442\u0443\u043f\u043d\u043e \u0432 \u043d\u043e\u0432\u044b\u0445 \u0432\u0435\u0440\u0441\u0438\u044f\u0445!</span></p></body></html>",
                                                      None))
        self.tools_tab.setTabText(self.tools_tab.indexOf(self.clean_tab),
                                  QCoreApplication.translate("MainWindow", u"\u041a\u043b\u0438\u043d", None))
    # retranslateUi

