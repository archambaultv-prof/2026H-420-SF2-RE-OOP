"""
Module main - Interface du gestionnaire de refuge animalier (procédural)
"""

from animal import Animal, Tigre, Singe, Pingouin, Autruche
from refuge import Refuge

mon_refuge = Refuge("Refuge du Roi Lion", [], 6)

def afficher_menu() -> None:
    """Affiche le menu principal."""
    print(f"\n{'='*60}")
    print("🦁 GESTIONNAIRE DE REFUGE ANIMALIER")
    print(f"{'='*60}")
    print("1. Ajouter un animal")
    print("2. Afficher tous les animaux")
    print("3. Retirer un animal")
    print("0. Quitter")
    print(f"{'='*60}\n")


def ajouter_animal_interactif() -> None:
    """Ajoute un animal au refuge."""
    print("\n➕ Ajouter un animal")
    
    nom = input("Nom: ").strip()
    if not nom:
        print("❌ Nom requis")
        return
    
    print(f"Espèces: Tigre, Singe, Pingouin, Autruche")
    espece = input("Espèce: ").strip()
    if espece not in ["Tigre", "Singe", "Pingouin", "Autruche"]:
        print("❌ Espèce invalide")
        return
    
    try:
        age = int(input("Âge (ans): "))
        if age < 0:
            raise ValueError("Âge doit être positif")
    except ValueError:
        print("❌ Âge invalide")
        return
    
    if espece == "Tigre":
        nouvel_animal = Tigre(nom, age, 100)
    elif espece == "Singe":
        nouvel_animal = Singe(nom, age, 100)
    elif espece == "Pingouin":
        nouvel_animal = Pingouin(nom, age, 100)
    elif espece == "Autruche":
        nouvel_animal = Autruche(nom, age, 100)

    try:
        mon_refuge.ajouter_animal(nouvel_animal)
    except ValueError as e:
        print(f"❌ {e}")


def retirer_animal_interactif(mon_refuge: dict) -> None:
    """Retire un animal."""
    nom = input("\nNom à retirer: ").strip()
    if nom:
        refuge.retirer_animal(mon_refuge, nom)


def creer_animaux_demo(mon_refuge: dict) -> None:
    """Crée des animaux de démonstration."""
    animaux = [
        Tigre("Shere Khan", "Tigre", 8, 85),
        Singe("Rafiki", 15, 75),
        Pingouin("Skipper", 5, 95),
        Autruche("Zazu", 3, 80),
    ]
    for a in animaux:
        mon_refuge.ajouter_animal(a)


def main() -> None:
    
    print("\n🌍 Initialisation du refuge...")
    creer_animaux_demo(mon_refuge)
    
    while True:
        afficher_menu()
        choix = input("Choix: ").strip()
        
        if choix == "1":
            ajouter_animal_interactif(mon_refuge)
        elif choix == "2":
            refuge.afficher_tous_animaux(mon_refuge)
        elif choix == "3":
            retirer_animal_interactif(mon_refuge)
        elif choix == "0":
            print("\n👋 Au revoir!\n")
            break
        else:
            print("❌ Choix invalide\n")


if __name__ == "__main__":
    main()
