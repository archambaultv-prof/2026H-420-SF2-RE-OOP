"""
Module main - Interface du gestionnaire de refuge animalier (procédural)
"""

import animal
import refuge


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


def ajouter_animal_interactif(mon_refuge: dict) -> None:
    """Ajoute un animal au refuge."""
    print("\n➕ Ajouter un animal")
    
    nom = input("Nom: ").strip()
    if not nom:
        print("❌ Nom requis")
        return
    
    try:
        age = int(input("Âge (ans): "))
        if age < 0:
            raise ValueError("Âge doit être positif")
    except ValueError:
        print("❌ Âge invalide")
        return
    
    try:
        nouvel_animal = animal.creer_animal(nom, espece, age)
        refuge.ajouter_animal(mon_refuge, nouvel_animal)
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
        animal.creer_animal("Shere Khan", "Tigre", 8, 85),
        animal.creer_animal("Rafiki", "Singe", 15, 75),
        animal.creer_animal("Skipper", "Pingouin", 5, 95),
        animal.creer_animal("Zazu", "Autruche", 3, 80),
    ]
    for a in animaux:
        refuge.ajouter_animal(mon_refuge, a)


def main() -> None:
    """Fonction principale."""
    mon_refuge = refuge.creer_refuge("Refuge du Roi Lion", capacite=20)
    
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
