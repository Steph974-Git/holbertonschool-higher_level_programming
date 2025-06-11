#!/usr/bin/python3
"""
Module pour récupérer et traiter des données depuis une API REST.

Ce module utilise la bibliothèque requests pour interagir avec l'API
JSONPlaceholder et effectuer diverses opérations sur les données récupérées.
"""

import requests
import csv


def fetch_and_print_posts():
    """
    Récupère les articles depuis l'API et affiche leurs titres.

    Cette fonction envoie une requête GET à l'API JSONPlaceholder,
    puis affiche le code d'état de la réponse ainsi que les titres
    de tous les articles si la requête a réussi.
    """
    # Envoi de la requête GET à l'API
    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    print("Status Code: {}".format(r.status_code))

    # Traitement de la réponse si elle est réussie (code 200)
    if r.status_code == 200:
        data = r.json()

        # Parcours et affichage de chaque titre d'article
        for post in data:
            print("{}".format(post['title']))


def fetch_and_save_posts():
    """
    Récupère les articles depuis l'API et les enregistre dans un fichier CSV.

    Cette fonction envoie une requête GET à l'API JSONPlaceholder,
    structure les données reçues et les enregistre dans un fichier CSV
    nommé 'posts.csv' avec les colonnes id, title et body.
    """
    # Envoi de la requête GET à l'API
    r = requests.get('https://jsonplaceholder.typicode.com/posts')

    # Traitement de la réponse si elle est réussie (code 200)
    if r.status_code == 200:
        data = r.json()

        # Structure les données dans un format approprié pour le CSV
        structured_posts = []
        for post in data:
            structured_posts.append({
                'id': post['id'],
                'title': post['title'],
                'body': post['body']
            })

        # Écriture des données dans un fichier CSV
        with open('posts.csv', 'w', newline='') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Écriture de l'en-tête du CSV
            writer.writeheader()

            # Écriture de toutes les lignes de données
            writer.writerows(structured_posts)

    print("Posts saved to posts.csv successfully")


if __name__ == "__main__":
    print("Fetching and printing posts:")
    fetch_and_print_posts()

    print("\nFetching and saving posts to CSV:")
    fetch_and_save_posts()
