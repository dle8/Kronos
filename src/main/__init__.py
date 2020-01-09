from flask import Flask
from flask_cors import CORS
from src.main.config import Config
from flask_mail import Mail
from cassandra.cluster import Cluster

app = Flask(__name__, template_folder='../../templates')
app.config.from_object(config)

mail = Mail()
mail.init_app(app)

cors = CORS()
cors.init_app(app)

# Connect to Cassandra db with 'Kronos' keyspace
cluster = Cluster()
session = cluster.connect()
session.execute(
    """
    CREATE KEYSPACE %s WITH replication = {'class': %s, 'replication_factor': %s};
    """,
    (config.KEYSPACE, config.STRATEGY, config.REPLICATION_FACTOR)
)

session.set_keyspace(config.KEYSPACE)

# Get the root query and mutation schemas
import src.main.schemas
from src.main.schemas.query import Query
from graphene import Schema

schema = Schema(query=Query)
# schema = Schema(
#     query=Query,
#     mutation=Mutation,
#     types=[]
#     subscription=Subscription
# )

import src.main.models
import src.main.controllers
