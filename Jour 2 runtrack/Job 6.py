class Commande:
    def __init__(self, numero):
        self.__numero = numero
        self.__liste_plats = {}  
        self.__statut = "en cours"

    
    def ajouter_plat(self, nom_plat, prix):
        self.__liste_plats[nom_plat] = prix
        print(f"Plat {nom_plat} ajouté à la commande.")

    
    def annuler_commande(self):
        self.__statut = "annulée"
        print("Commande annulée.")

    
    def __calculer_total(self):
        return sum(self.__liste_plats.values())

    
    def afficher_commande(self):
        print(f"Commande N°: {self.__numero}")
        print("Plats commandés :")
        for nom_plat, prix in self.__liste_plats.items():
            print(f"- {nom_plat} : {prix}€")
        total = self.__calculer_total()
        print(f"Total à payer : {total}€")

    
    def calculer_tva(self):
        total = self.__calculer_total()
        tva = total * 0.20
        print(f"TVA à payer : {tva}€")

    # Assesseurs 
    def get_numero(self):
        return self.__numero

    def get_liste_plats(self):
        return self.__liste_plats

    def get_statut(self):
        return self.__statut

    # Mutateurs
    def set_statut(self, statut):
        self.__statut = statut

commande1 = Commande(1915)


commande1.ajouter_plat("cote de boeuf", 30)
commande1.ajouter_plat("frites", 5)
commande1.ajouter_plat("moelleux chocolat", 6)



commande1.afficher_commande()


commande1.calculer_tva()


commande1.annuler_commande()
print("Statut de la commande :", commande1.get_statut())
