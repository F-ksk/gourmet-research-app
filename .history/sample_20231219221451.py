import requests

URL = 'http://webservice.recruit.co.jp/hotpepper/gourmet/v1/'

API_KEY = '5947c67fce02336b'

def search_hotpepper_gourmet(api_key, keyword):
    base_url = "http://webservice.recruit.co.jp/hotpepper/gourmet/v1/"
    endpoint = "shops"
    
    params = {
        "key": api_key,
        "name_any": keyword,
        "count": 100,
        "format": "json",
    }

    try:
        response = requests.get(f"{base_url}{endpoint}", params=params)
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

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTPエラーが発生しました: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"リクエストエラーが発生しました: {req_err}")
    except Exception as e:
        print(f"エラーが発生しました: {e}")

if __name__ == "__main__":
    API_KEY = "YOUR_API_KEY"
    keyword = "ラーメン"
    search_hotpepper_gourmet(API_KEY, keyword)
