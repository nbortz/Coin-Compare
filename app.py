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

def result():
    if request.method == "POST":
        user_input = request.form["user_value"] # Get input from form
        # Example for when main is restrucutred to input/output function 
        output_array = main(user_input)
        return render_template("result.html", output_array=output_array)

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
