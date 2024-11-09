import re

from bs4 import BeautifulSoup


with open('../scrap_tutorial/lesson1/blank/index.html') as file:
    src = file.read()
# print(scr)


soup = BeautifulSoup(src, 'lxml')

# title = soup.title
# print(title)
# print(title.text)
# print(title.string)

# .find() .find_all()
# page_h1 = soup.find('h1')
# print(page_h1)

# page_all_h1 = soup.find_all('h1')
# print(page_all_h1)

# for item in page_all_h1:
#     print(item.text)

# print()

# Объект BeautifulSoup в котором доступны методы этого класса
# user__name = soup.find('div', class_='user__name').find('span').text
# print(user__name)


# user_name = soup.find('div', {'class': 'user__name', 'id': 'aaa'}).find(
#     'span').text
# print(user_name)

# find_all_spans_in_user_info = soup.find(class_='user__info').find_all('span')
# for i in find_all_spans_in_user_info:
#     print(i.text)

# print(find_all_spans_in_user_info[0].text)

# social_links = soup.find(class_='social__networks').find(
#     'ul').find_all('a')
# print(social_links)

# all_a = soup.find_all('a')
# print(all_a)

# for i in all_a:
#     item_text = i.text
#     item_url = i.get('href')
#     print(f'{item_text}: {item_url}')


# .find_parent() .find_parents() используются когда нужно подниматься, а не опускаться вглубь кода

# post_text = soup.find(class_='post__text').find_parent('div', 'user__post')
# print(post_text)

# post_divs = soup.find(class_='post__text').find_parents('div', 'user__post')
# print(post_divs)

# .next_element .previous_element
# next_el = soup.find(class_='post__title').next_element.next_element.text
# print(next_el)

# next_el = soup.find(class_='post__title').find_next().text
# print(next_el)

# find_next_sibling() .find_previous_sibling()
# next_sib = soup.find(class_='post__title').find_next_sibling()
# print(next_sib)

# prev_sib = soup.find(class_='post__date').find_previous_sibling()
# print(prev_sib)

# post_title = soup.find(class_='post__date').find_previous_sibling(
# ).find_next().text
# print(post_title)

# links = soup.find(class_='some__links').find_all('a')
# print(links)

# for link in links:

#     link_href_attr = link.get('href')
#     link_href_attr1 = link['href']
#
#     link_data_attr = link.get('data-attr')
#     link_data_attr1 = link['data-attr']
#
#     print(link_href_attr)
#     print(link_href_attr1)
#     print(link_data_attr)
#     print(link_data_attr1)

# find_a_by_text = soup.find('a', text='Одежда')
# print(find_a_by_text)

# find_a_by_text = soup.find('a', text='Одежда для взрослых')
# print(find_a_by_text)

find_a_by_text = soup.find('a', string=re.compile('Одежда'))
print(find_a_by_text)

find_all_clothes = soup.find_all(string=re.compile('([Оо]дежда)'))
print(find_all_clothes)
print('([Оо]дежда)')
