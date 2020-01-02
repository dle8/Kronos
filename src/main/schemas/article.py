from graphene import ObjectType, UUID, String
from src.main.schemas.base_schema import ID


class Article(ObjectType):
    class Meta:
        interfaces = (ID,)

    id = UUID(required=True)
    url = String(required=True)
    thumbnail = String(required=True)
    title = String(required=True)
    snippet = String(required=True)

    def resolve_id(self, info, **kwargs):
        return self.id

    def resolve_url(self, info, **kwargs):
        return self.url

    def resolve_thumbnail(self, info, **kwargs):
        return self.thumbnail

    def resolve_title(self, info, **kwargs):
        return self.title

    def resolve_snippte(self, info, **kwargs):
        return self.snippet
