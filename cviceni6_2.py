import requests
import sys
import json

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print (f'Usage: {sys.argv[0]} prefix')
        sys.exit()

    prefix = sys.argv[1]
    print(f'Download modeles for prefix: {prefix}')

    response = requests.get('https://data.carnewschina.com/suggest?q=' + prefix)

    if not response.ok:
        print(f'Nastala chyaba: {response.status_code}')
        sys.exit()
    
    data = json.loads(response.text)
    for model in data['models']:
        print(model['name'])
    