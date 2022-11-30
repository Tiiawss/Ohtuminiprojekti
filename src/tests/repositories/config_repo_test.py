import unittest
from repositories.configuration_repository import ConfigurationRepository

studtoml = """
[Book]
author = ['Kirjailijan nimi', 'True']
name = ['Kirjan nimi', 'True']
year = ['Julkaisuvuosi', 'True']
not_required = ['Ei pakollinen', '']
"""

class TestConfigRepo(unittest.TestCase):
    def setUp(self):
        self.config_repo = ConfigurationRepository(studtoml)

    def test_config_repo_saves_cite_type_correctly(self):
        typ = list(self.config_repo.get_cites().keys)[0]

        self.assertEqual(typ, 'Book')
