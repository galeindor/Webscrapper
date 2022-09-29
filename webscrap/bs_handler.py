from bs4 import BeautifulSoup as bs
from selenium import webdriver
from consts import inner_class_name, outer_class_name


def create_url(symbol):
    return f"https://www.otcmarkets.com/stock/{symbol}/security"


class Soup:

    def __init__(self, symbol):
        self._driver = webdriver.Chrome()
        url = create_url(symbol)
        resp = self.get_html(url)
        self._soup = bs(resp, features="html.parser")
        self._symbol = symbol

    def get_html(self, url):
        self._driver.get(url)
        web_html = self._driver.page_source
        self._driver.close()
        return web_html

    def locate_market_cap(self, symbol=None):
        if symbol is None:
            symbol = self._symbol
        try:
            res = self._soup.find(class_=outer_class_name)
            res = res.find(class_=inner_class_name)
            return str(res.string)
        except AttributeError as e:
            print(f'Market Cap can not be found for symbol: {symbol} \n{e}')
            return None

    def close_driver(self):
        self._driver.close()
