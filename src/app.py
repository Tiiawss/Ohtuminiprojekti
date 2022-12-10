from flask import Flask  # pylint: disable=wrong-import-order

app = Flask(__name__)
import routes  # pylint: disable=unused-import, wrong-import-position, cyclic-import
# keep routes under flask
