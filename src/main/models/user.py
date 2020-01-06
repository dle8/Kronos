from cassandra.cqlengine.columns import *
from cassandra.cqlengine.models import Model
from cassandra.cqlengine.management import sync_table
from src.main.udts import *
from src.main.config import config
import uuid
import requests
import json


class User(Model):
    __keyspace__ = config.KEYSPACE  # CASSANDRA KEYSPACE
    id = UUID(default=uuid.uuid4())
    email = Text(required=True)
    hashed_password = Text(required=True)
    stocks = Set(UserDefinedType(stock))
    tags = Set(UserDefinedType(tag))
    articles = Set(UserDefinedType(article))

    def validate(self):
        super(User, self).validate()
        if self.email:
            api_response = requests.post(
                config.EMAIL_VERIFICATION_URL.format(config.API_KEY, self.email)
            ).content
            api_response = json.loads(api_response)

            if api_response['result'] == 'invalid':
                # raise Exception('Invalid email')
                pass


sync_table(User)
