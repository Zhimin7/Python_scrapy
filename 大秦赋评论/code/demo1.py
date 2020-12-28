import requests
from lxml import etree
import pandas as pd
import time

class Douban(object):
    def __init__(self):
        self.session = requests.session()
        self.session.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
        }
        self.login_url = 'https://accounts.douban.com/j/mobile/login/basic'

    def login(self):
        data = {
            'ck': '',
            'remember': 'true',
            'name': '18218138350',
            'password': '698350As?',
        }
        self.session.post(self.login_url, data=data)

    def get_content_url(self, i):
        url = f'https://movie.douban.com/subject/26413293/comments?start={i}&limit=20&status=P&sort=new_score'
        return url

    def get_info(self, url):
        response = self.session.get(url).content.decode('utf-8')
        html = etree.HTML(response)
        time = html.xpath('//div[@class="comment"]/h3/span/span[3]/@title')
        star = html.xpath('//div[@class="comment"]/h3/span/span[2]/@title')
        content = html.xpath('//p[@class=" comment-content"]/span/text()')
        content = [i.replace('\n', '') for i in content]
        df = pd.DataFrame(
            {'content_time': time,
             'star': star,
             'comment-content': content
    }
        )
        return df


if __name__ == '__main__':
    douban = Douban()
    douban.login()
    df = pd.DataFrame(columns=['content_time', 'star', 'comment-content'])
    for i in range(25):
        print(f'正在打印第{i+1}页')
        url = douban.get_content_url(i*20)
        df1 = douban.get_info(url)
        df = pd.concat([df, df1])
        time.sleep(3)
        df = df.reset_index(drop=True)
    df.to_csv('../data/conment-content_all.csv', encoding='utf-8-sig')
    print('获取成功')
