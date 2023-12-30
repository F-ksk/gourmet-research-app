from flask import Flask
from flask import render_template, request, redirect, url_for
from search import *

app = Flask(__name__)

# ページごとのアイテム数
ITEMS_PER_PAGE = 2

def get_pagination_info(page, items_per_page):
    total_items = len(dummy_results)
    start_index = (page - 1) * items_per_page
    end_index = start_index + items_per_page
    return start_index, end_index, total_items

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
            page = int(request.args.get('page', 1))
            start_index, end_index, total_items = get_pagination_info(page, ITEMS_PER_PAGE)
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


@app.route("/result", methods=['GET', 'POST'])
def result():
    if request.method == "POST":
        return redirect(url_for('detail'))
    return render_template("display.html")

@app.route("/<string:id>/detail")
def detail(id):
    shop_detail = id_search_detail(id)
    return render_template("detail.html", shop_detail=shop_detail[0])