import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, '.env'))
    load_dotenv(dotenv_path=os.path.join(dirname, 'secrets.env'))
except FileNotFoundError:
    pass

if os.path.exists(os.getenv("TOMLCONFIG")):
    TOML_FILENAME = os.getenv('TOMLCONFIG')
else:
    TOML_FILENAME = dotenv_path=os.path.join('src', os.getenv('TOMLCONFIG'))

MONGO_URL = os.getenv('MONGO_URL')
