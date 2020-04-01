import requests
import csv
import datetime
from bs4 import BeautifulSoup
import time
# time.sleep(10)


# URL_YA = 'https://yandex.ru/search/?lr=35&text='''
# https://www.yandex.ru/search/?text=abuse&lr=35


ROOT_URL_YA = 'https://yandex.ru/search/?'
# ROOT_URL_GOOGLE = 'https://google.com/search/?'
# URL_MAILRU = 'https://go.mail.ru/search?q=seat&fm=1'
HEADERS = {'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
date_stamp = datetime.datetime.today().strftime("%Y-%m-%d-%H-%M-%S-")


search_links = []
recursive_search_array = []


# Сначала ищем в Яндекс
serp_string = input('Что ищем?: ')
serp_results = input('Сколько результатов найти?: ')
rec_search = True
search_url = str(ROOT_URL_YA + 'text=' + serp_string + '&lr=' + serp_results)
result_type = input('Укажите конечный формат для результата: json, csv, console ')
# rec_search = input('Рекурсивный поиск (1) или только поисковая выдача (0) ?:')
result_type = 'csv'
result_file_serp = str(date_stamp + '--result.' + result_type)
result_file_recursive = str(date_stamp + '--result-recursive.' + result_type)
# print(result_file_serp)
if rec_search:
    print(result_file_recursive)
else:
    print(result_file_serp)


def main():
    response = requests.get(search_url, headers=HEADERS)
    response.encoding = 'utf-8'
    print(search_url)
    if response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')
        li = soup.find_all('li', class_='serp-item')
        for el in li:
            link = el.find('a').get('href')
            name = el.find('a').get_text()
            result_link = [name, link]
            search_links.append(result_link)
        print(len(search_links))
        # print(search_links)
        csv.writer(open(result_file_serp, "w", newline='')).writerows(search_links)
    else:
        print('Error!')


def recursive_search():
    look_for = search_links[0][1]
    print('Парсим сайт: ' + look_for)
    recursive_response = requests.get(look_for, headers=HEADERS)
    recursive_soup = BeautifulSoup(recursive_response.text, 'html.parser')
    for el in recursive_soup.findAll('a'):
        link = str(el.get('href'))
        name = str(el.get_text())
        # name = el.find('a').get_text()
        result_link = [link, name]
        recursive_search_array.append(result_link)
        print(result_link)
        csv.writer(open(result_file_recursive, "w", newline='')).writerows(recursive_search_array)
    print(len(recursive_search_array))


if __name__ == '__main__':
    main()
    recursive_search()
    if rec_search:
        print('Рекурсивный поиск завершен!')
    else:
        print('Поисковая выдача завершена!')