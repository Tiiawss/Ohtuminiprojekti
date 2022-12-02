class CitationRepository:
    """ Repository for saving bookreferences
    """

    def __init__(self):
        self.citations = []

    def add_citation(self, citation):
        """Save citation

        Args:
            citation
        """
        self.citations.append(
            citation
        )

    def get_citation(self) -> list:
        """Returns all citations

        Returns:
            list: _description_
        """
        return self.citations

    def remove_citation(self, cite_key: str):
        """Removes one citation"""
        index_to_remove = -1
        for index, element in enumerate(self.citations):
            if element["cite_key"] == cite_key:
                index_to_remove = index
        if index_to_remove != -1:
            self.citations.pop(index_to_remove)
            return True
        return False


citation_repository = CitationRepository()
# from pymongo import MongoClient
# from config import MONGO_URL


# class CitationRepository:
#     """ Repository for saving bookreferences
#     """

#     def __init__(self):
#         self.citations = []
#         client = MongoClient(MONGO_URL)
#         if True:
#             self._db = client["test"]
#         else:
#             self._db = client["production"]

#     def add_citation(self, citation):
#         """Save citation

#         Args:
#             citation
#         """
#         citations = self._db["citations"]
#         citations.insert_one(citation)

#     def get_citation(self) -> list:
#         """Returns all citations

#         Returns:
#             list: _description_
#         """
#         cursor = self._db["citations"].find({})
#         citations = []
#         for citation in cursor:
#             citation.pop("_id")
#             citations.append(citation)
#         return citations

#     def remove_citation(self, cite_key: str):
#         """Removes one citation"""
#         index_to_remove = -1
#         for index, element in enumerate(self.citations):
#             if element["cite_key"] == cite_key:
#                 index_to_remove = index
#         if index_to_remove != -1:
#             self.citations.pop(index_to_remove)
#             return True
#         return False

# citation_repository = CitationRepository()
