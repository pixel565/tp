""""
Que fait ce programme : interface graphique  
Auteur : Guillaume Aribaut & Pierre Bolzinger
When : 06/10/2026 à 8h56 (dernière modif: )
To do : 
"""

#Importations bibliothèques

import tkinter as tk

rayon = 15

class appli(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Brick Break")
        self.geometry("500x500")
        self.Canvas=tk.Canvas(self, width=450, height=400, bg='white')
        self.Canvas.pack()
        self.Button=tk.Button(self, text="Quitter", fg="navy", command=self.destroy)
        self.Button.pack()
    #dessine la boule rouge    
    def boule(self):
        self.x = 450/2
        self.y = 400/3
        self.balle = self.Canvas.create_oval(self.x-rayon, self.y-rayon, self.x+rayon, self.y+rayon, fill='red')


class jeu(appli):
    appli.Toplevel
    appli.Canvas_jeu=tk.Canvas(appli, bg='black')
class menu(appli):
    appli.Button_jouer=tk.Button(appli, text="Quitter", fg="navy", command=jeu(appli))
    appli.Button_options=tk.Button(appli, text="Quitter", fg="navy", command=appli.options())


    


