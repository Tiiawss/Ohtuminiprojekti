import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, '.env'))
    load_dotenv(dotenv_path=os.path.join(dirname, 'secrets.env'))
except FileNotFoundError:
    pass

TOML_FILENAME = os.getenv('TOMLCONFIG') or 'cite_types.toml'


MONGO_URL = os.getenv('MONGO_URL')
