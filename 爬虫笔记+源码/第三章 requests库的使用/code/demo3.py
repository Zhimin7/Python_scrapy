import requests

#目标url
url = 'http://www.baidu.com'
# 向url发送get请求
response = requests.get(url)
response.encoding='utf-8'
# 打印响应内容
print(response.text)
