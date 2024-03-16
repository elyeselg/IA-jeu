#**************************************************************************************************************

#L'objectif de ce développement est de générer 60 personnages dans le fichier Json au lieu de tous les écrire manuellement
# (le fichier servira de base de données de différents persos à deviner au code principal du jeu)
#Utilisation de la bibliothèque Faker pour génerer des noms aléatoirement pour chaque personnage

#**************************************************************************************************************



import json
import random
from faker import Faker

personnages = []

# Initialiser l'objet Faker
fake = Faker()

# Liste des critères possibles
critères = ["blond", "brune", "rousse", "barbu", "poilu", "lunettes", "chapeau", "cheveux_courts", "taches_rousseurs", "bijoux"]

# Générer 60 personnages avec des critères aléatoires
for i in range(60):
    personnage = {
        "nom": fake.name(),
    }
    for critère in critères:
        personnage[critère] = random.choice([True, False])
    personnages.append(personnage)

# Enregistrer les personnages dans un fichier JSON
with open("personnages.json", "w") as f:
    json.dump(personnages, f, indent=4)

