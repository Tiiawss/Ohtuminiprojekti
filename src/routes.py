from flask import redirect, render_template, request
from app import app


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/create", methods=["POST"])
def create():
    author_name = request.form["author"]
    title = request.form["title"]
    year = request.form["year"]
    publisher = request.form["publisher"]
    return render_template("index.html",author_name=author_name, title=title, year=year, publisher=publisher)
