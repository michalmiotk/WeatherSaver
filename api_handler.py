import json

import requests

class ApiHandler():
    def __init__(self):
        self.url = 'https://danepubliczne.imgw.pl/api/data/synop'

    def request_bytes_content(self):
        try:
            response = requests.get(self.url, timeout=(2,10))
        except requests.exceptions.ReadTimeout as e:
            print("za długie oczekiwanie na odpowiedz serwera", e)
            raise
        if response.status_code == 200:
            return response.content
        else:
            raise ConnectionError(f"kod odpowiedzi serwera to {response.status_code} problem z połączeniem, proszę spróbuj jeszcze raz włączyć program")
            return b''

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