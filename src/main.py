import sys
from window_elements import window
from ticker_processing import get_stock_data

if __name__ == '__main__':

    # CLI options for setting up the tickers
    parser = argparse.ArgumentParser(description='Get user API key')
    parser.add_argument('api_key', type=str,
                        help='a string with your AlphaVantage API Key')
    parser.add_argument('--update', '-U',
                        action='store_true', help='flag to update ticker data')
    parser.add_argument('--tickers', '-T',
                        action='store_true', help='flag to update tickers')
    parser.add_argument('--force', '-f',
                        action='store_true', help='force update ticker data')
    parser.add_argument('--merge', '-m',
                        action='store_true', help='run the merge of ticker data')
    args = parser.parse_args()
    if args.merge:
        get_stock_data.merge_snp_data(args.api_key, args.update, args.tickers, args.force)

    # Run the GUI program
    window.run_gui(0, 0, 500, 500, 'Stock Prices')
