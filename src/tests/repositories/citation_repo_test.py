import unittest
from repositories.citation_repository import citation_repository


class TestCitationRepository(unittest.TestCase):
    def setUp(self):
        self.citation_repository = citation_repository
        self.citation_repository.citations = []

    def test_new_citation_list_is_empty(self):
        self.assertEqual(self.citation_repository.citations, [])

    def test_add_new_citation(self):
        self.citation_repository.add_citation(citation={
            "cite_key": "1",
            "author": "Tee",
            "title": "Teeskentelyä",
            "year": "2022",
            "publisher": "Paras"
        }
        )

        self.assertEqual(len(self.citation_repository.citations), 1)
        self.assertEqual(
            self.citation_repository.citations[0]["cite_key"], "1")
        self.assertEqual(
            self.citation_repository.citations[0]["title"], "Teeskentelyä")

    def test_return_citations_correctly(self):
        self.citation_repository.add_citation(
            citation={
                "cite_key": "1",
                "author": "Tee",
                "title": "Teeskentelyä",
                "year": "2022",
                "publisher": "Paras"
            }
        )
        self.citation_repository.add_citation(
            citation={
                "cite_key": "2",
                "author": "Tee",
                "title": "Teeskentelyä2",
                "year": "2022",
                "publisher": "Paras"
            }
        )

        citations = self.citation_repository.get_citation()

        self.assertEqual(len(citations), 2)
        self.assertEqual(citations[0]["cite_key"], "1")

    def test_remove_citations(self):
        self.citation_repository.add_citation(
            citation={
                "cite_key": "1",
                "author": "Tee",
                "title": "Teeskentelyä",
                "year": "2022",
                "publisher": "Paras"
            }
        )
        self.citation_repository.add_citation(
            citation={
                "cite_key": "2",
                "author": "Tee",
                "title": "Teeskentelyä2",
                "year": "2022",
                "publisher": "Paras"
            }
        )
        citations = self.citation_repository.get_citation()
        cite_key = self.citation_repository.citations[0]["cite_key"]
        self.citation_repository.remove_citation(cite_key)
        self.assertEqual(len(citations), 1)

    def test_remove_citation_that_does_not_exist(self):
        self.citation_repository.add_citation(
            citation={
                "cite_key": "1",
                "author": "Tee",
                "title": "Teeskentelyä",
                "year": "2022",
                "publisher": "Paras"
            }
        )

        boolean = self.citation_repository.remove_citation("eiole")
        self.assertEqual(boolean, False)
