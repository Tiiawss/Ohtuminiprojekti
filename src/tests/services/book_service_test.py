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

class TestBookService(unittest.TestCase):
    def setUp(self):
        self.book_service = BookCitation(StudBookRepo())

    def test_saves_citation_correclty(self):
        re = self.book_service.save_citation(
                "Tee",
                "Teeskentelyä",
                "2022",
                "Paras"
            )

        books = self.book_service.get_all()

        self.assertEqual(len(books), 1)
        
        self.assertEqual(re, True)

    def test_does_not_save_incorrect_citation(self):
        re = self.book_service.save_citation(
                "",
                "Teeskentelyä",
                "2022",
                "Paras"
            )
        
        books = self.book_service.get_all()

        self.assertEqual(re, False)

        self.assertEqual(len(books), 0)
    
    def test_unique_citekey_proper_formatting(self):

        self.book_service.save_citation(
            "Pek pekka",
            "pekan seikkailut",
            "20",
            "pekan omakustanne"
        )
        self.book_service.save_citation(
            "Pekpekka",
            "pekan seikkailut",
            "2020",
            "pekan omakustanne"
        )
        for book in self.book_service.get_all():
            for character in book["cite_key"]:
                self.assertEqual(
                    character in string.ascii_letters or character in string.digits,
                    True
                )
        
    def test_unique_really_unique(self):

        self.book_service.save_citation(
            "Pek pekka",
            "pekan seikkailut",
            "20",
            "pekan omakustanne"
        )
        self.book_service.save_citation(
            "Pek pekka",
            "pekan seikkailut",
            "20",
            "pekan omakustanne"
        )
        self.assertNotEqual(
            self.book_service.get_all()[0]["cite_key"],
            self.book_service.get_all()[1]["cite_key"]
        )

    def test_get_last(self):
        self.book_service.save_citation(
            "joku",
            "Teeskentelyä",
            "2022",
            "Paras"
        )
        self.book_service.save_citation(
            "joku",
            "Teeskentelyä",
            "2022",
            "Paras"
        )
        
        book = self.book_service.get_last()
        self.assertEqual(
            book,
            self.book_service.get_all()[-1]
        )

