from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def search():
    return render_template("index.html")

@app.route("/result")
def result():
    return render_template("display.html")