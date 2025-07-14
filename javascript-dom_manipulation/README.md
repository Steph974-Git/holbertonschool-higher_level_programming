# JavaScript DOM Manipulation

Bienvenue dans mon projet d’apprentissage sur la manipulation du DOM avec JavaScript.  
Ce dossier regroupe des exercices progressifs pour comprendre et pratiquer les bases du DOM, des événements, et de l’interaction avec des APIs.

---

## Structure du dossier

Chaque exercice est composé de :
- Un fichier HTML (`*-main.html`) pour tester le script
- Un fichier JavaScript (`*-script.js`) où j’écris le code demandé

---

## Exercices détaillés et techniques utilisées

### 0. Modifier la couleur d’un élément
- **Fichiers :** `0-main.html`, `0-script.js`
- **Objectif :** Changer la couleur du texte du `<header>` en rouge.
- **Techniques :**
  - Sélection d’un élément avec `document.querySelector`
  - Modification du style via la propriété `.style.color`

### 1. Changer la couleur au clic
- **Fichiers :** `1-main.html`, `1-script.js`
- **Objectif :** Changer la couleur du `<header>` en rouge lors d’un clic sur un bouton.
- **Techniques :**
  - Sélection d’éléments (`querySelector`)
  - Ajout d’un gestionnaire d’événement avec `addEventListener('click', ...)`
  - Modification du style dynamique

### 2. Ajouter une classe CSS au clic
- **Fichiers :** `2-main.html`, `2-script.js`
- **Objectif :** Ajouter la classe `red` au `<header>` au clic.
- **Techniques :**
  - Utilisation de `classList.add` pour appliquer une classe CSS
  - Gestion d’événement sur un bouton

### 3. Basculer entre deux classes CSS
- **Fichiers :** `3-main.html`, `3-script.js`
- **Objectif :** Alterner entre les classes `red` et `green` sur le `<header>`.
- **Techniques :**
  - Utilisation de `classList.toggle` pour alterner les classes
  - Compréhension de la logique conditionnelle via le DOM

### 4. Ajouter un élément à une liste
- **Fichiers :** `4-main.html`, `4-script.js`
- **Objectif :** Ajouter un nouvel élément `<li>` à la liste `.my_list` au clic.
- **Techniques :**
  - Création d’élément avec `document.createElement`
  - Ajout d’un enfant avec `appendChild`
  - Modification du contenu avec `.textContent`

### 5. Modifier le texte du header
- **Fichiers :** `5-main.html`, `5-script.js`
- **Objectif :** Changer le texte du `<header>` en "New Header!!!" au clic.
- **Techniques :**
  - Modification du texte avec `.textContent`
  - Gestion d’événement

### 6. Récupérer des données d’une API (Fetch)
- **Fichiers :** `6-main.html`, `6-script.js`
- **Objectif :** Afficher le nom d’un personnage Star Wars récupéré via l’API SWAPI.
- **Techniques :**
  - Utilisation de la Fetch API pour faire une requête HTTP
  - Traitement de la réponse avec `.then()` et `.json()` (Promises)
  - Extraction d’une propriété d’un objet JSON

### 7. Afficher une liste de films Star Wars
- **Fichiers :** `7-main.html`, `7-script.js`
- **Objectif :** Récupérer la liste des films Star Wars via l’API SWAPI et les afficher dans une liste.
- **Techniques :**
  - Fetch API pour récupérer un tableau d’objets
  - Boucle `for...of` pour parcourir les résultats
  - Création dynamique de plusieurs éléments `<li>`

### 8. Afficher un message traduit
- **Fichiers :** `8-main.html`, `8-script.js`
- **Objectif :** Utiliser l’API HelloSalut pour afficher "Bonjour" en français.
- **Techniques :**
  - Fetch API pour récupérer une ressource externe
  - Affichage dynamique d’une donnée reçue d’une API

---

## Concepts clés rencontrés

- **Sélecteurs DOM** : `querySelector`, `createElement`
- **Gestion des événements** : `addEventListener`
- **Manipulation de classes CSS** : `classList.add`, `classList.toggle`
- **Modification du contenu** : `.textContent`, `.style`
- **Boucles** : `for`, `for...of`
- **Fetch API** : requêtes HTTP, récupération et traitement de données JSON
- **Promises** : gestion de l’asynchrone avec `.then()`
- **Création et ajout d’éléments dynamiques`

---

## Pour aller plus loin

- Ajouter des fonctionnalités comme la suppression d’éléments ou la gestion d’erreurs API.
- Explorer les frameworks modernes (React, Vue, Angular) pour manipuler le DOM de façon plus structurée.
- Approfondir la gestion des Promises et découvrir `async/await` pour un code asynchrone plus lisible.

---

**Ce projet me sert de référence pour revoir les bases de la manipulation du DOM et de l’asynchrone en JavaScript. Je peux y ajouter des notes personnelles, des liens vers des ressources utiles, ou des rappels sur des concepts clés.**
