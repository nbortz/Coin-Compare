from flask import Flask, request, render_template, jsonify
import requests
import matplotlib.pyplot as plt
from datetime import datetime
import io
import base64
import main

app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route("/", methods=["GET", "POST"])

def index():
    if request.method == "POST":
        user_input = request.form["user_value"] # Get input from form
        # Example for when main is restrucutred to input/output function 
        # TODO Main must also return tweet counts for user token and 1, 2, or 3 month counts for 
        bonkCor, wifCor, fartCor, fwogCor, gigaCor, goatCor, chillCor, popcatCor, mcapvolArray, holdertoMcapRatios, twitterCounts,  = main(user_input)

        return render_template("result.html", bonkCor=bonkCor, wifCor=wifCor, fartCor=fartCor,
                                fwogCor=fwogCor, gigaCor=gigaCor, goatCor=goatCor, chillCor=chillCor, popcatCor=popcatCor,
                                mcapvolArray=mcapvolArray, holdertoMcapRatios=holdertoMcapRatios, twitterCounts=twitterCounts)

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
