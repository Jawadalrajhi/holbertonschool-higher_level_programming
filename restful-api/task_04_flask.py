#!/usr/bin/env python3
"""
Flask-based RESTful API for basic user management.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)
users = {}


@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Flask API!"


@app.route("/data", methods=["GET"])
def data():
    return jsonify(list(users.keys())), 200


@app.route("/status", methods=["GET"])
def status():
    return "OK", 200


@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    if username in users:
        return jsonify(users[username]), 200
    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    new_user = request.get_json()

    if not new_user:
        return jsonify({"error": "Invalid JSON"}), 400

    if "username" not in new_user:
        return jsonify({"error": "Username is required"}), 400

    username = new_user["username"]

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = new_user
    return jsonify({"message": "User added", "user": new_user}), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, use_reloader=False)
