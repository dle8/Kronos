from cassandra.cqlengine import connection
from cassandra.cqlengine.columns import *
from cassandra.cqlengine.models import Model
from cassandra.cqlengine.management import sync_table
from src.main.config import config
from src.main.libs.neverbounce.verify_email import validate_email


class User(Model):
    __keyspace__ = config.KEYSPACE
    email = Text(required=True, primary_key=True)
    hashed_password = Text(required=True)
    stock_symbols = Set(Text)
    tag_names = Set(Text)
    article_urls = Set(Text)
    snapshot_names = Set(Text)

    def validate(self):
        super(User, self).validate()
        if self.email:
            validate_email(self.email)


connection.setup(['127.0.0.1'], "kronos", protocol_version=3)
sync_table(User)
