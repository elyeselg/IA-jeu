
#**************************************************************************************************************

# L'objectif de ce développement est de propser le jeu du "qui est ce" dont les principales étapes sont:
# Charger les personnages à partir du fichier JSON (voir fichier Json pour les personnages et fichier genPerso.py qui génére aléatoirement des personnages avec noms et caractéristiques)
# Choisir un personnage mystère
# Fonction pour poser une question à l'utilisateur
# Fonction pour trouver le personnage mystère
# Fonctions pour gérer l'interface tkinter (lancement du jeu, cases pour les questions, affichage liste persos...)

#**************************************************************************************************************


#import des bibliothèques nécessaires:
import random
import json
import tkinter as tk
from tkinter import messagebox

# Charger les personnages à partir du fichier JSON
with open("personnages.json") as f:
    personnages = json.load(f)

# Choisir un personnage mystère
personnage_mystere = random.choice(personnages)

# Fonction pour poser une question à l'utilisateur
def poser_question(caracteristique):
    reponse = messagebox.askyesno("Question", "Est-ce que le personnage est ou a " + caracteristique + " ?")
    return reponse

# Fonction pour trouver le personnage mystère
def trouver_personnage():
    # Initialisation de la liste de personnages possibles
    personnages_possibles = list(personnages)

    # Boucle jusqu'à ce qu'il ne reste qu'un seul personnage possible
    while len(personnages_possibles) > 1:
        # Choisir une caractéristique aléatoire
        caracteristique = random.choice(list(personnage_mystere.keys())[1:])
        # Poser la question à l'utilisateur
        reponse_utilisateur = poser_question(caracteristique)
        # Mettre à jour la liste de personnages possibles
        personnages_possibles = [p for p in personnages_possibles if p[caracteristique] == reponse_utilisateur]

    # Afficher le personnage mystère trouvé
    messagebox.showinfo("Résultat", "Le personnage mystère est : " + personnages_possibles[0]["nom"])
    
    
    # Fonction pour afficher la liste des personnages
def afficher_liste_personnages():
    liste_personnages = "\n".join([personnage["nom"] for personnage in personnages])
    messagebox.showinfo("Liste des personnages", liste_personnages)


# Créer la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Qui est-ce?")

# Créer un cadre pour afficher le personnage mystère
cadre_personnage = tk.Frame(fenetre, bd=5, relief=tk.RIDGE, bg="white")
cadre_personnage.pack(pady=10)

# Afficher le personnage mystère
label_personnage = tk.Label(cadre_personnage, text="Personnage mystère", font=("Arial", 16, "bold"), padx=20, pady=20)
label_personnage.pack()

# Créer un cadre pour les boutons de caractéristiques
cadre_boutons = tk.Frame(fenetre)
cadre_boutons.pack(pady=10)

# Couleurs des boutons de caractéristiques
couleurs_boutons = ["red", "green", "blue", "yellow", "orange","pink","gray","purple","brown","white"]

# Créer les boutons de caractéristiques
for i, caract in enumerate(list(personnage_mystere.keys())[1:]):
    bouton = tk.Button(cadre_boutons, text=caract, width=10, height=2, bg=couleurs_boutons[i])
    bouton.pack(side=tk.LEFT, padx=5)

    # Lier le bouton à la fonction poser_question
    bouton.config(command=lambda caract=caract: poser_question(caract))

# Créer un bouton pour lancer le jeu
bouton_jouer = tk.Button(fenetre, text="Jouer", font=("Arial", 14, "bold"), width=15, height=2, bg="gray", fg="white", command=trouver_personnage)
bouton_jouer.pack(pady=10)

# Créer un bouton pour afficher la liste des personnages
bouton_liste = tk.Button(fenetre, text="Afficher la liste des personnages", font=("Arial", 12), width=25, height=2, bg="gray", fg="white", command=afficher_liste_personnages)
bouton_liste.pack(pady=10)

# Lancer la boucle principale de l'interface utilisateur
fenetre.mainloop()
