# Get this deployed to flexible GAE: https://stackoverflow.com/a/51427118
from flask import Flask, request, Response, jsonify, redirect, render_template
import pandas as pd
import os

from util.vaccine_signup import send_to_signup
# Adapted from tracking/main.py
from util.nearest_pharmacies import get_nearest_pharmacies
# Adapted from tracking/main1.py
from util.phone_code import code_number, location_lat_long

#  flask_cors import CORS
app = Flask(__name__)


# Add the webdrivers to the path
os.environ['PATH'] += ':'+os.path.dirname(os.path.realpath(__file__))+"/webdrivers"

# CORS(app)

@app.route("/", methods=['GET', 'POST'])
def landing():
    return render_template("index.html")

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    """
    """
    return send_to_signup(request.values)


@app.route("/nearest-pharmacies/", methods=['GET', 'POST'])
def nearest_pharmacies():
    """
    Example:
    /nearest-pharmacies/?address=1600%20Amphitheatre%20Parkway%2C%20Mountain%20View%2C%20CA
    Output:
    {
    "results": [
        {
        "name": "NowRx", 
        "vicinity": "2224 Old Middlefield Way J, Mountain View"
        }, 
        {
        "name": "Costco Pharmacy", 
        "vicinity": "1000 N Rengstorff Ave, Mountain View"
        }
    ]
    }
    """
    return {"results": get_nearest_pharmacies(request.values["address"])}

@app.route("/phone-code/<phone>", methods=['GET', 'POST'])
def phone_code(phone):
    return str(code_number(phone))

@app.route("/coordinates/<location>", methods=['GET', 'POST'])
def coordinates(location):
    location_lat_long(location)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)