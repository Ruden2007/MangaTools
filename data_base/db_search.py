from data_base import sqlite_base
from fuzzywuzzy import fuzz


class SoundSearch:
    def __init__(self, accuracy=70):
        sqlite_base.sqlite_start()

        sqlite_base.cur.execute('''SELECT * FROM sounds''')
        self.res = sqlite_base.cur.fetchall()

        self.accuracy = accuracy

    def search(self, search_input: str):

        results = []  # список содержащий строки и коэффициент совпадения

        for i in self.res:
            # id строки
            str_id = i[0]

            # содержат один элемент в строке
            kun = i[1]  # Кунрэй
            hep = i[2]  # Хэпбёрн
            hir = i[3]  # Хирагана
            kat = i[4]  # Катакана

            # могут содержать несколько элементов в строке через ","
            eng = i[5]  # Английский
            rus = i[6]  # Русский

            # не участвуют в поиске
            mean = i[7]  # Значение
            mean2 = i[8]  # Уточнённое значение

            # ищем коэффициенты для элементов содержащих один элемент в строке
            k_kun = fuzz.WRatio(search_input, kun)  # Кунрэй
            k_hep = fuzz.WRatio(search_input, hep)  # Хэпбёрн
            k_hir = fuzz.WRatio(search_input, hir)  # Хирагана
            k_kat = fuzz.WRatio(search_input, kat)  # Катакана

            # ищем коэффициенты для элементов содержащих несколько элементов в строке
            k_eng = self.string_with_multiple(eng, search_input)
            k_rus = self.string_with_multiple(rus, search_input)

            match = max([k_kun, k_hep, k_hir, k_kat, k_eng, k_rus])

            if match > self.accuracy:
                results.append([str_id, kun, hep, hir, kat, eng, rus, mean, mean2, match])
                if __name__ == '__main__':
                    print(f"\n{i}")
                    print(f"Совпадение: {match}%")
                    print(f"Кунрэй {kun} совпадает на {k_kun}%")
                    print(f"Хэпбёрн {hep} совпадает на {k_hep}%")
                    print(f"Хирагана {hir} совпадает на {k_hir}%")
                    print(f"Катакана {kat} совпадает на {k_kat}%")
                    print(f"Английский {eng} совпадает на {k_eng}%")
                    print(f"Русский {rus} совпадает на {k_rus}%")

        results = sorted(results, key=lambda pairt: pairt[9], reverse=True)
        return results

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


def main():
    search_input = input("Введите звук:")

    s = SoundSearch()
    print(s.search(search_input))


if __name__ == '__main__':
    sqlite_base.sqlite_start()
    main()
