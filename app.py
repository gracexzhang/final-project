# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask, render_template, request
from datetime import datetime
from model import StockNews
import numpy as np
import pandas as pd
import yfinance as yf
import base64
from io import BytesIO
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
from datetime import date
from matplot import change_date
import os

# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index.html')
def index():
    return render_template("index.html", time = datetime.now())

@app.route('/new.html')
def new():
    article = StockNews()
    article_display = article[0]
    article_url = article[1]
    article_url_image = article[2]
    # article = article[0]["source"]["name"]
    return render_template("new.html", article_display = article_display,article_url = article_url,article_url_image = article_url_image )


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

@app.route('/simulation.html')
def pick_stock():
    return render_template("simulation.html", time = datetime.now())
@app.route('/interactive.html', methods = ["PUSH","GET","POST"])
def interactive(): 
    fig = Figure()
    user_stock = request.form["stock"]
    user_initial = request.form["start"]
    user_final = request.form["end"]
    stock_ticker =  yf.download(user_stock, start=user_initial, end=user_final)
    stock_close = stock_ticker.drop(columns=['Open', 'High',"Low","Adj Close","Volume"]) 
    # plt.xticks(rotation=90)
    fig.suptitle(user_stock + "'s Performance", fontweight ="bold")
    ax = fig.subplots()
    ax.set_ylabel('Price ($)') 
    
    new = change_date(user_initial)
    d0 = date(new[0],new[1],new[2])
    old = change_date(user_final)
    d1 = date(old[0],old[1],old[2])
    delta = d1 - d0
    if delta.days < 365:
        date_short_form = DateFormatter("%d-%m")
        ax.xaxis.set_major_formatter(date_short_form)
        ax.set_xlabel('Time (Day-Month)')
    elif delta.days > 18365:
        date_long_form = DateFormatter("%Y")
        ax.set_xlabel('Time (Year)')
        ax.xaxis.set_major_formatter(date_long_form)
    else: 
        date_medium_form = DateFormatter("%m-%Y")
        ax.set_xlabel('Time (Month-Year)')
        ax.xaxis.set_major_formatter(date_medium_form)
    ax.autoscale_view()
    ax.plot(stock_close)
    # ax.text(4.6,52, user_response + "Recent Performance", style='italic',bbox={'facecolor':'red', 'alpha':0.5, 'pad':10})
    # Save it to a temporary buffer.
    buf = BytesIO()
    fig.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    # Embed the result in the html output.
    return f"<img src='data:image/png;base64,{data}'/>" 










 





