from src.main import cluster
from cassandra.cqlengine.columns import *
from . import article


class Tag(object):
    name = Text(required=True)
    articles = List(UserDefinedType(article))


cluster.register_user_type('kronos', 'tag', Tag)
