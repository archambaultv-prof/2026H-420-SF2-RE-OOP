"""
Module animal - Gestion procédurale des animaux du refuge
Représentation sous forme de tuple: (nom, espèce, âge, santé)
"""
from abc import ABC, abstractmethod
ESPECES = ["Tigre", "Singe", "Pingouin", "Autruche"]
# Indices du tuple animal
class animal(ABC):
    def __init__(self,NOM,ESPECE,AGE):
        self.NOM = NOM
        self.ESPECE = ESPECE
        self.AGE = AGE
        
        



    def afficher_animal(self) -> str:
        """Affiche l'animal de manière lisible."""
        return f"🦁 [{self.ESPECE}] {self.NOM} ({self.AGE}ans)"

    @abstractmethod
    def animal_faire_bruit(self) -> str:
        
        pass
        
class tigre(animal):
    def animal_faire_bruit(self, animal):
        return "Grrr! Je suis un tigre!"
class singe(animal):
    def animal_faire_bruit(self, animal):
        return "Ooh ooh! Je suis un singe!"
class pingouin(animal):
    def animal_faire_bruit(self, animal):
        return "Squawk! Je suis un pingouin!"
class autruche(animal):
    def animal_faire_bruit(self, animal):
        return "Honk! Je suis une autruche!"