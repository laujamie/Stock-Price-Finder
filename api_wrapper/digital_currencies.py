import requests
import pandas as pd

from .api_request_base import AlphaVantageRequest

class DigitalCurrencies(AlphaVantageRequest):
    """ used to access cryptocurrency API data from AlphaVantage """

    def get_intraday(self, symbol, market):
        self._api_params['symbol'] = symbol
        self._api_params['function'] = 'DIGITAL_CURRENCY_INTRADAY'
        self._api_params['apikey'] = self._api_key
        self._api_params['market'] = market

        return self._get_response()

    def get_daily(self, symbol, market):
        self._api_params['symbol'] = symbol
        self._api_params['function'] = 'DIGITAL_CURRENCY_DAILY'
        self._api_params['apikey'] = self._api_key
        self._api_params['market'] = market

        return self._get_response()
