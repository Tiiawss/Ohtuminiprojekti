from services.book_citation_service import book_service as default_book_service


class BibTexService:
    """Class which is responsible for turning citations to bibtex
    """

    def __init__(self, book_service=default_book_service):
        """ Initialize the Service for use

        Args:
            book_service: The service for book citations
        """

        self.book_service = book_service
        self.bibtex = []

    def turn_books_to_bibtex(self):
        """Turns book citations to bibtex
        """

        books = self.book_service.get_all()

        for book in books:
            citekey = "@Book{" + book["cite_key"] + ","
            author = f'{"author"} = "{book["author"]}",'
            title = 'title = "' + book["title"] + '",'
            year = 'year = "' + book["year"] + '",'
            publisher = 'publisher = "' + book["publisher"] + '"'
            book_dict = {
                "Citekey": citekey,
                "Author": author,
                "Title": title,
                "Year": year,
                "Publisher": publisher,
                "Last": "}"
            }

            self.bibtex.append(book_dict)

    def get_bibtex(self):
        """Returns the bibtex formatted citations

        Returns:
            _description_
        """
        return self.bibtex
