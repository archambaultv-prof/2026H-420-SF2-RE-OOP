# 🦁 Gestionnaire de Refuge Animalier

## Test pour montrer comment faire une pull request

## 📋 Tâche

Transformer ce code 100% procédural (tuples + dicts + fonctions) en code
**orienté objet** (classes + héritage + polymorphisme).

### Étape 1 : Créer une classe `Animal`
- Transformer les tuples en classe `Animal` avec attributs : `nom`, `espece`, `age`, `sante`
- Implémenter les méthodes : `se_nourrir()`, `vieillir()`, `faire_bruit()`
- Utiliser `ABC` (Abstract Base Class) pour garantir une interface non instanciable
- La méthode `faire_bruit()` doit être généralisée pour chaque espèce et donc
  être une méthode abstraite

### Étape 2 : Créer les sous-classes polymorphes
- Créer 4 sous-classes : `Tigre`, `Singe`, `Pingouin`, `Autruche`
- Chaque sous-classe redéfinit `faire_bruit()` pour faire un bruit différent

### Étape 3 : Créer une classe `Refuge`
- Remplacer le dict par une classe `Refuge`
- Attributs : `nom`, `animaux`, `capacite`
- Methodes : `ajouter_animal()`, `retirer_animal()`, `afficher_tous_animaux()`

### Étape 4 : Adapter main.py
- Remplacer les appels procéduraux par les appels OOP
- Utiliser directement les instances de classe au lieu des tuples

## 🚀 Installation & Exécution

D'abord, faite une duplication (fork) du repo sur votre compte GitHub. Cela
permet de faire vos modifications sans affecter le repo original et de
soumettre une pull request à la fin. Vous pouvez faire le fork en cliquant sur
 le bouton "Fork" en haut à droite de la page du repo.
 
  ![image](fork.png)

Ensuite, clonez votre fork localement sur votre machine et suivez les étapes
ci-dessous pour lancer le programme.

```powershell
# 1. Créer le venv et installer dépendances (une seule fois)
python -m venv .venv

# 2. Activer le venv
.venv\Scripts\activate

# 3. Lancer le programme
python main.py
```
