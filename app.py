# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask, render_template, request
from datetime import datetime
# from model import getImageUrlFrom
import numpy as np
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
    user_response = request.form["stock"]
    stock_ticker =  yf.Ticker(user_response).history()
    stock_close = stock_ticker.drop(columns=['Open', 'High',"Low","Volume"])
    ax = fig.subplots()
    ax.plot(stock_close)
    plt.xlabel('Time (day)')
    plt.ylabel('Price ($)')  
    # Save it to a temporary buffer.
    buf = BytesIO()
    fig.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    # Embed the result in the html output.
    return f"<img src='data:image/png;base64,{data}'/>" , render_template("interactive.html")
