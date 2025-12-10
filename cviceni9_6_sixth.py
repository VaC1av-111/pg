from sixth import download_url_and_get_all_hrefs
from unittest.mock import MagicMock
import requests

def test_download_url_and_get_all_hrefs():
    data = '<html><body><a href="https://jcu.cz">odkaz</a><div><a href="https://ef.jcu.cz/kontakt">kontakt</a></div></body></html>'

    requests.get = MagicMock(
        return_value = MagicMock(ok = True, text = data))
href = download_url_and_get_all_hrefs('xxx')
   
if __name__ == "__main__":
    
    print (test_download_url_and_get_all_hrefs())