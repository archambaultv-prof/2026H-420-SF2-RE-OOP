"""
Module animal - Gestion procédurale des animaux du refuge
Représentation sous forme de tuple: (nom, espèce, âge, santé)
"""
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, espece : str, nom : str, age : int, sante : int = 100):
        self.nom = nom
        self.age = age
        if not 0 <= sante <= 100:
            raise ValueError("Santé doit être entre 0 et 100")
        else:
            self.sante = sante
        self.espece = espece
    
    def afficher_animal(self):
        return f"🦁 [{self.espece}] {self.nom} ({self.age}ans, santé: {self.sante}%)"

    @abstractmethod
    def animal_faire_bruit(self):
        pass

class Tigre(Animal):
    def __init__(self, nom : str, age : int, sante : int = 100):
        super().__init__("Tigre",nom,age,sante)
    
    def animal_faire_bruit(self):
        return "🐅 RAAAAAHHH!"

class Singe(Animal):
    def __init__(self, nom : str, age : int, sante : int = 100):
        super().__init__("Singe", nom,age,sante)
    
    def animal_faire_bruit(self):
        return "🐵 Ouh ouh ouh!"

class Pingouin(Animal):
    def __init__(self, nom : str, age : int, sante : int = 100):
        super().__init__("Pingouin",nom,age,sante)
    
    def animal_faire_bruit(self):
        return "🐧 Coin coin!"
    
    
class Autruche(Animal):
    def __init__(self, nom : str, age : int, sante : int = 100):
        super().__init__("Autruche", nom,age,sante)
    
    def animal_faire_bruit(self):
        return "🦤 Hou hou!"