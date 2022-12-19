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

    def test_get_cite_types(self):
        for cite_type in self.config_repo.get_cite_types():
            self.assertEqual(
                cite_type in ['Book', 'Misc', 'Article'],
                True
            )

    def test_get_fields_with_article(self):
        required_fields, optional_fields = self.config_repo.get_fields(
            'Book')
        req_fields_for_check = [("author", 'Kirjailijan nimi'),
                                ("name", 'Kirjan nimi'),
                                ("year", 'Julkaisuvuosi'),
                                ("not_required", 'Ei pakollinen'),
                                ]
        for required_field in required_fields:
            self.assertEqual(
                required_field in req_fields_for_check,
                True
            )

        self.assertEqual(
            optional_fields[0],
            ('not_required', 'Ei pakollinen')
        )
