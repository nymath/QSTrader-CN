import yfinance as yf
import sys
import os
sys.path.append(os.getcwd())

def get_ticker(ticker):
    x = yf.Ticker(ticker)
    rlt = x.history(period='max').copy()
    rlt.index = x.history(period='max').index.strftime('%Y-%m-%d')
    if 'Adj Close' not in rlt.columns:
        rlt['Adj Close'] = rlt['Close']
    return rlt


if __name__ == '__main__':
    ticker = sys.argv[1]
    rlt = get_ticker(ticker)
    rlt.to_csv(f'./datasource/{ticker}.csv')
    print(f'下载完成, {ticker}')