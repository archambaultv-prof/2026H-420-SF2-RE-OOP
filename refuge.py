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

    print(f"\n{'=' * 70}")
    print(f"📍 {refuge['nom']} - {len(refuge['animaux'])}/{refuge['capacite']} animaux")
    print(f"{'=' * 70}")

    for i, a in enumerate(refuge["animaux"], 1):
        print(f"{i}. {animal.afficher_animal(a)}")

    print(f"{'=' * 70}\n")


class refuge:
    def __inti__(self, nom, capacite):
        self.nom = nom
        self.capacite = capacite
        self.animal = []

    def ajouter_animal(self, nom):
        self.animal.append(nom)

    def retirer_animal(self, nom):
        self.animal.remove(nom)

    def __str__(self):
        """Affiche tous les animaux du refuge."""
        if not refuge["animaux"]:
            print(f"\n📍 {refuge['nom']} est vide\n")
            return

        print(f"\n{'=' * 70}")
        print(
            f"📍 {refuge['nom']} - {len(refuge['animaux'])}/{refuge['capacite']} animaux"
        )
        print(f"{'=' * 70}")

        for i, a in enumerate(refuge["animaux"], 1):
            print(f"{i}. {animal.afficher_animal(a)}")

        print(f"{'=' * 70}\n")
