from abc import ABC

#rework of the procedural code to an OOP approach
class Animal(ABC):
    def __init__(self, nom: str,  age: int):
        
        self.nom = nom
        self.espece = None
        self.age = age
    
    def __str__(self):
        return f"🦁 [{self.espece}] {self.nom} ({self.age} ans)"
    def afficher_animal(self):
        """Affiche l'animal de manière lisible."""
        print(self)
    def animal_faire_bruit(self):
       pass

class Tigre(Animal):
    def __init__(self, nom: str, age: int):
        super().__init__(nom,  age)
        self.espece = "tigre"
    def animal_faire_bruit(self):
        return "🐅 RAAAAAHHH!"

class Singe(Animal):
    def __init__(self, nom: str, age: int):
        super().__init__(nom, age)
        self.espece = "singe"
    def animal_faire_bruit(self):
        return "🐵 Ouh ouh ouh!"

class Pingouin(Animal):
    def __init__(self, nom: str, age: int):
        super().__init__(nom, age)
        self.espece = "pingouin"
    def animal_faire_bruit(self):
        return "🐧 Coin coin!"

class Autruche(Animal):
    def __init__(self, nom: str, age: int):
        super().__init__(nom, age)
        self.espece = "autruche"
    def animal_faire_bruit(self):        
        return "🦤 Hou hou!"