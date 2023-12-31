import requests
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

API_KEY = os.environ.get("API_KEY")
#from config import API_KEY

#-----------------------------------------------
# ホットペッパーグルメリサーチAPIからリスト作成
#-----------------------------------------------
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
                    "open": shop["open"],
                    "access" : shop["access"],
                    "catch": shop["catch"],
                    "photo_m": shop["photo"]["pc"]["m"],
                    "photo_l": shop["photo"]["pc"]["l"]
                }
                result_list.append(shop_info) 
        else:
            print("検索結果がありません。")

    except Exception as e:
        print(f"エラーが発生しました: {e}")

    return result_list

#-----------------------------------------------
# 店舗IDから検索
#-----------------------------------------------
def id_search_detail(id):
    params = {
        "key": API_KEY,
        "id": id,
        "format": "json",
    }
    return makeList(params)

#-----------------------------------------------
# 緯度・軽度, ジャンル, 範囲から検索
#-----------------------------------------------
def search_hotpepper_datum(genre, latitude, longitude, range):
    params = {
        "key": API_KEY,
        "lat": latitude,
        "lng": longitude,
        "range": range,
        "genre": genre,
        "count": 100,
        "format": "json",
    }

    return makeList(params)

#-----------------------------------------------
# エリア, ジャンル, 範囲から検索
#-----------------------------------------------
def search_hotpepper_area(genre, area, range):
    params = {
        "key": API_KEY,
        "small_area": area,
        "range": range,
        "genre": genre,
        "count": 100,
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
            return area['code']
        else:
            return "X874"

    except Exception as e:
        print(f"エラーが発生しました: {e}")
        return "X874"

#-------------------------------------
# 検索ジャンルをジャンルコードに変更
#-------------------------------------
def genre_code(genre):
    #居酒屋,ダイニングバー・バル,創作料理,和食,洋食,
    #イタリアン・フレンチ,中華,アジア・エスニック料理,各国料理
    #カラオケ・パーティ,バー・カクテル,ラーメン,お好み焼き・もんじゃ,
    #カフェ・スイーツ,その他グルメ
    print("API_KEY:"+API_KEY)
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
            return genre['code']
        else:
            return ""

    except Exception as e:
        print(f"エラーが発生しました: {e}")
        return ""

