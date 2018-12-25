import requests
import pandas as pd

from .exceptions import MissingApiKey

class AlphaVantageRequest(object):
    _api_url = 'https://www.alphavantage.co/query'

    def __init__(self, api_key):
        self._api_params = {}
        self._api_key = api_key

    def __init__(self):
        self._api_params = {}
        self._api_key = None

    def set_api_key(self, api_key):
        self._api_key = api_key

    def _get_response(self):
        if self._api_key is None or not self._api_key:
            raise MissingApiKey
        resp = requests.get(url=self._api_url, params=self._api_params)
        resp_data = resp.json()
        data = {}

        for key, val in resp_data.items():
            if 'Error' in key:
                return resp_data
            if 'Information' in key:
                return resp_data
            if 'Time Series' in key:
                data = val
                break

        self._api_params = {}

        stock_data = pd.DataFrame.from_dict(data, dtype=float)
        stock_data = stock_data.iloc[:, ::-1]
        return stock_data
        
