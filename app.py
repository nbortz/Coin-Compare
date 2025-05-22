from flask import Flask, render_template, jsonify, request
import main  # Your existing Python processing functions

app = Flask(__name__)

# Catch-all route for your single-page React app
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template('base.html')

# API endpoint for JSON-based queries
@app.route('/api/get_token_data', methods=["POST"])
def get_token_data():
    data = request.json
    mintAdd = data.get("mintAdd")
    if not mintAdd:
        return jsonify({"error": "Missing mintAdd"}), 400

    output_array = main.main(mintAdd)
    return jsonify({"data": output_array})

if __name__ == '__main__':
    app.run(debug=True)