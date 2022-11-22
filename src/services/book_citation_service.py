from repositories.book_repository import BookRepository


class bookCitation:
    def __init__(self) -> None:
        self.repo = BookRepository()

    def save_citation(self, id, author, title, year, publisher):

        if id and author and title and year and publisher:
            book = {
            "id": id,
            "author": author,
            "title": title,
            "year": year,
            "publisher": publisher
        }
            self.repo.add_book(book)
    
    def get_all(self):
        return self.repo.get_books()