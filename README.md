# tp
Casse brique de Pierre BOLZINGER et Guillaume ARIBAUT

Règles du jeu : Le but du jeu est de détruire toutes les briques avec la balle. Vous pouvez bouger la raquette horizontalement. La balle rebondit sur la raquette et sur les briques. Vous perdez une vie si la balle passe sous la raquette.

Lien SSH du GitHub : git@github.com:pixel565/tp.git

gui.py est le programme principal
testgui.py est le programme permettant un lancement rapide du jeu


Implémentations : 
Algorithme de collision cercle-rectangle basé sur le clampage 
Balle rouge respectant la loi de Descartes
Actualision toutes les 50 ms
classe appli (hérité de tkinter)

Améliorations :
Faire une classe niveau pour faire différents niveaux
Diviser le programmes en autres classes/objets
Ligne 167 : fonction brique pour créer la liste des briques
Ligne 75 : test de collision entre la balle et la brique et l'enlève si la brique est touchée
Ligne 58 : déplacement de la boule
Ligne 42 : boucle de jeu


