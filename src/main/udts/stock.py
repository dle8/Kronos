from src.main import cluster
from cassandra.cqlengine.columns import *


class Stock(object):
    name = Text(required=True)
    symbol = Text(required=True)


cluster.register_user_type('kronos', 'stock', Stock)
