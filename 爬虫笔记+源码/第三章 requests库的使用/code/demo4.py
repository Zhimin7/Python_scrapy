import requests

#目标url
url = 'http://www.baidu.com'
# 向url发送get请求
response = requests.get(url)
response.encoding='utf-8'
print(response.url)
print(response.status_code)
print(response.request.headers)
print(response.headers)
print(response.request._cookies)
print(response.cookies)
