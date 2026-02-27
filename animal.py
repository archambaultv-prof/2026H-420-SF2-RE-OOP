"""
Module animal - Gestion procédurale des animaux du refuge
Représentation sous forme de tuple: (nom, espèce, âge, santé)
"""
class Animal:

    def __init__(self, nom: str, espece: str, age: int, sante: int):
        self.nom = nom
        self.espece = espece
        self.age = 2
        self.sante = 100

class Tigre(Animal):
    def __init__(self, nom: str, age: int, sante: int = 100):
        super().__init__(nom, "Tigre", age, sante)
    def faire_bruit(self):
        return "🐅 RAAAAAHHH!"

class Singe(Animal):
    def __init__(self, nom: str, age: int, sante: int = 100):
        super().__init__(nom, "Singe", age, sante)
    def faire_bruit(self):
        return "🐵 Ouh ouh ouh!"

class Pingouin(Animal):
     def __init__(self, nom: str, age: int, sante: int = 100):
        super().__init__(nom, "Pingouin", age, sante)
     def faire_bruit(self):
        return "🐧 Coin coin!"

class Autruche(Animal):
     def __init__(self, nom: str, age: int, sante: int = 100):
        super().__init__(nom, "Autruche", age, sante)
     def faire_bruit(self):
        return "🦤 Hou hou!"
