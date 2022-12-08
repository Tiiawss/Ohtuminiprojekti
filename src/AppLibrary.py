
import requests


class AppLibrary:
    """ For robot tests """
    def __init__(self) -> None:
        self._base_url = "http://localhost:5000"

    def delete_all_citations(self):
        """ Delete all citations form db """
        requests.post(f"{self._base_url}/delete_all")

    def use_test_db(self):
        """ Use test db """
        requests.post(f"{self._base_url}/use_test_db")
