import requests
from config import API_KEY

URL = 'http://webservice.recruit.co.jp/hotpepper/gourmet/v1/'

def search_hotpepper_gourmet(api_key, keyword):
    base_url = "http://webservice.recruit.co.jp/hotpepper/gourmet/v1/"
    
    params = {
        "key": api_key,
        "name_any": keyword,
        "count": 10,
        "format": "json",
    }

    try:
        response = requests.get(f"{base_url}", params=params)
        response.raise_for_status()

        data = response.json()
        if data.get("results"):
            shops = data["results"]["shop"]
            for shop in shops:
                print(f"店舗名: {shop['name']}")
                print(f"住所: {shop['address']}")
                print(f"ジャンル: {shop['genre']['name']}")
                print("----------")
        else:
            print("検索結果がありません。")

    except Exception as e:
        print(f"エラーが発生しました: {e}")

if __name__ == "__main__":
    keyword = "ラーメン"
    search_hotpepper_gourmet(API_KEY, keyword)
