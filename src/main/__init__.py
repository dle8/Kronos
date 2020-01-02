from flask import Flask
from flask_cors import CORS
from src.main.config import Config
from flask_mail import Mail
from cassandra.cluster import Cluster

app = Flask(__name__, template_folder='../../templates')
app.config.from_object(config)


def _register_subpackages():
    pass


mail = Mail()
mail.init_app(app)

cors = CORS()
cors.init_app(app)

# Connect to Cassandra db with 'Kronos' keyspace
cluster = Cluster()
session = cluster.connect('Kronos')

_register_subpackages()
