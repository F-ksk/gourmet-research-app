from flask import Flask
from flask import render_template, request
from search import *

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def search():
    if request.method == "POST":
        # ラジオボタンの値を取得
        search_type = request.form.get("search-type")
        # ここで取得した値を使って必要な処理を実行
        if search_type == "location":
            location = request.form.get("location")
            area = area_code(location)
            genre = "ラーメン"
            genre = genre_code(genre)
            results = search_hotpepper_area(genre, area)
            return render_template("display.html", results=results, s=search_type)
        elif search_type == "current-location":
            range = int(request.form.get("search-range"))
            latitude = request.form.get("latitude")
            longitude = request.form.get("longitude")
            genre = "ラーメン"
            genre = genre_code(genre)
            results = search_hotpepper_datum(genre, latitude, longitude, range)
            return render_template("display.html", results=results)
    else :
        return render_template("index.html")

@app.route("/result")
def result():
    return render_template("display.html")