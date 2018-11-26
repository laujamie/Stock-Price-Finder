import argparse
import pickle
import os
import time
import pandas as pd
import requests
from api_wrapper import TimeSeries
import get_tickers

def get_daily_snp500(api_key, update_tickers=False):
    ts = TimeSeries(api_key)

    if update_tickers or not os.path.isfile('data/tickers.pickle'):
        get_tickers.update_snp500_tickers()

    with open('data/tickers.pickle', "rb") as f:
        tickers = pickle.load(f)

    for ticker in tickers:
        print("Getting prices for {}".format(ticker))
        resp = ts.get_daily(ticker)
        if type(resp) is dict:
            print('{} could not be retrieved'.format(ticker))
            time.sleep(14)
            continue
        resp.to_pickle("data/{}.pkl".format(ticker))
        time.sleep(14)

def merge_snp_data(api_key, get_ticker=False, update_tickers=False):
    if get_ticker:
        get_daily_snp500(api_key, update_tickers)

    with open('data/tickers.pickle', "rb") as f:
        tickers = pickle.load(f)

    processed_tickers = []
    res_df = None

    for ticker in tickers:
        if not os.path.isfile('data/{}.pkl'.format(ticker)):
            print("Could not find pickled data for {}".format(ticker))
            continue

        data = pd.read_pickle("data/{}.pkl".format(ticker))
        processed_tickers.append(ticker)

        if res_df is None:
            res_df = data
        else:
            temp = [res_df, data]
            res_df = pd.concat(temp, keys = processed_tickers)

    if res_df is not None:
        res_df.to_pickle("data/all_stocks.pickle")

    print(res_df)
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Get user API key')
    parser.add_argument('api_key', type=str,
                        help='a string with your AlphaVantage API Key')
    parser.add_argument('--update', '-U',
                        action='store_true', help='flag to update ticker data')
    parser.add_argument('--tickers', '-T',
                        action='store_true', help='flag to update tickers')
    args = parser.parse_args()
    print(args)
    merge_snp_data(args.api_key, args.update, args.tickers)
