from flask import redirect, render_template, request
from app import app
from services.book_citation_service import book_service
from services.bibtex_service import BibTexService
from repositories.configuration_repository import configuration_repository


@app.route("/")
def index():
    """Avaa etusivun
    """

    if not book_service.get_last():
        return render_template("index.html",
            last_citation_rows=None,
            cite_key = None
        )

    cite_type = book_service.get_last()["type"]
    dict_fields = configuration_repository.get_cites()[cite_type]
    last_citation_rows = []

    for field_key, value in book_service.get_last().items():
        if field_key in ["type", "cite_key"]:
            continue
        selostus_teksti = dict_fields[field_key][0]

        last_citation_rows.append(
            f"{selostus_teksti}: {value}"
        )


    return render_template("index.html",
        last_citation_rows=last_citation_rows,
        cite_key = book_service.get_last()["cite_key"]
    )


@app.route("/form", methods=["GET", "POST"])
def form():
    """Avaa lomakkeen, johon täytetään lähdeviitaus
    """
    cites = configuration_repository.get_cites()
    cite_types = []
    for keys in cites:
        cite_types.append(keys)
    required_fields = []
    optional_fields = []
    if request.method == "GET":
        typ = cite_types[0]
    else:
        typ = request.form.get("types")
    for key, values in cites[typ].items():
        if values[1]:
            required_fields.append((key, values[0]))
        else:
            optional_fields.append((key, values[0]))
    return render_template("form.html",
                           types=cite_types,
                           required_fields=required_fields,
                           optional_fields=optional_fields,
                           selected=typ
                           )


@app.route("/create", methods=["POST"])
def create():
    """Luo lomakkeen pohjalta lähdeviitauksen
    """

    cites = configuration_repository.get_cites()
    cite_values = []
    try:
        typ = request.form["selected"]
    except NameError:
        typ = list(cites.keys())[0]
    cite_values.append(("type", typ))
    for key in cites[typ]:
        field_input = request.form[key]
        if field_input:
            cite_values.append((key, field_input))
    if book_service.save_citation(cite_values):
        return redirect("/")
    return redirect("/form")


@app.route("/all")
def view_all_citations():
    """Näyttää kaikki lähdeviittauksen ihmisluettavassa muodossa
    """

    return render_template(
        "citations.html",
        citations=book_service.get_all()
    )


@app.route("/remove", methods=["POST"])
def remove_citation():
    """Poista lähdeviittaus sovelluksesta
    """

    citation_key = request.form["id"]
    book_service.remove_citation(citation_key)
    return redirect("/")


@app.route("/bibtex")
def generate_bibtex():
    """Muodostaa lähdeviittauksista bibtex muotoisen tekstin
    """

    bibtex_service = BibTexService()

    bibtex_service.turn_cites_to_bibtex()

    bibtex = bibtex_service.get_bibtex()

    return render_template("bibtex.html", bibtex=bibtex)
