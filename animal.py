from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nom: str, espece: str, age: int, sante: int = 100):
        self.nom = nom
        self.espece = espece
        self.age = age
        self.sante = sante

    @abstractmethod
    def faire_bruit(self) -> str:
        pass


class Tigre(Animal):
    def __init__(self, nom: str, age: int, sante: int = 100):
        super().__init__(nom, "Tigre", age, sante)

    def faire_bruit(self) -> str:
        return "🐅 RAAAAAHHH!"

class Singe(Animal):
    def __init__(self, nom: str, age: int, sante: int = 100):
        super().__init__(nom, "Singe", age, sante)

    def faire_bruit(self) -> str:
        return "🐵 Ouh ouh ouh!"
    
class Pingouin(Animal):
    def __init__(self, nom: str, age: int, sante: int = 100):
        super().__init__(nom, "Pingouin", age, sante)

    def faire_bruit(self) -> str:
        return "🐧 Coin coin!"

class Autruche(Animal):
    def __init__(self, nom: str, age: int, sante: int = 100):
        super().__init__(nom, "Autruche", age, sante)

    def faire_bruit(self) -> str:
        return "🦤 Hou hou!"
