#!/usr/bin/python3
"""
Module définissant une classe Rectangle avec méthode de création de carré.

Ce module étend la classe Rectangle avec des fonctionnalités
de calcul d'aire et de périmètre, des représentations visuelles,
un compteur d'instances, une méthode de comparaison d'aires, et
une méthode de classe permettant de créer des carrés.
"""


class Rectangle:
    """
    Classe représentant un rectangle avec fonctionnalités complètes.

    Cette classe implémente un rectangle avec:
    - Compteur de classe pour suivre le nombre d'instances
    - Symbole d'affichage personnalisable via print_symbol
    - Méthode statique pour comparer deux rectangles par leur aire
    - Méthode de classe pour créer un carré (rectangle avec côtés égaux)
    - Attributs width et height encapsulés par des propriétés
    - Méthodes pour calculer l'aire et le périmètre
    - Méthodes spéciales pour l'affichage, récréation et suppression
    """

    # Attributs de classe partagés par toutes les instances
    number_of_instances = 0  # Compteur d'instances actives
    print_symbol = "#"       # Symbole utilisé pour l'affichage visuel

    def __init__(self, width=0, height=0):
        """
        Initialise une nouvelle instance de Rectangle et incrémente le
        compteur.

        Args:
            width (int, optional): Largeur du rectangle. Par défaut 0.
            height (int, optional): Hauteur du rectangle. Par défaut 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1  # Incrémente le compteur de classe

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

    def area(self):
        """
        Calcule l'aire du rectangle.

        Returns:
            int: Surface du rectangle (width × height)
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calcule le périmètre du rectangle.

        Returns:
            int: Périmètre du rectangle (2 × (width + height))
            ou 0 si l'une des dimensions est nulle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Retourne une représentation visuelle du rectangle avec print_symbol.

        Returns:
            str: Représentation visuelle du rectangle ou chaîne vide
            si width ou height est 0
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        row = str(self.print_symbol) * self.__width + "\n"
        return row * (self.__height - 1) + \
            str(self.print_symbol) * self.__width

    def __repr__(self):
        """
        Retourne une représentation "officielle" du rectangle.

        Returns:
            str: Représentation du constructeur pour recréer l'objet
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """
        Méthode appelée lorsqu'une instance de Rectangle est détruite.

        Affiche un message d'adieu et décrémente le compteur de classe.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compare deux rectangles et retourne celui avec la plus grande aire.

        Cette méthode statique (indépendante des instances) permet de
        comparer deux objets Rectangle et de déterminer lequel a la plus
        grande surface.

        Args:
            rect_1 (Rectangle): Premier rectangle à comparer
            rect_2 (Rectangle): Second rectangle à comparer

        Returns:
            Rectangle: Le rectangle avec la plus grande aire,
            ou rect_1 si les aires sont égales

        Raises:
            TypeError: Si rect_1 ou rect_2 n'est pas une instance de Rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Crée un nouveau rectangle carré (largeur = hauteur = size).

        Cette méthode de classe agit comme une fabrique (factory method)
        qui crée une instance spécialisée: un rectangle dont les deux
        dimensions sont identiques, c'est-à-dire un carré.

        Args:
            size (int, optional): Taille du côté du carré. Par défaut 0.

        Returns:
            Rectangle: Une nouvelle instance de Rectangle ave
            width = height = size
        """
        return cls(size, size)
