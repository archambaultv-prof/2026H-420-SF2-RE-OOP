"""
Module animal - Gestion procédurale des animaux du refuge
Représentation sous forme de tuple: (nom, espèce, âge, santé)
"""

from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nom: str, espece: str, age: int):
        self.nom = nom
        self.espece = espece
        self.age = age

    def afficher(self):
        return f"{self.nom} est un/une {self.espece} qui a {self.age} ans."

    def vieillir(self, annees: int):
        self.age += annees

    @abstractmethod
    def faire_du_bruit(self):
        pass


class Tigre(Animal):
    def __init__(self, nom: str, age: int):
        super().__init__(nom, "Tigre", age)

    def faire_du_bruit(self):
        return "🐅 RAAAAHHH!"
    
class Singe(Animal):
    def __init__(self, nom: str, age: int):
        super().__init__(nom, "Singe", age)

    def faire_du_bruit(self):
        return "🐵 Ouh ouh ouh!"
    
class Pingouin(Animal):
    def __init__(self, nom: str, age: int):
        super().__init__(nom, "Pingouin", age)

    def faire_du_bruit(self):
        return "🐧 Coin coin!"
    
class Autruche(Animal):
    def __init__(self, nom: str, age: int):
        super().__init__(nom, "Autruche", age)

    def faire_du_bruit(self):
        return "🦤 Hou hou!"

singe = Singe("Charlie", 5)

