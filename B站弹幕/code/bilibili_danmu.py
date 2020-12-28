'''
@author:啃书君
@date:2020/12/3
@url:https://www.bilibili.com/bangumi/play/ep336156
@目的：
爬取：说唱新世界弹幕
'''
import requests
import pandas as pd
import time
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor


def get_bilibili_url(start, end):
    url_list = []
    date_list = [i for i in pd.date_range(start, end).strftime('%Y-%m-%d')]
    # print(date_list)
    for date in date_list:
        url = f'https://api.bilibili.com/x/v2/dm/history?type=1&oid=228684032&date={date}'
        # print(url)
        url_list.append(url)
    return url_list


def get_bilibili_danmu(url_list):
    headers = {
        "cookie": "_uuid=26700CA6-B740-3A62-A99F-CCB789B7723781325infoc; buvid3=48A5C859-4608-4959-A95A-AFDC0DE51586155803infoc; sid=9e68bg6g; LIVE_BUVID=AUTO1915824750315949; rpdid=|(umR|muJ|R|0J'ul)kR~l|RR; im_notify_type_401204029=0; blackside_state=1; CURRENT_FNVAL=80; Hm_lvt_8a6e55dbd2870f0f5bc9194cddf32a02=1602247800; CURRENT_QUALITY=64; PVID=1; finger=158939783; _dfcaptcha=97158264222de275e12eda888b22002f; DedeUserID=401204029; DedeUserID__ckMd5=276536be2f632326; SESSDATA=270c5838%2C1622544557%2C74cf7*c1; bili_jct=a3afe3089d55ef86b658ee5340793b8f",
        "user-agent": "'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
    }
    response = requests.get(url_list, headers=headers)
    response.encoding = 'utf-8'
    print(response.status_code)
    soup = BeautifulSoup(response.text, 'lxml')
    datas = soup.find_all('d')
    file = open('bilibili_danmu.txt', 'a')
    # print(datas)
    # texts = []
    for data in datas:
        text = data.text
        print(text)
        file.write(text)
        file.write('\n')
    file.close()
        # texts.append(text)
    # with open('bilibili_danmu.txt', 'wa', encoding='utf8') as f:
    #     f.write(texts)

    # with open('bilibili_danmu.txt', 'w') as f
    # for url in url_list:
    #     response = requests.get(url, headers=headers)
    #     response.encoding = 'utf-8'
    #     # print(response.status_code)
    #     soup = BeautifulSoup(response.text, 'lxml')
    #     datas = soup.find_all('d')
    #     for data in datas:
    #         print(data.text)
        # return response.status_code


def main():
    start = '2020-12-01'
    end = '2020-12-03'
    url_list = get_bilibili_url(start, end)
    # print(type(url_list))
    # print(url_list)
    with ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(get_bilibili_danmu, url_list)
    # get_bilibili_danmu(url_list)
    print('获取成功')


if __name__ == '__main__':
    main()