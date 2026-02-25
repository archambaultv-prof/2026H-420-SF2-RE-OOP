"""
Module main - Interface du gestionnaire de Refuge Animalier (procédural)
"""

import Animal
import Refuge
from Animal import animal, tigre, singe, pingouin, autruche


def afficher_menu() -> None:
    """Affiche le menu principal."""
    print(f"\n{'='*60}")
    print("🦁 GESTIONNAIRE DE Refuge AnimalIER")
    print(f"{'='*60}")
    print("1. Ajouter un Animal")
    print("2. Afficher tous les animaux")
    print("3. Retirer un Animal")
    print("0. Quitter")
    print(f"{'='*60}\n")


def ajouter_Animal_interactif(mon_Refuge: Refuge.refuge) -> None:
    """Ajoute un Animal au Refuge."""
    print("\n➕ Ajouter un Animal")
    
    nom = input("Nom: ").strip()
    if not nom:
        print("❌ Nom requis")
        return
    
    print(f"Espèces: {', '.join(Animal.ESPECES)}")
    espece = input("Espèce: ").strip()
    if espece not in Animal.ESPECES:
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
        #placeholder pas envie de faire match case trop paresseux
        nouvel_Animal = Animal.tigre(nom, espece, age)
        mon_Refuge.ajouter_Animal(nouvel_Animal)
    except ValueError as e:
        print(f"❌ {e}")


def retirer_Animal_interactif(mon_Refuge: Refuge.refuge) -> None:
    """Retire un Animal."""
    nom = input("\nNom à retirer: ").strip()
    if nom:
        mon_Refuge.retirer_Animal(nom)


def creer_animaux_demo(mon_Refuge: Refuge.refuge) -> None:
    """Crée des animaux de démonstration."""
    animaux = [
        tigre("Shere Khan", "Tigre", 8, 85),
        singe("Rafiki", "Singe", 15, 75),
        pingouin("Skipper", "Pingouin", 5, 95),
        autruche("Zazu", "Autruche", 3, 80),
    ]
    for a in animaux:
        mon_Refuge.ajouter_Animal(a)


def main() -> None:
    """Fonction principale."""
    mon_Refuge = Refuge.refuge("Refuge du Roi Lion", capacite=20)
    
    print("\n🌍 Initialisation du Refuge...")
    creer_animaux_demo(mon_Refuge)
    
    while True:
        afficher_menu()
        choix = input("Choix: ").strip()
        
        if choix == "1":
            ajouter_Animal_interactif(mon_Refuge)
        elif choix == "2":
            Refuge.refuge.afficher_tous_animaux(mon_Refuge)
        elif choix == "3":
            retirer_Animal_interactif(mon_Refuge)
        elif choix == "0":
            print("\n👋 Au revoir!\n")
            break
        else:
            print("❌ Choix invalide\n")


if __name__ == "__main__":
    main()