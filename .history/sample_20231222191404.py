import requests
from config import API_KEY


def search_hotpepper_area(genre, area):
    base_url = "http://webservice.recruit.co.jp/hotpepper/gourmet/v1/"
    
    params = {
        "key": API_KEY,
        #"name_any": keyword,
        "small_area": area,
        "genre": genre,
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

#---------------------------------
# 検索地名をエリアコードに変更
#---------------------------------
def area_code(area):
    base_url = "http://webservice.recruit.co.jp/hotpepper/small_area/v1/"
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
            area = data["results"]["small_area"][0]
            print(f"area_code: {area['code']}")
            print("----------")
            return area['code']
        else:
            return "Z011"

    except Exception as e:
        print(f"エラーが発生しました: {e}")

#-------------------------------------
# 検索ジャンルをジャンルコードに変更
#-------------------------------------
def genre_code(genre):
    #居酒屋,ダイニングバー・バル,創作料理,和食,洋食,
    #イタリアン・フレンチ,中華,アジア・エスニック料理,各国料理
    #カラオケ・パーティ,バー・カクテル,ラーメン,お好み焼き・もんじゃ,
    #カフェ・スイーツ,その他グルメ
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
    genre = "ラーメン"
    area = "東京"
    area = area_code(area)
    genre = genre_code(genre)
    search_hotpepper_gourmet(genre, area)
