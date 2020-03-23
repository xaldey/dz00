from bs4 import BeautifulSoup
import requests
from spider import HEADERS

# https://www.youtube.com/watch?v=zKuBDil5dlw&t=1582s



URL = 'https://translate.academic.ru/abuse/en/ru/'

response = requests.get(URL, headers=HEADERS)
print(response.text)

soup = BeautifulSoup(response, 'html.parser')
if response.status_code:
    div = soup.find('div')
    print(div)
else:
    print('Error!')


