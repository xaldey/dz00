from bs4 import BeautifulSoup
import requests
from spider import HEADERS

URL = 'https://translate.academic.ru/abuse/en/ru/'

response = requests.get(URL, headers=HEADERS)
print(response.text)

soup = BeautifulSoup(response, 'html.parser')
if response.status_code:
    div = soup.find('div')
    print(div)
else:
    print('Error!')