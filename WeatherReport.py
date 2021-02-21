import requests
from bs4 import BeautifulSoup as bs4
import re

urlName = "https://tenki.jp/forecast/3/14/4310/11203/1hour.html"
url = requests.get(urlName)
soup = bs4(url.content, 'lxml')

weathers = soup.find_all(class_='weather')

print(weathers)
