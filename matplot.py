
import matplotlib 
import pandas as pd
import yfinance as yf

# data = pdr.get_data_yahoo("SPY", start="2017-01-01", end="2017-04-30") 



data = yf.download("AAPL", start="2017-01-01", end="2017-05-30")



print (data.pandas.DataFrame)

