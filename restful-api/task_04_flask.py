#!/usr/bin/python3
"""
Module implémentant une API RESTful simple avec Flask.

Ce module définit plusieurs routes pour:
- Afficher un message de bienvenue
- Récupérer la liste des utilisateurs
- Vérifier le statut de l'API
- Récupérer des informations sur un utilisateur spécifique
- Ajouter un nouvel utilisateur
"""

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def home():
    """
    Route racine qui affiche un message de bienvenue.

    Returns:
        str: Message de bienvenue pour l'API
    """
    return "Welcome to the Flask API!"


dict_users = {}


@app.route("/data")
def get_data():
    """
    Récupère la liste des noms d'utilisateur enregistrés.

    Returns:
        Response: Liste JSON des noms d'utilisateur
    """
    return jsonify(list(dict_users.keys()))


@app.route("/status")
def get_status():
    """
    Vérifie le statut de l'API.

    Returns:
        Response: JSON indiquant que l'API est fonctionnelle
    """
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """
    Récupère les informations d'un utilisateur spécifique.

    Args:
        username (str): Nom de l'utilisateur à rechercher

    Returns:
        Response: Données de l'utilisateur si trouvé, sinon message d'erreur
                  avec code 404
    """
    if username in dict_users:
        return jsonify(dict_users[username])
    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def get_add_user():
    """
    Ajoute un nouvel utilisateur à partir des données JSON reçues.

    La requête doit contenir un champ 'username' pour être valide.

    Returns:
        Response: Message de confirmation avec données utilisateur et code 201
                  si réussi, sinon message d'erreur avec code 400
    """
    data = request.get_json()
    if 'username' in data:
        dict_users[data['username']] = data
        return jsonify({"message": "User added", "user": data}), 201
    return jsonify({"error": "Username is required"}), 400


if __name__ == "__main__":
    app.run()
