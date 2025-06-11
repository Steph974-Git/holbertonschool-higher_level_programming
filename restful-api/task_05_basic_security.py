#!/usr/bin/python3

from flask import Flask
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "john": {
        "password": generate_password_hash("hello"),
        "role": "admin"
    },
    "susan": {
        "password": generate_password_hash("bye"),
        "role": "user"
    }
}

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users[username]["password"], password):
        return username

@app.route("/status")
def get_status():
    return "OK"
