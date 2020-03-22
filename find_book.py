import requests
from bs4 import BeautifulSoup
import re


class FindBook:
    def __init__(self):
        super().__init__()
        self.r = re
        pass

    def get(self, url, method):
        try:
            res = requests.get(url)
            res.encoding = res.apparent_encoding
        except Exception:
            return '网络连接失败'
        soup = BeautifulSoup(res.text, 'html.parser')
        ans = {1: self.method1,
               2: self.method2}[method](soup)
        return ans


    def method1(self, soup):
        try:
            text = soup.find('div', class_='content').text
            text = self.clean(text)
            return text
        except Exception:
            return False

    def method2(self, soup):
        try:
            text = str(soup.find('div', id='content'))
            text = self.clean(text)
            return text
        except Exception:
            return False

    def clean(self, text):
        text = self.r.sub(r'[a-zA-Z0-9]+?\([a-zA-Z0-9]*?\);','' , text)
        return text


if __name__ == '__main__':
    fb = FindBook()
    # book = fb.get('https://www.85xs.cc/book/douluodalu1/1.html', 1)
    book = fb.get('http://www.tangsanshu.com/douluodalu/2253.html', 2)
    # book = fb.get('https://www.xsbiquge.com/2_2278/1036529.html', 2)
    if book:
        print(book)
    else:
        print('无法解析')