# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 22:17:01 2025

@author: josep
"""

class Personne:
    
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
            
    def sePresenter(self):
            return(f"je suis {self.prenom} {self.nom}")

personne1 = Personne('jonh', 'Doe')
personne2 = Personne('jean' , 'yves')
print(personne1.sePresenter())
print(personne2.sePresenter())
