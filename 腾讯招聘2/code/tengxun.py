import requests
import pandas as pd
import time
import pprint
import jsonpath


def get_info(data):
    recruit_post_name = jsonpath.jsonpath(data, '$..RecruitPostName')
    category_name = jsonpath.jsonpath(data, '$..CategoryName')
    country_name= jsonpath.jsonpath(data, '$..CountryName')
    location_name = jsonpath.jsonpath(data, '$.Data.Posts..LocationName')
    responsibility = jsonpath.jsonpath(data, '$..Responsibility')
    responsibility = [i.replace('\n', '').replace('\r', '') for i in responsibility]
    last_update_time = jsonpath.jsonpath(data, '$..LastUpdateTime')
    df = pd.DataFrame({
        'country_name': country_name,
        'location_name': location_name,
        'recruit_post_name':recruit_post_name,
        'category_name': category_name,
        'responsibility':responsibility,
        'last_update_time':last_update_time
    })
    return df


class TengXun(object):
    def __int__(self):
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
        }

    def get_url(self, page):
        url = f'https://careers.tencent.com/tencentcareer/api/post/Query?pageIndex={page}&pageSize=10'
        return url

    def get_json(self, url):
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
        }
        response = requests.get(url=url, headers=headers)
        return response.json()


if __name__ == '__main__':
    tengxun = TengXun()
    df = pd.DataFrame(columns=['country_name', 'location_name', 'category_name','recruit_post_name', 'responsibility', 'last_update_time'])

    for page in range(1, 330):
        print(f'正在获取第{page}页')
        url = tengxun.get_url(page)
        data = tengxun.get_json(url)
        time.sleep(0.03)

        df1 = get_info(data)
        df = pd.concat([df, df1])
        df = df.reset_index(drop=True)
    # pprint.pprint(data)

    df.to_csv('../data/腾讯招聘.csv', encoding='utf-8-sig')

