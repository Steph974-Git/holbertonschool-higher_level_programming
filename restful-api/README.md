# Introduction aux API RESTful et HTTP

## 1. Différences entre HTTP et HTTPS

| HTTP | HTTPS |
|------|-------|
| Protocole de communication standard pour l'échange de données sur le web | Version sécurisée de HTTP avec chiffrement SSL/TLS |
| Données transmises en clair | Données transmises chiffrées |
| Aucune authentification du serveur | Authentification du serveur via certificats |
| Utilise le port 80 | Utilise le port 443 |
| Préfixe `http://` | Préfixe `https://` avec icône de cadenas |

**Risques de HTTP :** Les données peuvent être interceptées par des tiers malveillants.

**Avantages de HTTPS :** Garantit la confidentialité, l'intégrité des données et l'authentification du serveur.

**Cas d'usage obligatoires pour HTTPS :** Sites manipulant des informations sensibles (paiements, comptes utilisateurs, données de santé).

## 2. Structure d'une requête et d'une réponse HTTP

### Requête HTTP

```
GET /index.html HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0
Accept: text/html
Accept-Language: fr

[Corps optionnel pour méthodes POST/PUT]
```

1. **Ligne de requête** : méthode, chemin de ressource, version du protocole
2. **En-têtes** : métadonnées envoyées par le client
3. **Ligne vide** : sépare les en-têtes du corps
4. **Corps** : données envoyées (optionnel)

### Réponse HTTP

```
HTTP/1.1 200 OK
Date: Wed, 21 Oct 2023 14:28:02 GMT
Server: Apache
Content-Type: text/html; charset=UTF-8
Content-Length: 1234

<!DOCTYPE html>
<html>
...
</html>
```

1. **Ligne de statut** : version, code d'état, message
2. **En-têtes** : métadonnées de la réponse
3. **Ligne vide** : sépare les en-têtes du corps
4. **Corps** : contenu retourné (HTML, JSON, etc.)

## 3. Méthodes et codes HTTP

### Méthodes HTTP courantes

| Méthode | Description | Cas d'usage |
|---------|-------------|-------------|
| **GET** | Récupère une ressource | Accéder à une page web, récupérer des données d'API |
| **POST** | Crée une ressource | Soumettre un formulaire, envoyer des données |
| **PUT** | Met à jour ou crée une ressource | Modifier un profil utilisateur complet |
| **DELETE** | Supprime une ressource | Supprimer un article ou un compte |
| **HEAD** | Similaire à GET sans corps de réponse | Vérifier si une ressource existe |
| **PATCH** | Modifie partiellement une ressource | Mettre à jour un champ spécifique |

### Codes HTTP courants

#### 1xx - Information
- **100 Continue** : Le serveur a reçu les en-têtes et attend le corps

#### 2xx - Succès
- **200 OK** : Requête réussie
- **201 Created** : Ressource créée avec succès
- **204 No Content** : Requête réussie sans contenu

#### 3xx - Redirection
- **301 Moved Permanently** : Redirection permanente
- **302 Found** : Redirection temporaire

#### 4xx - Erreur client
- **400 Bad Request** : Requête mal formée
- **401 Unauthorized** : Authentification nécessaire
- **403 Forbidden** : Accès refusé
- **404 Not Found** : Ressource introuvable

#### 5xx - Erreur serveur
- **500 Internal Server Error** : Erreur générique
- **502 Bad Gateway** : Réponse invalide d'un serveur en amont
- **503 Service Unavailable** : Serveur temporairement indisponible

## 4. Introduction à cURL et utilisation basique

### Qu'est-ce que cURL?

cURL (Client URL) est un outil en ligne de commande permettant de transférer des données via divers protocoles réseau, particulièrement utile pour tester des API.

### Installation

```bash
# Linux
sudo apt install curl

# macOS
brew install curl

# Vérification
curl --version
```

### Requêtes simples

#### Récupérer une page web
```bash
curl http://example.com
```

#### Requête GET vers une API JSON
```bash
curl https://jsonplaceholder.typicode.com/posts
```

#### Afficher uniquement les en-têtes
```bash
curl -I https://jsonplaceholder.typicode.com/posts
```

#### Envoyer une requête POST avec données
```bash
curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts
```

### Options utiles

| Option | Description |
|--------|-------------|
| `-I` | Affiche uniquement les en-têtes |
| `-X` | Spécifie la méthode HTTP (GET, POST, etc.) |
| `-d` | Envoie des données avec la requête |
| `-H` | Ajoute un en-tête HTTP |
| `-o` | Sauvegarde la sortie dans un fichier |
| `\| jq` | Formate la sortie JSON (si jq est installé) |

### Exemple avancé
```bash
curl -X POST \
     -H "Content-Type: application/json" \
     -d '{"title":"Mon titre","body":"Contenu","userId":1}' \
     https://jsonplaceholder.typicode.com/posts | jq
```

## Ressources complémentaires

- [MDN Web Docs: HTTP](https://developer.mozilla.org/fr/docs/Web/HTTP)
- [Documentation officielle de cURL](https://curl.se/docs/)
- [RESTful API Design - Best Practices](https://restfulapi.net/)