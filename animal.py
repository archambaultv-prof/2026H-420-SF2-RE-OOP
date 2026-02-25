"""
Module animal - Gestion procédurale des animaux du refuge
Représentation sous forme de tuple: (nom, espèce, âge, santé)
"""

from abc import ABC, abstractmethod

class Animal(ABC):

    def __init__(self, nom, espece, age, sante):
        self.nom = nom
        self.espece = espece
        self.age = age
        self.sante = sante

    @abstractmethod
    def faire_bruit(self):
        pass

    def afficher_animal(self):
        print(f" [{self.espece}] {self.nom} ({self.age}ans, santé: {self.sante}%)")


class Tigre(Animal):
    def __init__(self, nom, age, sante):
        super().__init__(nom,'Tigre', age, sante)

    def faire_bruit(self):
        print("🐅 RAAAAAHHH!")


class Singe(Animal):
    def __init__(self, nom, age, sante):
        super().__init__(nom, 'Singe', age, sante)

    def faire_bruit(self):
        print("🐵 Ouh ouh ouh!")


class Pingouin(Animal):
    def __init__(self, nom, age, sante):
        super().__init__(nom, 'Pingouin', age, sante)

    def faire_bruit(self):
        print("🐧 Coin coin!")


class Autruche(Animal):
    def __init__(self, nom, age, sante):
        super().__init__(nom, 'Autruche', age, sante)

    def faire_bruit(self):
        print("🦤 Hou hou!")
