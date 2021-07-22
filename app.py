# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask, render_template, request
from datetime import datetime
# from model import getImageUrlFrom
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