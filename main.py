"""
Module main - Interface du gestionnaire de refuge animalier (procédural)
"""

import animal
from animal import Animal, Autruche, Pinguin, Singe, Tigre
import refuge
from refuge import Refuge


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
    
    espece = input("Espèce: ").strip()
    if not espece:
        print("❌ Espèce requise")
        return

    try:
        age = int(input("Âge (ans): "))
        if age < 0:
            raise ValueError("Âge doit être positif")
    except ValueError:
        print("❌ Âge invalide")
        return
    
    try:
        nouvel_animal = animal.Animal(nom, espece, age)
        refuge.Refuge.ajouter_animal(nouvel_animal)
    except ValueError as e:
        print(f"❌ {e}")


def retirer_animal_interactif() -> None:
    """Retire un animal."""
    nom = input("\nNom à retirer: ").strip()
    if nom:
        Refuge.retirer_animal(nom)


def creer_animaux_demo() -> None:
    """Crée des animaux de démonstration."""
    animaux = [
    Tigre("Shere Khan", "Tigre", 8, 85),
    Singe("Rafiki", "Singe", 15, 75),
    Pinguin("Skipper", "Pingouin", 5, 95),
    Autruche("Zazu", "Autruche", 3, 80),
    ]
    
    for a in animaux:
        Refuge.ajouter_animal(a)


def main() -> None:
    """Fonction principale."""
    mon_refuge = Refuge("Refuge du Roi Lion", capacite=20)
    
    print("\n🌍 Initialisation du refuge...")
    creer_animaux_demo()

    while True:
        afficher_menu()
        choix = input("Choix: ").strip()
        
        if choix == "1":
            ajouter_animal_interactif(mon_refuge)
        elif choix == "2":
            Refuge.afficher_tous_animaux(mon_refuge)
        elif choix == "3":
            retirer_animal_interactif(mon_refuge)
        elif choix == "0":
            print("\n👋 Au revoir!\n")
            break
        else:
            print("❌ Choix invalide\n")


if __name__ == "__main__":
    main()







