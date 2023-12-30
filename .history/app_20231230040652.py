from flask import Flask
from flask import render_template, request, redirect, url_for
from flask_paginate import Pagination, get_page_parameter
from search import *

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def search():
    if request.method == "POST":
        # ラジオボタンの値を取得
        search_type = request.form.get("search-type")
        if search_type == "location":
            range = int(request.form.get("search-range"))
            location = request.form.get("location")
            area = area_code(location)
            genre = request.form.get("search-genre")
            genre = genre_code(genre)
            return redirect(url_for('result_area', genre=genre, area=area, range=range))
        elif search_type == "current-location":
            range = int(request.form.get("search-range"))
            latitude = request.form.get("latitude")
            longitude = request.form.get("longitude")
            genre = request.form.get("search-genre")
            genre = genre_code(genre)
            return redirect(url_for('result_coordinates', genre=genre, lat=latitude, lng=longitude, range=range))
    return render_template("index.html")


@app.route("/<string:genre>/<string:area>/<string:range>/result")
def result_area(genre, area, range):
    # ページングの処理
    page = request.args.get(get_page_parameter(), type=int, default=1)
    results = search_hotpepper_area(genre, area, range)  # ここに実際の処理を追加する必要があります
    res = results[(page - 1) * 2: page * 2]
    pagination = Pagination(page=page, total=len(results), per_page=2, css_framework='bootstrap4')
    #redirect_url_with_page = url_for('result', page=page)
    return render_template("display.html", results=res, pagination=pagination)


@app.route("/<string:genre>/<float:lat>/<float:lng>/<string:range>/result")
def result_coordinates(genre, lat, lng, range):
    # ページングの処理
    page = request.args.get(get_page_parameter(), type=int, default=1)
    results = search_hotpepper_datum(genre, lat, lng, range)  # ここに実際の処理を追加する必要があります
    res = results[(page - 1) * 2: page * 2]
    pagination = Pagination(page=page, total=len(results), per_page=2, css_framework='bootstrap4')
    #redirect_url_with_page = url_for('result', page=page)
    return render_template("display.html", results=res, pagination=pagination)
    return render_template("display.html", results=results)


@app.route("/<string:id>/detail")
def detail(id):
    shop_detail = id_search_detail(id)
    return render_template("detail.html", shop_detail=shop_detail[0])