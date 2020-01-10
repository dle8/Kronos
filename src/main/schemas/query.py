from graphene import ObjectType, List, NonNull, Field, Int, String
from src.main.schemas.stock import StockType
from src.main.schemas.user import UserType

from flask import session


class Query(ObjectType):
    stocks = Field(List(NonNull(StockType)), first=Int(), offset=Int(), symbol=String(required=True))
    user = Field(String, email=String(required=True))

    @staticmethod
    def resolve_user(parent, info, **kwargs):
        # Todo: Add email to JWT
        if session['email'] != kwargs['email']:
            raise Exception('Invalid user email.')

        return UserType(email=kwargs['email'])

    @staticmethod
    def resolve_stocks(parent, info, **kwargs):
        if kwargs.get('symbol', None):
            return [StockType(symbol=kwargs['symbol'])]

        # Todo: Use memcached for most recent searched stocks, here is just hardcoding
        return [StockType(symbol=symbol) for symbol in ['AAPL', 'FB', 'MSFT', 'GOOGL', 'AMZN']]
