
import matplotlib 
import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt 
# data = pdr.get_data_yahoo("SPY", start="2017-01-01", end="2017-04-30") 



# data = yf.download("AAPL", start="2017-01-01", end="2017-05-30")

msft = yf.Ticker("MSFT").history()

# msft_dictionary = dict.fromkeys(msft, "Price")

# msft_date = msft.drop(columns=['Close','Open', 'High',"Low","Volume","Dividends","Stock Splits"])
# msft_price = msft.drop(columns=["",'Open', 'High',"Low","Volume","Dividends","Stock Splits"])



msft_close = msft.drop(columns=['Open', 'High',"Low","Volume","Dividends","Stock Splits"])
print (msft_close.plot)
#date = data["date"]
# close = data ["close"]
# plt.plot(msft_date, msft_price)
plt.xlabel('Time (day)')
plt.ylabel('Price ($)')






