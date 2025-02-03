# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 22:20:06 2025

@author: josep
"""

class Personnage:
    def __init__(self, x, y, matrice):
        self.x = x
        self.y = y
        self.matrice = matrice
        self.nb_lignes = len(matrice)
        self.nb_colonnes = len(matrice[0]) if self.nb_lignes > 0 else 0

    def gauche(self, n=1):
        if self.x - n >= 0:
            self.x -= n
        else:
            self.x = 0  # Limite à la bordure gauche de la matrice

    def droite(self, n=1):
        if self.x + n < self.nb_colonnes:
            self.x += n
        else:
            self.x = self.nb_colonnes - 1  # Limite à la bordure droite de la matrice

    def haut(self, n=1):
        if self.y - n >= 0:
            self.y -= n
        else:
            self.y = 0  # Limite à la bordure supérieure de la matrice

    def bas(self, n=1):
        if self.y + n < self.nb_lignes:
            self.y += n
        else:
            self.y = self.nb_lignes - 1  # Limite à la bordure inférieure de la matrice

    def position(self):
        return (self.x, self.y)

 # matrice de jeu
matrice = [[0 for _ in range(5)] for _ in range(5)]

# Instanciation par rapport a la matrice
personnage = Personnage(2, 2, matrice)

# Déplacement du personnage
personnage.gauche(2)
print(personnage.position())

personnage.droite(1)  
print(personnage.position())

personnage.bas(3)
print(personnage.position())

personnage.haut(4)
print(personnage.position())

print(personnage.position())