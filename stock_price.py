import requests
import json
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd

url = 'https://www.alphavantage.co/query'

params = dict(
    function = "TIME_SERIES_DAILY",
    symbol = "GOOGL",
    apikey = "api_key"
)

resp = requests.get(url=url, params=params)
print(resp.url)
resp_data = resp.json()
data = {}

style.use('fivethirtyeight')

for key in resp_data.keys():
    if 'Time Series' in key:
        data = resp_data[key]
        break

stock_data = pd.DataFrame.from_dict(data, dtype=float)
stock_data = stock_data.iloc[:, ::-1]
print(stock_data)

plt.figure()
open_prices = stock_data.loc['1. open']
open_prices.plot()
plt.show()
