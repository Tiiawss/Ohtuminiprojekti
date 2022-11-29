import toml

class ConfigurationRepository:
    """Luokka, joka hakee sovellusta varten tiedot lähdeviittausten kentistä
    """

    def __init__(self) -> None:
        """Alustaa luokan 
        """

        self._cites = {}
        self.cites_fields()

    def cites_fields(self):
        """Hakee konfiguraatio tiedostosta kaikki viittausmuodot

        Template:
            [Citation type]
            field_id = [UI name, required bool]
            field_id_2 = [UI name, required bool]
            ...
        """

        content = toml.load("cite_types.toml")

        for typ, fields in content.items():
            self._cites[typ] = {}
            for field, values in fields.items():
                self._cites[typ][field] = (values[0], bool(values[1]))

    def get_cites(self):
        return self._cites

configuration_repository = ConfigurationRepository()
