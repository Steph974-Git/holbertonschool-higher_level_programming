#!/usr/bin/python3

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "<p>Welcome to the Flask API!</p>"

@app.route("/")


if __name__ == "__main__":
    app.run()
