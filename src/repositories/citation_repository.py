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
