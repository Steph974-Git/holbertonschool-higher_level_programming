#!/usr/bin/python3
"""Module définissant une classe Square avec position et taille"""


class Square:
    """
    Classe représentant un carré avec position et taille.

    En POO, une classe est un modèle qui définit:
    - Des attributs (données/propriétés des objets)
    - Des méthodes (comportements/actions des objets)
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Constructeur de classe - initialise une nouvelle instance de Square.

        En POO, le constructeur est appelé quand on crée un objet:
        mon_carre = Square(5, (2, 0))

        Args:
            size (int): Taille du carré
            position (tuple): Position du carré (décalage d'impression)

        Note:
            - Utilise les setters pour validation immédiate des données
            - "self" représente l'instance spécifique en cours de création
        """
        # Ces affectations appellent les setters définis plus bas
        self.size = size  # Équivalent à: self.__size = size après validation
        self.position = position  # Équivalent à: self.__position = position après validation

    def area(self):
        """
        Méthode d'instance calculant l'aire du carré.

        En POO, une méthode d'instance est une fonction attachée à la classe
        qui opère sur les données d'une instance spécifique via 'self'.

        Returns:
            int: Surface du carré (côté²)
        """
        return self.__size ** 2  # Accès à l'attribut privé via self

    @property
    def size(self):
        """
        Propriété getter - fournit accès en lecture à l'attribut privé __size.

        En POO, une propriété permet:
        - Accès contrôlé aux attributs privés
        - Lecture d'attribut comme une variable: carre.size (pas comme méthode)

        Returns:
            int: La taille actuelle du carré
        """
        return self.__size  # Retourne l'attribut privé

    @property
    def position(self):
        """
        Propriété getter - fournit accès en lecture à l'attribut privé __position.

        Returns:
            tuple: La position actuelle pour l'affichage du carré
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Propriété setter - valide et modifie l'attribut privé __position.

        En POO, un setter permet:
        - Validation avant stockage
        - Modification d'attribut comme une variable: carre.position = (1, 2)
        - Protection des données internes (encapsulation)

        Args:
            value (tuple): Nouvelle position (x, y) à définir

        Raises:
            TypeError: Si position ne respecte pas les critères de validation
        """
        # Validation complète avant affectation (principe d'encapsulation)
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        # Stockage dans l'attribut privé (__ = convention pour attribut privé)
        self.__position = value

    @size.setter
    def size(self, value):
        """
        Propriété setter - valide et modifie l'attribut privé __size.

        Args:
            value (int): Nouvelle taille à définir

        Raises:
            TypeError: Si la taille n'est pas un entier
            ValueError: Si la taille est négative
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        # L'attribut avec double underscore (__) est "privé" en Python
        # (accès direct plus difficile depuis l'extérieur)
        self.__size = value

    def my_print(self):
        """
        Méthode d'instance affichant le carré avec positionnement.

        Cette méthode montre comment le comportement d'une instance
        peut dépendre de son état interne (__size et __position).
        C'est une caractéristique essentielle de la POO: les objets
        encapsulent à la fois données et comportements.
        """
        if self.__size == 0:
            print()  # Ligne vide pour un carré de taille 0
        else:
            # Décalage vertical selon position[1]
            for _ in range(self.position[1]):
                print()
            # Impression de chaque ligne du carré
            for _ in range(self.__size):
                # Décalage horizontal + impression des caractères #
                print(" " * self.__position[0] + "#" * self.__size)
