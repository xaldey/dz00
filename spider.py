import requests
import datetime
from bs4 import BeautifulSoup
import time

# time.sleep(10)
URL_CENTR = 'https://centr-krasnodar.ru/blog'
#URL_YA = 'https://yandex.ru/search/?lr=35&text='''
#https://www.yandex.ru/search/?text=abuse&lr=35
#from requests import Response

ROOT_URL_YA = 'https://yandex.ru/search/?'
#ROOT_URL_GOOGLE = 'https://google.com/search/?'
# URL = 'https://go.mail.ru/search?q=seat&fm=1'
HEADERS = {'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
#date_stamp = datetime.datetime.today().strftime("%Y-%m-%d-%H-%M--")

search_links = []
recursive_search_array = []

#Сначала ищем в Яндекс
serp_string = input('Что ищем? ')
serp_results = input('Сколько результатов найти? ')
rec_search = True
search_url = ROOT_URL_YA + 'text=' + serp_string + '&lr=' + serp_results

#filename = date_stamp + 'index.html'
# YA SERP


def main():
    #Закомментировал, т.к. парсю пока локальную страницу
    # with open(filename, 'r') as input_file:
    response = requests.get(search_url, headers=HEADERS)
    if response.ok:
        soup = BeautifulSoup(response, 'html.parser')
        li = soup.find_all('li', class_='serp-item')
        for el in li:
            link = el.find('a').get('href')
            name = el.find('a').get_text()
            result_link = [link, name]
            search_links.append(result_link)
        print(len(search_links))
    else:
        print('Error!')


# def main():
#     #Закомментировал, т.к. парсю пока локальную страницу
#     # with open(filename, 'r') as input_file:
#     with open('index.html', 'r') as input_file:
#         soup = BeautifulSoup(input_file, 'html.parser')
#         li = soup.find_all('li', class_='serp-item')
#         for el in li:
#             link = el.find('a').get('href')
#             name = el.find('a').get_text()
#             result_link = [link, name]
#             search_links.append(result_link)
#         print(len(search_links))
#recursive_search()

#Блок для локального парсинга страницы
# def main():
#     #Закомментировал, т.к. парсю пока локальную страницу
#     # with open(filename, 'r') as input_file:
#     with open('index.html', 'r') as input_file:
#         soup = BeautifulSoup(input_file, 'html.parser')
#         li = soup.find_all('li', class_='serp-item')
#         for el in li:
#             link = el.find('a').get('href')
#             name = el.find('a').get_text()
#             result_link = [link, name]
#             search_links.append(result_link)
#         print(len(search_links))
#     #recursive_search()


#Сначала ищем в Яндекс
# serp_string = input('Что ищем? ')
# serp_results = input('Сколько результатов найти? ')
# filename = date_stamp + 'index.html'

# def save_serp_local():
#     response = requests.get(URL_YA + 'text=' + serp_string + '&lr=' + serp_results, headers=HEADERS)
#     if response.ok:
#         with open(filename, 'w') as output_file:
#             output_file.write(response.text)
#         print('Page saved. ' + filename)
#     else:
#         print('Error!')
# save_serp_local()

# YA SERP


def recursive_search():
    #возьмем только первый линк и найдем на нём все хрефы анкоров
    look_for = search_links[4][0]
    print('Парсим сайт: ' + look_for)
    # print('Парсим сайт: ' + URL_CENTR)
    recursive_response = requests.get(look_for, headers=HEADERS)
    recursive_soup = BeautifulSoup(recursive_response.text, 'html.parser')
    rec_links = []
    for el in recursive_soup.findAll('a'):
        link = str(el.get('href'))
        name = str(el.get_text())
        # name = el.find('a').get_text()
        result_link = [link, name]
        rec_links.append(result_link)
        print(result_link)
    print(len(rec_links))
    # else:
    #     print('Error!')
    # print(len(rec_links))

    # soup = BeautifulSoup(r, 'html.parser')
    # ancors = soup.find('a').get('href')
    # print(len(ancors))

        # look =print(type(name)) requests.get(look_for, headers=HEADERS)
        # recursive_soup = BeautifulSoup(look, 'html.parser')
        # print(recursive_soup)

        # for elem in search_links:
        #     resp = requests.get(elem[], headers=HEADERS)
        #     recursive_soup = BeautifulSoup(resp, 'html.parser')
        #     print(recursive_soup)

        # for elem in search_links:
        #     resp = requests.get(elem[0], headers=HEADERS)
        #     recursive_soup = BeautifulSoup(resp, 'html.parser')
        #     recursive_search = recursive_soup.find_all('a').get('href')
        #     recursive_search_array.append(recursive_search)
        #     print(len(recursive_search_array))
        # for elem in search_links:
        #     recursive_link = search_links[0]
        #     resp = requests.get(recursive_link, headers=HEADERS)
        #     recursive_soup = BeautifulSoup(resp, 'html.parser')
        #     recursive_search = recursive_soup.find_all('a')
        #     recursive_search_array.append(recursive_search)
        # print(len(recursive_search_array))


if __name__ == '__main__':
    main()
    recursive_search()