from cassandra.cqlengine.columns import *
from cassandra.cqlengine.models import Model
from cassandra.cqlengine.management import sync_table
from src.main.config import config
from src.main.udts.article import Article


class Snapshot(Model):
    __keyspace__ = config.KEYSPACE
    email = Text(required=True, primary_key=True)
    name = Text(required=True, primary_key=True)
    stock_symbol = Text(required=True)
    start_date = Date(required=True)
    end_date = Date(required=True)
    # Use Article but not Text (like in User Model). Trades off data denormalization for more efficient article fetching
    articles = Set(UserDefinedType(Article))


sync_table(Snapshot)
