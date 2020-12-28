import requests
from lxml import etree
import os
import time
from random import randint
from concurrent.futures import ThreadPoolExecutor


if not os.path.exists('女神套图'):
    os.mkdir('女神套图')

def get_taotu_url():
    taotu_urls = []
    for i in range(1, 6):
        url = f'http://www.win4000.com/mt/dilireba_{i}.html'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
        }
        # 发起请求  获取响应
        response = requests.get(url, headers=headers)
        html = etree.HTML(response.text)
        taotu_url = html.xpath('//div[@class="tab_box"]/div/ul/li/a/@href')
        taotu_url = [item for item in taotu_url if len(item) == 39]
        # print(taotu_url_lists, len(taotu_url_lists), sep='\n')
        taotu_urls.extend(taotu_url)
        return taotu_urls


def get_image(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
        'Referer': 'http://www.win4000.com/mt/yangmi_2.html'
    }
    response = requests.get(url, headers=headers)
    html = etree.HTML(response.text)
    # 获取套图名称
    name = html.xpath('//div[@class="ptitle"]/h1/text()')[0]
    print(name)
    # 最大页数
    max_page = html.xpath('//div[@class="ptitle"]/em/text()')[0]
    # print(max_page)
    os.mkdir(r'./女神套图/{}'.format(name))
    # print(url)
    url1 = url.replace('.html', '_{}.html')
    # print(url1)
    for i in range(1, int(max_page) + 1):
        url2 = url1.format(i)
        time.sleep(randint(1, 3))
        response = requests.get(url2, headers=headers)
        dom = etree.HTML(response.text)
        src = dom.xpath('//div[@class="main-wrap"]/div/a/img/@data-original')[0]
        print(src)
        file_name = name + f'第{i}张.jpg'
        img = requests.get(src, headers=headers).content
        with open(r'./女神套图/{}/{}'.format(name, file_name), 'wb') as f:
            f.write(img)
            print(f'成功下载图片：{file_name}')


def main():
    taotu_urls = get_taotu_url()
    # print(taotu_urls)

    with ThreadPoolExecutor(max_workers=6) as exector:
        exector.map(get_image, taotu_urls)
    print('======图片下载完成=======')


if __name__ == '__main__':
    # taotu_url_lists = get_taotu_url()
    main()