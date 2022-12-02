import unittest
import string
from services.citation_service import CitationService


class StudCitationRepo:
    def __init__(self) -> None:
        self.citations = []

    def add_citation(self, citation) -> None:

        self.citations.append(citation)

    def get_citation(self) -> list:
        return self.citations

    def remove_citation(self, cite_key) -> bool:
        """Removes one citation"""
        index_to_remove = -1
        for index, element in enumerate(self.citations):
            if element["cite_key"] == cite_key:
                index_to_remove = index
        if index_to_remove != -1:
            self.citations.pop(index_to_remove)
            return True
        return False


class TestCitationService(unittest.TestCase):
    def setUp(self):
        self.citation_service = CitationService(StudCitationRepo())

    def test_saves_citation_correclty(self):

        re = self.citation_service.save_citation([
        ("author", "tee"),
        ("title", "teee"), 
        ("year","2002"), 
        ("publisher","jtn")
        ])

        citations = self.citation_service.get_all()

        self.assertEqual(len(citations), 1)

        self.assertEqual(re, True)

    def test_does_not_save_incorrect_citation(self):
        re = self.citation_service.save_citation([
        ("author", ""),
        ("title", "teee"),
        ("year","2002"),
        ("publisher","jtn")
        ])

        citations = self.citation_service.get_all()

        self.assertEqual(re, False)

        self.assertEqual(len(citations), 0)

    def test_missing_author_field(self):

        self.citation_service.save_citation([
        ("title", "teee"),
        ("year","2002"),
        ("publisher","jtn")
        ])
        citation = self.citation_service.get_all()[0]
        self.assertEqual(citation["cite_key"], "noaut2002")

    def test_missing_year_field(self):

        self.citation_service.save_citation([
        ("author", "teee"),
        ("title", "tooo"),
        ("publisher","jtn")
        ])
        citation = self.citation_service.get_all()[0]
        self.assertEqual(citation["cite_key"], "teee420")

    def test_unique_citekey_proper_formatting(self):

        self.citation_service.save_citation([
        ("author", "pekpekka"),
        ("title", "teee"),
        ("year","2002"),
        ("publisher","jtn")
        ])

        self.citation_service.save_citation([
        ("author", "pekpekka"),
        ("title", "teee"),
        ("year","2002"),
        ("publisher","jtn")
        ])

        for citation in self.citation_service.get_all():
            for character in citation["cite_key"]:
                self.assertEqual(
                    character in string.ascii_letters or character in string.digits,
                    True
                )

    def test_unique_really_unique(self):

        self.citation_service.save_citation([
        ("author", "pekpekka"),
        ("title", "teee"),
        ("year","2002"),
        ("publisher","jtn")
        ])
        self.citation_service.save_citation([
        ("author", "pekpekka"),
        ("title", "teee"),
        ("year","2002"),
        ("publisher","jtn")
        ])
        self.assertNotEqual(
            self.citation_service.get_all()[0]["cite_key"],
            self.citation_service.get_all()[1]["cite_key"]
        )

    def test_only_letters_to_citekey_from_author(self):

        self.citation_service.save_citation([
        ("author", "pe1!3.,"),
        ("title", "teee"),
        ("year","2002"),
        ("publisher","jtn")
        ])
        cite_key = self.citation_service.get_all()[0]["cite_key"]
        self.assertEqual(cite_key, "pe2002")

    def test_only_digits_to_citekey_from_year(self):

        self.citation_service.save_citation([
        ("author", "pe1!3.,"),
        ("title", "teee"),
        ("year","2002 -- 2004"),
        ("publisher","jtn")
        ])
        cite_key = self.citation_service.get_all()[0]["cite_key"]
        self.assertEqual(cite_key, "pe2002")

    def test_get_last(self):

        self.citation_service.save_citation([
        ("author", "pekpekka"),
        ("title", "teee"),
        ("year","2002"),
        ("publisher","jtn")
        ])
        self.citation_service.save_citation([
        ("author", "pekpekka2"),
        ("title", "teee"),
        ("year","2002"),
        ("publisher","jtn")
        ])

        citation = self.citation_service.get_last()
        self.assertEqual(
            citation,
            self.citation_service.get_all()[-1]
        )

    def test_get_last_none(self):

        citations = self.citation_service.get_last()

        self.assertEqual(citations, None)

    def test_remove_citation(self):

        self.citation_service.save_citation([
        ("author", "pekpekka2"),
        ("title", "teee"),
        ("year","2002"),
        ("publisher","jtn")
        ])
        self.citation_service.save_citation([
        ("author", "pekpekka1"),
        ("title", "teee"),
        ("year","2002"),
        ("publisher","jtn")
        ])

        citekey = self.citation_service.get_all()[0]['cite_key']
        self.citation_service.remove_citation(citekey)
        all = self.citation_service.get_all()
        self.assertEqual(len(all), 1)
        self.assertEqual(all[0]["author"], "pekpekka1")
