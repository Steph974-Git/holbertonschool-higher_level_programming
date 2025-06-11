#!/usr/bin/python3

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "<p>Welcome to the Flask API!</p>"

dict_users = {}
@app.route("/data")
def data():
    return jsonify(list(dict_users.keys()))

@app.route("/status")


if __name__ == "__main__":
    app.run()
