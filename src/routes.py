from flask import redirect, render_template, request
from app import app
from services.citation_service import citation_service
from services.bibtex_service import BibTexService
from repositories.configuration_repository import configuration_repository


@app.route("/")
def index():
    """Avaa etusivun
    """

    if not citation_service.get_last():
        return render_template("index.html",
                               last_citation_rows=None,
                               cite_key=None
                               )

    cite_type = citation_service.get_last()["type"]
    dict_fields = configuration_repository.get_cites()[cite_type]
    last_citation_rows = []

    for field_key, value in citation_service.get_last().items():
        if field_key in ["type", "cite_key", "date"]:
            continue
        if field_key == "tagit":
            last_citation_rows.append(
                f"Tagit: {value}"
            )
            continue
        selostus_teksti = dict_fields[field_key][0]

        last_citation_rows.append(
            f"{selostus_teksti}: {value}"
        )

    return render_template("index.html",
                           last_citation_rows=last_citation_rows,
                           cite_key=citation_service.get_last()["cite_key"]
                           )


@app.route("/form", methods=["GET", "POST"])
def form():
    """Avaa lomakkeen, johon täytetään lähdeviitaus
    """
    cite_types = configuration_repository.get_cite_types()

    if request.method == "GET":
        typ = cite_types[0]

    else:
        typ = request.form.get("types")

    required_fields, optional_fields = configuration_repository.get_fields(typ)

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
    tags = request.form["tagit"]
    cite_values.append(("tagit", tags))
    if citation_service.save_citation(cite_values):
        return redirect("/")
    return redirect("/form")


@app.route("/all", methods=["GET", "POST"])
def view_all_citations():
    """Näyttää kaikki lähdeviittauksen ihmisluettavassa muodossa
    """
    tags_without_dublicates = sorted([*set(citation_service.get_tags())])
    if request.method == "GET":
        return render_template(
            "citations.html",
            citations=citation_service.get_all(),
            citations_copy=citation_service.get_all(),
            tags=tags_without_dublicates
        )
    tag = request.form["tags"]
    return render_template(
        "citations.html",
        citations=citation_service.get_citations_by_tag(tag),
        citations_copy=citation_service.get_citations_by_tag(tag),
        tags=tags_without_dublicates,
        tag_copy=tag,
        selected=tag
    )


@app.route("/remove", methods=["POST"])
def remove_citation():
    """Poista lähdeviittaus sovelluksesta
    """

    citation_key = request.form["id"]
    citation_service.remove_citation(citation_key)
    return redirect("/all")


@app.route("/bibtex")
def generate_bibtex():
    """Muodostaa lähdeviittauksista bibtex muotoisen tekstin
    """

    bibtex_service = BibTexService()

    bibtex_service.turn_cites_to_bibtex()

    bibtex = bibtex_service.get_bibtex()

    return render_template("bibtex.html", bibtex=bibtex)


@app.route("/bibtex_from_tag", methods=["POST"])
def generate_bibtex_from_tag():
    """ Muodostaa lähdeviittauksista bibtex muotoinen teksti tagien perusteella  """

    bibtex_service = BibTexService()

    tag = request.form["citations"]

    if tag:
        citations = citation_service.get_citations_by_tag(tag)
        bibtex_service.turn_cites_to_bibtex(citations)
    else:
        bibtex_service.turn_cites_to_bibtex()

    bibtex = bibtex_service.get_bibtex()

    return render_template("bibtex.html", bibtex=bibtex)


@app.route("/delete_all", methods=["POST"])
def delete_all():
    """ Delete all citations """
    citation_service.delete_all()
    return redirect("/")


@app.route("/use_test_db", methods=["POST"])
def use_test_db():
    """ Use test db for tests """
    citation_service.repo.move_to_tests()
