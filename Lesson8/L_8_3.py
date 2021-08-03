# from bs4 import BeautifulSoup
# import datetime
# import random
# import re
# from urllib.request import urlopen
# from time import sleep
#
# random.seed(datetime.datetime.now())
#
#
# def getlinks(articleurl):
#     html = urlopen(f'https://en.wikipedia.org{articleurl}')
#     bs = BeautifulSoup(html, 'html.parser')
#     content = bs.find('div', {'id': 'bodyContent'}).find_all()
#     links = content.find_all('a', href=re.compile('^(/wiki/)((?!:).)*$'))
#     return links
#
#
# links = getlinks("/wiki/Ozone.ru")
# while len(links) > 0:
#     newArticle  = random.choice(links).attrs['href']
#     print(newArticle)
#     links = getlinks(newArticle)
#     sleep(1)
#
# print('End')

from bs4 import BeautifulSoup
import random
import datetime
import re
from urllib.request import urlopen
from time import sleep

random.seed(datetime.datetime.now())

def getLinks(articleUrl):
    html = urlopen(f'https://en.wikipedia.org{articleUrl}')
    bs = BeautifulSoup(html, 'html.parser')
    content = bs.find('div', {'id':'bodyContent'})
    links = content.find_all('a', href=re.compile('^(/wiki)((?!:).)*$'))
    return links


links = getLinks('/wiki/Ozon.ru')
while len(links) > 0:
    newArticle = random.choice(links).attrs['href']
    print(newArticle)
    links = getLinks(newArticle)
    sleep(1)
print('End')