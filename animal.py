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
    def animal_faire_bruit(self):
        pass
    
    def se_nourrir(self):
        print(f"{self.nom} se nourrit.")

    def viellir(self):
        print(f"{self.nom} vieillit.")

class Tigre(Animal):
    def __init__(self, nom, espece, age, sante):
        super().__init__(nom, espece, age, sante)

    def animal_faire_bruit(self):
        return "Roar!"
    
class Singe(Animal):
    def __init__(self, nom, espece, age, sante):
        super().__init__(nom, espece, age, sante)

    def animal_faire_bruit(self):
        return "Ouh ouh!"
    
class Pingouin(Animal):
    def __init__(self, nom, espece, age, sante):
        super().__init__(nom, espece, age, sante)

    def animal_faire_bruit(self):
        return "Coin coin!"
    
class Autruche(Animal):
    def __init__(self, nom, espece, age, sante):
        super().__init__(nom, espece, age, sante)

    def animal_faire_bruit(self):
        return "Hou hou!"
    