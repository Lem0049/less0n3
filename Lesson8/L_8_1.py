import requests

# import urllib.request as request

payload = {'text': 'ozon', 'lr': 5}
req = requests.get('https://yandex.ru/search/', params= payload)
# print(req)
file = open('search.html', 'wb')
file.write(req.content)
file.close()
print(req.text)
print(req)
# print(type(req))
# print(dir(req))