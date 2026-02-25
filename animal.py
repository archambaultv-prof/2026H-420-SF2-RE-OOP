"""
Module animal - Gestion procédurale des animaux du refuge
Représentation sous forme de tuple: (nom, espèce, âge, santé)
"""
from abc import ABC, abstractmethod

ESPECES = ["Tigre", "Singe", "Pingouin", "Toucan"]


def creer_animal(nom: str, espece: str, age: int, sante: int = 100) -> tuple:
    """Crée un animal: (nom, espèce, âge, santé)"""
    if espece not in ESPECES:
        raise ValueError(f"Espèce invalide. Choisir parmi: {ESPECES}")
    if not 0 <= sante <= 100:
        raise ValueError("Santé doit être entre 0 et 100")
    match espece:
        case "Tigre":
            return Tigre(nom, age, sante)
        case "Singe":
            return Singe(nom, age, sante)
        case "Pingouin":
            return Pingouin(nom, age, sante)
        case "Toucan":
            return Toucan(nom, age, sante)



class Animal(ABC):
    def __init__(self, nom, espece, age, santé):
        self.nom = nom
        self.espece = espece
        self.age = age
        self.santé = santé
    
    def afficher_animal(self: Animal) -> str:
        """Affiche l'animal de manière lisible."""
        return f"[{self.espece}] {self.nom} ({self.age}ans, santé: {self.santé}%)"
    
    @abstractmethod
    def faire_bruit(self):
        pass

class Tigre(Animal):
    def __init__(self, nom, age, santé):
        super().__init__(nom, age, santé)
        self.espece = "Tigre"
    
    def afficher_animal(self: Tigre) -> str:
        return f"🐅{super().afficher_animal()}"
    
    def faire_bruit():
        return f"🐅 RAAAAAWWRR!"

class Singe(Animal):
    def __init__(self, nom, age, santé):
        super().__init__(nom, age, santé)
        self.espece = "Singe"

    def afficher_animal(self: Tigre) -> str:
        return f"🐒{super().afficher_animal()}"
    
    def faire_bruit():
        return f"🐒 ME AND MY MONKEY, MANKEY DOESN'T WEAR ANY PANT!"


class Pingouin(Animal):
    def __init__(self, nom, age, santé):
        super().__init__(nom, age, santé)
        self.espece = "Pingouin"

    def afficher_animal(self: Tigre) -> str:
        return f"🐧{super().afficher_animal()}"
    
    def faire_bruit():
        return f"🐧 Yes Rico, KABOOM"


class Toucan(Animal):
    def __init__(self, nom, age, santé):
        super().__init__(nom, age, santé)
        self.espece = "Toucan"

    def afficher_animal(self: Tigre) -> str:
        return f"🐦‍⬛{super().afficher_animal()}"
    
    def faire_bruit():
        return f"🐦‍⬛ TAH, TAH, TAH"

