import requests
from config import API_KEY

def makeList(params):
    base_url = "http://webservice.recruit.co.jp/hotpepper/gourmet/v1/"
    result_list = []

    try:
        response = requests.get(f"{base_url}", params=params)
        response.raise_for_status()

        data = response.json()
        if data.get("results"):
            shops = data["results"]["shop"]
            for shop in shops:
                shop_info = {
                    "shop_id": shop["id"],
                    "name": shop["name"],
                    "location": shop["address"],
                    "genre": shop["genre"]["name"],
                    "access" : shop["access"],
                    "photo": shop["photo"]["pc"]["m"]
                }
                result_list.append(shop_info) 
        else:
            print("検索結果がありません。")

    except Exception as e:
        print(f"エラーが発生しました: {e}")

    return result_list

def id_search_detail(id):
    params = {
        "key": API_KEY,
        "id": id,
        "format": "json",
    }

    base_url = "http://webservice.recruit.co.jp/hotpepper/gourmet/v1/"

    try:
        response = requests.get(f"{base_url}", params=params)
        response.raise_for_status()

        data = response.json()
        if data.get("results"):
            shop = data["results"]["shop"]
            shop_info = {
                "shop_id": shop["id"],
                "name": shop["name"],
                "location": shop["address"],
                "genre": shop["genre"]["name"],
                "photo": shop["photo"]["pc"]["l"],
                "open": shop["open"]
            }
            return shop_info    
        else:
            print("検索結果がありません。")

    except Exception as e:
        print(f"エラーが発生しました: {e}")

    

def search_hotpepper_datum(genre, latitude, longitude, range):
    
    params = {
        "key": API_KEY,
        "lat": latitude,
        "lng": longitude,
        "range": range,
        "genre": genre,
        "count": 30,
        "format": "json",
    }

    return makeList(params)

def search_hotpepper_area(genre, area):
    
    params = {
        "key": API_KEY,
        "small_area": area,
        "range": 5,
        "genre": genre,
        #"count": 30,
        "format": "json",
    }

    return makeList(params)

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
    area = ""
    latitude = 36.07337
    longitude = 136.2036019
    area = area_code(area)
    genre = genre_code(genre)
    print(search_hotpepper_datum(genre, latitude, longitude))
