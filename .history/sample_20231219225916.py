import requests
from config import API_KEY

URL = 'http://webservice.recruit.co.jp/hotpepper/gourmet/v1/'

def search_hotpepper_gourmet(keyword, area):
    base_url = "http://webservice.recruit.co.jp/hotpepper/gourmet/v1/"
    
    params = {
        "key": API_KEY,
        #"name_any": keyword,
        "large_area": area,
        "genre": keyword,
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


# 検索地名をエリアコードに変更
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
        if data.get("results"):
            large_area = data["results"]["large_area"][0]
            print(f"area_code: {large_area['code']}")
            print("----------")
            return large_area['code']
        else:
            return "Z011"

    except Exception as e:
        print(f"エラーが発生しました: {e}")

def genre_code(genre):
    base_url = "http://webservice.recruit.co.jp/hotpepper/genre/v1/"
    params = {
        "key": API_KEY,
        "keyword": genre,
        "format": "json",
    }
    try:
        response = requests.get(f"{base_url}", params=params)
        response.raise_for_status()

        data = response.json()
        if data.get("results"):
            genre = data["results"]["genre"][0]
            print(f"genre_code: {genre['code']}")
            print("----------")
            return genre['code']
        else:
            return ""

    except Exception as e:
        print(f"エラーが発生しました: {e}")

if __name__ == "__main__":
    keyword = "ラーメン"
    area = "東京"
    area = area_code(area)
    genre = genre_code(keyword)
    search_hotpepper_gourmet(genre, area)
