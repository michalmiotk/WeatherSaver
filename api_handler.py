import json

import requests


class ApiHandler():
    def __init__(self):
        self.url = 'https://danepubliczne.imgw.pl/api/data/synop'

    def request_bytes_content(self):
        status_code = None
        while status_code != 200:
            response = requests.get(self.url, timeout=(2,10))
            status_code = response.status_code
            if status_code == 200:
                return response.content
            else:
                print(f"kod odpowiedzi serwera to {response.status_code} \
                problem z połączeniem, proszę poczekać")

    def request_dict_list(self):
        bytes_response = self.request_bytes_content()
        if bytes_response:
            string_response = self.decoder(bytes_response)
            return json.loads(string_response)
        else:
            return []

    @staticmethod
    def decoder(bytes_input):
        return bytes_input.decode("unicode_escape")