import requests
from bs4 import BeautifulSoup as bs4
import re

urlName = "https://tenki.jp/forecast/3/16/4410/13103/1hour.html"
url = requests.get(urlName)
soup = bs4(url.content, 'lxml')

hours = soup.select_one('tr.hour')

for hour in hours:
    # if hour['class'] != 'past':
    print(hour['class'])

weathers = soup.find(class_='weather')
temperatures = soup.find(class_='temperature')

# print(hour)
# print(weather)
# print(temperature)
