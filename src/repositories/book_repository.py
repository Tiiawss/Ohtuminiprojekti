class BookRepository:
    """ Repository for saving bookreferences
    """
    def __init__(self):
        self.books = []

    def add_book(self, book):
        """Save book

        Args:
            book
        """
        self.books.append(
            book
        )

    def get_books(self) -> list:
        """Returns all books

        Returns:
            list: _description_
        """
        return self.books
