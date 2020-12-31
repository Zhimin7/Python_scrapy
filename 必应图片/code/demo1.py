import requests
from lxml import etree
import time
from concurrent.futures import ThreadPoolExecutor

class BiYing(object):
    def get_page_url(self):
        page_url = []
        for i in range(1,148):
            url = f'https://bing.ioliu.cn/?p={i}'
            page_url.append(url)
        return page_url


    def get_img_url(self, urls):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
        }
        img_urls = []
        count = 1
        for url in urls:
            # time.sleep(3)
            text = requests.get(url, headers=headers).content.decode('utf-8')
            html = etree.HTML(text)
            img_url = html.xpath('//div[@class="item"]//img/@data-progressive')
            img_url = [i.replace('640x480', '1920x1080') for i in img_url]
            print(f'正在获取第{count}页图片链接')

            img_urls.extend(img_url)
            count += 1
        return img_urls


    def get_img_name(self, urls):
        img_names = []
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
        }
        for url in urls:
            time.sleep(3)
            text = requests.get(url, headers=headers).content.decode('utf-8')
            html = etree.HTML(text)
            img_name = html.xpath('//div[@class="item"]//h3/text()')
            img_names.extend(img_name)
        return img_names




    def save_img(self, img_urls):

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
        }
        count = 1

        for img_url in img_urls:
            content = requests.get(img_url, headers=headers).content
            print(f'正在下载第{count}张')
            with open(f'../image/{count}.jpg', 'wb') as f:
                f.write(content)
            count += 1











    def run(self):
        urls = self.get_page_url()
        img_urls = self.get_img_url(urls)
        # img_names = self.get_img_name(urls)
        self.save_img(img_urls)




if __name__ == '__main__':
    biying = BiYing()
    biying.run()