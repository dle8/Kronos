from src.main import cluster, session
from cassandra.cqlengine.columns import *
from cassandra.cqlengine.usertype import UserType

session.execute("""CREATE TYPE IF NOT EXISTS article (url text, thumbnail text, title text, snippet text);""")


class Article(UserType):
    url = Text(required=True)
    thumbnail = Text(required=True)
    title = Text(required=True)
    snippet = Text(required=True)


cluster.register_user_type('kronos', 'article', Article)
