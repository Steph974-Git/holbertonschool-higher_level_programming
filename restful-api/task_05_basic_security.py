#!/usr/bin/python3

from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = 'secret key here'
jwt = JWTManager(app)
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

@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted {}".format(auth.current_user())

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    if data == None:
        return jsonify({"error": "Missing JSON data"}), 400
         
    username = data.get("username")
    password = data.get("password")

    if username in users and check_password_hash(users[username]["password"], password):
        access_token = create_access_token(identity={"username": username, "role": users[username]["role"]})
        return jsonify(access_token=access_token)
    
    return jsonify({"Unauthorized"}), 401
    
@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    identity = get_jwt_identity()
    if identity["role"] == "admin":
        return jsonify({"Admin Access: Granted"})
    return jsonify({"Forbidden"}), 403

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
      return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
      return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
      return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(err):
      return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
      return jsonify({"error": "Fresh token required"}), 401

if __name__ == "__main__":
    app.run()
