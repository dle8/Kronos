from graphene import ObjectType, UUID, Date, List, NonNull
from src.main.schemas.base_schema import ID
from src.main.schemas.article import Article


class Snapshot(ObjectType):
    class Meta:
        interfaces = (ID,)

    id = UUID(required=True)
    start = Date()
    end = Date()
    articles = List(NonNull(Article))

    def resolve_id(self, info, **kwargs):
        return self.id

    def resolve_start(self, info, **kwargs):
        return self.start

    def resolve_end(self, info, **kwargs):
        return self.end

    def resolve_articles(self, info, **kwargs):
        return self.articles
