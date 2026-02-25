"""
Module animal - Gestion par classes (avec héritage) 
des animaux du refuge
"""

from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nom: str, espece: str, age: int, sante: int = 100):
        self.nom = nom
        self.espece = espece
        self.age = age
        if not 0 <= sante <= 100:
            raise ValueError("Santé doit être entre 0 et 100")
        self.sante = sante

    @abstractmethod
    def faire_bruit(self):
        pass

    def afficher_animal(self) -> str:
        """Affiche l'animal de manière lisible."""
        return f"[{self.espece}] {self.nom} ({self.age}ans, santé: {self.sante}%)"

class Tigre(Animal):
    def __init__(nom: str, espece: str, age: int, sante: int = 100):
        if espece != "Tigre":
            raise ValueError("Espèce invalide.")
        super().__init__(nom, espece, age, sante)

    def faire_bruit(self) -> str:
        return "🐅 RAAAAAHHH!"
    
    def afficher_animal(self) -> str:
        """Affiche l'animal de manière lisible."""
        afficher_sans_emoji = super().afficher_animal()
        return "🐅" + afficher_sans_emoji
    
class Singe(Animal):
    def __init__(nom: str, espece: str, age: int, sante: int = 100):
        if espece != "Singe":
            raise ValueError("Espèce invalide.")
        super().__init__(nom, espece, age, sante)

    def faire_bruit(self) -> str:
        return "🐵 Ouh ouh ouh!"
    
    def afficher_animal(self) -> str:
        """Affiche l'animal de manière lisible."""
        afficher_sans_emoji = super().afficher_animal()
        return "🐵" + afficher_sans_emoji
    
class Pingouin(Animal):
    def __init__(nom: str, espece: str, age: int, sante: int = 100):
        if espece != "Pingouin":
            raise ValueError("Espèce invalide.")
        super().__init__(nom, espece, age, sante)

    def faire_bruit(self) -> str:
        return "🐧 Coin coin!"
    
    def afficher_animal(self) -> str:
        """Affiche l'animal de manière lisible."""
        afficher_sans_emoji = super().afficher_animal()
        return "🐧" + afficher_sans_emoji
    
class Autruche(Animal):
    def __init__(nom: str, espece: str, age: int, sante: int = 100):
        if espece != "Autruche":
            raise ValueError("Espèce invalide.")
        super().__init__(nom, espece, age, sante)

    def faire_bruit(self) -> str:
        return "🦤 Hou hou!"
    
    def afficher_animal(self) -> str:
        """Affiche l'animal de manière lisible."""
        afficher_sans_emoji = super().afficher_animal()
        return "🦤" + afficher_sans_emoji