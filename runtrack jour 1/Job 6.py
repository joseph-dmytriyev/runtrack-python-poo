# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 22:17:58 2025

@author: josep
"""

class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def afficher_age(self):
        print(f"L'âge de l'animal est {self.age} ans")

    def vieillir(self):
        self.age += 1

    def nommer(self, nom):
        self.prenom = nom

    def afficher_prenom(self):
        print(f"Le nom de l'animal est {self.prenom}")

# Instanciation
animal = Animal()

# Affichage 
animal.afficher_age()

# Faire vieillir l'animal et afficher son âge mis à jour
animal.vieillir()
animal.afficher_age()

# Nommer l'animal et afficher son prénom
animal.nommer("Léon")
animal.afficher_prenom()