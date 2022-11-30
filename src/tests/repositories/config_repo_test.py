import unittest
import os
from repositories.configuration_repository import ConfigurationRepository


class TestConfigRepo(unittest.TestCase):
    def setUp(self):
        dirname = os.path.dirname(__file__)
        file = os.path.join(dirname, 'toml', 'test.toml')
        self.config_repo = ConfigurationRepository(file)

    def test_config_repo_saves_cite_type_correctly(self):
        typ = list(self.config_repo.get_cites().keys())[0]

        self.assertEqual(typ, 'Book')

    def test_config_repo_saves_correct_amount_of_cite_types(self):
        typ = list(self.config_repo.get_cites().keys())

        self.assertEqual(len(typ), 2)

    def test_config_repo_saves_correct_amount_of_cite_fields(self):
        typ = list(self.config_repo.get_cites().keys())[0]
        cites = self.config_repo.get_cites()
        fields = cites[typ]

        self.assertEqual(len(fields), 4)

    def test_config_repo_saves_required_fields_with_true(self):
        typ = list(self.config_repo.get_cites().keys())[0]
        cites = self.config_repo.get_cites()
        req = []
        for field, values in cites[typ].items():
            if values[1]:
                req.append(values[0])

        self.assertEqual(len(req), 3)
