"""
Module refuge - Gestion procédurale du refuge animalier
Un refuge est un dictionnaire: {"animaux": [...], "nom": "...", "capacite": N}
"""

import animal
from animal import Animal

class Refuge:
    def __init__(self, nom: str, animaux: list, capacite: int):
        self.nom = nom
        self.animaux = animaux
        self.capacite = capacite

    def afficher_tous_animaux(self):
        for i in self.animaux:
            print(f" - {i.nom} ({i.espece})")

    def ajouter_animal(self, animal: Animal):
        if len(self.animaux) >= self.capacite:
            print(f"❌ Refuge plein! ({len(self.animaux)}/{self.capacite})")
            return False
        
        self.animaux.append(animal)
        print(f"✅ {animal.nom} ({animal.espece}) ajouté au refuge")
        return True
    
    def retirer_animal(self, nom: str):
        for i in self.animaux:
            if i.nom == nom:
                self.animaux.remove(i)
                print(f"✅ {nom} retiré du refuge")
                return True
        print(f"❌ Animal '{nom}' non trouvé")
        return False


refuge = Refuge("Refuge du Bonheur", [], 3)
tigre = animal.Tigre("Shere Khan", 7)
refuge.ajouter_animal(tigre)
singe = animal.Singe("Charlie", 5)
refuge.ajouter_animal(singe)
pingouin = animal.Pingouin("Pingu", 3)
refuge.ajouter_animal(pingouin)
refuge.afficher_tous_animaux()
refuge.retirer_animal("Charlie")
refuge.afficher_tous_animaux()
