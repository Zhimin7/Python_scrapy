from requests import utils
import requests

url = 'http://www.baidu.com'
response = requests.get(url)
print(type(response.cookies))
print(response.cookies)
# 将cookieJar转换为dict
dict_cookies = requests.utils.dict_from_cookiejar(response.cookies)
print(dict_cookies)
# 将dict转换为cookieJar
jar_cookies = requests.utils.cookiejar_from_dict(dict_cookies)
print(jar_cookies)