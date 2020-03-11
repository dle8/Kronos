from functools import wraps
from src.main.libs.yahoo_finance.fetch_stock_data import fetch_stock_historical_data
from inspect import getattr_static

import json
data = {}
with open('./utils/stock_data.json') as fi:
    data = json.load(fi)


def fetch_stock(f, **fields):
    @wraps(f)
    def wrapper(*args, **kwargs):
        kwargs['stock'] = fields['stock']

        return f(*args, **kwargs)

    return wrapper


def fetch_stock_all_methods(Cls):
    class NewCls(object):

        def __init__(self, *args, **kwargs):
            # Query in JSON field
            stock = data[kwargs['symbol']]
            name = stock.get('Name', None)
            if not name:
                stock_data = fetch_stock_historical_data(kwargs['symbol'], fields=['longName'])
                name = stock_data['name']
            self.stock = {
                'symbol': kwargs['symbol'],
                'name': name
            }
            self.oInstance = Cls(*args, **kwargs)

        def __getattribute__(self, s):
            try:
                x = super(NewCls, self).__getattribute__(s)
            except AttributeError:
                pass
            else:
                return x
            x = self.oInstance.__getattribute__(s)
            if isinstance(getattr_static(Cls, s), staticmethod):
                return fetch_stock(x, stock=self.stock)
            else:
                return x

    return NewCls
