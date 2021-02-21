import requests
from bs4 import BeautifulSoup as bs4
import re

urlName = "https://tenki.jp/forecast/3/16/4410/13103/1hour.html"
url = requests.get(urlName)
soup = bs4(url.content, 'lxml')

hour = soup.find(class_='hour')
weather = soup.find(class_='weather')
temperature = soup.find(class_='temperature')

print(hour)
print(weather)
print(temperature)
