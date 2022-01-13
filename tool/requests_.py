import json
import requests

from data.config_data import UPSTREAM_HEADERS, DOWNSTREAM_HEADERS,TEST_IP


class Requests:
    def __init__(self, up_or_down='up'):
        self.ip=TEST_IP
        self.up_or_down = up_or_down
        if self.up_or_down == 'up':
            self.headers = UPSTREAM_HEADERS
        elif self.up_or_down == 'down':
            self.headers = DOWNSTREAM_HEADERS

    def get(self, url):
        result = requests.get(url=self.ip+url, headers=self.headers)

        return result

    def post(self, url, data):
        result = requests.post(url=self.ip+url, headers=self.headers, data=json.dumps(data))
        return result
