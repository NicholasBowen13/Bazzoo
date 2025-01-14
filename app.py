# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask, render_template, request
from datetime import datetime
from model import getClothingWomenDetails
import os

# -- Initialization section --
app = Flask(__name__)



# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    details = getClothingWomenDetails()
    # urllist = getClothingUrl()
    # print(urllist)
    return render_template("index.html", time = datetime.now(), details =details)

@app.route('/men')
def men():
    return render_template("men.html")