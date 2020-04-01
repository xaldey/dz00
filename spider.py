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
search_links = []
recursive_search_array = []
# print(result_file_serp)


def main():
    if rec_search:
        print(result_file_recursive)
        print('Рекурсивный поиск запущен!')
        response = requests.get(search_url, headers=HEADERS)
        # response.encoding = 'cp1251'
        print(search_url)
        if response.ok:
            soup = BeautifulSoup(response.text, 'html.parser')
            li = soup.find_all('li', class_='serp-item')
            for el in li:
                link = el.find('a').get('href')
                name = el.find('a').get_text()
                result_link = [name, link]
                search_links.append(result_link)
                # csv.writer(open(result_file_serp, "w", newline='')).writerows(search_links)
            print(len(search_links))
        else:
            print('Error!')
    else:
        print(result_file_serp)
        print('Поисковая выдача запущена!')


def recursive_search():
    look_for = search_links[0][1]
    print('Парсим сайт: ' + look_for)
    recursive_response = requests.get(look_for, headers=HEADERS)
    if recursive_response.ok:
        recursive_soup = BeautifulSoup(recursive_response.text, 'html.parser')
        # a_list = recursive_soup("a")
        # print(a_list)
        for el in recursive_soup.findAll('a'):
            link = str(el.get('href'))
            name = str(el.get_text())
            result_link = [name, link]
            recursive_search_array.append(result_link)
            #print(result_link)
            csv.writer(open(result_file_recursive, "w", newline='')).writerows(recursive_search_array)
        print(len(recursive_search_array))
    else:
        print('error! cant get response')


def result_export():
    if result_type == 'csv':
        print('CSV export!')
        for el in search_links:
            csv.writer(open(result_file_serp, "w", newline='')).writerows(search_links)
    elif result_type == 'json':
        pass
    else:
        print('Console output!')
        print(search_links)


if __name__ == '__main__':
    main()
    recursive_search()
    result_export()