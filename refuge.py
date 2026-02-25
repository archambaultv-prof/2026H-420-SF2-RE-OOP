"""
Module refuge - Gestion procédurale du refuge animalier
Un refuge est un dictionnaire: {"animaux": [...], "nom": "...", "capacite": N}
"""

import animal


def creer_refuge(nom: str, capacite: int = 20) -> dict:
    """Crée un refuge vide."""
    return {"nom": nom, "animaux": [], "capacite": capacite}


def ajouter_animal(refuge: dict, animal_tuple: tuple) -> bool:
    """Ajoute un animal au refuge si de la place existe."""
    if len(refuge["animaux"]) >= refuge["capacite"]:
        print(f"❌ Refuge plein! ({refuge['capacite']}/{refuge['capacite']})")
        return False
    
    refuge["animaux"].append(animal_tuple)
    nom = animal_tuple[animal.NOM]
    espece = animal_tuple[animal.ESPECE]
    print(f"✅ {nom} ({espece}) ajouté au refuge")
    return True


def retirer_animal(refuge: dict, nom: str) -> bool:
    """Retire un animal du refuge par son nom."""
    for i, a in enumerate(refuge["animaux"]):
        if a[animal.NOM] == nom:
            refuge["animaux"].pop(i)
            print(f"✅ {nom} retiré du refuge")
            return True
    
    print(f"❌ Animal '{nom}' non trouvé")
    return False


def afficher_tous_animaux(refuge: dict) -> None:
    """Affiche tous les animaux du refuge."""
    if not refuge["animaux"]:
        print(f"\n📍 {refuge['nom']} est vide\n")
        return
    
    print(f"\n{'='*70}")
    print(f"📍 {refuge['nom']} - {len(refuge['animaux'])}/{refuge['capacite']} animaux")
    print(f"{'='*70}")
    
    for i, a in enumerate(refuge["animaux"], 1):
        print(f"{i}. {animal.afficher_animal(a)}")
    
    print(f"{'='*70}\n")

class Refuge:
    def __init__(self, nom, capacite, animaux=[]):
        self.nom = nom
        self.animaux = animaux
        self.capacite = capacite
    
    def ajouter_animal(self, animal: animal.Animal) -> bool:
        if len(self.animaux) >= self.capacite:
            print(f"❌ Refuge plein! ({self.capacite}/{self.capacite})")
            return False
        
        self.animaux.append(animal.nom)
        nom = animal.nom
        espece = animal.espece
        print(f"✅ {nom} ({espece}) ajouté au refuge")
        return True

    def retirer_animal(self, animal: str) -> bool:
        """Retire un animal du refuge par son nom."""
        for i in self.animaux:
            if i == animal:
                self.animaux.pop(i)
                print(f"✅ {animal} retiré du refuge")
                return True
        
        print(f"❌ Animal '{animal}' non trouvé")
        return False

    def afficher_tous_animaux(self):
        for i in self.animaux:
            print(animal.afficher_animal(self.i))
