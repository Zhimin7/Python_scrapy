import requests


url = 'https://www.baidu.com'
html = requests.get(url).content
with open('baidu.html', 'wb') as f:
    f.write(html)