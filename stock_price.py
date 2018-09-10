from api_wrapper import TimeSeries

if __name__ == '__main__':

    api_key = 'insert_api_key_here'
    t_series = TimeSeries(api_key)
    print(t_series.get_daily('MSFT'))

