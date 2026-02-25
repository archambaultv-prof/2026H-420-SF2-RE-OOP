"""
Module refuge - Gestion procédurale du refuge animalier
Un refuge est un dictionnaire: {"animaux": [...], "nom": "...", "capacite": N}
"""

from animal import *

class Refuge:
    def __init__(self, nom: str, animaux: list = [], capacite: int = 20):
        self.nom = nom
        self.animaux = animaux
        self.capacite = capacite

    def ajouter_animal(self, animal) -> bool:
        if len(self.animaux) >= self.capacite:
            print(f"❌ Refuge plein! ({self.capacite}/{self.capacite})")
            return False
        self.animaux.append(animal)
        print(f"✅ {animal.nom} ({animal.espece}) ajouté au refuge")
        return True
    
    def retirer_animal(self, nom: str) -> bool:
        """Retire un animal du refuge par son nom."""
        for animal in self.animaux:
            if animal.nom == nom:
                self.animaux.remove(animal)
                print(f"✅ {nom} retiré du refuge")
                return True
        print(f"❌ Animal '{nom}' non trouvé")
        return False
    
    def afficher_tous_animaux(self):
        """Affiche tous les animaux du refuge."""
        if not self.animaux:
            print(f"\n📍 {self.nom} est vide\n")
            return
        print(f"\n{'='*70}")
        print(f"📍 {self.nom} - {len(self.animaux)}/{self.capacite} animaux")
        print(f"{'='*70}")
        for i in range(1, len(self.animaux)+1):
            print(f"{i}. {self.animaux[i].afficher_animal()}")
        print(f"{'='*70}\n")