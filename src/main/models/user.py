from cassandra.cqlengine.columns import *
from cassandra.cqlengine.models import Model
from cassandra.cqlengine.management import sync_table
from src.main.udts.tag import Tag
from src.main.udts.article import Article
from src.main.config import config
from src.main.libs.neverbounce.verify_email import validate_email


class User(Model):
    __keyspace__ = config.KEYSPACE
    email = Text(required=True, primary_key=True)
    hashed_password = Text(required=True)
    stock_symbols = Set(Text)
    tag_names = Set(UserDefinedType(Tag))
    article_urls = Set(UserDefinedType(Article))

    def validate(self):
        super(User, self).validate()
        if self.email:
            validate_email(self.email)


sync_table(User)
