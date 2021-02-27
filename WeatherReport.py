import requests
from bs4 import BeautifulSoup as bs4
from selenium import webdriver
import re
from selenium.webdriver.chrome.options import Options
import chromedriver_binary
import time


# print('どこの天気を知りたい？')
#
# place = input('>> ')

def main():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('disable-infobars')
    options.add_argument('--no-sandbox')

    driver = webdriver.Chrome(options=options)
    driver_path = 'https://tenki.jp/forecast/3/16/4410/13103/1hour.html'
    driver.get(driver_path)

    print(driver.title)

    element = driver.find_element_by_id("keyword")
    element.send_keys('新宿区')

    btn = driver.find_element_by_id("btn")
    btn.click()
    time.sleep(3)

    elements = driver.find_elements_by_class_name('search-entry-data')

    for element in elements:
        print(element.text)

    driver.quit()

    # stats = driver.find_element_by_id("btn").text

    # urlName = 'https://tenki.jp/forecast/3/16/4410/13103/1hour.html'
    # url = requests.get(urlName)
    # soup = bs4(url.content, 'lxml')
    #
    # hours = soup.select_one('tr.hour')
    # hours = hours.select('span:not(.past)')
    #
    # weathers = soup.select_one('tr.weather')
    # weathers = weathers.select('p:not(.past)')
    #
    # temperatures = soup.select_one('tr.temperature')
    # temperatures = temperatures.select('span:not(.past)')

if __name__ == '__main__':
    main()
