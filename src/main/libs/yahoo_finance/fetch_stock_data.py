import yfinance as yf


def fetch_stock_data(symbol, fields=None, **kwargs):
    """
    Fetch historical stock data from Yahoo Finance API
    :param symbol: Stock symbol
    :param fields: A list of fields needed to be extracted from Yahoo Finance response.
                   Return the whole information if this is None.
    :Sample: fetch_stock_data(symbol='MSFT', fields=['sector', 'zip', 'shortName'])
    """
    stock_ticker = yf.Ticker(symbol)
    stock_info = dict(stock_ticker.info)
    if not fields:
        return stock_info

    return {field: stock_info[field] for field in fields if stock_info.get(field, None)}
