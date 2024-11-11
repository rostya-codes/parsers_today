import requests
from bs4 import BeautifulSoup
import json


# persons_url_list = []

# for offset in range(0, 740, 12):
#     # Получить все ссылки на учасников и сохранить их в .txt файл
#     url = f'https://www.bundestag.de/ajax/filterlist/en/members/863330-863330?limit=12&noFilterSet=true&offset={offset}'
#     print(url)

#     q = requests.get(url)
#     result = q.content

#     soup = BeautifulSoup(result, 'lxml')
#     persons = soup.find_all(class_='bt-slide-content')

#     for person in persons:
#         a = person.find('a')
#         person_page_url = a.get('href')
#         persons_url_list.append(person_page_url)
#         print(a['href'])


# with open('persons_url_list.txt', 'a') as file:
#     for line in persons_url_list:
#         file.write(f'{line}\n')


with open('persons_url_list.txt') as file:

    lines = [line.strip() for line in file.readlines()]

    data_dicts = []
    count = 0
    for line in lines:
        q = requests.get(line)
        result = q.content

        soup = BeautifulSoup(result, 'lxml')
        person = soup.find(class_='bt-biografie-name').find('h2').text
        person_name_company = person.strip().split(',')
        person_name = person_name_company[0]
        person_company = person_name_company[1].strip()

        social_networks = soup.find_all(class_='bt-link-extern')

        social_networks_urls = []
        for item in social_networks:
            social_networks_urls.append(item.get('href'))

        data = {
            'person_name': person_name,
            'company_name': person_company,
            'social_networks': social_networks_urls,
        }
        count += 1
        print(f'#{count}: {line} is done!')

        data_dicts.append(data)

        with open('data.json', 'w') as json_file:
            json.dump(data_dicts, json_file, indent=4, ensure_ascii=False)
