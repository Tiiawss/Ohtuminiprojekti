import toml
from config import TOML_FILENAME


class ConfigurationRepository:
    """Luokka, joka hakee sovellusta varten tiedot lähdeviittausten kentistä
    """

    def __init__(self, toml_file=TOML_FILENAME) -> None:
        """Alustaa luokan
        """

        self._cites = {}
        self.cites_fields(toml_file)

    def cites_fields(self, file: str) -> None:
        """Hakee konfiguraatio tiedostosta kaikki viittausmuodot

        Template:
            [Citation type]
            field_id = [UI name, required bool]
            field_id_2 = [UI name, required bool]
            ...
        """

        content = toml.load(file)

        for typ, fields in content.items():
            self._cites[typ] = {}
            for field, values in fields.items():
                field_name = values[0]
                boolean = values[1] == "True"
                self._cites[typ][field] = (field_name, boolean)

    def get_cites(self) -> dict:
        """Palauta lähdeviittaus tyypit
        """

        return self._cites

    def get_cite_types(self):
        
        cite_types = []

        for keys in self.get_cites():
            cite_types.append(keys)
        
        return cite_types

    def get_fields(self, typ):
        cites = self.get_cites()
        required_fields = []
        optional_fields = []

        for key, value in cites[typ].items():
            if value[1]:
                required_fields.append((key, value[0]))
            else:
                optional_fields.append((key, value[0]))

        return required_fields, optional_fields

configuration_repository = ConfigurationRepository()
