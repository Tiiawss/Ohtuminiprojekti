import unittest
import string
import random
from services.bibtex_service import BibTexService


class StudCitationService:
    def __init__(self):
        self._citations = []

    def _get_unique_cite_key(self, author: str, year: str) -> str:

        def get_unique_from(citekey: str):
            for citation in self.get_all():
                if citation['cite_key'] == citekey:
                    return get_unique_from(
                        f"{citekey}{random.choice(string.ascii_lowercase)}"
                    )
            return citekey
        citekey = ""

        for i, character in enumerate(author):
            if i >= 6:
                break
            if character in string.ascii_letters:
                citekey += character

        for i, digit_string in enumerate(year):
            if i >= 5:
                break
            if digit_string in string.digits:
                citekey += digit_string

        return get_unique_from(citekey)

    def save_citation(self, field_keys_values: list) -> bool:
        citation_to_save = {}
        for key, value in field_keys_values:

            if value.strip() == "":
                return False

            citation_to_save[key] = value

        cite_key_author = "no_author"
        if citation_to_save.get("author"):
            cite_key_author = citation_to_save["author"]

        cite_key_year = "420"
        if citation_to_save.get("year"):
            cite_key_year = citation_to_save["year"]

        citation_to_save['cite_key'] = self._get_unique_cite_key(
            cite_key_author,
            cite_key_year
        )

        self._citations.append(citation_to_save)
        return True

    def get_all(self):
        return self._citations


class TestBibtexService(unittest.TestCase):
    def setUp(self):
        self._citation_service = StudCitationService()
        self.bibservice = BibTexService(self._citation_service)

    def test_one_citation_correctly_turned_to_bibtex(self):
        self._citation_service.save_citation([
            ("author", "tee"),
            ("title", "teee"),
            ("year", "2002"),
            ("type", "book"),
            ("publisher", "jtn")
        ])

        self.bibservice.turn_cites_to_bibtex()
        cites = self.bibservice.get_bibtex()

        self.assertEqual(len(cites), 1)
        self.assertEqual(cites[0][0], '@book{tee2002,')

    def test_one_citatoin_with_scandic_letters_turned_to_bibtex_correctly(self):
        self._citation_service.save_citation([
            ("author", "tee"),
            ("title", "teetä"),
            ("year", "2002"),
            ("type", "book"),
            ("publisher", "jtn")
        ])

        self.bibservice.turn_cites_to_bibtex()
        cites = self.bibservice.get_bibtex()

        self.assertEqual(cites[0][2], '    title = "teet{\\"{a}}",')

    def test_multiple_citations_added_correctly(self):
        random.seed(1)
        self._citation_service.save_citation([
            ("author", "tee"),
            ("title", "teetä"),
            ("year", "2002"),
            ("type", "book"),
            ("publisher", "jtn")
        ])
        self._citation_service.save_citation([
            ("author", "tee"),
            ("title", "teetä"),
            ("year", "2002"),
            ("type", "article"),
            ("publisher", "jtn")
        ])

        self.bibservice.turn_cites_to_bibtex()
        cites = self.bibservice.get_bibtex()

        self.assertEqual(len(cites), 2)
        self.assertEqual(cites[0][0], '@book{tee2002,')
        self.assertEqual(cites[1][0], '@article{tee2002e,')
