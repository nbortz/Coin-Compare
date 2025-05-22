from flask import Flask, request, render_template, jsonify
import requests
import matplotlib.pyplot as plt
from datetime import datetime
import io
import base64
import main  # Your existing Python functions

app = Flask(__name__)

# Catch-all route for your single-page application
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    # This returns the base.html template,
    # which contains the mounting point (e.g. <div id="root"></div>)
    # and loads the bundled React app.
    return render_template('base.html')

# API Endpoint for JSON-based queries remains unchanged
@app.route('/api/get_token_data', methods=["POST"])
def get_token_data():
    data = request.json  # Get JSON input from the frontend
    mintAdd = data.get("mintAdd")

    if not mintAdd:
        return jsonify({"error": "Missing mintAdd"}), 400

    # Call main.main() (your Python function) with user input
    output_array = main.main(mintAdd)

    return jsonify({"data": output_array})  # Respond with JSON output

if __name__ == '__main__':
    app.run(debug=True)