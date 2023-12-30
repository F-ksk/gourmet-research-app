import requests
from config import API_KEY

URL = 'http://webservice.recruit.co.jp/hotpepper/gourmet/v1/'

def search_hotpepper_gourmet(keyword, area):
    base_url = "http://webservice.recruit.co.jp/hotpepper/gourmet/v1/"
    
    params = {
        "key": API_KEY,
        "name_any": keyword,
        "area": area,
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

def area_code(area):
    base_url = "http://webservice.recruit.co.jp/hotpepper/large_area/v1/"
    params = {
        "key": API_KEY,
        "keyword": area,
        "format": "json",
    }
    try:
        response = requests.get(f"{base_url}", params=params)
        response.raise_for_status()

        data = response.json()
        print(data)

    except Exception as e:
        print(f"エラーが発生しました: {e}")

if __name__ == "__main__":
    keyword = "ラーメン"
    area  = "東京エリア"
    area_code(area)
    search_hotpepper_gourmet(keyword, area)
