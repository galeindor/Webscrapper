from time import sleep

from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from consts import class_names,endings, EMPTY_CELL, SLEEP_TIME


def create_url(symbol, key):
    return f"https://www.otcmarkets.com/stock/{symbol}/{endings[key]}"


def driver_test(symbols, keyword):
    driver = webdriver.Chrome()
    web_pages = []
    for symbol in symbols:
        url = create_url(symbol, keyword)
        driver.get(url)
        sleep(2)
        web_pages.append(driver.page_source)
    driver.close()
    for page in web_pages:
        soup = bs(page, features="html.parser")
        try:
            res1 = soup.find(class_=class_names[keyword]['outer'])
        except AttributeError as e:
            print(f'couldnt find outer for symbol: {symbol} \n{e}')
            continue
        try:
            res2 = res1.find(class_=class_names[keyword]['inner'])
        except AttributeError as e:
            print(f'couldnt find inner for symbol: {symbol} \n{e}')
            continue
        print(f'res2:{res2.string}')


class Soup:

    def __init__(self, symbol, keyword):
        self._symbol = None
        self._soup = None
        self._key = keyword
        self._driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        self.reset(symbol)

    def get_html(self, url):
        self._driver.get(url)
        sleep(SLEEP_TIME)
        web_html = self._driver.page_source
        return web_html

    def safe_get_html(self, url):
        self._driver = webdriver.Chrome()
        self._driver(url)
        web_html = self._driver.page_source
        self._driver.close()
        return web_html

    def locate_keyword(self, symbol=None, key=None):
        if symbol is None:
            symbol = self._symbol
        if key is None:
            key = self._key
        try:
            out_index = class_names[key]['outer_index']
            inner_index = class_names[key]['inner_index']
            outer = self._soup.find_all(class_=class_names[key]['outer'])[out_index]
            res = outer.find_all(class_=class_names[key]['inner'])[inner_index]
            return str(res.string)
        except AttributeError as e:
            print(f'{key} can not be found for symbol: {symbol} \n{e}')
            return EMPTY_CELL

    def reset(self, symbol=None):
        url = create_url(symbol, self._key)
        resp = self.get_html(url)
        self._soup = bs(resp, features="html.parser")
        self._symbol = symbol

    def close_driver(self):
        self._driver.close()
