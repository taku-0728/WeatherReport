import requests
import time
# import urllib
import json
import datetime
import os
from bs4 import BeautifulSoup as bs4
# from janome.tokenizer import Tokenizer
import urllib.request, urllib.parse

def lambda_handler(request, context):
    for event in json.loads(request['body'])['events']:

        place = event['message']['text']

        # tokenizer = Tokenizer()
        # place = ''

        # # 引数で与えられたテキストを形態素解析し、地域を指定
        # for token in tokenizer.tokenize(text):
        #     p = token.part_of_speech.split(',')
        #     if '地域' in p:
        #         place += token.surface

        placeUrl = 'http://www.geocoding.jp/api/?q=' + place

        # スクレイピング用にURLを指定
        url = requests.get(placeUrl)
        soup = bs4(url.content, 'html.parser')

        if soup.find('error'):
            return '', ''

        lat = soup.find('lat').string
        lon = soup.find('lng').string

        # 緯度経度取得APIの規定で10秒待つ
        time.sleep(5)

        baseUrl =  os.environ['BASE_URL']
        appId = os.environ['APP_ID']

        url = baseUrl + lon + ',' + lat + '&output=json&appid=' + appId

        tmp = urllib.request.urlopen(url).read()

        json_tree = json.loads(tmp)

        weatherList = json_tree['Feature'][0]['Property']['WeatherList']['Weather']

        for weather in weatherList:
            dt = datetime.datetime.strptime(weather['Date'], '%Y%m%d%H%M')
            dt = dt.strftime("%Y/%m/%d %H:%M")

            if weather['Rainfall'] == 0.0:
                message = dt + ': 傘は必要ありません'
            elif weather['Rainfall'] > 0.0 and weather['Rainfall'] < 1.0:
                message = dt + ': 長時間出かける場合は傘を持っていきましょう'
            elif weather['Rainfall'] >= 1.0:
                message = dt + ': 絶対に傘を持って出かけてください'

        url = 'https://api.line.me/v2/bot/message/reply'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + os.environ['ChannelAccessToken']
        }
        body = {
            'replyToken': event['replyToken'],
            'messages': [
                {
                    "type": "text",
                    "text": message,
                }
            ]
        }

        req = urllib.request.Request(url, data=json.dumps(body).encode('utf-8'), method='POST', headers=headers)
        with urllib.request.urlopen(req) as res:
            res.read().decode("utf-8")

    return {'statusCode': 200, 'body': '{}'}
