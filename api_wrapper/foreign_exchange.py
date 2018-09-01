import requests

from .api_request_base import AlphaVantageRequest

class Forex(AlphaVantageRequest):
    """ used to get Forex data from Alpha Vantage API. """

    def get_exchange_rate(self, from_cur, to_cur):
        self._api_params['function'] = 'CURRENCY_EXCHANGE RATE'
        self._api_params['from_currency'] = from_cur
        self._api_params['to_currency'] = to_cur
        self._api_params['apikey'] = self._api_key

        resp =  requests.get(self._api_url)
        return resp.json()

    def get_intraday(self, from_sym, to_sym, interval, outputsize='compact'):
        self._api_params['function'] = 'FX_INTRADAY'
        self._api_params['from_symbol'] = from_sym
        self._api_params['to_symbol'] = to_sym
        self._api_params['interval'] = interval
        self._api_params['outputsize'] = outputsize
        self._api_params['apikey'] = self._api_key

        return self._get_response()
