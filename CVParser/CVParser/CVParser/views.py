"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from CVParser import app
import os

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(PROJECT_ROOT, "data.json"), "r") as myfile:
        data=myfile.read()
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
        cv_data=data
    )

