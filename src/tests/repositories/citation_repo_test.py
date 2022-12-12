import unittest
from repositories.citation_repository import citation_repository
from datetime import datetime


class TestCitationRepository(unittest.TestCase):
    def setUp(self):
        self.citation_repository = citation_repository
        self.citation_repository.move_to_tests()
        self.citation_repository.delete_all()
        self.tag_test_citations = ([{
            "type": "Book",
            "cite_key": "1",
            "author": "Tee",
            "title": "Teeskentelyä",
            "year": "2022",
            "publisher": "Paras",
            "tagit": "testi"
        }, {
            "type": "Book",
            "cite_key": "2",
            "author": "Tee",
            "title": "Teeskentelyä2",
            "year": "2022",
            "publisher": "Paras",
            "tagit": "testi1"
        }
        ])

    def tearDown(self) -> None:
        self.citation_repository.delete_all()

    def test_new_citation_list_is_empty(self):
        self.assertEqual(self.citation_repository.get_citation(), [])

    def test_add_new_citation(self):
        self.citation_repository.add_citation(citation={
            "type": "Book",
            "cite_key": "1",
            "author": "Tee",
            "title": "Teeskentelyä",
            "year": "2022",
            "publisher": "Paras"
        }
        )

        all_citations = self.citation_repository.get_citation()
        self.assertEqual(len(all_citations), 1)
        self.assertEqual(all_citations[0]["cite_key"], "1")
        self.assertEqual(all_citations[0]["title"], "Teeskentelyä")

    def test_return_citations_correctly(self):
        self.citation_repository.add_citation(
            citation={
                "type": "Book",
                "cite_key": "1",
                "author": "Tee",
                "title": "Teeskentelyä",
                "year": "2022",
                "publisher": "Paras"
            }
        )
        self.citation_repository.add_citation(
            citation={
                "type": "Book",
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
                "type": "Book",
                "cite_key": "1",
                "author": "Tee",
                "title": "Teeskentelyä",
                "year": "2022",
                "publisher": "Paras"
            }
        )
        self.citation_repository.add_citation(
            citation={
                "type": "Book",
                "cite_key": "2",
                "author": "Tee",
                "title": "Teeskentelyä2",
                "year": "2022",
                "publisher": "Paras"
            }
        )
        citations = self.citation_repository.get_citation()
        cite_key = citations[0]["cite_key"]
        self.citation_repository.remove_citation(cite_key)
        citations = self.citation_repository.get_citation()
        self.assertEqual(len(citations), 1)

    def test_remove_citation_that_does_not_exist(self):
        self.citation_repository.add_citation(
            citation={
                "type": "Book",
                "cite_key": "1",
                "author": "Tee",
                "title": "Teeskentelyä",
                "year": "2022",
                "publisher": "Paras"
            }
        )

        boolean = self.citation_repository.remove_citation("eiole")
        self.assertEqual(boolean, False)

    def get_test_citations(self):
        return ([{
            "type": "Book",
            "cite_key": "1",
            "author": "Tee",
            "title": "Teeskentelyä",
            "year": "2022",
            "publisher": "Paras",
            "tagit": "testi"
        }, {
            "type": "Book",
            "cite_key": "2",
            "author": "Tee",
            "title": "Teeskentelyä2",
            "year": "2022",
            "publisher": "Paras",
            "tagit": "testi1"
        }
        ])

    def test_get_tags_finds_multiple(self):
        for citation in self.get_test_citations():
            self.citation_repository.add_citation(citation)
        tagit = [tagi["tagit"]
                 for tagi in self.citation_repository.get_citation()]
        self.assertEqual(len(tagit), 2)
        self.assertEqual(
            all((tagi in self.citation_repository.get_tags())
                for tagi in tagit),
            True
        )

    def test_get_tags_finds_none(self):
        self.assertEqual(
            self.citation_repository.get_tags(),
            []
        )

    def test_get_citation_by_tag(self):
        for citation in self.get_test_citations():
            self.citation_repository.add_citation(citation)
        self.assertEqual(
            self.get_test_citations()[:1],
            self.citation_repository.get_citations_by_tag("testi")
        )

    def test_get_last_citation_multiple(self):
        """
        Huom pitää lisätä datetime.now(), muuten .get_last ei toimi
        Huom citation_repository.add_citation() muokkaa sille annettua oliota
             sen vuoksi se haetaan uudestaan metodilta Equal checkiä varten!
        """
        for i in range(len(self.get_test_citations())):
            citation_to_add = self.get_test_citations()[i]
            citation_to_add["date"] = datetime.now()
            self.citation_repository.add_citation(
                citation_to_add
            )
            self.assertEqual(
                self.citation_repository.get_last(),
                self.get_test_citations()[i]
            )

    def test_get_last_citation_single(self):
        self.citation_repository.add_citation(self.get_test_citations()[1])
        self.assertEqual(
            self.citation_repository.get_last(),
            self.get_test_citations()[1]
        )

    def test_get_last_citation_none(self):
        self.assertEqual(
            self.citation_repository.get_last(),
            None
        )
