"""
Module refuge - Gestion procédurale du refuge animalier
Un refuge est un dictionnaire: {"animaux": [...], "nom": "...", "capacite": N}
"""

import animal
class Refuge():
    def __init__(self, nom: str, animaux, capacite: int = 20):
        self.nom = nom
        self.animaux = animaux
        self.capacite = capacite

    def creer_refuge(nom: str, capacite: int = 20):
        """Crée un refuge vide."""
        return Refuge(nom, [], capacite)
    def __str__(self):
        return self.nom
    
    def afficher_refuge(self):
        return f"{self.nom}, {self.animaux}"
    
    def ajouter_animal(self, animaux):
        if len(self.animaux) >= self.capacite:
            print(f"❌ Refuge plein! ({self.capacite}/{self.capacite})")
            return False
        self.animaux.append(animaux)
        nom = animaux.nom
        espece = animaux.espece
        print(f"✅ {nom} ({espece}) ajouté au refuge")
        return True


    def retirer_animal(self, nom: str) -> bool:
         """Retire un animal du refuge par son nom."""
         for i in range(len(self.animaux)):
            if self.animaux[i].nom == nom:
               self.animaux.pop(i)
               print(f"✅ {nom} retiré du refuge")
               return True

         print(f"❌ Animal '{nom}' non trouvé")
         return False

    def afficher_tous_animaux(self):
        if not self.animaux:
            print(f"\n📍 {self.nom} est vide\n")
            return
    
        print(f"\n{'='*70}")
        print(f"📍 {self.nom} - {len(self.animaux)}/{self.capacite} animaux")
        for i in range(len(self.animaux)):
            print(self.animaux[i].afficher())
        print(f"{'='*70}\n")