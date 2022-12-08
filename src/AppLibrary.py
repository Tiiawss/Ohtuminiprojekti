
import requests


class AppLibrary:
    def __init__(self) -> None:
        self._base_url = "http://localhost:5000"

    def delete_all_citations(self):
        requests.post(f"{self._base_url}/delete_all")

    def use_test_db(self):
        requests.post(f"{self._base_url}/use_test_db")
