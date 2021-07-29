import json

import requests

class ApiHandler():
    def __init__(self):
        self.url = 'https://danepubliczne.imgw.pl/api/data/synop'

    def request_bytes_content(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.content
        else:
            return b''

    def request_dict(self):
        bytes_response = self.request_bytes_content()
        if bytes_response:
            string_response = self.decoder(bytes_response)
            return json.loads(string_response)
        else:
            return {}

    @staticmethod
    def decoder(bytes_input):
        return bytes_input.decode("unicode_escape")