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


def ajouter_animal_interactif(mon_refuge) -> None:
    """Ajoute un animal au refuge."""
    especes = ["Tigre", "Singe","Pingouin","Autruche"]
    print("\n➕ Ajouter un animal")
    
    nom = input("Nom: ").strip()
    if not nom:
        print("❌ Nom requis")
        return
    
    print(f"Espèces: {', '.join(especes)}")
    espece = input("Espèce: ").strip()
    if espece not in especes:
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
                nouvel_animal = animal.Tigre(nom, age)
            case "Singe":
                nouvel_animal = animal.Singe(nom, age)
            case "Pingouin":
                nouvel_animal = animal.Pingouin(nom, age)
            case "Autruche":
                nouvel_animal = animal.Autruche(nom, age)
        mon_refuge.ajouter_animal(nouvel_animal)
    except ValueError as e:
        print(f"❌ {e}")


def retirer_animal_interactif(mon_refuge) -> None:
    """Retire un animal."""
    nom = input("\nNom à retirer: ").strip()
    if nom:
        mon_refuge.retirer_animal(nom)


def creer_animaux_demo(mon_refuge) -> None:
    """Crée des animaux de démonstration."""
    mon_refuge.ajouter_animal(animal.Tigre("Shere Khan", 8, 85))
    mon_refuge.ajouter_animal(animal.Singe("Rafiki", 15, 75))
    mon_refuge.ajouter_animal(animal.Pingouin("Skipper", 5, 95))
    mon_refuge.ajouter_animal(animal.Autruche("Zazu", 3, 80))


def main() -> None:
    """Fonction principale."""
    mon_refuge = refuge.Refuge("Refuge du Roi Lion", capacite=20)
    
    print("\n🌍 Initialisation du refuge...")
    creer_animaux_demo(mon_refuge)
    
    while True:
        afficher_menu()
        choix = input("Choix: ").strip()
        
        if choix == "1":
            ajouter_animal_interactif(mon_refuge)
        elif choix == "2":
            mon_refuge.afficher_tous_animaux()
        elif choix == "3":
            retirer_animal_interactif(mon_refuge)
        elif choix == "0":
            print("\n👋 Au revoir!\n")
            break
        else:
            print("❌ Choix invalide\n")


if __name__ == "__main__":
    main()
