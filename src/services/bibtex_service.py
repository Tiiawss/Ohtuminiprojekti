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

    def turn_cites_to_bibtex(self):
        """Turns book citations to bibtex
        """

        cites = self.book_service.get_all()

        print(cites)
        for cite in cites:
            cite_list = []
            first_row = '@' + cite['type'] + '{' + cite['cite_key'] + ','
            cite_list.append(first_row)
            lenght = len(cite.keys()) - 1
            i = 1
            for key, value in cite.items():
                if key in ['type', 'cite_key']:
                    continue
                i += 1
                if i == lenght:
                    break
                row = f'    {key} = {value},'
                cite_list.append(row)
            row_values = list(cite.items())[-2]
            row = f'    {row_values[0]} = {row_values[1]}'
            cite_list.append(row)
            cite_list.append('}')

            # book_dict = {
            #    "Citekey": citekey,
            #    "Author": author,
            #    "Title": title,
            #    "Year": year,
            #    "Publisher": publisher,
            #    "Last": "}"
            # }

            self.bibtex.append(cite_list)

    def get_bibtex(self):
        """Returns the bibtex formatted citations

        Returns:
            _description_
        """
        return self.bibtex
