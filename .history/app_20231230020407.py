from flask import Flask
from flask import render_template, request, redirect, url_for
from search import *

app = Flask(__name__)
@app.route("/", methods=['GET', 'POST'])
def search():
    if request.method == "POST":
        # ラジオボタンの値を取得
        search_type = request.form.get("search-type")
        # ここで取得した値を使って必要な処理を実行
        if search_type == "location":
            range = int(request.form.get("search-range"))
            location = request.form.get("location")
            area = area_code(location)
            genre = request.form.get("search-genre")
            genre = genre_code(genre)
            results = search_hotpepper_area(genre, area, range)
            return render_template("display.html", results=results)
        elif search_type == "current-location":
            range = int(request.form.get("search-range"))
            latitude = request.form.get("latitude")
            longitude = request.form.get("longitude")
            genre = request.form.get("search-genre")
            genre = genre_code(genre)
            results = search_hotpepper_datum(genre, latitude, longitude, range)
            return render_template("display.html", results=results)
    return render_template("index.html")


@app.route("/result", methods=['GET', 'POST'])
def result():
    if request.method == "POST":
        return redirect(url_for('detail'))

    return render_template("display.html")

@app.route("/<string:id>/detail")
def detail(id):
    shop_detail = id_search_detail(id)
    return render_template("detail.html", shop_detail=shop_detail[0])