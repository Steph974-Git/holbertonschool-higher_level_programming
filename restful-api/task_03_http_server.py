#!/usr/bin/python3
"""
Un module simple qui implémente un serveur HTTP avec des endpoints API
basiques.

Ce module utilise http.server de la bibliothèque standard pour créer
un serveur HTTP léger qui répond à différentes routes avec des données JSON.
"""

import json
import http.server
from http.server import HTTPServer, BaseHTTPRequestHandler


class Server(http.server.BaseHTTPRequestHandler):
    """Classe gérant les requêtes HTTP pour notre API simple.

    Cette classe étend BaseHTTPRequestHandler pour implémenter les
    différentes routes de notre API et définir le comportement pour
    chaque endpoint.
    """

    def do_GET(self):
        """Gère les requêtes GET vers différents endpoints.

        Routes disponibles:
            /data: Renvoie des données utilisateur en JSON
            /: Page d'accueil simple
            /status: Renvoie le statut du serveur
            /info: Renvoie des informations sur l'API
        """
        if self.path == "/data":
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            json_data = json.dumps({"name": "John", "age": 30,
                                   "city": "New York"})
            self.wfile.write(json_data.encode())

        elif self.path == "/":
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/status":
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(b'{"status": "OK"}')

        elif self.path == "/info":
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            json_info = json.dumps({"version": "1.0", "description":
                                    "A simple API built with http.server"})
            self.wfile.write(json_info.encode())

        else:
            self.send_response(404)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


def run(server_class=HTTPServer, handler_class=Server):
    """Démarre le serveur HTTP avec les paramètres spécifiés.

    Args:
        server_class: Classe du serveur à utiliser (défaut: HTTPServer)
        handler_class: Classe gérant les requêtes (défaut: Server)
    """
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print("Serveur démarré sur le port 8000...")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
