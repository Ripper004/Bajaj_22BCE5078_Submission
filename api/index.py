from flask import Flask, request, jsonify
from utils import process_array, generate_user_id
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "BFHL Flask API running"})

@app.route("/bfhl", methods=["POST"])
def bfhl():
    try:
        body = request.get_json(force=True)
        result = process_array(body, os.environ)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({
            "is_success": False,
            "user_id": generate_user_id(os.environ),
            "email": os.environ.get("EMAIL", "john@xyz.com"),
            "roll_number": os.environ.get("ROLL_NUMBER", "ABCD123"),
            "odd_numbers": [],
            "even_numbers": [],
            "alphabets": [],
            "special_characters": [],
            "sum": "0",
            "concat_string": "",
            "error": str(e)
        }), 200
