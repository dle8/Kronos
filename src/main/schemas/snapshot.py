from graphene import ObjectType, Date, List, NonNull, String
from src.main.schemas.article import ArticleType


class SnapshotType(ObjectType):
    name = String(required=True)
    start_date = Date()
    end_date = Date()
    articles = List(NonNull(ArticleType))

    def __init__(self, *args, **kwargs):
        pass

    @staticmethod
    def resolve_name(parent, info, **kwargs):
        snapshot = kwargs['snapshot']

        return snapshot['name']

    @staticmethod
    def resolve_start_date(parent, info, **kwargs):
        snapshot = kwargs['snapshot']

        return snapshot['start_date']

    @staticmethod
    def resolve_end_date(parent, info, **kwargs):
        snapshot = kwargs['snapshot']

        return snapshot['end_date']

    @staticmethod
    def resolve_articles(parent, info, **kwargs):
        snapshot = kwargs['snapshot']

        return snapshot.article
