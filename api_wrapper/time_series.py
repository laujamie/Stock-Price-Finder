import requests
import pandas as pd

class TimeSeries(object):
    def __init__(self, api_key):
        self._api_url = 'https://www.alphavantage.co/query'
        self._api_params = {}
        self._api_key = api_key

    def _get_response(self):
        """ general function to perform api requests """
        resp = requests.get(url=self._api_url, params=self._api_params)
        resp_data = resp.json()
        data = {}

        for key, val in resp_data.items():
            if 'Error' in key:
                return resp_data
            if 'Time Series' in key:
                data = val
                break

        self._api_params = {}
        
        stock_data = pd.DataFrame.from_dict(data, dtype=float)
        stock_data = stock_data.iloc[:, ::-1]
        return stock_data

    def get_daily(self, symbol, output_size='compact'):
        self._api_params['function'] = 'TIME_SERIES_DAILY'
        self._api_params['symbol'] = symbol
        self._api_params['outputsize'] = output_size
        self._api_params = self._api_key
        return self._get_response()

    def get_daily_adjusted(self, symbol, output_size='compact'):
        self._api_params['function'] = 'TIME_SERIES_DAILY_ADJUSTED'
        self._api_params['symbol'] = symbol
        self._api_params['outputsize'] = output_size
        self._api_params = self._api_key
        return self._get_response()

    def get_weekly(self, symbol, output_size='compact'):
        self._api_params['function'] = 'TIME_SERIES_WEEKLY'
        self._api_params['symbol'] = symbol
        self._api_params['outputsize'] = output_size
        self._api_params = self._api_key
        return self._get_response()

    def get_weekly_adjusted(self, symbol, output='compact'):
        self._api_params['function'] = 'TIME_SERIES_WEEKLY_ADJUSTED'
        self._api_params['symbol'] = symbol
        self._api_params['outputsize'] = output_size
        self._api_params = self._api_key
        return self._get_response()

    def get_monthly(self, symbol, output_size='compact'):
        self._api_params['function'] = 'TIME_SERIES_MONTHLY'
        self._api_params['symbol'] = symbol
        self._api_params['outputsize'] = output_size
        self._api_params = self._api_key
        return self._get_response()

    def get_monthly_adjusted(self, symbol, output_size='compact'):
        self._api_params['function'] = 'TIME_SERIES_MONTHLY_ADJUSTED'
        self._api_params['symbol'] = symbol
        self._api_params['outputsize'] = output_size
        self._api_params = self._api_key
        return self._get_response()

    def get_intraday(self, symbol, interval, output_size='compact'):
        self._api_params['function'] = 'TIME_SERIES_INTRADAY'
        self._api_params['symbol'] = symbol
        self._api_params['interval'] = interval
        self._api_params['outputsize'] = output_size
        self._api_params = self._api_key
        return self._get_response()
