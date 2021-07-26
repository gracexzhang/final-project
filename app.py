# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask, render_template, request
from datetime import datetime
# from model import getImageUrlFrom
# import numpy as np
# import pandas as pd
# import yfinance as yf
# import base64
# from io import BytesIO
# from matplotlib.figure import Figure
# import matplotlib.pyplot as plt


import os

# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index.html')
def index():
    return render_template("index.html", time = datetime.now())

@app.route('/left-sidebar.html')
def leftsidebar():
    return render_template("left-sidebar.html")

@app.route('/right-sidebar.html')
def rightsidebar():
    return render_template("right-sidebar.html")

@app.route('/no-sidebar.html')
def nosidebar():
    return render_template("no-sidebar.html")

@app.route('/stock-lessons.html')
def stocklessons():
    return render_template("stock-lessons.html")

@app.route('/stock-market-game.html')
def stockmarketgame():
    return render_template("stock-market-game.html")

@app.route('/online-courses.html')
def onlinecourses():
    return render_template("online-courses.html")

@app.route('/bibliography.html')
def bibliography():
    return render_template("bibliography.html")

@app.route('/simulation.html')
def simulation():
    return render_template("simulation.html")

@app.route('/pick_stock.html')
def pick_stock():
    return render_template("pick_stock.html", time = datetime.now())
@app.route('/interactive.html', methods = ["PUSH","GET","POST"])
def interactive(): 
    fig = Figure()
    user_stock = request.form["stock"]
    user_initial = request.form["start"]
    user_final = request.form["end"]
    stock_ticker =  yf.download(user_stock, start=user_initial, end=user_final)
    stock_close = stock_ticker.drop(columns=['Open', 'High',"Low","Adj Close","Volume"]) 
    plt.xlabel('Time (day)')
    plt.ylabel('Price ($)') 
    plt.xticks(rotation=90)
    ax = fig.subplots()
    ax.plot(stock_close)
    #plt.text(4.6,52, user_response + "Recent Performance", style='italic',bbox={'facecolor':'red', 'alpha':0.5, 'pad':10})
    # Save it to a temporary buffer.
    buf = BytesIO()
    fig.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    # Embed the result in the html output.
    return f"<img src='data:image/png;base64,{data}'/>" 
