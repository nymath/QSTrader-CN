import akshare as ak
import pandas as pd
import sys

def get_ticker(ticker):
    code = ticker.split('.')[0]
    ak.index_zh_a_hist(symbol="000300", period="daily")
    df = ak.index_zh_a_hist(symbol=code, period="daily").iloc[:,:6]
    df.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
    df.set_index('Date',inplace=True)
    if 'Adj Close' not in df.columns:
        df['Adj Close'] = df['Close']
    return df

if __name__ == '__main__':
    ticker = "000300.XSHG"
    rlt = get_ticker(ticker)
    rlt.to_csv(f'./datasource/{ticker}.csv')
    print(f'下载完成, {ticker}')