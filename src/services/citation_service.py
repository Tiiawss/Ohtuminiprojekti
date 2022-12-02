import random
import string
from repositories.citation_repository import citation_repository


class CitationService:
    """ Citation Service """

    def __init__(self, citationrepository=citation_repository) -> None:
        self.repo = citationrepository

    def _get_unique_cite_key(self, author: str, year: str) -> str:
        """ Returns unique citeky based on author and year

        Args:
            author (str):
            year (str):

        Returns:
            str: unique citekey
        """

        def get_unique_from(citekey: str):
            """ Appends ascii_letters to citeky until unique

            Returns:
                str: unique citekey
            """
            for citation in self.get_all():
                if citation['cite_key'] == citekey:
                    return get_unique_from(
                        f"{citekey}{random.choice(string.ascii_lowercase)}"
                    )
            return citekey

        citekey = ""

        for i, character in enumerate(author):
            if i >= 6:
                break
            if character in string.ascii_letters:
                citekey += character

        for i, digit_string in enumerate(year):
            if i >= 5:
                break
            if digit_string in string.digits:
                citekey += digit_string

        return get_unique_from(citekey)

    def save_citation(self, field_keys_values: list) -> bool:
        """

        Args:
            field_keys_values (list): list of tuples

        Returns:
            bool: true for success
        """
        citation_to_save = {}
        for key, value in field_keys_values:

            # If string contains only white space characters
            if value.strip() == "":
                return False

            citation_to_save[key] = value

        cite_key_author = "no_author"
        if citation_to_save.get("author"):
            cite_key_author = citation_to_save["author"]

        cite_key_year = "420"
        if citation_to_save.get("year"):
            cite_key_year = citation_to_save["year"]

        citation_to_save['cite_key'] = self._get_unique_cite_key(
            cite_key_author,
            cite_key_year
        )

        self.repo.add_citation(citation_to_save)
        return True

    def get_all(self):
        """ Return list of all citations """
        return self.repo.get_citation()

    def get_last(self):
        """ Return last element of citations
        """
        citations = self.repo.get_citation()
        if len(citations) > 0:
            return citations[-1]
        return None

    def remove_citation(self, cite_key: str) -> bool:
        """Remove citation. True for success false for fail.

        Args:
            id (str):

        Returns:
            bool:
        """

        return self.repo.remove_citation(cite_key)


citation_service = CitationService(citation_repository)
