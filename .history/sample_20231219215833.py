import requests

URL = 'http://webservice.recruit.co.jp/hotpepper/gourmet/v1/'

API_KEY = '5947c67fce02336b'


body = {
    'key':API_KEY,
    'keyword':'恵比寿駅',
    'format':'json',
    'count':15
}

response = requests.get(URL,body)

datum = response.json()
# JSONデータの中からお店のデータを取得
stores = datum['results']['shop']
# お店のデータの中から、店名を抜き出して表示させる
for store_name in stores:
    name = store_name['name']
    print(name)