""""
Que fait ce programme : interface graphique  
Auteur : Guillaume Aribaut Pierre Bolzinger
When : 06/10/2026 à 8h56 (dernière modif: )
To do : 
"""

#Importations bibliothèques

import tkinter as tk
class appli(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Brick Break")
        self.geometry("500x500")
        Canvas=tk.Canvas(self, width=450, height=400, bg='black')
        Canvas.pack()
        

    





    
