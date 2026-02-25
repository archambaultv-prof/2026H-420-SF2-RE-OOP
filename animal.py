

ESPECES = ["Tigre", "Singe", "Pingouin", "Autruche"]


class Animal:

    def __init__(self, nom: str, espece: str, age: int, sante: int = 100):
        if espece not in ESPECES:
            raise ValueError(f"Espèce invalide. Choisir parmi: {ESPECES}")
        if not 0 <= sante <= 100:
            raise ValueError("l'animal doit être vivant")

        self.nom = nom
        self.espece = espece
        self.age = age
        self.sante = sante

    def afficher(self) :
        return f"🦁 [{self.espece}] {self.nom} ({self.age} ans, santé: {self.sante}%)"

    def faire_bruit(self) :
        bruits = {"Tigre": "🐅 RAAAAAHHH!", "Singe": "🐵 Ouh ouh ouh!", "Pingouin": "🐧 Coin coin!", "Autruche": "🦤 Hou hou!"}
        return bruits.get(self.espece, "...")



animal1 = Animal("Rico", "Pingouin", 5)
print(animal1.afficher())
print(animal1.faire_bruit())
animal2 = Animal("Tony", "Tigre", 3)
print(animal2.afficher())
print(animal2.faire_bruit())
      
