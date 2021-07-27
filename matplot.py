import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import base64
from io import BytesIO
from matplotlib import interactive

interactive(True)
# data = pdr.get_data_yahoo("SPY", start="2017-01-01", end="2017-04-30") 

"2017-01-01"
def change_date(date):
    year = int(date[:4])
    month = int( date [5:7])
    day = int( date[8:10])
    return [year,month, day]


print (change_date("2021-07-01"))

# user_initial_new = user_initial.replace('-', '') 
    # user_initial_new_new = str(user_initial_new)[:4] + "," + str(user_initial_new)[4:]
    # user_initial_new_new_new = user_initial_new_new[:7] + "," + user_initial_new_new[7:]
    # user_final_new = user_final.replace('-', '') 
    # user_final_new_new = str(user_final_new)[:4] + "," + str(user_final_new)[4:]
    # user_final_new_new_new = user_final_new_new[:7] + "," + user_final_new_new[7:]
# data = yf.download("AAPL", start="2017-01-01", end="2017-05-30")



# msft_dictionary = dict.fromkeys(msft, "Price")

# msft_date = msft.drop(columns=['Close','Open', 'High',"Low","Volume","Dividends","Stock Splits"])
# msft_price = msft.drop(columns=["",'Open', 'High',"Low","Volume","Dividends","Stock Splits"])

# stock = input("Choose a stock")
# stock_ticker = yf.Ticker(stock).history()
# msft_close = stock_ticker.drop(columns=['Open', 'High',"Low","Volume","Dividends","Stock Splits"])
# print (msft_close)
# # # plt.plot(msft_close)
# def GraphStock(stock):
    
# #     return stock_close 

# data = yf.download("AAPL", start="2017-01-01", end="2017-04-30")
# data_close = data.drop(columns=['Open', 'High',"Low","Adj Close","Volume"]) 
# print(data_close)

#date = data["date"]
# close = data ["close"]
# plt.plot(msft_date, msft_price)




# plt.show()


