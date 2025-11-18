import sys
import requests
import re


def download_url_and_get_all_hrefs(url):
    """
    Funkce stahne url predanou v parametru url pomoci volani response = requests.get(),
    zkontroluje navratovy kod response.status_code, ktery musi byt 200,
    pokud ano, najdete ve stazenem obsahu stranky response.content vsechny vyskyty
    <a href="url">odkaz</a> a z nich nactete url, ktere vratite jako seznam pomoci return
    """

    hrefs = []

    response = requests.get(url)

    if response.status_code == 200:
        hrefs = re.findall(r'href="(.*?)"', response.text)
    else: print(f'Navratovy kod != 200')

    return hrefs


if __name__ == "__main__":
    
    try:
        url = sys.argv[1]
        print(download_url_and_get_all_hrefs(url))
    except Exception as e:
        print(f"Program skoncil chybou: {e}")

