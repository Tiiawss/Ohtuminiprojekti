from flask import redirect, render_template, request
from app import app
from services.book_citation_service import book_service

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

@app.route("/all")
def view_all_citations():

    return render_template(
        "citations.html",
        citations = book_service.get_all()
    )
