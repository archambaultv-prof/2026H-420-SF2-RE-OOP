"""
Module animal - Gestion procédurale des animaux du refuge
Représentation sous forme de tuple: (nom, espèce, âge, santé)
"""

# Indices du tuple animal
NOM = 0
ESPECE = 1
AGE = 2
SANTE = 3
from abc import abstractmethod
ESPECES = ["Tigre", "Singe", "Pingouin", "Autruche"]
class Animal():
    @abstractmethod
    def __init__(self, nom: str, espece: str, age: int, sante: int = 100):
        self.nom = nom
        self.espece = espece
        self.age = age
        self.sante = sante
    def creer_animal(nom: str, espece: str, age: int):
        nouveau_animal = Animal(nom, espece, age)
        return nouveau_animal
    def afficher(self):
        return f"({self.espece}) {self.nom} ({self.age} ans)"
class Tigre(Animal):
        def faire_bruit(self):
            return "🐅 RAAAAAHHH!"
class Singe(Animal):
        def faire_bruit(self):
            return "🐵 Ouh ouh ouh!"
class Pingouin(Animal):
        def faire_bruit(self):
            return "🐧 Coin coin!"
class Autruche(Animal):
        def faire_bruit(self):
            return "🦤 Hou hou!"
