import requests


headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
}

url = 'https://careers.tencent.com/tencentcareer/api/data/GetMultiDictionary?timestamp=1611136655752&language=zh-cn&type=Nationality,WorkPlace,OuterType,BG,PostAttr'
response = requests.get(url, headers=headers)
json = response.text
with open('position.json', 'w', encoding='utf-8') as f:
    f.write(json)