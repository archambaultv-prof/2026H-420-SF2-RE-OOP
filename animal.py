"""
Module animal - Gestion procédurale des animaux du refuge
Représentation sous forme de tuple: (nom, espèce, âge, santé)
"""

from abc import ABC, abstractmethod


# Indices du tuple animal
NOM = 0
ESPECE = 1
AGE = 2
SANTE = 3

ESPECES = ["Tigre", "Singe", "Pingouin", "Autruche"]


def creer_animal(nom: str, espece: str, age: int, sante: int = 100) -> tuple:
    """Crée un animal: (nom, espèce, âge, santé)"""
    if espece not in ESPECES:
        raise ValueError(f"Espèce invalide. Choisir parmi: {ESPECES}")
    elif espece == "Tigre":
        nom = Tigre(nom, espece, age, sante, "🐅")
    elif espece == "Tigre":
        nom = Singe(nom, espece, age, sante, "🐵")
    elif espece == "Tigre":
        nom = Pingouin(nom, espece, age, sante, "🐧")
    elif espece == "Tigre":
        nom = Autruche(nom, espece, age, sante, "🦤")
    if not 0 <= sante <= 100:
        raise ValueError("Santé doit être entre 0 et 100")
    return (nom, espece, age, sante)


def afficher_animal(animal: tuple) -> str:
    """Affiche l'animal de manière lisible."""
    return f"🦁 [{animal[ESPECE]}] {animal[NOM]} ({animal[AGE]}ans, santé: {animal[SANTE]}%)"


def animal_faire_bruit(animal: tuple) -> str:
    """Retourne le bruit selon l'espèce (polymorphisme)."""
    bruits = {
        "Tigre": "🐅 RAAAAAHHH!",
        "Singe": "🐵 Ouh ouh ouh!",
        "Pingouin": "🐧 Coin coin!",
        "Autruche": "🦤 Hou hou!",
    }
    return bruits.get(animal[ESPECE], "...")


class Animal(ABC):
    def __init__(self, nom, espece, age, sante, emot):
        self.nom = nom
        self.espece = espece
        self.age = age
        self.sante = sante
        self.emot = emot

    @abstractmethod
    def faire_bruit(self):
        pass

    def __str__(self):
        return f"[{self.emot}] [{self.espece}] {self.nom} ({self.age}ans, santé: {self.sante}%)"


class Tigre(Animal):
    def __init__(self, nom, espece, age, sante, emot):
        super().__init__(nom, espece, age, sante, emot)

    def faire_bruit(self):
        print("RAAAAAHHH!")

    def __str__(self):
        return super().__str__()


class Singe(Animal):
    def __init__(self, nom, espece, age, sante, emot):
        super().__init__(nom, espece, age, sante, emot)

    def faire_bruit(self):
        print("Ouh ouh ouh!")

    def __str__(self):
        return super().__str__()


class Pingouin(Animal):
    def __init__(self, nom, espece, age, sante, emot):
        super().__init__(nom, espece, age, sante, emot)

    def faire_bruit(self):
        print("Coin coin!")

    def __str__(self):
        return super().__str__()


class Autruche(Animal):
    def __init__(self, nom, espece, age, sante, emot):
        super().__init__(nom, espece, age, sante, emot)

    def faire_bruit(self):
        print("Hou hou!")

    def __str__(self):
        return super().__str__()
