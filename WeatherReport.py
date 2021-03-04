import chromedriver_binary
import requests
import time
from bs4 import BeautifulSoup as bs4
from janome.tokenizer import Tokenizer
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def main():
    print('どこの天気を知りたい？')

    place = input('>> ')

    tokenizer = Tokenizer()

    for token in tokenizer.tokenize(place):
        print(token)

    # options = Options()
    # # ヘッドレスモードを有効にする(無効にすると画面が表示される)
    # options.add_argument('--headless')
    #
    # # WebDriver(ブラウザ)の起動
    # driver = webdriver.Chrome(options=options)
    # driver_path = 'https://tenki.jp/'
    # driver.get(driver_path)
    #
    # # コンソールから入力された場所をテキストボックスに入力
    # element = driver.find_element_by_id("keyword")
    # element.send_keys(place)
    #
    # # 検索ボタン押下
    # btn = driver.find_element_by_id("btn")
    # btn.click()
    #
    # # 画面描画、負荷軽減用に3秒待つ
    # time.sleep(3)
    #
    # # 検索結果の一覧を取得
    # searchResults = driver.find_elements_by_class_name('search-entry-data')
    #
    # # 1番目の検索結果のリンクをクリック
    # searchResults[0].click()
    #
    # # 画面描画、負荷軽減用に3秒待つ
    # time.sleep(3)
    #
    # # 1時間ごとの天気を表示するためのリンクを選択し、クリック
    # onehour = driver.find_elements_by_class_name('forecast-select-1h')
    # onehour[0].click()
    #
    # # 画面描画、負荷軽減用に3秒待つ
    # time.sleep(3)
    #
    # # スクレイピング用に現在のURLを取得
    # currentUrl = driver.current_url
    #
    # # ブラウザの自動操作終了
    # driver.quit()
    #
    # # スクレイピング用にURLを指定
    # url = requests.get(currentUrl)
    # soup = bs4(url.content, 'lxml')
    #
    # # 現在時刻以降の時間を取得
    # hours = soup.select_one('tr.hour')
    # hours = hours.select('span:not(.past)')
    #
    # # 現在時刻以降の天気を取得
    # weathers = soup.select_one('tr.weather')
    # weathers = weathers.select('p:not(.past)')
    #
    # # 現在時刻以降の気温を取得
    # temperatures = soup.select_one('tr.temperature')
    # temperatures = temperatures.select('span:not(.past)')
    #
    # for hour in hours:
    #     print(hour.get_text())
    #
    # for weather in weathers:
    #     print(weather.get_text())
    #
    # for temperature in temperatures:
    #     print(temperature.get_text())

if __name__ == '__main__':
    main()
