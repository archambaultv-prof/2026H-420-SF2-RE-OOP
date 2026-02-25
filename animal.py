"""
Module animal - Gestion procédurale des animaux du refuge
Représentation sous forme de tuple: (nom, espèce, âge, santé)
"""

# Indices du tuple animal
NOM = 0
ESPECE = 1
AGE = 2
SANTE = 3

ESPECES = ["Tigre", "Singe", "Pingouin", "Autruche"]


def creer_animal(nom: str, espece: str, age: int, sante: int = 100) -> tuple:
    """Crée un animal: (nom, espèce, âge, santé)"""
    if espece not in ESPECES:
        raise ValueError(f"Espèce invalide. Choisir parmi: {ESPECES}")
    if not 0 <= sante <= 100:
        raise ValueError("Santé doit être entre 0 et 100")
    return (nom, espece, age, sante)


def afficher_animal(animal: tuple) -> str:
    """Affiche l'animal de manière lisible."""
    return f"🦁 [{animal[ESPECE]}] {animal[NOM]} ({animal[AGE]}ans, santé: {animal[SANTE]}%)"


def animal_faire_bruit(animal: tuple) -> str:
    """Retourne le bruit selon l'espèce (polymorphisme)."""
    bruits = {
        "Tigre": "🐅 RAAAAAHHH!",
        "Singe": "🐵 Ouh ouh ouh!",
        "Pingouin": "🐧 Coin coin!",
        "Autruche": "🦤 Hou hou!"
    }
    return bruits.get(animal[ESPECE], "...")



