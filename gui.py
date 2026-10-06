""""
Que fait ce programme : interface graphique  
Auteur : Guillaume Aribaut Pierre Bolzinger
When : 06/10/2026 à 8h56 (dernière modif: )
To do : 
"""

#Importations bibliothèques

import tkinter as tk
def initfenetre():
    casse_brique= tk.Tk()
    casse_brique.title("Brick Break")
    casse_brique.geometry('500x500')
    Canevas=tk.Canvas(casse_brique, width=450, height=400, bg='black') 
    Canevas.pack(padx=5, pady=5)
    casse_brique.mainloop()
    

"cercle=Canevas.create_oval(30,20,40,30,outline='red', fill='red')"