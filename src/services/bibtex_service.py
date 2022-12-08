from services.citation_service import citation_service as default_citation_service


class BibTexService:
    """Class which is responsible for turning citations to bibtex
    """

    def __init__(self, citation_service=default_citation_service):
        """ Initialize the Service for use

        Args:
            citation_service: The service for citations
        """

        self.citation_service = citation_service
        self.bibtex = []

    def _replace_scandic_letters(self, word):
        letters = {"ö": '{\\"{o}}', "Ö": '{\\"{O}}', "ä": '{\\"{a}}',
                   "Ä": '{\\"{A}}', "å": '{\\r{a}}', "Å": '{\\r{A}}'}
        for key, value in letters.items():
            word = word.replace(key, value)
        return word

    def turn_cites_to_bibtex(self):
        """Turns citations to bibtex
        """

        cites = self.citation_service.get_all()

        for cite in cites:
            cite_list = []
            first_row = '@' + cite['type'] + '{' + cite['cite_key'] + ','
            cite_list.append(first_row)
            for key, value in cite.items():
                if key in ['type', 'cite_key', 'tagit']:
                    continue
                value = self._replace_scandic_letters(value)
                row = f'    {key} = "{value}",'
                cite_list.append(row)
            cite_list[-1] = cite_list[-1][:-1]
            cite_list.append('}')

            self.bibtex.append(cite_list)

    def get_bibtex(self):
        """Returns the bibtex formatted citations

        Returns:
            _description_
        """

        return self.bibtex
