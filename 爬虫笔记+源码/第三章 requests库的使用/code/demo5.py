import requests

#目标url
url = 'http://www.baidu.com'
# 向url发送get请求
response = requests.get(url)
# 打印响应内容
print(response.content.decode())

# 打印对应请求头信息
print(response.request.headers)
