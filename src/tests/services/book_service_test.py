import unittest
import string
from services.book_citation_service import BookCitation


class StudBookRepo:
    def __init__(self) -> None:
        self.books = []

    def add_book(self, book) -> None:

        self.books.append(book)

    def get_books(self) -> list:
        return self.books

    def remove_book(self, cite_key) -> bool:
        """Removes one book"""
        index_to_remove = -1
        for index, element in enumerate(self.books):
            if element["cite_key"] == cite_key:
                index_to_remove = index
        if index_to_remove != -1:
            self.books.pop(index_to_remove)
            return True
        return False


class TestBookService(unittest.TestCase):
    def setUp(self):
        self.book_service = BookCitation(StudBookRepo())

    def test_saves_citation_correclty(self):

        re = self.book_service.save_citation([
        ("author", "tee"),
        ("title", "teee"), 
        ("year","2002"), 
        ("publisher","jtn")
        ])

        books = self.book_service.get_all()

        self.assertEqual(len(books), 1)

        self.assertEqual(re, True)

    def test_does_not_save_incorrect_citation(self):
        re = self.book_service.save_citation([
        ("author", ""),
        ("title", "teee"),
        ("year","2002"),
        ("publisher","jtn")
        ])

        books = self.book_service.get_all()

        self.assertEqual(re, False)

        self.assertEqual(len(books), 0)

    def test_missing_author_field(self):

        self.book_service.save_citation([
        ("title", "teee"),
        ("year","2002"),
        ("publisher","jtn")
        ])
        citation = self.book_service.get_all()[0]
        self.assertEqual(citation["cite_key"], "noaut2002")

    def test_missing_year_field(self):

        self.book_service.save_citation([
        ("author", "teee"),
        ("title", "tooo"),
        ("publisher","jtn")
        ])
        citation = self.book_service.get_all()[0]
        self.assertEqual(citation["cite_key"], "teee420")

    def test_unique_citekey_proper_formatting(self):

        self.book_service.save_citation([
        ("author", "pekpekka"),
        ("title", "teee"),
        ("year","2002"),
        ("publisher","jtn")
        ])

        self.book_service.save_citation([
        ("author", "pekpekka"),
        ("title", "teee"),
        ("year","2002"),
        ("publisher","jtn")
        ])

        for book in self.book_service.get_all():
            for character in book["cite_key"]:
                self.assertEqual(
                    character in string.ascii_letters or character in string.digits,
                    True
                )

    def test_unique_really_unique(self):

        self.book_service.save_citation([
        ("author", "pekpekka"),
        ("title", "teee"),
        ("year","2002"),
        ("publisher","jtn")
        ])
        self.book_service.save_citation([
        ("author", "pekpekka"),
        ("title", "teee"),
        ("year","2002"),
        ("publisher","jtn")
        ])
        self.assertNotEqual(
            self.book_service.get_all()[0]["cite_key"],
            self.book_service.get_all()[1]["cite_key"]
        )

    def test_only_letters_to_citekey_from_author(self):

        self.book_service.save_citation([
        ("author", "pe1!3.,"),
        ("title", "teee"),
        ("year","2002"),
        ("publisher","jtn")
        ])
        cite_key = self.book_service.get_all()[0]["cite_key"]
        self.assertEqual(cite_key, "pe2002")

    def test_only_digits_to_citekey_from_year(self):

        self.book_service.save_citation([
        ("author", "pe1!3.,"),
        ("title", "teee"),
        ("year","2002 -- 2004"),
        ("publisher","jtn")
        ])
        cite_key = self.book_service.get_all()[0]["cite_key"]
        self.assertEqual(cite_key, "pe2002")

    def test_get_last(self):

        self.book_service.save_citation([
        ("author", "pekpekka"),
        ("title", "teee"),
        ("year","2002"),
        ("publisher","jtn")
        ])
        self.book_service.save_citation([
        ("author", "pekpekka2"),
        ("title", "teee"),
        ("year","2002"),
        ("publisher","jtn")
        ])

        book = self.book_service.get_last()
        self.assertEqual(
            book,
            self.book_service.get_all()[-1]
        )

    def test_get_last_none(self):

        books = self.book_service.get_last()

        self.assertEqual(books, None)

    def test_remove_citation(self):

        self.book_service.save_citation([
        ("author", "pekpekka2"),
        ("title", "teee"),
        ("year","2002"),
        ("publisher","jtn")
        ])
        self.book_service.save_citation([
        ("author", "pekpekka1"),
        ("title", "teee"),
        ("year","2002"),
        ("publisher","jtn")
        ])

        citekey = self.book_service.get_all()[0]['cite_key']
        self.book_service.remove_citation(citekey)
