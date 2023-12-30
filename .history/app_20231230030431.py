from flask import Flask
from flask import render_template, request, redirect, url_for
from flask_paginate import Pagination, get_page_parameter
from search import *

RESULTS_PER_PAGE = 2

app = Flask(__name__)
@app.route("/", methods=['GET', 'POST'])
def search():
    # ラジオボタンの値を取得
    pagination = ""
    search_type = request.form.get("search-type")
    # ここで取得した値を使って必要な処理を実行
    if search_type == "location":
        range = int(request.form.get("search-range"))
        location = request.form.get("location")
        area = area_code(location)
        genre = request.form.get("search-genre")
        genre = genre_code(genre)
        results = search_hotpepper_area(genre, area, range)
        page = request.args.get(get_page_parameter(), type=int, default=1)
        res = results[(page - 1)*2: page*2]
        pagination = Pagination(page=page, total=len(results),  per_page=2, css_framework='bootstrap4')
        return render_template("display.html", results=res, pagination=pagination)
    elif search_type == "current-location":
        range = int(request.form.get("search-range"))
        latitude = request.form.get("latitude")
        longitude = request.form.get("longitude")
        genre = request.form.get("search-genre")
        genre = genre_code(genre)
        results = search_hotpepper_datum(genre, latitude, longitude, range)
        return render_template("display.html", results=results)
    get_page_parameter()
    return render_template("index.html")
#@app.route("/", methods=['GET', 'POST'])
#def search():
#    if request.method == "POST":
#        # ラジオボタンの値を取得
#        search_type = request.form.get("search-type")
#        # ここで取得した値を使って必要な処理を実行
#        if search_type == "location":
#            range = int(request.form.get("search-range"))
#            location = request.form.get("location")
#            area = area_code(location)
#            genre = request.form.get("search-genre")
#            genre = genre_code(genre)
#            results = search_hotpepper_area(genre, area, range)
#            print(results)
#
#            # ページングの設定
#            page = request.args.get(get_page_parameter(), type=int, default=1)
#            start = (page - 1) * RESULTS_PER_PAGE
#            end = start + RESULTS_PER_PAGE
#            res = results[start:end]
#
#            pagination = Pagination(
#                page=page,
#                total=len(results),
#                per_page=RESULTS_PER_PAGE,
#                css_framework='bootstrap4'
#            )
#
#            # ページごとの検索結果を表示するURLを構築
#            redirect_url = url_for('search', _external=True, **request.form.to_dict())
#            redirect_url_with_page = f"{redirect_url}?{get_page_parameter()}={page}"
#
#            return render_template("display.html", results=res, pagination=pagination, redirect_url=redirect_url_with_page)
#
#
#            page = request.args.get(get_page_parameter(), type=int, default=1)
#            res = results[(page - 1)*2: page*2]
#            pagination = Pagination(page=page, total=len(results),  per_page=2, css_framework='bootstrap4')
#            return render_template("display.html", results=res, pagination=pagination)
#        elif search_type == "current-location":
#            range = int(request.form.get("search-range"))
#            latitude = request.form.get("latitude")
#            longitude = request.form.get("longitude")
#            genre = request.form.get("search-genre")
#            genre = genre_code(genre)
#            results = search_hotpepper_datum(genre, latitude, longitude, range)
#            return render_template("display.html", results=results)
#    return render_template("index.html")
#

@app.route("/result", methods=['GET', 'POST'])
def result():
    if request.method == "POST":
        return render_template("display.html")
    return render_template("display.html")

@app.route("/<string:id>/detail")
def detail(id):
    shop_detail = id_search_detail(id)
    return render_template("detail.html", shop_detail=shop_detail[0])