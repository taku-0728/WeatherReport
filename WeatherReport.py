import requests
from bs4 import BeautifulSoup as bs4
from selenium import webdriver
import re
from selenium.webdriver.chrome.options import Options
import chromedriver_binary
import time


def main():
    print('どこの天気を知りたい？')

    place = input('>> ')

    options = Options()
    options.add_argument('--headless')
    options.add_argument('disable-infobars')
    options.add_argument('--no-sandbox')

    driver = webdriver.Chrome(options=options)
    driver_path = 'https://tenki.jp/'
    driver.get(driver_path)

    element = driver.find_element_by_id("keyword")
    element.send_keys(place)

    btn = driver.find_element_by_id("btn")
    btn.click()
    time.sleep(3)

    searchResults = driver.find_elements_by_class_name('search-entry-data')

    searchResults[0].click()
    time.sleep(3)

    onehour = driver.find_elements_by_class_name('forecast-select-1h')
    onehour[0].click()
    time.sleep(3)

    currentUrl = driver.current_url

    driver.quit()

    url = requests.get(currentUrl)
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

if __name__ == '__main__':
    main()
