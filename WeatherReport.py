import time
import urllib.request, urllib.parse
import json
import datetime
from bs4 import BeautifulSoup as bs4

# 場所から緯度経度を取得
def getLatitude(place):

    params = {
        'q': place
    }

    params = urllib.parse.urlencode(params)

    url = 'http://www.geocoding.jp/api/?' + params

    # スクレイピング用にURLを指定
    url = urllib.request.urlopen(url).read()
    soup = bs4(url, 'html.parser')

    if soup.find('error'):
        return '', ''

    lat = soup.find('lat').string
    lon = soup.find('lng').string

    # 緯度経度取得APIの規定で10秒待つ
    time.sleep(5)

    return lat, lon

# 経度緯度から天気予報を取得
def getWeatherReport(lat, lon):
    baseUrl =  'https://map.yahooapis.jp/weather/V1/place?coordinates='
    appId = 'dj00aiZpPWNxa0FvMWwyOWxIciZzPWNvbnN1bWVyc2VjcmV0Jng9NDg-'

    url = baseUrl + lon + ',' + lat + '&output=json&appid=' + appId

    tmp = urllib.request.urlopen(url).read()

    json_tree = json.loads(tmp)

    weatherList = json_tree['Feature'][0]['Property']['WeatherList']['Weather']

    for weather in weatherList:
        dt = datetime.datetime.strptime(weather['Date'], '%Y%m%d%H%M')
        dt = dt.strftime("%Y/%m/%d %H:%M")

        if weather['Rainfall'] == 0.0:
            print(dt + ': 傘は必要ありません')
        elif weather['Rainfall'] >= 0.5:
            print(dt + ': 長時間出かける場合は傘を持っていきましょう')
        elif weather['Rainfall'] >= 1.0:
            print(dt + ': 絶対に傘を持って出かけてください')

    return weatherList


def main():
    print('どこの天気を知りたい？')

    text = input('>> ')

    # 天気予報取得のために緯度、経度を取得
    lat, lon = getLatitude(text)

    # 緯度、経度を用いて天気予報を取得
    weatherReport = getWeatherReport(lat, lon)

if __name__ == '__main__':
    main()
