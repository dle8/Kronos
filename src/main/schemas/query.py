from graphene import ObjectType, List, NonNull, Field, Int, String, UUID
from src.main.schemas.stock import Stock
from src.main.schemas.tag import Tag
from src.main.schemas.snapshot import Snapshot
from src.main.schemas.article import Article


class Query(ObjectType):
    stocks = Field(List(NonNull(Stock)), last=Int())
    tags = Field(List(NonNull(Stock)), last=Int())
    articles = Field(List(NonNull(Article)), last=Int())

    stock = Field(Stock, ticker_symbol=String(required=True))
    tag = Field(Tag, name=String(required=True))
    article = Field(Article, id=UUID(required=True))
    snapshot = Field(Snapshot, id=UUID(required=True))

    # Todo: resolver functions for each query
