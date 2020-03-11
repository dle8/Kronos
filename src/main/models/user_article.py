from cassandra.cqlengine import connection
from cassandra.cqlengine.models import Model
from cassandra.cqlengine.management import sync_table
from cassandra.cqlengine.columns import *
from src.main.config import config


class UserArticle(Model):
    __keyspace__ = config.KEYSPACE
    email = Text(required=True, primary_key=True)
    tag_name = Text(required=True, primary_key=True)
    urls = Set(Text)


connection.setup(['127.0.0.1'], "kronos", protocol_version=3)
sync_table(UserArticle)
