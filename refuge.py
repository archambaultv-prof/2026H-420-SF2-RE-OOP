"""
Module refuge - Gestion procédurale du refuge animalier
Un refuge est un dictionnaire: {"animaux": [...], "nom": "...", "capacite": N}
"""


from animal import Animal


class Refuge:

    def __init__(self, nom: str, animaux: list [Animal], capacite: int = 20):

        self.nom = nom
        self.capacite = capacite
        self.animaux = animaux


    def ajouter_animal(self, animal: Animal) -> bool:
        """Ajoute un animal au refuge si de la place existe."""
        if len(self.animaux) >= self.capacite:
            print(f"❌ Refuge plein! ({self.capacite}/{self.capacite})")
            return False

        self.animaux.append(animal)
        print(f"✅ {animal.nom} ({animal.espece}) ajouté au refuge")


    def retirer_animal(self, nom: str) -> bool:
        """Retire un animal du refuge par son nom."""
        for i, a in enumerate(self.animaux):
            if a.nom == nom:
                self.animaux.pop(i)
                print(f"✅ {nom} retiré du refuge")
                return True
            else:
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
        
        for i, a in enumerate(self.animaux):
            print(f"{i}. {a.afficher_animal()}")
        
        print(f"{'='*70}\n")



