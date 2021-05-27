import matplotlib.pyplot as plt
import yfinance as yf
import pandas as pd

def print_stock_price(ticker, start, end):
    data = yf.download(ticker , start, end)
    new_df = data.filter(["Close"])
    new_df.plot()
    plt.title(ticker + " Price from " + start + ' to ' + end)
    plt.ylabel("Price in USD")
    plt.xlabel("Time")
    plt.show()


if __name__ == "__main__":
    print_stock_price("AAPL", "2020-01-01", "2020-12-25")

