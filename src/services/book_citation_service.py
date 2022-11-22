from urllib import request
from flask import requests


class bookCitation:
    def save_citation(self, citation):
        author = request.form["author"]
        title = request.form["title"]
        year = request.form["year"]
        publisher = request.form["publisher"]

        if author and title and year and publisher:
            # Lähetä eteenpäin
            pass
    
    def get_all(self):
        pass