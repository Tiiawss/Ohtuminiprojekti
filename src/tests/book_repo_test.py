import unittest
from repositories.book_repository import book_repository

class TestBookRepository(unittest.TestCase):
    def setUp(self):
        self.book_repository = book_repository
        self.book_repository.books = []

    def test_new_book_list_is_empty(self):
        self.assertEqual(self.book_repository.books, [])

    def test_add_new_book(self):
        self.book_repository.add_book("book")

        self.assertEqual(len(self.book_repository.books), 1)
        self.assertEqual(self.book_repository.books[0], "book")

    def test_return_books_correctly(self):
        self.book_repository.add_book("book")
        self.book_repository.add_book("book2")

        books = self.book_repository.get_books()

        self.assertEqual(len(books), 2)
        self.assertEqual(books[0], "book")
