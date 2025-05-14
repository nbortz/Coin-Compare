from flask import Flask, request, render_template, jsonify
import requests
import matplotlib.pyplot as plt
from datetime import datetime
import io
import base64
import main  # Your existing Python functions

app = Flask(__name__)

# Home page route
@app.route('/', methods=["GET"])
def home():
    return render_template('index.html')

# Existing result page (still uses templates)
@app.route("/result", methods=["POST", "GET"])
def result():
    if request.method == "POST":
        user_input = request.form["user_value"]  # Get input from form
        output_array = main.main(user_input)
        print(output_array)
        return render_template("result.html", output_array=output_array)

@app.route('/about')
def about():
    return render_template('about.html')

# 🚀 **NEW API Endpoint for JSON-based queries**
@app.route('/api/get_token_data', methods=["POST"])
def get_token_data():
    data = request.json  # Get JSON input from frontend
    mintAdd = data.get("mintAdd")

    if not mintAdd:
        return jsonify({"error": "Missing mintAdd"}), 400

    # Call `main.main()` with user input
    output_array = main.main(mintAdd)

    return jsonify({"data": output_array})  # Respond with JSON output

if __name__ == '__main__':
    app.run(debug=True)