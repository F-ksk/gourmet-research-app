from flask import Flask, render_template, request, redirect, url_for
from flask_paginate import Pagination, get_page_parameter
from search import *

app = Flask(__name__)

# ページごとの表示数
RESULTS_PER_PAGE = 2

# ページング処理
def pagination(results):
    page = request.args.get(get_page_parameter(), type=int, default=1)
    res = results[(page - 1) * RESULTS_PER_PAGE: page * RESULTS_PER_PAGE]
    pagination = Pagination(page=page, total=len(results), per_page=RESULTS_PER_PAGE, css_framework='bootstrap4')
    return render_template("display.html", results=res, pagination=pagination)

# search_typeからリダイレクト先URLへ
def search_type_to_redirect(search_type):
    if search_type == "location":
        location = request.form.get("location")
        range_value = int(request.form.get("search-range"))
        area = area_code(location)
        genre = request.form.get("search-genre")
        genre = genre_code(genre)
        return redirect(url_for('result_area', genre=genre, area=area, range=range_value))
    elif search_type == "current-location":
        range_value = int(request.form.get("search-range"))
        latitude = request.form.get("latitude")
        longitude = request.form.get("longitude")
        genre = request.form.get("search-genre")
        genre = genre_code(genre)
        return redirect(url_for('result_coordinates', genre=genre, lat=latitude, lng=longitude, range=range_value))

#---------------------------------
# 検索条件設定ページ
#---------------------------------
@app.route("/", methods=['GET', 'POST'])
def search():
    if request.method == "POST":
        search_type = request.form.get("search-type")
        return search_type_to_redirect(search_type)
    return render_template("index.html")

#---------------------------------
# 検索結果ページ(エリア)
#---------------------------------
@app.route("/<string:genre>/<string:area>/<string:range>/result")
def result_area(genre, area, range):
    results = search_hotpepper_area(genre, area, range)  
    return pagination(results)

#---------------------------------
# 検索結果ページ(緯度・経度)
#---------------------------------
@app.route("/<string:genre>/<float:lat>/<float:lng>/<string:range>/result")
def result_coordinates(genre, lat, lng, range):
    results = search_hotpepper_datum(genre, lat, lng, range)
    return pagination(results)

#---------------------------------
# 店舗詳細ページ
#---------------------------------
@app.route("/<string:id>/detail")
def detail(id):
    shop_detail = id_search_detail(id)
    return render_template("detail.html", shop_detail=shop_detail[0])
