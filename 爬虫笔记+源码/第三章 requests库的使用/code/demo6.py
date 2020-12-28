import requests

#目标url
url = 'http://www.baidu.com'
# 构造请求头
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"}
# 向url发送get请求
response = requests.get(url, headers=headers)
# 打印响应内容
print(response.content.decode())

# 打印对应请求头信息
print(response.request.headers)
