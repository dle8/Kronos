from graphene import ObjectType, String
from src.main.utils.fetch_article import fetch_article_all_methods


@fetch_article_all_methods
class ArticleType(ObjectType):
    url = String(required=True, url=String())
    thumbnail = String(required=True)
    title = String(required=True)
    snippet = String(required=True)

    def __init__(self, *args, **kwargs):
        pass

    @staticmethod
    def resolve_url(parent, info, **kwargs):
        return parent.url

    @staticmethod
    def resolve_thumbnail(parent, info, **kwargs):
        article = kwargs['article']

        return article.thumbnail

    @staticmethod
    def resolve_title(parent, info, **kwargs):
        article = kwargs['article']

        return article.title

    @staticmethod
    def resolve_snippet(parent, info, **kwargs):
        article = kwargs['article']

        return article.snippet

    @staticmethod
    def resolve_date_published(parent, info, **kwargs):
        article = kwargs['article']

        return article.date_published
