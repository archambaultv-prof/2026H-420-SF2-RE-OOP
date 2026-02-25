"""
Module animal - Gestion procédurale des animaux du refuge
Représentation sous forme de tuple: (nom, espèce, âge, santé)
"""

from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nom: str, espece: str, age: int, sante: int = 100):
        self.nom = nom
        self.espece = espece
        self.age = age
        self.sante = sante
        if not 0 <= self.sante <= 100:
            raise ValueError("Santé doit être entre 0 et 100")

    @abstractmethod
    def faire_bruit(self) -> str:
        pass


    def afficher(self) -> str:
        """Affiche l'animal de manière lisible."""
        return f"[{self.espece}] {self.nom} ({self.age}ans, santé: {self.sante}%)"


class Tigre(Animal):
    def __init__(self, nom: str, age: int, sante: int = 100):
        super().__init__(nom, "Tigre", age, sante)

    def faire_bruit(self) -> str:
        return "🐅 RAAAAAHHH!"

    def afficher(self) -> str:
        s = super().afficher()
        return f"🐅 {s}"

class Singe(Animal):
    def __init__(self, nom: str, age: int, sante: int = 100):
        super().__init__(nom, "Singe", age, sante)

    def faire_bruit(self) -> str:
        return "🐵 Ouh ouh ouh!"

    def afficher(self) -> str:
        s = super().afficher()
        return f"🐵 {s}"

class Pingouin(Animal):
    def __init__(self, nom: str, age: int, sante: int = 100):
        super().__init__(nom, "Pingouin", age, sante)

    def faire_bruit(self) -> str:
        return "🐧 Coin coin!"

    def afficher(self) -> str:
        s = super().afficher()
        return f"🐧 {s}"

class Autruche(Animal):
    def __init__(self, nom: str, age: int, sante: int = 100):
        super().__init__(nom, "Autruche", age, sante)

    def faire_bruit(self) -> str:
        return "🦤 Hou hou!"

    def afficher(self) -> str:
        s = super().afficher()
        return f"🦤 {s}"

class AnimalFactory:
    ESPECES = {"Tigre": Tigre, "Singe": Singe, "Pingouin": Pingouin, "Autruche": Autruche}

    @staticmethod
    def creer_animal(nom: str, espece: str, age: int, sante: int = 100) -> Animal:
        if espece not in AnimalFactory.ESPECES:
            raise ValueError(f"Espèce '{espece}' non reconnue")
        
        cls = AnimalFactory.ESPECES[espece]
        return cls(nom, age, sante)

class AnimalFactoryV2:
    _registry: dict[str, type[Animal]] = {}

    @classmethod
    def enregistrer(cls, espece: str, animal_cls: type[Animal]) -> None:
        cls._registry[espece] = animal_cls

    @classmethod
    def creer_animal(cls, espece: str, *args, **kwargs) -> Animal:
        if espece not in cls._registry:
            raise ValueError(f"Espèce '{espece}' non reconnue")
        
        animal_cls = cls._registry[espece]
        return animal_cls(*args, **kwargs)

if __name__ == "__main__":
    # Test de la factory V2
    # Enregistrement des classes d'animaux
    AnimalFactoryV2.enregistrer("Tigre", Tigre)
    AnimalFactoryV2.enregistrer("Singe", Singe)
    AnimalFactoryV2.enregistrer("Pingouin", Pingouin)
    AnimalFactoryV2.enregistrer("Autruche", Autruche)

    a1 = AnimalFactoryV2.creer_animal("Tigre", "Shere Khan", 8, 85)
    print(a1.afficher())