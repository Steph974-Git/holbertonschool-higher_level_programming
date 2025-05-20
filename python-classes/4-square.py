#!/usr/bin/python3
"""Module définissant une classe Square"""


class Square:
    """
    Classe représentant un carré.

    Cette classe illustre plusieurs concepts de POO:
    - Encapsulation: protège les attributs avec des méthodes d'accès
    - Propriétés: utilise des getters/setters via décorateurs
    - Validation: vérifie les données avant affectation
    """

    def __init__(self, size=0):
        """
        Constructeur de la classe - appelé lors de l'instanciation.

        Args:
            size (int, optional): Taille du côté du carré

        Note:
            self fait référence à l'instance en cours de création
            self.size utilise le setter défini plus bas
            (pas d'affectation directe)
        """
        self.size = size  # Utilise le setter de la propriété size

    def area(self):
        """
        Méthode d'instance - calcule l'aire du carré.

        Returns:
            int: L'aire du carré

        Note:
            Une méthode d'instance reçoit automatiquement self,
            qui représente l'objet sur lequel la méthode est appelée
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        Getter (accesseur) - convertit l'attribut privé en propriété lisible.

        Le décorateur @property transforme une méthode en attribut accessible
        en lecture (square.size au lieu de square.size())

        Returns:
            int: La taille du carré
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter (mutateur) - permet de modifier l'attribut avec validation.

        Le décorateur @size.setter définit le comportement lors de
        l'affectation (square.size = 5)

        Args:
            value (int): Nouvelle taille à affecter

        Raises:
            TypeError: Si la taille n'est pas un entier
            ValueError: Si la taille est négative
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        # Attribut privé (encapsulation) - non accessible directement hors de
        # la classe
        self.__size = value
