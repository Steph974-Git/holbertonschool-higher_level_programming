#!/usr/bin/python3
"""
Module définissant une classe Rectangle avec attributs width et height.

Ce module implémente les bases d'une classe Rectangle avec encapsulation
et validation des données via les propriétés Python.
"""


class Rectangle:
    """
    Classe représentant un rectangle avec largeur et hauteur.

    Cette classe implémente un rectangle avec:
    - Attributs width et height encapsulés par des propriétés
    - Validation des types et valeurs lors de l'affectation
    - Accès contrôlé via getters et setters
    """

    def __init__(self, width=0, height=0):
        """
        Initialise une nouvelle instance de Rectangle.

        Args:
            width (int, optional): Largeur du rectangle. Par défaut 0.
            height (int, optional): Hauteur du rectangle. Par défaut 0.
        """
        self.width = width   # Utilise le setter pour validation
        self.height = height  # Utilise le setter pour validation

    @property
    def width(self):
        """
        Propriété getter pour la largeur du rectangle.

        Returns:
            int: La largeur actuelle du rectangle
        """
        return self.__width

    @property
    def height(self):
        """
        Propriété getter pour la hauteur du rectangle.

        Returns:
            int: La hauteur actuelle du rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Propriété setter pour définir la hauteur du rectangle.

        Args:
            value (int): Nouvelle hauteur à affecter

        Raises:
            TypeError: Si value n'est pas un entier
            ValueError: Si value est négatif
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @width.setter
    def width(self, value):
        """
        Propriété setter pour définir la largeur du rectangle.

        Args:
            value (int): Nouvelle largeur à affecter

        Raises:
            TypeError: Si value n'est pas un entier
            ValueError: Si value est négatif
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
