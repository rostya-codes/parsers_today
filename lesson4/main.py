import json

import requests
from bs4 import BeautifulSoup
import lxml


headers = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0',

}

for offset in range(0, 24, 24):
    url = f'https://www.skiddle.com/festivals/search/?sort=0&fest_name=&from_date=11%20Nov%202024&to_date=&maxprice=500&o={offset}'

    req = requests.get(url=url, headers=headers)
    json_data = json.loads(req.text)
    html_response = json_data['html']

    with open(f'index_{offset}.html', 'w') as file:
        file.write(html_response)
