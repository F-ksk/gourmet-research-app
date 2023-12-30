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
        # ここで取得した値を使って必要な処理を実行
        if search_type == "location":
            range = int(request.form.get("search-range"))
            location = request.form.get("location")
            area = area_code(location)
            genre = request.form.get("search-genre")
            genre = genre_code(genre)
            results = search_hotpepper_area(genre, area, range)
            return redirect(url_for('result', genre=genre, area=area))
            redirect_url_with_page = url_for('result', genre=genre, area=area)
            return render_template("display.html", results=results, redirect_url=redirect_url_with_page)
            #page = request.args.get(get_page_parameter(), type=int, default=1)
            #res = results[(page - 1)*2: page*2]
            #pagination = Pagination(page=page, total=len(results),  per_page=2, css_framework='bootstrap4')
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


@app.route("/<string:genre>/<string:area>/result")
def result(genre, area):
    # ページングの処理
    page = request.args.get(get_page_parameter(), type=int, default=1)
    results = search_hotpepper_area(genre, area, range)  # ここに実際の処理を追加する必要があります
    res = results[(page - 1) * 2: page * 2]
    pagination = Pagination(page=page, total=len(results), per_page=2, css_framework='bootstrap4')
    #redirect_url_with_page = url_for('result', page=page)
    return render_template("display.html", results=res, pagination=pagination)
    return render_template("display.html", results=results)


@app.route("/<string:id>/detail")
def detail(id):
    shop_detail = id_search_detail(id)
    return render_template("detail.html", shop_detail=shop_detail[0])