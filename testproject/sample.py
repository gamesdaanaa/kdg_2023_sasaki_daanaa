import requests
import json

api_key = '42e7f97b2a2c4889a763ffedb7f8bde2'
api_url = 'https://newsapi.org/v2/top-headlines? country=us & category=business &apiKey=42e7f97b2a2c4889a763ffedb7f8bde2'

# APIエンドポイントにGETリクエストを送信
response = requests.get(f'{api_url}&apiKey={api_key}')
titles = []

# HTTPステータスが200 OKであることを確認
if response.status_code == 200:
    # JSONデータを取得して解析
    data = response.json()
    # レスポンスデータを表示
    for article in data["articles"]:
        titles.append(article["title"])

    print(titles)
else:
    # エラーメッセージを表示
    print(f'HTTP error! Status: {response.status_code}')
