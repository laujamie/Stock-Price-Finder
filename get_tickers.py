import pickle
from bs4 import BeautifulSoup
import requests

def update_snp500_tickers():
    resp = requests.get("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")
    soup = BeautifulSoup(resp.text, 'lxml')
    table = soup.find('table', {'class': 'wikitable sortable'})

    tickers = []
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[0].text
        tickers.append(ticker)

    print(tickers)

    with open("./data/tickers.pickle", "wb") as f:
        pickle.dump(tickers, f)

update_snp500_tickers()
