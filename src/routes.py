from flask import redirect, render_template, request
from app import app
from services.book_citation_service import book_service

@app.route("/")
def index():
    return render_template("index.html", book=book_service.get_last())

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/create", methods=["POST"])
def create():
    author_name = request.form["author"]
    title = request.form["title"]
    year = request.form["year"]
    publisher = request.form["publisher"]
    book_service.save_citation(author_name, title, year, publisher)
    return redirect("/")

@app.route("/all")
def view_all_citations():

    return render_template(
        "citations.html",
        citations = book_service.get_all()
    )
