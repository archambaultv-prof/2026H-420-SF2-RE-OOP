"""
Module refuge - Gestion procédurale du refuge animalier
Un refuge est un dictionnaire: {"animaux": [...], "nom": "...", "capacite": N}
"""

import animal


class Refuge:
    def __init__(self, nom: str, animaux: list, capacite: int):
        self.nom = nom
        self.capacite = capacite
        self.animaux = animaux

    def ajouter_animal(self, animal: animal.Animal) -> bool:
        if len(self.animaux) >= self.capacite:
            print(f"❌ Refuge plein! ({self.capacite}/{self.capacite})")
        
        else:
            self.animaux.append(animal)
            print(f"✅ {animal.nom} ({animal.espece}) ajouté au refuge")

    def retirer_animal(self, nom: str) -> bool:
        for i, a in enumerate(self.animaux):
            if a.nom == nom:
                self.animaux.pop(i)
                print(f"✅ {nom} retiré du refuge")

            else:
                print(f"❌ Animal '{nom}' non trouvé")

    def afficher_tous_animaux(self, nom: str, animaux: list) -> None:
        """Affiche tous les animaux du refuge."""
        if not animaux:
            print(f"\n📍 {nom} est vide\n")

        else:
            print(f"\n📍 {nom} - {len(animaux)}/{self.capacite} animaux")
            print(f"{'='*70}")

            for i, a in enumerate(animaux, 1):
                print(f"{i}. {animal.afficher_animal(a)}")
    
            print(f"{'='*70}\n")