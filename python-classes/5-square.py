#!/usr/bin/python3
"""Module définissant une classe Square avec fonctionnalités d'affichage"""


class Square:
    """
    Classe représentant un carré avec taille et méthodes associées.

    En POO, une classe est un modèle qui définit la structure (attributs)
    et les comportements (méthodes) que partageront toutes ses instances.
    """

    def __init__(self, size=0):
        """
        Constructeur de la classe Square.

        Cette méthode spéciale est appelée lors de la création d'une instance:
        carré = Square(5)

        Args:
            size (int, optional): Longueur du côté du carré

        Note:
            - Utilise le setter de la propriété size (validation automatique)
            - 'self' représente l'instance spécifique en cours de création
        """
        self.size = size  # Appelle le setter @size.setter

    def area(self):
        """
        Méthode d'instance qui calcule l'aire du carré.

        En POO, une méthode d'instance est une fonction attachée à la classe
        qui opère sur une instance spécifique (référencée par 'self').

        Returns:
            int: Surface du carré (taille au carré)
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        Propriété getter - accesseur pour l'attribut privé __size.

        Le décorateur @property transforme une méthode en attribut
        accessible en lecture (square.size au lieu de square.size()).

        Returns:
            int: La taille actuelle du carré
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Propriété setter - mutateur pour l'attribut privé __size.

        Le décorateur @size.setter définit le comportement lors de
        l'affectation d'une valeur (square.size = 5).
        Permet la validation des données avant stockage.

        Args:
            value (int): Nouvelle taille à affecter

        Raises:
            TypeError: Si value n'est pas un entier
            ValueError: Si value est négatif
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")  # Correction de la typo
        if value < 0:
            raise ValueError("size must be >= 0")
        # Attribut privé (double underscore) - principe d'encapsulation
        self.__size = value  # Stockage dans l'attribut privé

    def my_print(self):
        """
        Méthode d'instance qui affiche le carré avec des #.

        Cette méthode illustre comment une instance peut avoir un
        comportement (affichage) basé sur son état interne (__size).
        Aucun paramètre n'est nécessaire car elle utilise l'attribut
        de l'instance courante via self.
        """
        if self.__size == 0:
            print()  # Ligne vide pour un carré de taille 0
        else:
            # Utilisation d'une variable muette (_) quand l'indice n'est pas
            # utilisé
            for _ in range(self.__size):  # Boucle pour chaque ligne
                # Multiplication de chaînes pour répétition
                print("#" * self.__size)
