from graphene import String, Float, Int, ObjectType, Field
from src.main.libs.alpha_advantage.query_stock import fetch_stock_prices
from . import data


class Stock(ObjectType):
    name = String(required=True)
    symbol = String(required=True, symbol=String())  # Index in Cassandra
    price = Int()
    price_difference = Float()

    @staticmethod
    def resolve_name(parent, info, **kwargs):
        stock = data[parent.symbol]
        name = stock.get('Name', None)
        if not name:
            raise Exception('Stock whose symbol is {} does not exist.'.format(parent.symbol))
        return name

    @staticmethod
    def resolve_symbol(parent, info, **kwargs):
        return parent.symbol

    # Query stock intra day price for each 1 min
    @staticmethod
    def resolve_price(parent, info, **kwargs):
        prices = fetch_stock_prices(parent.symbol)
        list_prices = list(prices.items())
        price = list_prices[0][1]['4. close']

        return price

    @staticmethod
    def resolve_price_difference(parent, info, **kwargs):
        prices = fetch_stock_prices(parent.symbol)
        last_close_price = prices[0]['4. close']

        price_difference = 0
        for i in range(len(prices) - 1):
            nearest_trade_time = prices[i][0].split(' ')[0]
            previous_trade_time = prices[i + 1][0].split(' ')[0]
            if previous_trade_time != nearest_trade_time:
                price_difference = prices[i + 1][1]['4. close'] - last_close_price
                break

        return price_difference
