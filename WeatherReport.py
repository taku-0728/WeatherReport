import requests
import time
import urllib
import json
import datetime
from bs4 import BeautifulSoup as bs4
from janome.tokenizer import Tokenizer


def setPlace(text):
    tokenizer = Tokenizer()
    place = ''

    # 引数で与えられたテキストを形態素解析し、地域を指定
    for token in tokenizer.tokenize(text):
        p = token.part_of_speech.split(',')
        if '地域' in p:
            place += token.surface

    return place

# 場所から緯度経度を取得
def getLatitude(place):

    url = 'http://www.geocoding.jp/api/?q=' + place

    # スクレイピング用にURLを指定
    url = requests.get(url)
    soup = bs4(url.content, 'lxml')

    if soup.find('error'):
        return '', ''

    lat = soup.find('lat').string
    lon = soup.find('lng').string

    # 緯度経度取得APIの規定で10秒待つ
    time.sleep(5)

    return lat, lon

# 経度緯度から天気予報を取得
def getWeatherReport(lat, lon):
    APP_ID = '********************************'
    BASE_URL = 'https://map.yahooapis.jp/weather/V1/place?coordinates='

    url = BASE_URL + lon + ',' + lat + '&output=json&appid=' + APP_ID

    tmp = urllib.request.urlopen(url).read()

    json_tree = json.loads(tmp)

    weatherList = json_tree['Feature'][0]['Property']['WeatherList']['Weather']

    for weather in weatherList:
        for key, value in weather.items():
            if key == 'Date':
                dt = datetime.datetime.strptime(value, '%Y%m%d%H%M')
                print(dt.strftime("%Y/%m/%d %H:%M"))


    return weatherList


def main():
    print('どこの天気を知りたい？')

    text = input('>> ')

    # 入力されたテキストから場所を取得
    place = setPlace(text)

    # 天気予報取得のために緯度、経度を取得
    lat, lon = getLatitude(place)

    # 緯度、経度を用いて天気予報を取得
    weatherReport = getWeatherReport(lat, lon)

if __name__ == '__main__':
    main()
