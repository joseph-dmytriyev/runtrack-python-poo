# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 22:21:46 2025

@author: josep
"""

import math

class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def changerRayon(self, rayon):
        self.rayon = rayon

    def afficherInfos(self):
        print(f"Rayon: {self.rayon}")
        print(f"Diamètre: {self.diametre()}")
        print(f"Circonférence: {self.circonference()}")
        print(f"Aire: {self.aire()}")

    def circonference(self):
        return 2 * math.pi * self.rayon

    def aire(self):
        return math.pi * (self.rayon ** 2)

    def diametre(self):
        return 2 * self.rayon

# Créer deux cercles avec des rayons de 4 et 7
cercle1 = Cercle(4)
cercle2 = Cercle(7)

# Afficher les informations des cercle
print("Informations pour le cercle avec un rayon de 4 :")
cercle1.afficherInfos()

print("Informations pour le cercle avec un rayon de 7 :")
cercle2.afficherInfos()
