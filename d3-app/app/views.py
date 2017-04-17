"""
Contains main routes for the Prediction App
"""
from flask import render_template
from . import app

@app.route('/', methods=('GET', 'POST'))
def index():
    return render_template('index.html')
