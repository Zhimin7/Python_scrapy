import requests


headers = {

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
}

url = 'https://github.com/Zhimin7'

response = requests.get(url, headers=headers)
with open('github_without_cookie.html', 'wb') as f:
    f.write(response.content)