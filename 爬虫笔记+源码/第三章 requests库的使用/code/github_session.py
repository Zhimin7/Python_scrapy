import requests
from lxml import etree


class GitHub(object):
    def __init__(self):
        self.session = requests.session()
        self.session.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
        }
        self.login_url = 'https://github.com/login'

    def login(self):
        response = self.session.get(self.login_url)
        html = etree.HTML(response.content.decode())
        return html

    def get_token(self):
        # url = 'https://github.com/login'
        # response = self.session.get(self.login_url)
        # html = etree.HTML(response.content.decode())
        authenticity_token = self.login().xpath('//form/input[1]/@value')[0]
        # print(authenticity_token)
        return authenticity_token

    def get_timestamp_secret(self):
        timestamp_secret = self.login().xpath('//div[@class="auth-form-body mt-3"]/input[11]/@value')[0]
        # print(timestamp_secret)
        return timestamp_secret

    def get_timestamp(self):
        timestamp = self.login().xpath('//div[@class="auth-form-body mt-3"]/input[10]/@value')[0]
        # print(timestamp)
        return timestamp


    def get_profile(self):
        url_session = 'https://github.com/session'
        url_profile = 'https://github.com/Zhimin7'
        data = {
            'commit': 'Sign in',
            'authenticity_token': self.get_token(),
            'ga_id':'',
            'login': '你的邮箱',
            'password': '你的密码',
            'webauthn - support': 'supported',
            'webauthn - iuvpaa - support': 'supported',
            'return_to':'',
            'allow_signup':'',
            'client_id':''
            'integration:',
            'required_field_86b0':'',
            'timestamp': self.get_timestamp(),
            'timestamp_secret': self.get_timestamp_secret()
        }
        # print(data)
        self.session.post(url_session, data=data)
        # self.session.get()
        html = self.session.get(url_profile).content
        with open('github.html', 'wb') as f:
            f.write(html)
        print(data)



if __name__ == "__main__":
    github = GitHub()
    github.get_token()
    github.get_timestamp()
    github.get_timestamp_secret()
    github.get_profile()