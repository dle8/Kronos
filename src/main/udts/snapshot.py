from src.main import cluster
from cassandra.cqlengine.columns import *
from . import article
from datetime import datetime
import uuid


class Snapshot(object):
    id = UUID(default=uuid.uuid4)
    start = Date(default=datetime.now().date)
    end = Date(default=datetime.now().date)
    articles = List(UserDefinedType(article))


cluster.register_user_type('kronos', 'snapshot', Snapshot)
