from bs4 import BeautifulSoup as bs
from selenium import webdriver


def get_html(url):
    driver = webdriver.Chrome()
    driver.get(url)
    web_html = driver.page_source
    driver.close()
    return web_html


def create_url(symbol):
    return f"https://www.otcmarkets.com/stock/{symbol}/security"


class Soup:
    def __init__(self, symbol):
        url = create_url(symbol)
        resp = get_html(url)
        self._soup = bs(resp, features="html.parser")
        self._symbol = symbol

    def locate_market_cap(self):
        try:
            res = self._soup.find(class_='_8AXJn4ourf sc-htpNat jtWIOA sc-bdVaJa gRrvFh')
            res = res.find(class_='sc-bdVaJa kYmYWE')
            return str(res.string)
        except AttributeError as e:
            print(f'Market Cap can not be found for symbol: {self._symbol}')
            return ' '
