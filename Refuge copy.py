"""
Module refuge - Gestion procédurale du refuge Animalier
Un refuge est un dictionnaire: {"animaux": [...], "nom": "...", "capacite": N}
"""

import Animal
class refuge:

    def __init__(self, nom: str, capacite: int):
        self.nom = nom
        self.animaux = []
        self.capacite = capacite



    def ajouter_Animal(self, Animal_tuple = Animal.animal) -> bool:
        """Ajoute un Animal au refuge si de la place existe."""
        if len(self.animaux) >= self.capacite:
            print(f"❌ Refuge plein! ({self.capacite}/{self.capacite})")
            return False

        self.animaux.append(Animal_tuple)
        nom = Animal_tuple.NOM
        espece = Animal_tuple.ESPECE
        print(f"✅ {nom} ({espece}) ajouté au refuge")
        return True


    def retirer_Animal(self, nom: str) -> bool:
        """Retire un Animal du refuge par son nom."""
        for i, a in enumerate(self.animaux):
            if a[Animal.animal.NOM] == nom:
                self.animaux.pop(i)
                print(f"✅ {nom} retiré du refuge")
                return True
        
        print(f"❌ Animal '{nom}' non trouvé")
        return False


    def afficher_tous_animaux(self) -> None:
        """Affiche tous les animaux du refuge."""
        if not self.animaux:
            print(f"\n📍 {self.nom} est vide\n")
            return
        
        print(f"\n{'='*70}")
        print(f"📍 {self.nom} - {len(self.animaux)}/{self.capacite} animaux")
        print(f"{'='*70}")

        for i, a in enumerate(self.animaux, 1):
            print(f"{i}. {Animal.animal.afficher_animal(a)}")
        
        print(f"{'='*70}\n")