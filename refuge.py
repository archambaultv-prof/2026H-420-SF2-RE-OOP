"""
Module refuge - Gestion procédurale du refuge animalier
Un refuge est un dictionnaire: {"animaux": [...], "nom": "...", "capacite": N}
"""
from animal import animal
class Refuge:
    def __init__(self, nom: str, animaux: list = None, capacite: int = 20):
        self.nom = nom
        self.capacite = capacite
        self.animaux = animaux if animaux is not None else []



    def creer_refuge(nom: str, capacite: int = 20) -> dict:
        """Crée un refuge vide."""
        return {"nom": nom, "animaux": [], "capacite": capacite}


    def ajouter_animal(self, animal_tuple: tuple) -> bool:
        """Ajoute un animal au refuge si de la place existe."""
        if len(self.animaux) >= self.capacite:
            print(f"❌ Refuge plein! ({self.capacite}/{self.capacite})")
            return False
        
        self.animaux.append(animal_tuple)
        nom = animal_tuple[animal.NOM]
        espece = animal_tuple[animal.ESPECE]
        print(f"✅ {nom} ({espece}) ajouté au refuge")
        return True


    def retirer_animal(self, nom: str) -> bool:
        """Retire un animal du refuge par son nom."""
        for i, a in enumerate(self.animaux):
            if a[animal.NOM] == nom:
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
            print(f"{i}. {animal.afficher_animal(a)}")
        
        print(f"{'='*70}\n")
