from flask import Flask
from flask import render_template, request, redirect, url_for
from search import *

app = Flask(__name__)

from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # セキュアなランダムな文字列に置き換えてください




@app.route("/result", methods=['GET', 'POST'])
def result():
    # 以前の結果と検索条件をセッションから取得
    prev_results = session.get("results", [])
    prev_search_type = session.get("search_type", "")
    prev_location = session.get("location", "")
    prev_range = session.get("range", 0)
    prev_genre = session.get("genre", "")

    if request.method == "POST":
        # ボタンが押されたときの処理
        return redirect(url_for('detail'))

    # ページを開いたときに以前の結果を表示
    return render_template("display.html", results=prev_results, s=prev_search_type)

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
            return render_template("display.html", results=results, s=search_type)
        elif search_type == "current-location":
            range = int(request.form.get("search-range"))
            latitude = request.form.get("latitude")
            longitude = request.form.get("longitude")
            genre = request.form.get("search-genre")
            genre = genre_code(genre)
            results = search_hotpepper_datum(genre, latitude, longitude, range)
            return render_template("display.html", results=results)
    return render_template("index.html")
#
#@app.route("/result", methods=['GET', 'POST'])
#def result():
#    if request.method == "POST":
#        return redirect(url_for('detail'))
#    return render_template("display.html")
#
@app.route("/<string:id>/detail")
def detail(id):
    shop_detail = id_search_detail(id)
    return render_template("detail.html", shop_detail=shop_detail[0])