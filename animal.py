"""
Module animal - Gestion procédurale des animaux du refuge
Représentation sous forme de tuple: (nom, espèce, âge, santé)
"""

from abc import ABC, abstractmethod

ESPECES = ["Tigre", "Singe", "Pingouin", "Autruche"]

class Animal:
    def __init__(self, nom, espece, age):
        self.nom = nom
        self.espece = espece
        self.age = age

    @abstractmethod
    def se_nourrir(self):
        pass

    def vieillir(self):
        self.age += 1
        return f"{self.nom} a maintenant {self.age} ans!"

    @abstractmethod
    def faire_bruit(self):
        pass
    
    def afficher_animal(self):
        return f"🦁 Espèce: {self.espece} | Nom: {self.nom} | Âge: {self.age} ans"


class Tigre(Animal):
    def __init__(self, nom, espece, age):
        super().__init__(self, nom, espece, age)
    
    def se_nourrir(self):
        return f"{self.nom} mange de la viande!"

    def vieillir(self):
        super().vieillir()

    def faire_bruit(self):
        return f"{self.nom}: RAAAAAHHH!"
    
    def afficher_animal(self):
        super().afficher_animal()


class Singe(Animal):
    def __init__(self, nom, espece, age):
        super().__init__(self, nom, espece, age)
    
    def se_nourrir(self):
        return f"{self.nom} mange des bananes!"

    def vieillir(self):
        super().vieillir()

    def faire_bruit(self):
        return f"{self.nom}: Ouh ouh ouh!"
    
    def afficher_animal(self):
        super().afficher_animal()


class Pingouin(Animal):
    def __init__(self, nom, espece, age):
        super().__init__(self, nom, espece, age)
    
    def se_nourrir(self):
        return f"{self.nom} mange du poisson!"

    def vieillir(self):
        super().vieillir()

    def faire_bruit(self):
        return f"{self.nom}: Coin coin!"

    def afficher_animal(self):
        super().afficher_animal()


class Autruche(Animal):
    def __init__(self, nom, espece, age):
        super().__init__(self, nom, espece, age)
    
    def se_nourrir(self):
        return f"{self.nom} mange de l'herbe!"

    def vieillir(self):
        super().vieillir()

    def faire_bruit(self):
        return f"{self.nom}: Hou hou!"
    
    def afficher_animal(self):
        super().afficher_animal()