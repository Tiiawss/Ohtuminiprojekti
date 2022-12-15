from pymongo import MongoClient
from config import MONGO_URL


class CitationRepository:
    """ Repository for saving bookreferences
    """

    def __init__(self, test_environment: bool = False):
        self._client = MongoClient(MONGO_URL)
        if test_environment:
            self._db = self._client["test"]
        else:
            self._db = self._client["production"]

    def move_to_tests(self):
        """ change to test db """
        self._db = self._client["test"]

    def add_citation(self, citation):
        """Save citation

        Args:
            citation
        """
        citations = self._db["citations"]

        try:
            citations.insert_one(citation)
            return True
        except Exception:
            return False

    def delete_all(self):
        """ Delete all citations from db """
        try:
            self._db["citations"].delete_many({})
            return True
        except Exception:
            return False

    def get_last(self):
        """ Get citation with newest date """
        try:
            citation = self._db["citations"].find(
                {}).sort("date", -1).limit(1)[0]
            citation = self.remove_unnecessary_fields(citation)
            return citation
        except Exception:
            return None

    def get_all(self) -> list:
        """Returns all citations

        Returns:
            list: _description_
        """
        cursor = self._db["citations"].find({})
        citations = []
        for citation in cursor:
            citation = self.remove_unnecessary_fields(citation)
            citations.append(citation)
        return citations

    def remove_citation(self, cite_key: str):
        """Removes one citation

        Args:
            cite_key: str

        Returns:
            bool
        """
        deleted_count = 0
        try:
            result = self._db["citations"].delete_one({"cite_key": cite_key})
            deleted_count = result.deleted_count
        except Exception:
            return False

        if deleted_count > 0:
            return True
        return False

    def remove_unnecessary_fields(self, citation):
        """ Remove fields that are not needed in application """
        try:
            citation.pop("_id")
            citation.pop("date")
        except Exception:
            pass
        return citation

    def get_citations_by_tag(self, tag: str) -> list:
        """ Get all citations by a tag
        """

        citations = self.get_citation()
        tag_citations = []
        for citation in citations:
            tags = citation["tagit"].split(',')
            if tag in tags:
                tag_citations.append(citation)

        return tag_citations

    def get_tags(self):
        """ Get all citations """
        citations = self.get_citation()
        all_tags = []
        for citation in citations:
            tags = citation["tagit"].split(',')
            for tag in tags:
                all_tags.append(tag)

        return all_tags


citation_repository = CitationRepository()
