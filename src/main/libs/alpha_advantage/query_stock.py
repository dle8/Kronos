from src.main.config import config
import requests


def fetch_stock_prices(symbol='MSFT'):
    response = requests.get(
        config.ALPHA_ADVANTAGE_TIME_SERIES_INTRADAY_API.format(
            symbol,
            '1min',
            'full',
            config.ALPHA_ADVANTAGE_API_KEY
        )
    ).content.decode('utf-8')
    return response['Time Series (1min)']
