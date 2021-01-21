'''
项目名称：获取猫眼电影TOP100排行榜
作者：啃书君
时间：2021/1/17
'''


import requests
from pyquery import PyQuery as pq
import time

class MaoYan(object):
    def __init__(self):
        self.session = requests.session()
        self.session.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
        }

    # 构造URL地址
    def get_url(self, page):
        url = f'https://maoyan.com/board/4?offset={page}'
        return url

    # 获取每一页的HTML代码
    def get_html(self, url):
        response = self.session.get(url)
        html = response.content.decode('utf-8')
        return html

    # 获取信息
    def get_info(self, html):

        doc = pq(html)
        movie_name = doc('.board-item-main .board-item-content .movie-item-info p a').text().split()
        p = doc('.board-item-main .board-item-content .movie-item-info')
        star = p.children('.star').text().split()
        time = p.children('.releasetime').text().split()
        score1 = doc('.board-item-main .movie-item-number.score-num .integer').text().split()
        score2 = doc('.board-item-main .movie-item-number.score-num .fraction').text().split()
        score = [score1[i]+score2[i] for i in range(0, len(score1))]
        info = zip(movie_name, star, score, time)
        info = list(info)
        return info



if __name__ == '__main__':
    maoyan = MaoYan()
    for page in range(10):
        time.sleep(3)
        url = maoyan.get_url(page*10)
        html = maoyan.get_html(url)
        info = maoyan.get_info(html)
        print(info)
