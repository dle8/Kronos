from src.main import cluster, session
from cassandra.cqlengine.columns import *
from src.main.udts.article import Article

session.execute(
    """CREATE TYPE IF NOT EXISTS snapshot (name text, start_date date, end_date date, articles list<frozen<article>>);""")


class Snapshot(object):
    name = Text(required=True)
    start_date = Date()
    end_date = Date()
    articles = List(UserDefinedType(Article))


cluster.register_user_type('kronos', 'snapshot', Snapshot)
