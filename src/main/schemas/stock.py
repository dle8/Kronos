from graphene import UUID, String, Float, Int, ObjectType
from src.main.schemas.base_schema import ID


class Stock(ObjectType):
    class Meta:
        interfaces = (ID,)

    id = UUID(required=True)
    name = String(required=True)
    ticker_symbol = String(required=True)
    price = Int(required=True)
    percentage_variation = Float(required=True)

    def resolve_id(self, info, **kwargs):
        return self.id

    def resolve_name(self, info, **kwargs):
        return self.name

    def resolve_ticker_symbol(self, info, **kwargs):
        return self.ticker_symbol

    def resolve_price(self, info, **kwargs):
        return self.price

    def resolve_percentage_variation(self, info, **kwargs):
        return self.percentage_variation
