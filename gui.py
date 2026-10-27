""""
Que fait ce programme : interface graphique  
Auteur : Guillaume Aribaut & Pierre Bolzinger
When : 06/10/2026 à 8h56 (dernière modif: 27/10/2026 à 15h16 par Guillaume)
To do : collision avec les briques
"""

#Importations bibliothèques

import tkinter as tk
import random as rd
import math

#Valeurs importantes non-modifiables
rayon = 15
largeur = 450
hauteur = 400

class appli(tk.Tk): #Creation et parametration du menu principal
    def __init__(self):
        super().__init__()
        self.title("Brick Break")
        self.geometry("500x500")
        self.btn_jeu=tk.Button(self, text="Brick Break", command=self.jeu)
        self.btn_options=tk.Button(self, text="Options", command= self.options)
        self.btn_jeu.pack()
        self.btn_options.pack()
        self.touches = set()
        self.bind("<KeyPress>", self.appui)
        self.bind("<KeyRelease>", self.relache)

        
  
    def options(self): #Creation et parametrage des options
        self.opt=tk.Toplevel(self, bg='white')
        self.opt.title("Options")
        self.quitter_opt = tk.Button(self.opt, text="Quitter Options", command= self.opt.destroy)
        self.quitter_opt.pack()
        self.quitter_jeu = tk.Button(self.opt, text="Quitter Jeu", command=self.destroy)
        self.quitter_jeu.pack()

    def jeu(self): #Creation et parametrage de la fenetre de jeu
        self.jeu = tk.Toplevel(self)
        self.Canvas = tk.Canvas(self.jeu, width=largeur, height=hauteur, bg="black")
        self.Canvas.pack()
        self.pv = 5
        self.texte_pv = self.Canvas.create_text(20,12, text= "PV :", font= ("Helvetica", 12), fill='yellow')
        self.compteur_pv = self.Canvas.create_text(45, 12, text= str(self.pv), font= ("Helvetica", 12), fill='yellow')
        self.score = 0
        self.texte_score = self.Canvas.create_text(390, 12, text= "SCORE :", font= ("Helvetica", 12), fill='yellow')
        self.compteur_score = self.Canvas.create_text(430, 12, text= str(self.score), font= ("Helvetica", 12), fill='yellow')
        self.raquette()
        self.brique()
        self.boule()
        


    def boule(self): #Creation et initialisation de la balle
        self.xb = largeur / 2
        self.yb = hauteur * 2/3
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
            #test collision liste brique/balle

            for brique in list(self.draw):
                if self.collision_brick(brique):
                    self.Canvas.delete(brique)
                    self.draw.remove(brique)
                    self.dy= -self.dy
                    self.score += 1
                    self.Canvas.itemconfig(self.compteur_score, text=(self.score))

            
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
                self.yb = hauteur * 2/3
                self.vitesse = rd.uniform(1.8,2)*5
                self.angle = rd.uniform(0, 2*math.pi)
                self.dx = self.vitesse*math.cos(self.angle)
                self.dy = self.vitesse*math.sin(self.angle)
                self.xr = largeur/2
                self.yr = hauteur *15 /16
                self.pv -=1
                self.mort()

            #Collision avec la raquette
            if self.xb + rayon + self.dx>self.xr-(3/2)*rayon and self.xb - rayon + self.dx <self.xr+(3/2)*rayon :
                if self.yb + self.dy +rayon<self.yr+5 and self.yb + self.dy + rayon >self.yr-5:
                    self.yb = self.yr - 5 - rayon
                    self.dy = -self.dy
    
        
            self.xb = self.xb + self.dx
            self.yb = self.yb + self.dy
            # affichage
            self.Canvas.coords(self.balle,self.xb-rayon,self.yb-rayon,self.xb+rayon,self.yb+rayon)
            self.Canvas.itemconfig(self.compteur_pv, text = str(self.pv))
            # mise à jour toutes les 50 ms
            self.after(50,self.deplacementBoule)

    def raquette(self): #Creation de la raquette et mise en mouvement
        self.xr = largeur/2
        self.yr = hauteur * 15 / 16
        self.raq = self.Canvas.create_rectangle(self.xr-2*rayon, self.yr+5,self.xr+2*rayon, self.yr-5, fill='blue')
        self.mvt_raquette()

    def appui(self, event):
        self.touches.add(event.keysym)

    def relache(self, event):
        self.touches.discard(event.keysym)

    def mvt_raquette(self): #Enclanche le mouvement de la raquette et vérifie qu'elle reste dans les bordures
        if "Left" in self.touches: 
            self.xr -= 10
        if "Right" in self.touches:
            self.xr += 10
        if self.xr + (3/2)*rayon > largeur:
            self.xr = largeur - (3/2)*rayon
        elif self.xr - (3/2)*rayon < 0:
            self.xr = (3/2)*rayon
        self.Canvas.coords(self.raq, self.xr-(3/2)*rayon, self.yr+5,self.xr+(3/2)*rayon, self.yr-5)
        self.after(50, self.mvt_raquette)

    def mort(self): #Fenetre de mort, l'une des fins du jeu
        if self.pv <= 0 :
            self.jeu.destroy()
            self.fen_mort = tk.Toplevel(self, bg = 'black')
            self.fen_mort.title("Bonjour c'est la mort")
            self.texte_mort = tk.Label(self.fen_mort, text= "VOUS ÊTES MORT", font = ('Optimus Princeps', 42), fg = 'red', bg = 'black')
            self.texte_mort.pack()
            self.boutton_mort = tk.Button(self.fen_mort, text = "Retourner au menu", fg= 'red', bg= 'black', command= self.fen_mort.destroy)
            self.boutton_mort.pack()

    def brique(self): #Creation des briques
        self.draw = []
        for x in range(0,largeur-40,50):
            for y in range(20,200,60):
                    brique=self.Canvas.create_rectangle(x, y, x+50, y+20, fill="green")
                    self.draw.append(brique)

    def collision_brick(self,coord_rect): # test unitaire de collision avec une brique
        coords = self.Canvas.coords(coord_rect)
        if not coords:
            return False
        rx, ry, rw, rh= coords
        x_clamp=max(rx, min(self.xb + self.dx, rw))
        y_clamp= max(ry , min(self.yb + self.dy, rh))
        distx= (self.xb + self.dx) - x_clamp
        disty= (self.yb + self.dy) - y_clamp
        dist= distx**2 + disty**2
        return (dist<=rayon**2)

       



  

    def victoire(self): #Fenetre de victoire, autre fin du jeu
        if self.score == 27 :
            self.jeu.destroy()
            self.fen_vict = tk.Toplevel(self, bg= 'gold')
            self.fen_vict.title("Bravo")
            self.texte_victoire = tk.Label(self.fen_vict, text="Félicitation ! \n Vous avez gagné !", bg = 'gold', fg ='blue')
            self.texte_victoire.pack()
            self.boutton_victoire = tk.Button(self.fen_vict, text= "Retour au menu", bg = 'gold', fg = 'blue', command= self.fen_vict.destroy)
            self.boutton_victoire.pack()