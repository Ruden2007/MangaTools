from data_base import SoundBase
from fuzzywuzzy import fuzz


class SoundSearch:
    def search(self, search_input: str):
        results = []  # список содержащий строки и коэффициент совпадения

        for i in self.res:
            # id строки(int)
            str_id = i[0]

            # содержат один элемент в строке
            kun = i[1]  # Кунрэй(str)
            hep = i[2]  # Хэпбёрн(str)
            hir = i[3]  # Хирагана(str)
            kat = i[4]  # Катакана(str)

            # могут содержать несколько элементов в строке через ","
            eng = i[5]  # Английский(str)
            rus = i[6]  # Русский(str)

            # не участвуют в поиске
            mean = i[7]  # Значение(str)
            mean2 = i[8]  # Уточнённое значение(str)

            # ищем коэффициенты для элементов содержащих один элемент в строке
            k_kun = fuzz.WRatio(search_input, kun)  # Кунрэй(int 0-100)
            k_hep = fuzz.WRatio(search_input, hep)  # Хэпбёрн(int 0-100)
            k_hir = fuzz.WRatio(search_input, hir)  # Хирагана(int 0-100)
            k_kat = fuzz.WRatio(search_input, kat)  # Катакана(int 0-100)

            # ищем коэффициенты для элементов содержащих несколько элементов в строке
            k_eng = self.string_with_multiple(eng, search_input)
            k_rus = self.string_with_multiple(rus, search_input)

            match = max([k_kun, k_hep, k_hir, k_kat, k_eng, k_rus])

            if match > self.accuracy:
                results.append([str_id, kun, hep, hir, kat, eng, rus, mean, mean2, match])
        results = sorted(results, key=lambda pairt: pairt[9], reverse=True)
        return results

    @staticmethod
    def fetch_from_id(sound_id: int):
        sb = SoundBase()
        cursor = sb.base.cursor()
        cursor.execute("""SELECT * FROM sounds WHERE id = ?""", (sound_id, ))
        return cursor.fetchone()

    @staticmethod
    def string_with_multiple(string: str, search_input: str):
        if "," in string:
            split_string = string.split(",")
            k_list = []

            for e in split_string:
                k = fuzz.WRatio(search_input, e)
                k_list.append(k)

            return max(k_list)

        else:
            return fuzz.WRatio(search_input, string)

    def update_data(self):
        self.res = SoundBase().get_all()

    def __init__(self, accuracy: int = 70):
        self.res = SoundBase().get_all()

        self.accuracy = accuracy
