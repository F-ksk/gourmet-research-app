from flask import Flask
from flask import render_template, request

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
            return f"地名から検索: {location}"
        elif search_type == "current-location":
            return "現在地から検索"
        else:
            return "何も選択されていません"
    return render_template("display.html")