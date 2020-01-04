from cassandra.cqlengine.columns import *
from cassandra.cqlengine.models import Model
from cassandra.cqlengine.management import sync_table
from src.main.udts import *
from src.main.config import config
import uuid


class User(Model):
    __keyspace__ = config.KEYSPACE  # CASSANDRA KEYSPACE
    id = UUID(default=uuid.uuid4())
    email = Text(required=True)
    hashed_password = Text(required=True)
    stocks = Set(UserDefinedType(stock))
    tags = Set(UserDefinedType(tag))
    articles = Set(UserDefinedType(article))


sync_table(User)
