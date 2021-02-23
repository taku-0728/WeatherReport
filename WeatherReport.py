import requests
from bs4 import BeautifulSoup as bs4
import re

urlName = "https://tenki.jp/forecast/3/16/4410/13103/1hour.html"
url = requests.get(urlName)
soup = bs4(url.content, 'lxml')

hours = soup.select_one('tr.hour')
hours = hours.select('span:not(.past)')

weathers = soup.select_one('tr.weather')
weathers = weathers.select('p:not(.past)')

temperatures = soup.select_one('tr.temperature')
temperatures = temperatures.select('span:not(.past)')

for hour in hours:
    print(hour.get_text())

for weather in weathers:
    print(weather.get_text())

for temperature in temperatures:
    print(temperature.get_text())
