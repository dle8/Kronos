from graphene import ObjectType, String, List, NonNull
from src.main.schemas.stock import StockType
from src.main.schemas.tag import TagType
from src.main.utils.fetch_user import fetch_user_all_methods


@fetch_user_all_methods
class UserType(ObjectType):
    email = String(required=True, email=String())
    hashed_password = String()
    stocks = List(NonNull(StockType))
    tags = List(NonNull(TagType))

    def __init__(self, *args, **kwargs):
        pass

    @staticmethod
    def resolve_email(parent, info, **kwargs):
        return parent.email

    @staticmethod
    def resolve_hashed_password(parent, info, **kwargs):
        user = kwargs['user']

        return user.hashed_password

    @staticmethod
    def resolve_stocks(parent, info, **kwargs):
        user = kwargs['user']

        return [StockType(symbol=stock_symbol) for stock_symbol in user.stock_symbols]

    @staticmethod
    def resolve_tags(parent, info, **kwargs):
        user = kwargs['user']

        return [TagType(name=tag_name) for tag_name in user.tag_names]
