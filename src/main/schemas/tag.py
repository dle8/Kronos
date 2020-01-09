from graphene import ObjectType, String, List, NonNull
from src.main.schemas.article import ArticleType
from src.main.models.user_article import UserArticle


class TagType(ObjectType):
    name = String(required=True, name=String())
    articles = List(NonNull(ArticleType))

    @staticmethod
    def resolve_name(parent, info, **kwargs):
        return parent.name

    # Remember to pass email into to fetch a certain user's articles
    @staticmethod
    def resolve_articles(parent, info, **kwargs):
        # Todo: Allowing query for a certain article with certain url
        article_urls = UserArticle.objects.filter(
            email=kwargs['email'],
            tag_name=parent.name
        ).first().urls

        return [ArticleType(url=article_url) for article_url in article_urls]
