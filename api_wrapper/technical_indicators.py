from .api_request_base import AlphaVantageRequest

class TechnicalIndicators(AlphavantageRequest):
    """ used to get the technical indicator data from AlphaVantage """

    def set_params(self, func, symbol, interval, time_period, series_type):
        self._api_params['function'] = func
        self._api_params['symbol'] = symbol
        self._api_params['interval'] = interval
        self._api_params['time_period'] = time_period
        self._api_params['series_type'] = series_type
        self._api_params['apikey'] = self._api_key

    def get_sma(self, symbol, interval, time_period, series_type):
        self.set_params('SMA', symbol, interval, time_period, series_type)
        return self._get_response()

    def get_ema(self, symbol, interval, time_period, series_type):
        self.set_params('EMA', symbol, interval, time_period, series_type)
        return self._get_response()

    def get_wma(self, symbol, interval, time_period, series_type):
        self.set_params('WMA', symbol, interval, time_period, series_type)
        return self._get_response()

    def get_dema(self, symbol, interval, time_period, series_type):
        self.set_params('DEMA', symbol, interval, time_period, series_type)
        return self._get_response()

    def get_tema(self, symbol, interval, time_period, series_type):
        self.set_params('TEMA', symbol, interval, time_period, series_type)
        return self._get_response()

    def get_trima(self, symbol, interval, time_period, series_type):
        self.set_params('TRIMA', symbol, interval, time_period, series_type)
        return self._get_response()

    def get_kama(self, symbol, interval, time_period, series_type):
        self.set_params('KAMA', symbol, interval, time_period, series_type)
        return self._get_response()

    def get_mama(self, symbol, interval, time_period, series_type):
        self.set_params('MAMA', symbol, interval, time_period, series_type)
        return self._get_response()

    def get_t3(self, symbol, interval, time_period, series_type):
        self.set_params('T3', symbol, interval, time_period, series_type)
        return self._get_response()

    def get_macd(self, symbol, interval, time_period, series_type):
        self.set_params('MACD', symbol, interval, time_period, series_type)
        return self._get_response()

    def get_macdext(self, symbol, interval, time_period, series_type, fastperiod=12, slowperiod=26, signalperiod=9):
        self.set_params('MACDEXT', symbol, interval, time_period, series_type)
        return self._get_response()
