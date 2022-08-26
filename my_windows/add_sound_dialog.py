from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow

from ui_designer import Ui_AddSoundDialog
from api import RudenAPI
from sqlite import pb


class AddSoundDialog(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(AddSoundDialog, self).__init__(*args, **kwargs)
        self.cleared_text = None
        self._pressed = False
        self.Direction = None
        self.send_data = None

        # Нет границы
        self.setWindowFlag(Qt.FramelessWindowHint)

        # Отслеживание мыши
        self.setMouseTracking(True)

        self.ui = Ui_AddSoundDialog()
        self.ui.setupUi(self)

        # слот сигнала
        self.ui.TitleBar.windowClosed.connect(self.close)
        self.ui.TitleBar.windowMoved.connect(self.move)

        # привязываем кнопки к событиям
        self.ui.close_btn.clicked.connect(self.ui.TitleBar.windowClosed.emit)
        self.ui.cancel.clicked.connect(self.ui.TitleBar.windowClosed.emit)
        self.ui.send.clicked.connect(self.send)
        self.ui.save_local.clicked.connect(self.save_local)

    def add_send_data(self, data: dict):
        self.send_data = data

    def send(self):
        if self.send_data:
            api = RudenAPI()
            result = api.add_sound(self.send_data)
            print(result)
            self.save_local()
            if not result:
                return 'Не удалось отправить данные, попробуйте включить "Использовать прокси" в настройках.'
            else:
                return 'Отправка данных успешна!'
        else:
            return 'Вы не добавили данне для отправки, пожалуйста воспользуйтесь методом add_send_data(data: dict)'

    def save_local(self):
        cur = pb.base.cursor()
        data = self.send_data
        cur.execute("""INSERT INTO sounds (kun, hep, hir, kat, eng, rus, mean, mean2) 
                          VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", (data['kun'], data['hep'], data['hir'], data['kat'],
                                                               data['eng'], data['rus'], data['mean'], data['mean2']))
        pb.base.commit()
