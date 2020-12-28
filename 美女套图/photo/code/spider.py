import requests
from lxml import etree
import time
import random
from concurrent.futures import ThreadPoolExecutor
import os


if not os.path.exists('钟丽丽'):
    os.mkdir('钟丽丽')


def get_taotu_url():
    taotu_urls = []
    for i in range(1, 6):
        url = f'http://www.win4000.com/mt/zhonglili_{i}.html'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        html = etree.HTML(response.text)
        taotu_url = html.xpath('//div[@class="tab_box"]/div/ul/li/a/@href')
        taotu_url = [item for item in taotu_url if len(item) == 39]
        taotu_urls.extend(taotu_url)
    return taotu_urls


def get_img(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
    }
    response = requests.get(url, headers=headers)
    html = etree.HTML(response.text)
    name = html.xpath('//div[@class="ptitle"]/h1/text()')[0]
    os.mkdir(f'./钟丽丽/{name}')
    max_page = html.xpath('//div[@class="ptitle"]/em/text()')[0]
    max_page = int(max_page)
    url1 = url.replace('.html', '_{}.html')
    for i in range(1, max_page+1):
        url2 = url1.format(i)
        # print(url2)
        time.sleep(random.randint(1, 3))
        response = requests.get(url2, headers)
        html = etree.HTML(response.text)
        src = html.xpath('//div[@class="main-wrap"]/div/a/img/@data-original')[0]
        print(src)
        data = requests.get(src, headers=headers).content
        file_name = name+f'第{i}张.jpg'
        with open(f'./钟丽丽/{name}/{file_name}', 'wb') as f:
            f.write(data)

            print(f'成功下载图片:{file_name}')

def main():
    taotu_urls = get_taotu_url()
    print(taotu_urls)
    with ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(get_img, taotu_urls)
    print('========下载完成======')


if __name__ == '__main__':
    main()