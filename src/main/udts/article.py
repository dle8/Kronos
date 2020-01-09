from src.main import cluster
from cassandra.cqlengine.columns import *
from cassandra.cqlengine.usertype import UserType
import uuid


class Article(UserType):
    url = Text(required=True)
    thumbnail = Text(required=True)
    title = Text(required=True)
    snippet = Text(required=True)


cluster.register_user_type('kronos', 'article', Article)
