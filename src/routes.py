from flask import redirect, render_template, request
from app import app
from services.book_citation_service import book_service
from services.bibtex_service import BibTexService

@app.route("/")
def index():
    """Avaa etusivun
    """

    return render_template("index.html", book=book_service.get_last())

@app.route("/form", methods=["GET", "POST"])
def form():
    """Avaa lomakkeen, johon täytetään lähdeviitaus
    """
    cite_types = [("book", "kirja"), ("article", " artikkeli"), ("movie", "leffa")]
    required_fields = [("author", "kirjailija"), ("title", "Kirjan nimi"),
        ("year", "Julkaisuvuosi"), ("publisher", "Julkaisija")]
    optional_fields = [("wert", "areg"), ("argr", "eraij")]
    if request.method == "POST":
        return render_template("form.html",
            types = cite_types,
            required_fields = required_fields,
            optional_fields = optional_fields)
    return render_template("form.html", types=cite_types)

@app.route("/create", methods=["POST"])
def create():
    """Luo lomakkeen pohjalta lähdeviitauksen
    """

    author_name = request.form["author"]
    title = request.form["title"]
    year = request.form["year"]
    publisher = request.form["publisher"]
    if book_service.save_citation(author_name, title, year, publisher):
        return redirect("/")
    return redirect("/form")

@app.route("/all")
def view_all_citations():
    """Näyttää kaikki lähdeviittauksen ihmisluettavassa muodossa
    """

    return render_template(
        "citations.html",
        citations = book_service.get_all()
    )
    
@app.route("/remove",methods=["POST"])
def remove_citation():
    citation_key = request.form["id"]
    book_service.remove_citation(citation_key)
    return redirect("/")
    

@app.route("/bibtex")
def generate_bibtex():
    """Muodostaa lähdeviittauksista bibtex muotoisen tekstin
    """

    bibtex_service = BibTexService()

    bibtex_service.turn_books_to_bibtex()

    bibtex = bibtex_service.get_bibtex()

    return render_template("bibtex.html", bibtex=bibtex)
