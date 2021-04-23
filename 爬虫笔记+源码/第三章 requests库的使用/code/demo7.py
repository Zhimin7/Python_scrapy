import requests

#目标url
url = 'https://www.baidu.com/s?wd=Python'
# 构造请求头
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"}
# 向url发送get请求
response = requests.get(url, headers=headers)
with open('baidu.html', 'wb') as f:
    f.write(response.content)
