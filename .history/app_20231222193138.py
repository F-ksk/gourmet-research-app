from flask import Flask
from flask import render_template, request
from search import *

app = Flask(__name__)

@app.route("/")
def search():
    return render_template("index.html")

@app.route("/result")
def result():
    if request.method == "POST":
        # ラジオボタンの値を取得
        search_type = request.form.get("search-type")
        
        # ここで取得した値を使って必要な処理を実行
        if search_type == "location":
            location = request.form.get("location")
            area = area_code(location)
            genre = "ラーメン"
            search_hotpepper_datum(genre, latitude, longitude)
            return f"地名から検索: {location}"
        elif search_type == "current-location":
            latitude = request.form.get("latitude")
            longitude = request.form.get("logitude")
            genre = "ラーメン"
            search_hotpepper_datum(genre, latitude, longitude)
            return render_template("display.html" )
        else:
            return "何も選択されていません"
    return render_template("display.html")