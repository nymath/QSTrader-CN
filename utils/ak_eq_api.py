import akshare as ak
import pandas as pd
import sys

def get_ticker(ticker):
    code = ticker.split('.')[0]
    df = ak.stock_zh_a_hist(symbol=code, adjust="").iloc[:,:6]
    df.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
    df.set_index('Date',inplace=True)
    if 'Adj Close' not in df.columns:
        df['Adj Close'] = df['Close']
    return df

if __name__ == '__main__':
    ticker = sys.argv[1]
    rlt = get_ticker(ticker)
    rlt.to_csv(f'./datasource/{ticker}.csv')
    print(f'下载完成, {ticker}')