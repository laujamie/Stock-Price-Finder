import argparse
import pickle
import os
import time
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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Get user API key')
    parser.add_argument('api_key', type=str,
                        help='a string with your AlphaVantage API Key')
    parser.add_argument('--update', '-U',
                        action='store_true', help='flag to update tickers')
    args = parser.parse_args()
    print(args)
    get_daily_snp500(args.api_key, args.update)
