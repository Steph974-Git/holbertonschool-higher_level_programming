
# JavaScript Warm Up

Bienvenue dans ce dossier d’exercices pour s’échauffer avec JavaScript en ligne de commande. Chaque script m’a permis de découvrir ou de réviser des bases essentielles du langage, de la gestion des arguments à la manipulation de fonctions, d’objets et de tableaux.

---

## 📁 Structure du dossier

Chaque fichier `.js` est un exercice indépendant à lancer avec Node.js.

Exemple :
```bash
node 0-javascript_is_amazing.js
```

---

## 📝 Exercices détaillés et techniques utilisées

### 0. Afficher une chaîne
- **Fichier :** `0-javascript_is_amazing.js`
- **Objectif :** Afficher "JavaScript is amazing"
- **Techniques :**
  - Déclaration de constante (`const`)
  - Utilisation de `console.log`

### 1. Afficher plusieurs lignes
- **Fichier :** `1-multi_languages.js`
- **Objectif :** Afficher trois phrases sur trois lignes
- **Techniques :**
  - Utilisation de `\n` pour les retours à la ligne
  - `console.log` pour afficher du texte

### 2. Afficher un message selon le nombre d’arguments
- **Fichier :** `2-arguments.js`
- **Objectif :** Afficher un message selon le nombre d’arguments passés au script
- **Techniques :**
  - Accès aux arguments via `process.argv`
  - Utilisation de `.length` sur un tableau
  - Structure conditionnelle `if/else`

### 3. Afficher le premier argument
- **Fichier :** `3-value_argument.js`
- **Objectif :** Afficher le premier argument ou "No argument"
- **Techniques :**
  - Accès direct à un élément de tableau
  - Vérification d’existence d’une valeur

### 4. Concaténer deux arguments
- **Fichier :** `4-concat.js`
- **Objectif :** Afficher deux arguments sous la forme "arg1 is arg2"
- **Techniques :**
  - Concaténation de chaînes avec `+`
  - Accès à plusieurs arguments

### 5. Conversion en entier
- **Fichier :** `5-to_integer.js`
- **Objectif :** Afficher "My number: X" si l’argument est un entier, sinon "Not a number"
- **Techniques :**
  - Conversion avec `parseInt`
  - Vérification avec `isNaN`
  - Structure conditionnelle

### 6. Afficher plusieurs lignes avec une boucle
- **Fichier :** `6-multi_languages_loop.js`
- **Objectif :** Afficher plusieurs phrases à l’aide d’une boucle
- **Techniques :**
  - Déclaration d’un tableau
  - Boucle `for` pour parcourir le tableau

### 7. Répéter une phrase X fois
- **Fichier :** `7-multi_c.js`
- **Objectif :** Afficher "C is fun" X fois, X étant le premier argument
- **Techniques :**
  - Conversion d’argument en entier
  - Boucle `for`
  - Vérification d’entrée utilisateur

### 8. Afficher un carré de X
- **Fichier :** `8-square.js`
- **Objectif :** Afficher un carré de taille X avec le caractère "X"
- **Techniques :**
  - Boucle pour les lignes
  - Utilisation de `"X".repeat()`
  - Gestion d’erreur si l’argument n’est pas un nombre

### 9. Additionner deux nombres avec une fonction
- **Fichier :** `9-add.js`
- **Objectif :** Afficher la somme de deux arguments
- **Techniques :**
  - Définition d’une fonction
  - Conversion des arguments
  - Vérification avec `isNaN`

### 10. Factorielle récursive
- **Fichier :** `10-factorial.js`
- **Objectif :** Calculer la factorielle d’un nombre de façon récursive
- **Techniques :**
  - Fonction récursive
  - Gestion du cas de base et des entrées invalides

### 11. Deuxième plus grand nombre
- **Fichier :** `11-second_biggest.js`
- **Objectif :** Trouver le deuxième plus grand nombre parmi les arguments
- **Techniques :**
  - Conversion de tous les arguments en nombres
  - Tri d’un tableau avec `.sort()`
  - Gestion des cas particuliers (0 ou 1 argument)

### 12. Modifier un objet
- **Fichier :** `12-object.js`
- **Objectif :** Modifier la valeur d’une propriété d’objet
- **Techniques :**
  - Déclaration et modification d’objet
  - Affichage d’objet avec `console.log`

### 13. Exporter une fonction
- **Fichiers :** `13-add.js`, `13-main.js`
- **Objectif :** Créer une fonction d’addition exportable et la tester dans un autre fichier
- **Techniques :**
  - Définition et export d’une fonction avec `exports`
  - Import et utilisation d’une fonction dans un autre fichier

---

## 🧠 Concepts clés rencontrés

- **Gestion des arguments en ligne de commande** : `process.argv`
- **Conversion de types** : `parseInt`, `Number`, `isNaN`
- **Structures de contrôle** : `if/else`, boucles `for`
- **Fonctions** : déclaration, appel, export/import
- **Objets et tableaux**
- **Manipulation de chaînes**
- **Bonne pratique : utiliser `const` au lieu de `var`**

---

## 🚀 Conseils pour ma progression

- Lire la documentation MDN sur chaque méthode ou objet utilisé
- Tester chaque script avec différents arguments pour bien comprendre les cas limites
- Refaire certains exercices en essayant d’autres méthodes (ex : boucle `while`, fonctions fléchées)
- Ajouter des commentaires pour expliquer chaque étape du code

---

## 🔎 Pour aller plus loin

- Découvrir les modules ES6 (`import`/`export`)
- Expérimenter avec la gestion d’erreurs (`try/catch`)
- S’entraîner à écrire des tests unitaires pour les fonctions

---

**Ce dossier me sert de référence pour les bases JavaScript côté terminal, et pour m’entraîner à écrire du code propre et réutilisable.**