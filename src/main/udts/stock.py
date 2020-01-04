import uuid
from src.main import cluster
from cassandra.cqlengine.columns import *


class Stock(object):
    id = UUID(default=uuid.uuid4())
    name = Text(required=True)
    ticker_symbol = Text(required=True)
    price = Integer(required=True)
    percentage_variation = Float(required=True)


cluster.register_user_type('kronos', 'stock', Stock)
