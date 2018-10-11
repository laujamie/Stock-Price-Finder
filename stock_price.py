import sys
from api_wrapper import TimeSeries
import window

if __name__ == '__main__':

    api_key = 'insert_api_key_here'
    t_series = TimeSeries(api_key)
    print(type(t_series.get_daily('ksadhsajdsajkdajks')) is dict)

    # window.run_gui(0, 0, 500, 500, 'Stock Prices')
