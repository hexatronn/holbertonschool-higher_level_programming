#!/usr/bin/python3
"""A simple Flask API with in-memory user storage."""

from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage: username -> user dict
users = {}


@app.route("/", methods=["GET"])
def home():
    """Root endpoint."""
    return "Welcome to the Flask API!"


@app.route("/status", methods=["GET"])
def status():
    """Health check endpoint."""
    return "OK"


@app.route("/data", methods=["GET"])
def data():
    """Return a list of all usernames."""
    return jsonify(list(users.keys()))


@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    """Return user data by username or 404."""
    user = users.get(username)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)


@app.route("/add_user", methods=["POST"])
def add_user():
    """Add a new user from JSON body with validations."""
    payload = request.get_json(silent=True)
    if payload is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = payload.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = payload
    return jsonify({"message": "User added", "user": payload}), 201


if __name__ == "__main__":
    app.run()
