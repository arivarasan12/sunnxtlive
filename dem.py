import requests

headers = {
    'authority': 'www.sunnxt.com',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
    'accept': '*/*',
    'origin': 'https://www.sunnxt.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.sunnxt.com/tamil-music/detail/134156/musicvideo/0/arabic-kuthu---beast?carouselAction=watchNowPortal',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': '_ga=GA1.2.263978556.1634833038; WZRK_G=fd68a56c26914dd691fe1acf97f3a095; laravel_session=FuPPo1rZKGHpWCHwqRljX34KrzXXf1yNqfkSqvKw; _gid=GA1.2.1877874459.1644981870; _gat=1; RT="z=1&dm=sunnxt.com&si=514f01dd-bacf-46b7-b3af-76c9f7e1efe5&ss=kzozqg2j&sl=k&tt=532&bcn=%2F%2Fbeacon.s.llnwi.net%2Fstarling%2Fbeacon.txt"; WZRK_S_WW6-54K-855Z=%7B%22p%22%3A5%2C%22s%22%3A1644981869%2C%22t%22%3A1644982413%7D; XSRF-TOKEN=eyJpdiI6InZBa0dBTWVJOEFiY20yaGxmUHRpREE9PSIsInZhbHVlIjoiYzI1TXlCV0hoRVhVblJcL2dWXC9NZnQ3c3IwdnF5QzRacjBrbUZ3MEh0bEx5QXpvY1RkcnJFdjJVaDVOaEhGcCtteVZjRUJseTQ3b1kxTGRYSzA2TmtVUT09IiwibWFjIjoiOTJiZDc5YWQwMzg2NGQwZTJkM2ZlNmU5MjdiY2NlZGNlOTgxODgwNDU5NTc5MmU0MjMwZjNlMmYwMGUyZjExZCJ9',
}

params = (
    ('content_id', '134156'),
)

data = '\b\x04'

response = requests.post('https://www.sunnxt.com/content/license/', headers=headers, params=params, data=data)

# Note: original query string below. It seems impossible to parse and
# reproduce query strings 100% accurately so the one below is given
# in case the reproduced version is not "correct".
#response = requests.post('https://www.sunnxt.com/content/license/?content_id=134156', headers=headers, data=data)
print(response.text)