"""
Module main - Interface du gestionnaire de refuge animalier (procédural)
"""

from animal import Autruche, Pingouin, Singe, Tigre, AnimalFactory
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


def ajouter_animal_interactif(mon_refuge: Refuge) -> None:
    """Ajoute un animal au refuge."""
    print("\n➕ Ajouter un animal")
    
    nom = input("Nom: ").strip()
    if not nom:
        print("❌ Nom requis")
        return
    
    print(f"Espèces: {', '.join(AnimalFactory.ESPECES)}")
    espece = input("Espèce: ").strip()
    
    try:
        age = int(input("Âge (ans): "))
        if age < 0:
            raise ValueError("Âge doit être positif")
    except ValueError:
        print("❌ Âge invalide")
        return
    
    try:
        nouvel_animal = AnimalFactory.creer_animal(nom, espece, age)
        mon_refuge.ajouter_animal(nouvel_animal)
    except ValueError as e:
        print(f"❌ {e}")


def retirer_animal_interactif(mon_refuge: Refuge) -> None:
    """Retire un animal."""
    nom = input("\nNom à retirer: ").strip()
    if nom:
        mon_refuge.retirer_animal(nom)


def creer_animaux_demo(mon_refuge: Refuge) -> None:
    """Crée des animaux de démonstration."""
    animaux = [
        Tigre("Shere Khan", 8, 85),
        Singe("Rafiki", 15, 75),
        Pingouin("Skipper", 5, 95),
        Autruche("Zazu", 3, 80),
    ]
    for a in animaux:
        mon_refuge.ajouter_animal(a)


def main() -> None:
    """Fonction principale."""
    mon_refuge = Refuge("Refuge du Roi Lion", capacite=20)
    
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
