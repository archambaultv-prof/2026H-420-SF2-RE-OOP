"""
Module refuge - Gestion procédurale du refuge animalier
Un refuge est un dictionnaire: {"animaux": [...], "nom": "...", "capacite": N}
"""

import animal

class Refuge:
    def __init__(self, nom : str, capacite : int = 20):
        self.nom = nom
        self.capacite = capacite
        self.animaux : list[animal.Animal] = []

    def ajouter_animal(self, animal):
        if len(self.animaux) >= self.capacite:
            print(f"❌ Refuge plein! ({self.capacite}/{self.capacite})")
        else:
            self.animaux.append(animal)
    
    def retirer_animal(self, nom):
        cache = None
        for element in self.animaux:
            if element.nom == nom:
                cache = element
        if cache == None:
            print(f"❌ Animal '{nom}' non trouvé")
        else: 
            self.animaux.pop(self.animaux.index(cache))
    
    def retirer_animal_1(self, nom):
        idx = None
        for i, element in enumerate(self.animaux):
            if element.nom == nom:
                idx = i
                break

        if idx == None:
            print(f"❌ Animal '{nom}' non trouvé")
        else: 
            self.animaux.pop(idx)

    def afficher_tous_animaux(self):
        for element in self.animaux:
            print(element.afficher_animal())

