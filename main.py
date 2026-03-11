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
    
    refuge.ajouter_animal(mon_refuge, nom, espece, age, sante=100)

def retirer_animal_interactif(mon_refuge: dict) -> None:
    """Retire un animal."""
    nom = input("\nNom à retirer: ").strip()
    if nom:
        refuge.retirer_animal(mon_refuge, nom)

def main() -> None:
    """Fonction principale."""
    animaux = [
        ("Shere Khan", "Tigre", 8, 85),
        ("Rafiki", "Singe", 15, 75),
        ("Skipper", "Pingouin", 5, 95),
        ("Zazu", "Autruche", 3, 80),
    ]

    mon_refuge = refuge.Refuge("Refuge de la Jungle", animaux, 10)
    
    print("\n🌍 Initialisation du refuge...")
    refuge.afficher_tous_animaux(mon_refuge)

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