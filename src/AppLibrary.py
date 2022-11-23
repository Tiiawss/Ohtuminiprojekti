import requests


class AppLibrary:
    def __init__(self) -> None:
        self._base_url = "http://localhost:5000"

    def create_book(self, author, title, year, publisher):
        data = {
            "author": author,
            "title": title,
            "year": year,
            "publisher": publisher
        }
        requests.post(f"{self._base_url}/create", data=data)