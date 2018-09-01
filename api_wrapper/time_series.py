from .api_request_base import AlphaVantageRequest

class TimeSeries(AlphaVantageRequest):
    """ object to access global stock data from the AlphaVantage API """

    def get_daily(self, symbol, output_size='compact'):
        """ get daily data from api """
        self._api_params['function'] = 'TIME_SERIES_DAILY'
        self._api_params['symbol'] = symbol
        self._api_params['outputsize'] = output_size
        self._api_params = self._api_key
        return self._get_response()

    def get_daily_adjusted(self, symbol, output_size='compact'):
        """ get daily adjusted data from api """
        self._api_params['function'] = 'TIME_SERIES_DAILY_ADJUSTED'
        self._api_params['symbol'] = symbol
        self._api_params['outputsize'] = output_size
        self._api_params = self._api_key
        return self._get_response()

    def get_weekly(self, symbol, output_size='compact'):
        """ get weekly data from api """
        self._api_params['function'] = 'TIME_SERIES_WEEKLY'
        self._api_params['symbol'] = symbol
        self._api_params['outputsize'] = output_size
        self._api_params = self._api_key
        return self._get_response()

    def get_weekly_adjusted(self, symbol, output='compact'):
        """ get weekly adjusted data from api """
        self._api_params['function'] = 'TIME_SERIES_WEEKLY_ADJUSTED'
        self._api_params['symbol'] = symbol
        self._api_params['outputsize'] = output_size
        self._api_params = self._api_key
        return self._get_response()

    def get_monthly(self, symbol, output_size='compact'):
        """ get monthly data from api """
        self._api_params['function'] = 'TIME_SERIES_MONTHLY'
        self._api_params['symbol'] = symbol
        self._api_params['outputsize'] = output_size
        self._api_params = self._api_key
        return self._get_response()

    def get_monthly_adjusted(self, symbol, output_size='compact'):
        """ get monthly adjusted data from api """
        self._api_params['function'] = 'TIME_SERIES_MONTHLY_ADJUSTED'
        self._api_params['symbol'] = symbol
        self._api_params['outputsize'] = output_size
        self._api_params = self._api_key
        return self._get_response()

    def get_intraday(self, symbol, interval, output_size='compact'):
        """ get intraday data from api """
        self._api_params['function'] = 'TIME_SERIES_INTRADAY'
        self._api_params['symbol'] = symbol
        self._api_params['interval'] = interval
        self._api_params['outputsize'] = output_size
        self._api_params = self._api_key
        return self._get_response()

