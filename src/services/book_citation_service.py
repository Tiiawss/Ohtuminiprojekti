import random
import string
from repositories.book_repository import book_repository


class BookCitation:
    """ Book Service """

    def __init__(self, bookrepository=book_repository) -> None:
        self.repo = bookrepository

    def _get_unique_cite_key(self, author: str, year: str) -> str:
        """ Returns unique citeky based on author and year

        Args:
            author (str):
            year (str):

        Returns:
            str: unique citekey
        """

        def get_unique_from(citekey: str):
            """ Appends ascii_letters to citeky until unique

            Returns:
                str: unique citekey
            """
            for book in self.get_all():
                if book['cite_key'] == citekey:
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
        """

        Args:
            field_keys_values (list): list of tuples

        Returns:
            bool: true for success
        """
        book_to_save = {}
        for key, value in field_keys_values:

            # If string contains only white space characters
            if value.strip() == "":
                return False

            book_to_save[key] = value

        cite_key_author = "no_author"
        if book_to_save.get("author"):
            cite_key_author = book_to_save["author"]

        cite_key_year = "420"
        if book_to_save.get("year"):
            cite_key_year = book_to_save["year"]

        book_to_save['cite_key'] = self._get_unique_cite_key(
            cite_key_author,
            cite_key_year
        )

        self.repo.add_book(book_to_save)
        return True

    def get_all(self):
        """ Return list of all books """
        return self.repo.get_books()

    def get_last(self):
        """ Return last element of books
        """
        books = self.repo.get_books()
        if len(books) > 0:
            return books[-1]
        return None

    def remove_citation(self, cite_key: str) -> bool:
        """Remove citation. True for success false for fail.

        Args:
            id (str):

        Returns:
            bool:
        """

        return self.repo.remove_book(cite_key)


book_service = BookCitation(book_repository)
