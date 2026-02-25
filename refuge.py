"""
Module refuge - Gestion procédurale du refuge animalier
Un refuge est un dictionnaire: {"animaux": [...], "nom": "...", "capacite": N}
"""

class Refuge:

    def __init__(self,nom,animaux:list ,capacite):
        self.nom = nom
        self.animaux = animaux
        self.capacite = capacite


    def ajouter_animal(self,animal):
        if len(self.animaux) >= self.capacite:
            print(f" Refuge plein! il y a deja {self.capacite} animaux")
            return False
        else:
            self.animaux.append(animal)
            print(f" {animal.nom} ({animal.espece}) ajouté au refuge")
            return True
        
    def retirer_animal(self,animal):
        if animal in self.animaux:
            self.animaux.remove(animal)
            print(f" {animal.nom} ({animal.espece}) retiré du refuge")
        else:
            print(f" Animal non trouvé dans le refuge")


    def afficher_tous_animaux(self):
        print(f'Les animaux du refuge {self.nom} sont :')
        for animal in self.animaux :
            print(animal.afficher_annimal())