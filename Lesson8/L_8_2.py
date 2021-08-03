import requests
from bs4 import BeautifulSoup


payload = {'text': 'ozon', 'lr': 5}
req = requests.get('https://yandex.ru/search/', params= payload)
result = req.text
soup = BeautifulSoup(result, 'html.parser')
print(soup.prettify())

file = open('result.text', 'a')
for link in soup.findAll('a'):
    file.write(link.get('href') + '\n')
