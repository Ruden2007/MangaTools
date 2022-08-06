import configparser

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QIcon, QCursor
from PySide6.QtWidgets import QMessageBox

dictionary = configparser.ConfigParser()
dictionary.read("dictionaries/transcript.dict", "utf-8")


class Transcript:
    @staticmethod
    def hir_to_hep(text: str) -> str:
        """Генерирует хэпбёрном
        транскрипцию хираганы"""

        dict_hir_to_hep = dictionary.__dict__['_sections']['hiragana_to_hepburn']

        for key in dict_hir_to_hep.keys():
            text = text.replace(key, str(dict_hir_to_hep[key]))

        return text

    @staticmethod
    def hir_to_kun(text: str) -> str:
        """Генерирует кунреем
        транскрипцию хираганы"""

        dict_hir_to_hep = dictionary.__dict__['_sections']['hiragana_to_kunrei']

        for key in dict_hir_to_hep.keys():
            text = text.replace(key, str(dict_hir_to_hep[key]))

        return text

    @staticmethod
    def hir_to_kat(text: str) -> str:
        """Генерирует катаканой
        транскрипцию хираганы"""

        dict_hir_to_kat = dictionary.__dict__['_sections']['hiragana_to_katakana']

        for key in dict_hir_to_kat.keys():
            text = text.replace(key, str(dict_hir_to_kat[key]))

        return text

    @staticmethod
    def kat_to_hep(text: str) -> str:
        """Генерирует хэпбёрном
        транскрипцию катаканы"""

        dict_kat_to_hep = dictionary.__dict__['_sections']['katakana_to_hepburn']

        for key in dict_kat_to_hep.keys():
            text = text.replace(key, str(dict_kat_to_hep[key]))

        return text

    @staticmethod
    def kat_to_kun(text: str) -> str:
        """Генерирует кунреем
        транскрипцию катаканы"""

        dict_kat_to_hep = dictionary.__dict__['_sections']['katakana_to_kunrei']

        for key in dict_kat_to_hep.keys():
            text = text.replace(key, str(dict_kat_to_hep[key]))

        return text

    @staticmethod
    def kat_to_hir(text: str) -> str:
        """Генерирует хираганой
        транскрипцию катаканы"""

        dict_kat_to_hir = {v: k for k, v in dictionary.__dict__['_sections']['hiragana_to_katakana'].items()}

        for key in dict_kat_to_hir.keys():
            text = text.replace(key, str(dict_kat_to_hir[key]))

        return text
