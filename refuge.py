
from animal import Animal


class Refuge:

    def __init__(self, nom: str, capacite: int = 20):
        self.nom = nom
        self.capacite = capacite
        self.animaux = []

    def ajouter_animal(self, animal: Animal) :
        if len(self.animaux) >= self.capacite:
            print(f"❌ Refuge plein! ({self.capacite}/{self.capacite})")
            return False

        self.animaux.append(animal)
        print(f"✅ {animal.nom} ({animal.espece}) ajouté au refuge")
        return True

    def retirer_animal(self, nom: str) :
        for a in self.animaux:
            if a.nom == nom:
                self.animaux.remove(a)
                print(f"✅ {nom} retiré du refuge")
                return True

        print(f"❌ Animal '{nom}' non trouvé")
        return False

    def afficher_tous_animaux(self) :
        if not self.animaux:
            print(f"\n📍 {self.nom} est vide\n")
            return

        print(f"\n{'='*70}")
        print(f"📍 {self.nom} - {len(self.animaux)}/{self.capacite} animaux")
        print(f"{'='*70}")


