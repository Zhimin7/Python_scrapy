import requests
from lxml import etree
import os
import time
import random
from concurrent.futures import ThreadPoolExecutor



if not os.path.exists('手机壁纸'):
    os.mkdir('手机壁纸')


def get_taotu_urls():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
    }
    taotu_urls = []
    for i in range(1, 6):
        url = f'http://www.win4000.com/mobile_0_0_0_{i}.html'
        response = requests.get(url, headers=headers)
        html = etree.HTML(response.text)
        taotu_url = html.xpath('//div[@class="tab_box"]/div/ul[@class="clearfix"]/li/a/@href')
        taotu_url = [item for item in taotu_url if len(item) == 48]
        taotu_urls.extend(taotu_url)
    return taotu_urls


def get_img(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    html = etree.HTML(response.text)
    name = html.xpath('//div[@class="Bigimg"]/div/h1/text()')[0]
    if not os.path.exists(f'./手机壁纸/{name}'):
        os.mkdir(f'./手机壁纸/{name}')
    max_page = html.xpath('//div[@class="Bigimg"]/div/em/text()')[0]
    max_page = int(max_page)
    url1 = url.replace('.html', '_{}.html')

    for i in range(1, max_page+1):
        url2 = url1.format(i)
        time.sleep(random.randint(1, 3))
        response = requests.get(url2, headers=headers)
        html = etree.HTML(response.text)
        src = html.xpath('//div[@class="main-wrap"]/div/a/img/@src')[0]
        data = requests.get(src, headers=headers).content
        file_name = name + f'第{i}张.jpg'
        with open(f'./手机壁纸/{name}/{file_name}', 'wb') as f:
            f.write(data)
            print(f'成功下载图片：{file_name}')



def main():
    taotu_urls = get_taotu_urls()
    print(taotu_urls)
    with ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(get_img, taotu_urls)
    print('=========下载完成==========')


if __name__ == '__main__':
    main()