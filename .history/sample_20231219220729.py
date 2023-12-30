import requests

URL = 'http://webservice.recruit.co.jp/hotpepper/gourmet/v1/'

API_KEY = '5947c67fce02336b'

def search_hotpepper_gourmet(api_key, keyword):
    base_url = "http://webservice.recruit.co.jp/hotpepper/gourmet/v1/"
    endpoint = "shops"
    
    params = {
        "key": api_key,
        "name_any": keyword,
        "format": "json",  # レスポンスのフォーマットをJSONに指定
    }

    try:
        response = requests.get(f"{base_url}{endpoint}", params=params)
        response.raise_for_status()  # エラーレスポンスがあれば例外を発生させる

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

    except requests.exceptions.RequestException as e:
        print(f"エラーが発生しました: {e}")

if __name__ == "__main__":
    # ここに自分のAPIキーを設定
    API_KEY = "5947c67fce02336b"

    # 検索キーワードを設定
    keyword = "ラーメン"

    # 検索実行
    search_hotpepper_gourmet(API_KEY, keyword)