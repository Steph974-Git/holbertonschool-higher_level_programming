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

