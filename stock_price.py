import requests
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd

if __name__ == '__main__':

    url = 'https://www.alphavantage.co/query'

    params = dict(
        function = "TIME_SERIES_DAILY",
        symbol = "GOOGL",
        apikey = "api_key"
    )

    resp = requests.get(url=url, params=params)
    # print(resp.url)
    resp_data = resp.json()
    # print(resp_data)
    data = {}

    success = False
    style.use('ggplot')

    for key, val in resp_data.items():
        if 'Error' in key:
            break
        if 'Time Series' in key:
            data = val
            success = True
            break

    if success:
        stock_data = pd.DataFrame.from_dict(data, dtype=float)
        stock_data = stock_data.iloc[:, ::-1]
        print(stock_data)
        plt.figure()
        open_prices = stock_data.loc['1. open']
        print(open_prices.index)
        new_plot = open_prices.plot()
        plt.show()
    else:
        print('There was an error retrieving your data')

