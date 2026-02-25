"""
Module animal - Gestion procédurale des animaux du refuge
Représentation sous forme de tuple: (nom, espèce, âge, santé)
"""

# Indices du tuple animal
from abc import ABC, abstractmethod


class Animal(ABC):

    def __init__(self, nom: str, espece: str, age: int, sante: int = 100) -> None:
        self.nom = nom
        self.espece = espece
        self.age = age
        self.sante = sante


    def afficher_animal(self):
        """Affiche l'animal de manière lisible."""
        return f"🦁 [{self.espece}] {self.nom} ({self.age} ans, santé: {self.sante}%)"

    @abstractmethod
    def faire_bruit(self):
         pass
    


class Tigre(Animal):
     
    def __init__(self, nom, espece, age):
          super().__init__(nom, espece, age)
        
    def faire_bruit(self):
         print("🐅 RAAAAAHHH!")

class Singe(Animal):
     
    def __init__(self, nom, espece, age):
          super().__init__(nom, espece, age)
        
    def faire_bruit(self):
         print("🐵 Ouh ouh ouh!")

class Pinguin(Animal):
     
    def __init__(self, nom, espece, age):
          super().__init__(nom, espece, age)
        
    def faire_bruit(self):
         print("🐧 Coin coin!")

class Autruche(Animal):
     
    def __init__(self, nom, espece, age):
          super().__init__(nom, espece, age)
        
    def faire_bruit(self):
         print("🦤 Hou hou!")
