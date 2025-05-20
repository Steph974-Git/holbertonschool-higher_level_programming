#!/usr/bin/python3
"""Module définissant une classe Square (carré)"""


class Square:
    """
    Classe représentant un carré.

    En POO, une classe est un modèle qui définit les attributs et
    comportements que ses instances (objets) vont posséder.
    """

    def __init__(self, size=0):
        """
        Méthode d'initialisation (constructeur) de la classe Square.

        Cette méthode est appelée automatiquement quand on crée une
        nouvelle instance: my_square = Square(5)

        Args:
            size (int, optional): Taille du côté du carré

        Note:
            - 'self' représente l'instance en cours de création
            - '__size' avec double underscore est un attribut privé
        """
        # Validation des données avant attribution
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")

        # Attribution à l'attribut privé (encapsulation)
        self.__size = size  # L'attribut est stocké dans l'instance (self)

    def area(self):
        """
        Méthode d'instance qui calcule l'aire du carré.

        Une méthode d'instance est une fonction attachée à la classe
        qui opère sur une instance spécifique (référencée par 'self').

        Returns:
            int: L'aire du carré (taille au carré)
        """
        # Accès à l'attribut privé via self
        return self.__size ** 2
