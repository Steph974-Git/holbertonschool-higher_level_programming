#!/usr/bin/python3
"""
Module définissant une classe Square (carré).

En POO, un module est un fichier Python qui contient des définitions
de classes, fonctions ou variables utilisables dans d'autres programmes.
"""


class Square:
    """
    Classe représentant un carré.

    En POO, une classe est un modèle (ou template) qui définit:
    - La structure des données (attributs)
    - Les comportements (méthodes)
    pour tous les objets de ce type.
    """

    def __init__(self, size):
        """
        Constructeur de la classe Square.

        Le constructeur (__init__) est appelé automatiquement chaque fois
        qu'une nouvelle instance (objet) est créée à partir de la classe.

        Args:
            size: La taille du côté du carré

        Note:
            - 'self' désigne l'instance spécifique en cours de création
            - Chaque instance aura son propre attribut __size
            - L'utilisation de '__' crée un attribut privé (encapsulation)
        """
        # Attribut privé: l'underscore double (__) rend l'attribut moins
        # accessible
        # depuis l'extérieur de la classe, c'est un principe d'encapsulation
        self.__size = size  # 'self' fait référence à l'instance elle-même

        # Exemple d'utilisation:
        # mon_carre = Square(5)  # Crée une instance avec __size = 5
        # autre_carre = Square(10)  # Crée une autre instance avec __size = 10
