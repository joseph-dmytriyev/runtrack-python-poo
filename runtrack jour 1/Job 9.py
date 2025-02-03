# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 22:21:55 2025

@author: josep
"""

class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def CalculerPrixTTC(self):
        return self.prixHT * (1 + self.TVA / 100)

    def afficher(self):
        return f"Nom: {self.nom}, Prix HT: {self.prixHT}, TVA: {self.TVA}%, Prix TTC: {self.CalculerPrixTTC()}"

    def modifier_nom(self, nouveau_nom):
        self.nom = nouveau_nom

    def modifier_prixHT(self, nouveau_prixHT):
        self.prixHT = nouveau_prixHT

    def get_nom(self):
        return self.nom

    def get_prixHT(self):
        return self.prixHT

    def get_TVA(self):
        return self.TVA

# On creer les produits
produit1 = Produit("telephone", 100, 20)
produit2 = Produit("tablette ", 200, 20)

# On Calcule et affichr leurs TVA
print(produit1.afficher())
print(produit2.afficher())

# Modification  des nom  prix de chaque produit
produit1.modifier_nom("aspirateur")
produit1.modifier_prixHT(120)
produit2.modifier_nom("fauteil ")
produit2.modifier_prixHT(220)

# Afficher les nouvelles informations des produits
print(produit1.afficher())
print(produit2.afficher())