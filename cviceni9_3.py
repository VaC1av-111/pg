from cviceni6 import fibonacci
import requests
import unittest
from unittest.mock import MagicMock


class Downloader:
    def __init__(self):
        self.url = ""
        self.data = {}
        self.get()
    def get(self):
        response = requests.get(self.url)
        if not response.ok:
            return None
        for line in response.text.split('\n')[2:]:
            s = line.split('|')
            if len(s) < 5:
                continue
            self.data[s[3]] =float(s[4].replace(',','.'))
    def convert_from_czk(self, amount_czk, code):
             return amount_czk / self.data[code]
    
def test_downloader_nok():
    requests.get = MagicMock(return_value =MagicMock(ok = False))
    downloader = Downloader()
    assert len(downloader.data) == 0


def test_downloader():
        assert downloader.convert_from_czk(100, 'USD') == 4.84
        requests.get = MagicMock(return_value =MagicMock(ok = True, text="""""" ))
        downloader = Downloader()
        assert round(downloader.convert_from_czk(100, 'USD'),2) == 5.0    

if __name__ == "__main__":
        downloader = Downloader ()
        downloader.get()
        print(downloader.convert_from_czk(100, 'USD'))