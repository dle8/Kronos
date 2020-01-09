from functools import wraps

import json

data = {}
with open('../stock_data.json') as fi:
    data = json.load(fi)


def fetch_stock(f, **fields):
    @wraps(f)
    def wrapper(*args, **kwargs):
        stock = data[fields['symbol']]
        name = stock.get('Name', None)
        if not name:
            raise Exception('Stock whose symbol is {} does not exist.'.format(fields['symbol']))

        kwargs['stock'] = {
            'symbol': fields['symbol'],
            'name': name
        }
        return f(*args, **kwargs)

    return wrapper


def fetch_stock_all_methods(Cls):
    class NewCls(object):

        def __init__(self, *args, **kwargs):
            self.symbol = kwargs['symbol']
            self.oInstance = Cls(*args, **kwargs)

        def __getattribute__(self, s):
            """
            this is called whenever any attribute of a NewCls object is accessed. This function first tries to
            get the attribute off NewCls. If it fails then it tries to fetch the attribute from self.oInstance (an
            instance of the decorated class). If it manages to fetch the attribute from self.oInstance, and
            the attribute is an instance method then `time_this` is applied.
            """
            try:
                x = super(NewCls, self).__getattribute__(s)
            except AttributeError:
                pass
            else:
                return x
            x = self.oInstance.__getattribute__(s)
            if type(x) == type(self.__init__):  # it is an instance method
                return fetch_stock(x, symbol=self.symbol)
            else:
                return x

    return NewCls
