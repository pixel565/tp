""""
Que fait ce programme : interface graphique  
Auteur : Guillaume Aribaut & Pierre Bolzinger
When : 06/10/2026 à 8h56 (dernière modif: )
To do : 
"""

#Importations bibliothèques

import tkinter as tk
import random as rd
import math

rayon = 15
largeur = 450
hauteur = 400

class appli(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Brick Break")
        self.geometry("500x500")
        self.Canvas=tk.Canvas(self, width=largeur, height=hauteur, bg='black')
        self.Canvas.pack()
    def boule(self):
        self.x = largeur/2
        self.y = hauteur/3
        self.balle = self.Canvas.create_oval(self.x-rayon, self.y-rayon, self.x+rayon, self.y+rayon, fill='red')
        self.vitesse = rd.uniform(1.8,2)*5
        self.angle = rd.uniform(-2*math.pi, 0)
        self.dx = self.vitesse*math.cos(self.angle)
        self.dy = self.vitesse*math.sin(self.angle)
    def deplacementBoule(self):
        """ Déplacement de la balle """
        
        # rebond à droite
        if self.x + rayon + self.dx > largeur:
            self.x = 2*(largeur-rayon)-self.x
            self.dx = -self.dx
        
        # rebond à gauche
        if self.x - rayon + self.dx < 0:
            self.x = 2*rayon-self.x
            self.dx = -self.dx
        
        # rebond en haut
        if self.y - rayon + self.dy < 0:
            self.y = 2*rayon - self.y
            self.dy = -self.dy

        # passage en bas
        if self.y + rayon + self.dy > hauteur:
            self.x = largeur/2
            self.y = hauteur/3
            self.vitesse = rd.uniform(1.8,2)*5
            self.angle = rd.uniform(-2*math.pi, 0)
            self.dx = self.vitesse*math.cos(self.angle)
            self.dy = self.vitesse*math.sin(self.angle)
            #self.pv -=1

    
        self.x = self.x + self.dx
        self.y = self.y + self.dy
        # affichage
        self.Canvas.coords(self.balle,self.x-rayon,self.y-rayon,self.x+rayon,self.y+rayon)
        # mise à jour toutes les 50 ms
        self.after(50,self.deplacementBoule)