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

    def remove_book(self, id: str):
        """Removes one book"""
        index_to_remove = -1
        for index, element in enumerate(self.books):
            if element["reference"] == id:
                index_to_remove = index
        if index_to_remove != -1:
            self.books.pop(index_to_remove)
            return True
        return False

book_repository = BookRepository()
