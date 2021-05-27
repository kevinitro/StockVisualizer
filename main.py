import matplotlib.pyplot as plt
import yfinance as yf
import pandas as pd

data = yf.download('AAPL','2016-01-01','2018-01-01')
new_df = data.filter(["Close"])

new_df.plot()
plt.show()
