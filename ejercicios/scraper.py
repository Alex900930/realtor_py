from os import path
from pathlib import PurePath

import requests

with open('urls.txt', 'r') as fh:
    urls = fh.readlines()
urls = [url.strip() for url in urls]  # strip `\n`

for url in urls:
    file_name = PurePath(url).name
    file_path = path.join('.', file_name)
    text = ''

    try:
        response = requests.get(url)
        if response.ok:
            text = response.text
    except requests.exceptions.ConnectionError as exc:
        print(exc)
    
    with open(file_path, 'w') as fh:
        fh.write(text)

    print('Written to', file_path)
