def set_keymap(self, keymap: str, keyboard: str):
    if keyboard == "add_sound":
        keyboard_keymaps = [
            # карта расположения кнопок
            [self.btn_ra, self.btn_ya, self.btn_ma, self.btn_ha, self.btn_na, self.btn_ta, self.btn_sa, self.btn_ka,
             self.btn_a,
             self.btn_ri, self.btn_, self.btn_mi, self.btn_hi, self.btn_ni, self.btn_chi, self.btn_shi, self.btn_ki,
             self.btn_i,
             self.btn_ru, self.btn_yu, self.btn_mu, self.btn_fu, self.btn_nu, self.btn_tsu, self.btn_su, self.btn_ku,
             self.btn_u,
             self.btn_re, self.btn_1, self.btn_me, self.btn_he, self.btn_ne, self.btn_te, self.btn_se, self.btn_ke,
             self.btn_e,
             self.btn_ro, self.btn_yo, self.btn_mo, self.btn_ho, self.btn_no, self.btn_to, self.btn_so, self.btn_ko,
             self.btn_o,
             self.btn_kana, self.btn_small, self.btn_mark, self.btn_backspace, self.btn_dash, self.btn_clear,
             self.btn_spliter, self.btn_n, self.btn_wa],
            # раскладка для хираганы
            ["ら", "や", "ま", "は", "な", "た", "さ", "か", "あ",
             "り", "_", "み", "ひ", "に", "ち", "し", "き", "い",
             "る", "ゆ", "む", "ふ", "ぬ", "つ", "す", "く", "う",
             "れ", "_", "め", "へ", "ね", "て", "せ", "け", "え",
             "ろ", "よ", "も", "ほ", "の", "と", "そ", "こ", "お",
             "ア", "あぁ", "゜゛", "←", "ー", "×", ", ", "わ", "ん"],
            # раскладка для катаканы
            ["ラ", "ヤ", "マ", "ハ", "ナ", "タ", "サ", "カ", "ア",
             "リ", "_", "ミ", "ヒ", "ニ", "チ", "シ", "キ", "イ",
             "ル", "ユ", "ム", "フ", "ヌ", "ツ", "ス", "ク", "ウ",
             "レ", "_", "メ", "ヘ", "ネ", "テ", "セ", "ケ", "エ",
             "ロ", "ヨ", "モ", "ホ", "ノ", "ト", "ソ", "コ", "オ",
             "abc", "アァ", "゜゛", "←", "ー", "×", ", ", "ワ", "ン"],
            # раскладка для английского
            ["a", "b", "c", "d", "e", "f", "g", "h", "i",
             "j", "k", "l", "m", "n", "o", "p", "q", "r",
             "s", "t", "u", "v", "w", "x", "y", "z", "_",
             "_", "_", "_", "_", "_", "_", "_", "_", "_",
             "_", "_", "_", "_", "_", "_", "_", "_", "_",
             "абв", "Aa", "_", "←", "-", "×", ", ", "_", "_"],
            # раскладка для российского
            ["а", "б", "в", "г", "д", "е", "ё", "ж", "з",
             "и", "й", "к", "л", "м", "н", "о", "п", "р",
             "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ",
             "ъ", "ы", "ь", "э", "ю", "я", "_", "_", "_",
             "_", "_", "_", "_", "_", "_", "_", "_", "_",
             "あ", "Аа", "", "←", "-", "×", ", ", "_", "_"]
        ]
    elif keyboard == "main":
        keyboard_keymaps = [
            # карта расположения кнопок
            [self.btn_na, self.btn_ta, self.btn_sa, self.btn_ka, self.btn_a,
             self.btn_ni, self.btn_chi, self.btn_shi, self.btn_ki, self.btn_i,
             self.btn_nu, self.btn_tsu, self.btn_su, self.btn_ku, self.btn_u,
             self.btn_ne, self.btn_te, self.btn_se, self.btn_ke, self.btn_e,
             self.btn_no, self.btn_to, self.btn_so, self.btn_ko, self.btn_o,
             self.btn_wa, self.btn_ra, self.btn_ya, self.btn_ma, self.btn_ha,
             self.btn_wo, self.btn_ri, self.btn_1, self.btn_mi, self.btn_hi,
             self.btn_n, self.btn_ru, self.btn_yu, self.btn_mu, self.btn_fu,
             self.btn_dash, self.btn_re, self.btn_2, self.btn_me, self.btn_he,
             self.btn_backspace, self.btn_ro, self.btn_yo, self.btn_mo, self.btn_ho,
             self.btn_kana, self.btn_small, self.btn_mark, self.btn_clear, self.btn_search],
            # раскладка для хираганы
            ["な", "た", "さ", "か", "あ",
             "に", "ち", "し", "き", "い",
             "ぬ", "つ", "す", "く", "う",
             "ね", "て", "せ", "け", "え",
             "の", "と", "そ", "こ", "お",

             "わ", "ら", "や", "ま", "は",
             "_", "り", "_", "み", "ひ",
             "ん", "る", "ゆ", "む", "ふ",
             "ー", "れ", "_", "め", "へ",
             "←", "ろ", "よ", "も", "ほ",

             "ア", "あぁ", "゜゛", "×", "↵"],
            # раскладка для катаканы
            ["ナ", "タ", "サ", "カ", "ア",
             "ニ", "チ", "シ", "キ", "イ",
             "ヌ", "ツ", "ス", "ク", "ウ",
             "ネ", "テ", "セ", "ケ", "エ",
             "ノ", "ト", "ソ", "コ", "オ",

             "ワ", "ラ", "ヤ", "マ", "ハ",
             "_", "リ", "_", "ミ", "ヒ",
             "ン", "ル", "ユ", "ム", "フ",
             "ー", "レ", "_", "メ", "ヘ",
             "←", "ロ", "ヨ", "モ", "ホ",

             "ア", "アァ", "゜゛", "×", "↵"],
            # раскладка для английского
            ["a", "b", "c", "d", "e",
             "f", "g", "h", "i", "j",
             "k", "l", "m", "n", "o",
             "p", "q", "r", "s", "t",
             "u", "v", "w", "x", "y",

             "z", "_", "_", "_", "_",
             "_", "_", "_", "_", "_",
             "_", "_", "_", "_", "_",
             "-", "_", "_", "_", "_",
             "←", "_", "_", "_", "_",

             "абв", "Aa", "_", "×", "↵"],
            # раскладка для российского
            ["а", "б", "в", "г", "д",
             "е", "ё", "ж", "з", "и",
             "й", "к", "л", "м", "н",
             "о", "п", "р", "с", "т",
             "у", "ф", "х", "ц", "ч",

             "ш", "щ", "ъ", "ы", "ь",
             "э", "ю", "я", "_", "_",
             "_", "_", "_", "_", "_",
             "-", "_", "_", "_", "_",
             "←", "_", "_", "_", "_",

             "あ", "Аа", "_", "×", "↵"]
        ]

    if keymap == 'hiragana':
        keymap_index = 1
    elif keymap == 'katakana':
        keymap_index = 2
    elif keymap == 'english':
        keymap_index = 3
    elif keymap == "russian":
        keymap_index = 4
    else:
        keymap_index = 1

    index = 0

    for i in keyboard_keymaps[0]:
        symbol = keyboard_keymaps[keymap_index][index]
        if symbol == "_":
            symbol = ""
        i.setText(symbol)
        index += 1
