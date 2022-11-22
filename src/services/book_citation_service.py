from repositories.book_repository import book_repository


class BookCitation:
    """ Book Service """
    def __init__(self, bookrepository = book_repository) -> None:
        self.repo = bookrepository

    def save_citation(self, bookid, author, title, year, publisher):
        """ Save book to repository """

        if bookid and author and title and year and publisher:
            book = {
            "id": bookid,
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
