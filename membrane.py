#!/usr/bin/python
# -*- coding: utf-8 -*

# Le but de ce programme est de créer une animation qui représente la membrane plasmique 
# et le flux de sodium(Na) et potassium(K ) qui circulent de part et d'autre.
# Il faudra représenter Na et K sous forme de boules colorées qu'on déplacera en fonction
# des gradients de concentration
# ainsi que les canaux de fuite et la pompe Na/K
# Les flux entrant et sortant doivent s'annuler mutuellement
# de sorte que la concentration en soluté soit toujours la même d'un coté comme de l'autre.
# par la suite, on pourra envisager des boutons pour faire varier certains paramètres
# comme la quantité de pompe Na/K, ce qui changera le potentiel de repos
# et la quantité de soluté, en cliquant directement sur l'espace extra ou intracellulaire.

from tkinter import *
from math import *

###Définition des fonctions de gestion des objets

def calcPotentielK():
    "fonction qui calcul le quotient des concentration en K"
    "entre la mb interne et la mb externe ==> [K]interne / [K]externe"
    global potentielK, y, y1, x1
    nbK = 6
    i = 0   #variable compteur de la boucle (de 0 à (len(x1) -1) )

    while i < (len(x1) - 1):                        #calcul de la quantité de K
        if y1[i] > y[1] and nbK < len(x1) - 1:  #dans son compartiment de référence
            nbK += 1                                     #ici : intracellulaire pour K
        elif y1[i] < y[0]:                             #par commodité, ici, on considerera pour l'instant que
            nbK -= 1                                      #1 ion dans son compartiment de référence
        i += 1                                              # = 1mMole/L ou 1mEq/L

    potentielK = nbK / (len(x1) - nbK)    #quotient des concentration de K intra / extra cellulaires
    round(potentielK, 2)
    lab2.configure(text="concentration K+: "+str(potentielK)) #affichage dans lab2

def calcPotentielNa():
    "Fonction qui calcul le quotient des concentration en Na"
    "entre la mb interne et la mb externe ==> [Na]interne / [Na]externe"
    global potentielNa, y, y2, x2
    nbNa = 6
    i = 0
    while i < len(x1) - 1:
        if y2[i] < y[0] and nbNa < len(x2) -1:                     
            nbNa += 1
        elif y2[i] > y[1]:
            nbNa -= 1
        i += 1
   
    potentielNa = (len(x2)-nbNa) / nbNa #quotient des concentrations de Na   
    round(potentielNa, 2)
    lab3.configure(text="concentration Na+: "+str(potentielNa))   #affichage dans lab3
       
       
###Variables globales

potentielK = 0        #quotient de la qté intra et extracellulaire de K et Na
potentielNa = 0
x, y = [0, 0], [230, 270]   #coordonnées de la membrane cellulaire
x1, y1 = [300, 330, 345, 360, 375, 390, 405], [200, 300, 300, 300, 300, 300, 300] #coordonnées K
x2, y2 = [300, 330, 345, 360, 375, 390, 405], [300, 200, 200, 200, 200, 200, 200] #coordonnées Na


### programme principal

fen = Tk()      #création du widget maître

can = Canvas(fen, bg="dark grey", width=600, height=500)    # création du canevas
can.grid(row=1, column=1, columnspan=3)

lab1 = Label(fen, width=30, text="potentiel de repos", padx=5, pady=5)    # Création des  différentes
lab2 = Label(fen, width=30,  text="concentration K+", padx=5, pady=5)       #  étiquettes de valeurs
lab3 = Label(fen, width=30, text="concentration Na+",padx=5,pady=5)
lab1.grid(row=2, column=1)
lab2.grid(row=2, column=2)
lab3.grid(row=2, column=3)

can.create_line(x[0], y[0], x[0]+600, y[0], width=10, fill="yellow") #les deux couches de la membrane
can.create_line(x[1], y[1], x[1]+600, y[1], width=10, fill="yellow")

k1 = can.create_oval(x1[0], y1[0], x1[0]+10, y1[0]+10, fill="green") # Création des "rond colorés"
k2 = can.create_oval(x1[1], y1[1], x1[1]+10, y1[1]+10, fill="green") # représentant les ions potassium
k3 = can.create_oval(x1[2], y1[2], x1[2]+10, y1[2]+10, fill="green")
k4 = can.create_oval(x1[3], y1[3], x1[3]+10, y1[3]+10, fill="green")
k5 = can.create_oval(x1[4], y1[4], x1[4]+10, y1[4]+10, fill="green")
k6 = can.create_oval(x1[5], y1[5], x1[5]+10, y1[5]+10, fill="green")
k7 = can.create_oval(x1[6], y1[6], x1[6]+10, y1[6]+10, fill="green")

p1 = can.create_oval(x2[0], y2[0], x2[0]+10, y2[0]+10, fill="red") # Création des "rond colorés"
p2 = can.create_oval(x2[1], y2[1], x2[1]+10, y2[1]+10, fill="red") # représentant les ions sodium
p3 = can.create_oval(x2[2], y2[2], x2[2]+10, y2[2]+10, fill="red")
p4 = can.create_oval(x2[3], y2[3], x2[3]+10, y2[3]+10, fill="red")
p5 = can.create_oval(x2[4], y2[4], x2[4]+10, y2[4]+10, fill="red")
p6 = can.create_oval(x2[5], y2[5], x2[5]+10, y2[5]+10, fill="red")
p7 = can.create_oval(x2[6], y2[6], x2[6]+10, y2[6]+10, fill="red")

calcPotentielK()
calcPotentielNa()

#démarrage de la boucle principale
fen.mainloop()
