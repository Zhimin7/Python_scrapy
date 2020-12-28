import requests
import re
import execjs
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# 关闭ssl验证错误提醒
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class FanYi:
    def __init__(self, keyword):
        self.keyword = keyword
        self.url = ['https://fanyi.baidu.com/?aldtype=16047',
                    'https://fanyi.baidu.com/v2transapi?']
        self.session = requests.session()
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
            'referer': 'https://fanyi.baidu.com/?aldtype=16047',
            'origin': 'https://fanyi.baidu.com',
        }

    def key_parameter(self):
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
        }
        response = self.session.get(self.url[0], headers=headers, verify=False).content.decode()
        # 获取页面中的token/gtk
        token = re.findall("token: '(.*?)',", response)[0]
        gtk = re.findall("window.gtk = '(.*?)';", response)[0]
        # 读取js
        with open('baidu.js', 'r', encoding='utf-8') as f:
            js = f.read()
        # 生成js对象
        exec_obj = execjs.compile(js)
        # 调用js中的e函数并传入参数生成sign
        sign = exec_obj.call("e", self.keyword, gtk)
        return token, sign

    def form_data(self, token, sign):
        data = {
            'from': 'zh',
            'to': 'en',
            'query': self.keyword,
            'transtype': 'realtime',
            'simple_means_flag': 3,
            'sign': sign,
            'token': token,
            'domain': 'common'
        }
        return data

    def run(self):
        # 调用两次key_parameter函数以保证token为最新的，否则请求不到数据
        self.key_parameter()
        token, sign = self.key_parameter()
        form_data = self.form_data(token, sign)
        data = self.session.post(self.url[1], headers=self.headers, data=form_data, verify=False).json()
        result = data['trans_result']['data'][0]['dst']
        print('翻译结果:', result)


if __name__ == '__main__':
    word = input('请输入原文: ')
    fy = FanYi(word)
    fy.run()
