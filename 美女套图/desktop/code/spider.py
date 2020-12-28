import requests
from lxml import etree
import os
import time
from concurrent.futures import ThreadPoolExecutor


if not os.path.exists('桌面壁纸'):
    os.mkdir('桌面壁纸')


def get_taotu_url():
    taotu_urls = [] # 保存URL
    for i in range(1, 6):
        url = f'http://www.win4000.com/wallpaper_0_0_0_{i}.html'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
        }
        # 发起请求
        response = requests.get(url, headers=headers)
        html = etree.HTML(response.text)
        taotu_url = html.xpath('//div[@class="tab_box"]/div/ul/li/a/@href')
        # 每一页的套图URL
        taotu_url = [item for item in taotu_url if len(item) == 51]
        taotu_urls.extend(taotu_url)
    return taotu_urls


def get_img(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
    }
    response = requests.get(url, headers=headers)
    html = etree.HTML(response.text)
    # 获取套图名称
    name = html.xpath('//div[@class="Bigimg"]/div/h1/text()')[0]
    # print(name)

    os.mkdir(f'./桌面壁纸/{name}')
    max_page = html.xpath('//div[@class="Bigimg"]/div/em/text()')[0]
    url1 = url.replace('.html', '_{}.html')
    # print(url1)
    for i in range(1, int(max_page) + 1):
        url2 = url1.format(i)
        # print(url2)
        response = requests.get(url2, headers=headers)
        dom = etree.HTML(response.text)
        src = dom.xpath('//div[@class="pic-meinv"]/a/img/@src')[0]
        # print(src)
        data = requests.get(src, headers=headers).content
        file_name = name + f'第{i}张.jpg'
        with open('./桌面壁纸/{}/{}'.format(name, file_name), 'wb') as f:
            f.write(data)
            print(f'下载成功{file_name}')


def main():
    taotu_urls = get_taotu_url()
    # print(taotu_urls)
    with ThreadPoolExecutor(max_workers=6) as executer:
        executer.map(get_img, taotu_urls)
    print('-----下载完成-----')

if __name__ == '__main__':
    main()




