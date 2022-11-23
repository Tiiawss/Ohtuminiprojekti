import random, string
from repositories.book_repository import book_repository


class BookCitation:
    """ Book Service """
    def __init__(self, bookrepository = book_repository) -> None:
        self.repo = bookrepository

    def _get_unique_cite_key(self, author :str, year :str) -> str:
        """Returns unique citeky based on author and year

        Args:
            author (str): 
            year (str): 

        Returns:
            str: unique citekey
        """
        def get_unique_from(citekey :str):
            """ Appends ascii_letters to citeky until unique

            Returns:
                str: unique citekey
            """
            for book in self.get_all():
                if book['reference'] == citekey:
                    get_unique_from(
                        f"{citekey}{random.choice(string.ascii_lowercase)}"
                    )
            return citekey

        citekey = ""

        for i, character in enumerate(author):
            if i >=6: break
            if character in string.ascii_letters:
                citekey += character

        for i, digit_string, in enumerate(year):
            if i >= 5: break
            if digit_string in string.digits:
                citekey += digit_string

        return get_unique_from(citekey)
         
        

    def save_citation(self, author, title, year, publisher):
        """ Save book to repository """

        if author and title and year and publisher:
            book = {
            "reference": 
                self._get_unique_cite_key(author,year),
            "author": author,
            "title": title,
            "year": year,
            "publisher": publisher
            }
            self.repo.add_book(book)
            return True
        return False

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
    
        

book_service = BookCitation(book_repository)
