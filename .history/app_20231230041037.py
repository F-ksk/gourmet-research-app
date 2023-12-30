from flask import Flask, render_template, request, redirect, url_for
from flask_paginate import Pagination, get_page_parameter
from search import *

app = Flask(__name__)

# ページごとの表示数
RESULTS_PER_PAGE = 2

def paginate_results(results, page):
    """ページネーションを適用して結果を返す"""
    return results[(page - 1) * RESULTS_PER_PAGE: page * RESULTS_PER_PAGE]

def render_results_template(results, pagination):
    """結果とページネーションをテンプレートに渡してレンダリング"""
    return render_template("display.html", results=results, pagination=pagination)

def search_and_render(genre, area, range, search_function):
    """検索関数を適用し、結果をページネーションしてテンプレートに渡す"""
    page = request.args.get(get_page_parameter(), type=int, default=1)
    results = search_function(genre, area, range)
    paginated_results = paginate_results(results, page)
    pagination = Pagination(page=page, total=len(results), per_page=RESULTS_PER_PAGE, css_framework='bootstrap4')
    return render_results_template(paginated_results, pagination)

@app.route("/", methods=['GET', 'POST'])
def search():
    """検索ページの表示と検索条件に応じたリダイレクト"""
    if request.method == "POST":
        search_type = request.form.get("search-type")
        if search_type == "location":
            # エリア検索の場合は result_area にリダイレクト
            return redirect(url_for('result_area', genre=request.form['search-genre'], area=request.form['location'], range=request.form['search-range']))
        elif search_type == "current-location":
            # 現在地検索の場合は result_coordinates にリダイレクト
            return redirect(url_for('result_coordinates', genre=request.form['search-genre'], lat=request.form['latitude'], lng=request.form['longitude'], range=request.form['search-range']))
    return render_template("index.html")

@app.route("/<string:genre>/<string:area>/<string:range>/result")
def result_area(genre, area, range):
    """エリア検索の結果表示"""
    return search_and_render(genre, area, range, search_hotpepper_area)

@app.route("/<string:genre>/<float:lat>/<float:lng>/<string:range>/result")
def result_coordinates(genre, lat, lng, range):
    """現在地検索の結果表示"""
    return search_and_render(genre, lat, lng, range, search_hotpepper_datum)

@app.route("/<string:id>/detail")
def detail(id):
    """詳細ページの表示"""
    shop_detail = id_search_detail(id)
    return render_template("detail.html", shop_detail=shop_detail[0])
