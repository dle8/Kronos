from src.main.config import config
import requests
import json


def fetch_stock_current_data(symbol='MSFT', interval='5min', outputsize='compact', **kwargs):
    """
    Fetch real time stock price from Alpha Vantage API.
    :param symbol: Stock symbol
    :param interval: Time interval between two consecutive data points in the time series.
                     The following values are supported: 1min, 5min, 15min, 30min, 60min
    :param outputsize: Strings compact and full are accepted with the following specifications:
                       compact returns only the latest 100 data points in the intraday time series;
                       full returns the full-length intraday time series.
    """

    response = requests.get(
        config.ALPHA_ADVANTAGE_TIME_SERIES_INTRADAY_API.format(
            symbol,
            interval,
            outputsize,
            config.ALPHA_ADVANTAGE_API_KEY
        )
    ).content.decode('utf-8')
    response = json.loads(response)
    return response['Time Series ({})'.format(interval)]
