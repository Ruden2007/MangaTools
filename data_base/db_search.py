from fuzzywuzzy import fuzz
from colorama import init, Fore
from sqlite import sb, pb, sbcursor, pbcursor


class SoundSearch:
    def search(self, search_input: str):
        self.results = []  # список содержащий строки и коэффициент совпадения
        self.sound_filter(res=self.res, search_input=search_input, base="main")
        self.sound_filter(res=self.personal_res, search_input=search_input, base="personal")

        results = sorted(self.results, key=lambda pairt: pairt[9], reverse=True)
        return results

    def sound_filter(self, res, search_input: str, base: str):
        if base == "main":
            pass
        elif base == "personal":
            pass
        else:
            print(Fore.RED + f"Error: base может принимать значения: main, personal. Вы передали {base = }")
            return

        for i in res:
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
                if base == "personal":
                    str_id = f"{str_id}P"
                self.results.append([str_id, kun, hep, hir, kat, eng, rus, mean, mean2, match])

    @staticmethod
    def fetch_from_id(sound_id: str):
        sound_id = str(sound_id)
        if "P" in sound_id:
            sound_id = int(sound_id.replace("P", ""))
            pbcursor.execute("""SELECT * FROM sounds WHERE id = ?""", (sound_id, ))
            result = list(pbcursor.fetchone())
            result[0] = f"{result[0]}P"
            return result
        else:
            sound_id = int(sound_id)
            sbcursor.execute("""SELECT * FROM sounds WHERE id = ?""", (sound_id,))
            return sbcursor.fetchone()

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
        self.res = sb.get_all()

    def __init__(self, accuracy: int = 70):
        init()
        self.results = []
        self.res = sb.get_all()
        self.personal_res = pb.get_all_sounds()

        self.accuracy = accuracy
