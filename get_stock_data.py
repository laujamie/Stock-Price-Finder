import argparse
import pickle
import os
import time
import pandas as pd
import requests
from api_wrapper import TimeSeries
import get_tickers

def get_daily_snp500(api_key, update_tickers=False, redo=False):
    """ pickle all the data from AlphaVantage for SNP500 """
    ts = TimeSeries(api_key)

    if update_tickers or not os.path.isfile('data/tickers.pickle'):
        get_tickers.update_snp500_tickers()

    with open('data/tickers.pickle', "rb") as f:
        tickers = pickle.load(f)

    for ticker in tickers:
        # If not force updating, don't redownload existing files
        if not redo and os.path.isfile('data/{}.pkl'.format(ticker)):
            print("Pickled data for {} exists".format(ticker))
            continue
        
        print("Getting prices for {}".format(ticker))
        resp = ts.get_daily_adjusted(ticker)
        if type(resp) is dict:
            print('{} could not be retrieved'.format(ticker))
            time.sleep(14)
            continue
        resp = resp.T  # transpose to have dates as the rows
        resp.to_pickle("data/{}.pkl".format(ticker))
        time.sleep(14)

def merge_snp_data(api_key, get_ticker=False, update_tickers=False, force_update=False):
    """ merges all the ticker data into a df with close prices """
    if get_ticker:
        get_daily_snp500(api_key, update_tickers, force_update)

    with open('data/tickers.pickle', "rb") as f:
        tickers = pickle.load(f)

    processed_tickers = []
    res_df = pd.DataFrame()

    for ticker in tickers:
        if not os.path.isfile('data/{}.pkl'.format(ticker)):
            print("Could not find pickled data for {}".format(ticker))
            continue

        data = pd.read_pickle("data/{}.pkl".format(ticker))
        processed_tickers.append(ticker)
        to_drop = []

        # Create a list of columns to drop
        for column in data.columns:
            if "adjusted close" not in column.lower():
                to_drop.append(column)
        
        if data.empty:
            print("{} has no stock data, deleting pickle...".format(ticker))
            if os.path.isfile('data/{}.pkl'.format(ticker)):
                os.remove('data/{}.pkl'.format(ticker))
            continue

        data.drop(to_drop, 1, inplace=True)
        data.rename(columns={data.columns[0]:ticker}, inplace=True)

        if res_df.empty:
            res_df = data
        else:
            res_df = res_df.join(data, how='outer')

    if not res_df.empty:
        res_df.to_pickle("data/adj_close.pickle")

    print(res_df.tail())
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Get user API key')
    parser.add_argument('api_key', type=str,
                        help='a string with your AlphaVantage API Key')
    parser.add_argument('--update', '-U',
                        action='store_true', help='flag to update ticker data')
    parser.add_argument('--tickers', '-T',
                        action='store_true', help='flag to update tickers')
    parser.add_argument('--force', '-f',
                        action='store_true', help='force update ticker data')
    args = parser.parse_args()
    merge_snp_data(args.api_key, args.update, args.tickers, args.force)
