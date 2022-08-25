import configparser

import requests


class RudenAPI:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read("../settings.ini", "utf-8")

        if config['api']['use_proxy_server'] == "True":
            self.url = "https://rudenapi.000webhostapp.com/"
        else:
            self.url = "http://ruden.sytes.net/api/"
        print("Use url: " + self.url + "add-sound/")
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/103.0.5060.114 Safari/537.36 OPR/89.0.4447.64'
        }

    def add_sound(self, sound: dict):
        response = requests.post(url=self.url + "add-sound/", headers=self.headers, data=sound)
        j = response.json()
        print(j)
        if j['status'] == 'Ok':
            return True

    def set_headers(self, headers: dict):
        self.headers = headers


if __name__ == "__main__":
    api = RudenAPI()
    request = {
        'kun': 'ehthe',
        'hep': 'ekeg',
        'hir': 'eke',
        'kat': 'ewitjw',
        'eng': 'eori',
        'rus': 'qkrt',
        'mean': 'qtrk3',
        'mean2': 'q3rq39'
    }
    api.add_sound(sound=request)
