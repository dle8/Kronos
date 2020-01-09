from graphene import String, Int, ObjectType, List, NonNull, Date
from src.main.libs.alpha_advantage.query_stock import fetch_stock_prices
from src.main.schemas.article import ArticleType
from src.main.libs.google_search.fetch_article_metadata import fetch_url_metadata
from src.main.utils.fetch_stock import fetch_stock_all_methods

from datetime import datetime


@fetch_stock_all_methods
class StockType(ObjectType):
    name = String(required=True)
    symbol = String(required=True, symbol=String())  # Index in Cassandra
    price = Int()
    articles = List(
        NonNull(ArticleType),
        start_date=Date(),
        end_data=Date(default_value=datetime.now().date()),
        start=Int(default_value=1)
    )  # start for pagination

    @staticmethod
    def resolve_name(parent, info, **kwargs):
        return kwargs['name']

    @staticmethod
    def resolve_symbol(parent, info, **kwargs):
        return kwargs['symbol']

    # Query stock intra day price for each 1 min
    @staticmethod
    def resolve_price(parent, info, **kwargs):
        prices = fetch_stock_prices(kwargs['symbol'])
        list_prices = list(prices.items())
        price = list_prices[0][1]['4. close']

        return price

    @staticmethod
    def resolve_articles(parent, info, **kwargs):
        # Todo: Try different search term & use NLP to pick out the best
        time_range = 'date:r:'
        if kwargs.get('start_date', None):
            time_range += str(kwargs['start_date'])
        time_range += ':' + kwargs['end_date']

        articles = fetch_url_metadata(
            kwargs['name'] + ' market news',
            start=kwargs['start'],
            sort=time_range
        )

        return [ArticleType(article=article) for article in articles]
