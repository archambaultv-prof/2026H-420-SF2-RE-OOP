"""
Module refuge - Gestion procédurale du refuge animalier
Un refuge est un dictionnaire: {"animaux": [...], "nom": "...", "capacite": N}
"""

import animal

class Refuge:
    def __init__(self, nom, animaux: list, capacite):
        self.nom = nom
        self.animaux = animaux
        self.capacite = capacite

    def ajouter_animal(self, animal_ajoute):
        if len(self.animaux) >= self.capacite:
            print(f"❌ Refuge plein! ({self.capacite}/{self.capacite} animaux)")
            return False
        else:
            self.animaux.append(animal_ajoute)
            print(f"✅ {animal_ajoute} ajouté au refuge")
            return True

    def retirer_animal(self, animal_retire):
        for i in range(len(self.animaux)):
            if self.animaux[i] == animal_retire:
                self.animaux.remove(self.animaux[i])
                print(f"✅ {animal_retire} retiré du refuge")
                return True
    
        print(f"❌ Animal '{animal_retire}' non trouvé")
        return False

    def afficher_tous_animaux(self):
        if self.animaux == 0:
            print(f"Le refuge est vide")
            return False
        else:
            for i in range(len(self.animaux)):
                print(f"{self.animaux[i]}")