import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import base64
from io import BytesIO
from matplotlib import interactive

interactive(True)
# data = pdr.get_data_yahoo("SPY", start="2017-01-01", end="2017-04-30") 



# data = yf.download("AAPL", start="2017-01-01", end="2017-05-30")



# msft_dictionary = dict.fromkeys(msft, "Price")

# msft_date = msft.drop(columns=['Close','Open', 'High',"Low","Volume","Dividends","Stock Splits"])
# msft_price = msft.drop(columns=["",'Open', 'High',"Low","Volume","Dividends","Stock Splits"])

# stock = input("Choose a stock")
# stock_ticker = yf.Ticker(stock).history()
# msft_close = stock_ticker.drop(columns=['Open', 'High',"Low","Volume","Dividends","Stock Splits"])
# print (msft_close)
# # plt.plot(msft_close)
# def GraphStock(stock):
    
#     return stock_close 

tickers =['FNF', 'ASML', 'GOOGL', 'CVS']
# data = yf.download(tickers, group_by="ticker", period='1y')
# print(data)
#date = data["date"]
# close = data ["close"]
# plt.plot(msft_date, msft_price)




# plt.show()


