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
    
    print(f"Espèces: {', '.join(animal.ESPECES)}")
    espece = input("Espèce: ").strip()
    if espece not in animal.ESPECES:
        print("❌ Espèce invalide")
        return
    
    try:
        age = int(input("Âge (ans): "))
        if age < 0:
            raise ValueError("Âge doit être positif")
    except ValueError:
        print("❌ Âge invalide")
        return
    try:
        match espece:
            case "Tigre":
                nouvel_animal = animal.Tigre(nom, espece, age)
            case "Singe":
                nouvel_animal = animal.Singe(nom, espece, age)
            case "Pingouin":
                nouvel_animal = animal.Pingouin(nom, espece, age)
            case "Autruche":
                nouvel_animal = animal.Autruche(nom, espece, age)
    except ValueError as e:
        print(f"❌ {e}")


def retirer_animal_interactif(mon_refuge: dict) -> None:
    """Retire un animal."""
    nom = input("\nNom à retirer: ").strip()
    if nom:
        refuge.Refuge.retirer_animal(mon_refuge, nom)


def creer_animaux_demo(mon_refuge) -> None:
    """Crée des animaux de démonstration."""
    animaux = [
        animal.Animal.creer_animal("Shere Khan", "Tigre", 8),
        animal.Animal.creer_animal("Rafiki", "Singe", 15),
        animal.Animal.creer_animal("Skipper", "Pingouin", 5),
        animal.Animal.creer_animal("Zazu", "Autruche", 3),
    ]
    for a in animaux:
        refuge.Refuge.ajouter_animal(mon_refuge, a)


def main() -> None:
    """Fonction principale."""
    mon_refuge = refuge.Refuge.creer_refuge("Refuge du Roi Lion", capacite=20)
    
    print("\n🌍 Initialisation du refuge...")
    creer_animaux_demo(mon_refuge)

    while True:
        afficher_menu()
        choix = input("Choix: ").strip()
        
        if choix == "1":
            ajouter_animal_interactif(mon_refuge)
        elif choix == "2":
            refuge.Refuge.afficher_tous_animaux(mon_refuge)
        elif choix == "3":
            retirer_animal_interactif(mon_refuge)
        elif choix == "0":
            print("\n👋 Au revoir!\n")
            break
        else:
            print("❌ Choix invalide\n")


if __name__ == "__main__":
    main()
