import re
import requests
import pandas as pd
import time

class DangDang(object):
    def __init__(self):
        self.session = requests.session()
        self.session.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
        }

    def get_url(self, page):
        url = f'http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-24hours-0-0-1-{page}'
        return url

    def get_html(self, url):
        html = self.session.get(url).content.decode('gb2312', 'ignore')
        return html



    def get_info(self, html):
        pattern_name = re.compile('li.*?<div class="name">.*?title="(.*?)".*?</a>', re.S)
        pattern_author = re.compile('li.*?<div class="publisher_info">.*?<a .*?target="_blank">(.*?)</a>', re.S)
        pattern_time = re.compile('li.*?<div class="publisher_info">.*?<span>(.*?)</span>', re.S)
        pattern_price = re.compile('li.*?<div class="price">.*?<span class="price_n">(.*?)</span>', re.S)
        name = re.findall(pattern_name, html)
        author = re.findall(pattern_author, html)
        print('清洗前：',author)
        # author = [i for i in author if '出版社' not in i]
        if page == 3:
            author = [i for i in author if '出版社' not in i]
        if page == 14:
            author = [i for i in author if '机械工业出版社' not in i]
        print('清洗后：',author)
        print(len(author))
        time = re.findall(pattern_time, html)
        price = re.findall(pattern_price, html)
        price = [i.replace('&yen;', '￥') for i in price]
        df = pd.DataFrame({
            'book_name': name,
            'author': author,
            'edition_time': time,
            'price': price
        })
        print(list(df['author']))
        return df



if __name__ == '__main__':
    df = pd.DataFrame(columns=['book_name', 'author', 'edition_time', 'price'])
    page = 1
    dangdang = DangDang()
    for pages in range(1,26):

        print(f'正在获取第{pages}页')
        url = dangdang.get_url(pages)
        html = dangdang.get_html(url)


        df1 = dangdang.get_info(html)

        time.sleep(3)
        df = pd.concat([df, df1])
        df = df.reset_index(drop=True)
        page += 1

    df.to_csv('../data/TOP500.csv', encoding='utf-8-sig')
    print('获取完毕')

