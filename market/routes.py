from market import app
from flask import render_template
from market.models import item

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/market")
def market_page():
    items = item.query
    return render_template('market.html', items=items)