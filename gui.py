""""
Que fait ce programme : interface graphique  
Auteur : Guillaume Aribaut & Pierre Bolzinger
When : 06/10/2026 à 8h56 (dernière modif: 13/102026 à 10h24)
To do : Faire marcher les fenetres menu et jeu
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
        self.btn_jeu=tk.Button(self, text="Brick Break", command=self.jeu)
        self.btn_options=tk.Button(self, text="Options", command= self.options)
        self.btn_jeu.pack()
        self.btn_options.pack()
        
  
    def options(self):
        opt=tk.Toplevel(self, bg='white')
        opt.geometry('500x500')
        options = tk.Button(self, text="quitter", command=self.destroy)
        options.pack()

    def jeu(self):
        self.jeu = tk.Toplevel(self)
        self.Canvas = tk.Canvas(self.jeu, width=largeur, height=hauteur, bg="black")
        self.Canvas.pack()
        self.raquette()
        self.boule()
        

    def boule(self):
        self.xb = largeur / 2
        self.yb = hauteur *2 / 3
        self.balle = self.Canvas.create_oval(
            self.xb - rayon, self.yb - rayon, self.xb + rayon, self.yb + rayon,
            fill="red"
        )
        self.vitesse = rd.uniform(1.8, 2) * 5
        self.angle = rd.uniform(-2 * math.pi, 0)
        self.dx = self.vitesse * math.cos(self.angle)
        self.dy = self.vitesse * math.sin(self.angle)
        self.deplacementBoule()
        
    def deplacementBoule(self):
            """ Déplacement de la balle """
            
            # rebond à droite
            if self.xb + rayon + self.dx > largeur:
                self.xb = 2*(largeur-rayon)-self.xb
                self.dx = -self.dx
            
            # rebond à gauche
            if self.xb - rayon + self.dx < 0:
                self.xb = 2*rayon-self.xb
                self.dx = -self.dx
            
            # rebond en haut
            if self.yb - rayon + self.dy < 0:
                self.yb = 2*rayon - self.yb
                self.dy = -self.dy
    
            # passage en bas
            if self.yb + rayon + self.dy > hauteur:
                self.xb = largeur/2
                self.yb = hauteur/3
                self.vitesse = rd.uniform(1.8,2)*5
                self.angle = rd.uniform(-2*math.pi, 0)
                self.dx = self.vitesse*math.cos(self.angle)
                self.dy = self.vitesse*math.sin(self.angle)
                #self.pv -=1

            #Collision avec la raquette
            if self.xb>self.xr-(3/2)*rayon and self.xb<self.xr+(3/2)*rayon :
                if self.yb-rayon<self.yr+5 and self.yb-rayon >self.yr-5:
                    #self.yb = 2*(hauteur - (self.yr + 5) -rayon)-self.yb
                    self.dy = -self.dy
    
        
            self.xb = self.xb + self.dx
            self.yb = self.yb + self.dy
            # affichage
            self.Canvas.coords(self.balle,self.xb-rayon,self.yb-rayon,self.xb+rayon,self.yb+rayon)
            # mise à jour toutes les 50 ms
            self.after(50,self.deplacementBoule)

    def raquette(self):
        self.xr = largeur/2
        self.yr = hauteur *3 /4
        self.raq = self.Canvas.create_rectangle(self.xr-2*rayon, self.yr+5,self.xr+2*rayon, self.yr-5, fill='blue')
        self.mvt_raquette()
    def move_xr(self, modif):
        self.xr += modif
    
    def mvt_raquette(self):
        self.bind("<Left>", lambda event : self.move_xr(-10))
        self.bind("<Right>", lambda event : self.move_xr(10))
        self.Canvas.coords(self.raq, self.xr-(3/2)*rayon, self.yr+5,self.xr+(3/2)*rayon, self.yr-5)
        self.after(50, self.mvt_raquette)
