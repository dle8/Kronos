from src.main import cluster
from cassandra.cqlengine.columns import *
from src.main.udts.article import Article


class Snapshot(object):
    name = Text(required=True)
    start_date = Date()
    end_date = Date()
    articles = List(UserDefinedType(Article))


cluster.register_user_type('kronos', 'snapshot', Snapshot)
