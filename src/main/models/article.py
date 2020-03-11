from cassandra.cqlengine import connection
from cassandra.cqlengine.models import Model
from cassandra.cqlengine.columns import *
from cassandra.cqlengine.management import sync_table
from src.main.config import config


class Article(Model):
    __keyspace__ = config.KEYSPACE
    url = Text(required=True, primary_key=True)
    thumbnail = Text(required=True)
    title = Text(required=True)
    snippet = Text(required=True)
    date_published = Date(required=True)


connection.setup(['127.0.0.1'], "kronos", protocol_version=3)
sync_table(Article)
