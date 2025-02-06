class CompteBancaire:
    def __init__(self, numCompte, nom, prenom, solde, decouvert=False):
        self.__numCompte = numCompte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert
        
    def afficher(self):
        print(f"Compte N°{self.__numCompte} - Titulaire: {self.__nom} {self.__prenom} - Solde: {self.__solde} euros")
        
    def afficher_solde(self):
        print(f"Le solde du compte s'élève à {self.__solde} euros")
        
    def versement(self, somme):
        self.__solde += somme
        print(f"Grâce au versement de {somme} euros, le solde du compte s'élève à {self.__solde} euros")
        
    def retrait(self, somme):
        if self.__solde >= somme or self.__decouvert:
            self.__solde -= somme
            print(f"Retrait de {somme} euros effectué. Le nouveau solde est de {self.__solde} euros")
        else:
            print("Retrait impossible, solde insuffisant pour cette somme")
            
    def agios(self):
        if self.__solde < 0:
            fraisAgios = abs(self.__solde) * 0.1  # 10% d'agios
            self.__solde -= fraisAgios
            print(f"Agios de {fraisAgios} euros appliqués. Nouveau solde: {self.__solde} euros")
            
    def virement(self, compte_destinataire, somme):
        if self.__solde >= somme or self.__decouvert:
            self.__solde -= somme
            compte_destinataire.versement(somme)
            print(f"Virement de {somme} euros effectué vers le compte N°{compte_destinataire.__numCompte}.")
        else:
            print("Erreur: Solde insuffisant pour ce virement.")

# Création d'un compte avec les valeurs de construction de votre choix
compte1 = CompteBancaire("12580", "Marshall", "Ericsen", 500)
compte1.afficher()
compte1.afficher_solde()
compte1.versement(200)
compte1.retrait(100)
compte1.afficher_solde()

# Création d'un deuxième compte avec un découvert
compte2 = CompteBancaire("20325", "Martin", "Marie", -50, decouvert=True)
compte2.afficher()
compte2.afficher_solde()
compte1.virement(compte2, 50)

# Affichage des soldes après le virement
compte1.afficher_solde()
compte2.afficher_solde()
