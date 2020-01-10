import yfinance as yf


def fetch_stock_data(symbol, **kwargs):
    stock = yf.Ticker(symbol)
    info = dict(stock.info)
    fields = kwargs.get('fields', None)
    if not fields:
        return info

    return {field: info[field] for field in fields if info.get(field, None)}
