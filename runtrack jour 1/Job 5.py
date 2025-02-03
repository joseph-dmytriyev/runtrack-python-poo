# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 22:17:07 2025

@author: josep
"""

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        print(f"Les coordonnées du point sont {self.x} {self.y}")

    def afficherX(self):
        print(f"Les coordonnées x sont {self.x}")

    def afficherY(self):
        print(f"Les coordonnées y sont {self.y}")

    def changerX(self, x):
        self.x = x

    def changerY(self, y):
        self.y = y

point = Point(3, 4)

# Appel des méthodes pour vérifier le fonctionnement
point.afficherLesPoints()
point.afficherX()
point.afficherY()
point.changerX(10)
point.changerY(20)
point.afficherLesPoints()