import unittest
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
                "1",
                "Tee",
                "Teeskentelyä",
                "2022",
                "Paras"
            )

        books = self.book_service.get_all()

        self.assertEqual(len(books), 1)

        self.assertEqual(books[0]["id"], "1")
        
        self.assertEqual(re, True)

    def test_does_not_save_incorrect_citation(self):
        re = self.book_service.save_citation(
                None,
                "Tee",
                "Teeskentelyä",
                "2022",
                "Paras"
            )
        
        books = self.book_service.get_all()

        self.assertEqual(re, False)

        self.assertEqual(len(books), 0)
