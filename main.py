"""
Module main - Interface du gestionnaire de refuge animalier (procédural)
"""

from animal import Animal, Tigre, Singe, Pingouin, Autruche
from refuge import Refuge

ESPECES = ["Tigre", "Singe", "Pingouin", "Autruche"]

def afficher_menu() -> None:
    """Affiche le menu principal."""
    print(f"\n{'='*60}")
    print("🦁 GESTIONNAIRE DE REFUGE ANIMALIER")
    print(f"{'='*60}")
    print("1. Ajouter un animal")
    print("2. Afficher tous les animaux")
    print("3. Retirer un animal")
    print(f"{'='*60}\n")


def ajouter_animal_interactif(mon_refuge: dict) -> None:
    """Ajoute un animal au refuge."""
    print("\n➕ Ajouter un animal")
    
    nom = input("Nom: ").strip()
    if not nom:
        print("❌ Nom requis")
        return
    
    print(f"Espèce: {', '.join(ESPECES)}")
    espece = input("Espèce: ").strip()
    if espece not in ESPECES:
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
        nouvel_animal = Animal(nom, espece, age)
        Refuge.ajouter_animal(nouvel_animal)
    except ValueError as e:
        print(f"❌ {e}")


def retirer_animal_interactif(mon_refuge: dict) -> None:
    """Retire un animal."""
    nom = input("\nNom à retirer avec espèce (ex: Bibi(Pingouin)): ").strip()
    if nom:
        Refuge.retirer_animal(nom)


def main() -> None:
    """Fonction principale."""
    mon_refuge = Refuge("Refuge du Roi Lion", [], capacite=20)
    
    print("\n🌍 Initialisation du refuge...")
    
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
