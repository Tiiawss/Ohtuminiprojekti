from repositories.book_repository import book_repository


class bookCitation:
    def __init__(self, bookrepository = book_repository) -> None:
        self.repo = bookrepository

    def save_citation(self, id, author, title, year, publisher):
        """ Save book to repository """

        if id and author and title and year and publisher:
            book = {
            "id": id,
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
