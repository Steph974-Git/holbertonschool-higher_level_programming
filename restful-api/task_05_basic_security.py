#!/usr/bin/python3
"""
Module d'API Flask avec sécurité basique et JWT.

Ce module implémente une API Flask avec deux mécanismes d'authentification:
- HTTP Basic Authentication pour la protection de base
- JSON Web Tokens (JWT) pour l'authentification sans état

Il inclut également un système de contrôle d'accès basé sur les rôles
permettant de restreindre certaines routes aux administrateurs.
"""

from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token,
    jwt_required, get_jwt_identity
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
# Clé secrète utilisée pour signer les tokens JWT
app.config["JWT_SECRET_KEY"] = 'secret key here'
jwt = JWTManager(app)
auth = HTTPBasicAuth()

# Dictionnaire des utilisateurs avec mots de passe hashés et rôles
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
    """
    Vérifie les identifiants pour l'authentification HTTP basique.

    Args:
        username (str): Nom d'utilisateur à vérifier
        password (str): Mot de passe à vérifier

    Returns:
        str: Nom d'utilisateur si les identifiants sont valides, None sinon
    """
    if username in users and check_password_hash(
            users[username]["password"], password):
        return username
    return None


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    """
    Route protégée par authentification HTTP basique.

    Cette route nécessite des identifiants valides via HTTP Basic Auth.

    Returns:
        str: Message confirmant l'accès avec le nom d'utilisateur
    """
    current_user = auth.current_user()
    if current_user not in users:
        return jsonify({"error": "Unauthorized"}), 401
    return "Basic Auth: Access Granted"


@app.route("/login", methods=["POST"])
def login():
    """
    Route pour se connecter et obtenir un token JWT.

    Attend un JSON contenant username et password, vérifie les identifiants
    et retourne un JWT token si valides.

    Returns:
        Response: Token JWT si succès, message d'erreur sinon
    """
    data = request.get_json()
    if not data:
        return jsonify({"error": "Missing JSON data"}), 400

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    if username in users and check_password_hash(
            users[username]["password"], password):
        # Création d'un token avec l'identité de l'utilisateur et son rôle
        access_token = create_access_token(
            identity={
                "username": username,
                "role": users[username]["role"]})
        return jsonify({"access_token": access_token})
    else:
        return jsonify({"error": "Unauthorized"}), 401


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    """
    Route protégée par authentification JWT.

    Cette route nécessite un token JWT valide.

    Returns:
        Response: Message confirmant l'accès autorisé
    """
    return jsonify({"message": "JWT Auth: Access Granted"}), 200


@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    """Route accessible uniquement aux administrateurs"""
    current_user = get_jwt_identity()

    # Validation plus robuste de l'identité
    if not current_user or not isinstance(current_user, dict):
        return jsonify({"error": "Invalid token"}), 401

    if current_user.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """
    Gestionnaire pour token JWT manquant.

    Args:
        err: Détails de l'erreur

    Returns:
        Response: Message d'erreur avec code 401
    """
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """
    Gestionnaire pour token JWT invalide.

    Args:
        err: Détails de l'erreur

    Returns:
        Response: Message d'erreur avec code 401
    """
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    """
    Gestionnaire pour token JWT expiré.

    Args:
        first: Header JWT
        second: Payload JWT

    Returns:
        Response: Message d'erreur avec code 401
    """
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    """
    Gestionnaire pour token JWT révoqué.

    Args:
        first: Header JWT
        second: Payload JWT

    Returns:
        Response: Message d'erreur avec code 401
    """
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """
    Gestionnaire pour token JWT non-frais.

    Args:
        err: Détails de l'erreur

    Returns:
        Response: Message d'erreur avec code 401
    """
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run()
