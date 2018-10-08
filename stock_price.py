import sys
from api_wrapper import TimeSeries
import window

if __name__ == '__main__':

    api_key = 'insert_api_key_here'
    t_series = TimeSeries(api_key)
    print(t_series.get_daily('msft'))

    window.run_gui(50, 50, 500, 300, 'Stock Prices')
