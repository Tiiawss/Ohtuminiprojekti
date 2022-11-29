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

    def remove_book(self, cite_key: str):
        """Removes one book"""
        index_to_remove = -1
        for index, element in enumerate(self.books):
            if element["cite_key"] == cite_key:
                index_to_remove = index
        if index_to_remove != -1:
            self.books.pop(index_to_remove)
            return True
        return False

book_repository = BookRepository()
