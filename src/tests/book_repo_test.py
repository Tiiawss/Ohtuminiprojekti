import unittest
from repositories.book_repository import book_repository

class TestBookRepository(unittest):
    def __init__(self):
        self.book_repository = book_repository

    def test_new_book_list_is_empty(self):
        self.assertEqual(self.book_repository.books, [])

