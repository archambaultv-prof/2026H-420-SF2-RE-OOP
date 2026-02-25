import animal.py as animal

# rework de la gestion du refuge en OOP approche
class Refuge:
    def __init__(self, nom: str, capacite: int = 20):
        self.nom = nom
        self.animaux = []
        self.capacite = capacite

    def ajouter_animal(self, animal: animal.Animal) -> bool:
        """Ajoute un animal au refuge si de la place existe."""
        if len(self.animaux) >= self.capacite:
            print(f"❌ Refuge plein! ({len(self.animaux)}/{self.capacite})")
            return False
        
        self.animaux.append(animal)
        print(f"✅ {animal.nom} ({animal.espece}) ajouté au refuge")
        return True
    
    def retirer_animal(self, animal: animal.Animal) -> bool:
        """Retire un animal du refuge."""
        if animal in self.animaux:
            self.animaux.remove(animal)
            print(f"✅ {animal.nom} retiré du refuge")
            return True
        print(f"❌ Animal '{animal.nom}' non trouvé")
        return False
    
    def __str__(self):
        return f"\n{'='*70}\n📍 {self.nom} - {len(self.animaux)}/{self.capacite} animaux\n{'='*70}\n"
    
    def afficher_tous_animaux(self) -> None:
        """Affiche tous les animaux du refuge."""
        if not self.animaux:
            print(f"\n📍 {self.nom} est vide\n")
        else:
            print(self)
            for i, animal in enumerate(self.animaux):
                print(f"{i+1}. {animal}")