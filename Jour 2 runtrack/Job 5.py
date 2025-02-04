


class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = False
        self.__reservoir = 50

    # Mutateurs
    def set_marque(self, marque):
        if isinstance(marque, str):
            self.__marque = marque

    def set_modele(self, modele):
        if isinstance(modele, str):
            self.__modele = modele

    def set_annee(self, annee):
        if isinstance(annee, int) and annee > 1900:  
            self.__annee = annee

    def set_kilometrage(self, kilometrage):
        if isinstance(kilometrage, int) and kilometrage >= 0:
            self.__kilometrage = kilometrage

    def set_en_marche(self, en_marche):
        if isinstance(en_marche, bool):
            self.__en_marche = en_marche

    def set_reservoir(self, reservoir):
        if isinstance(reservoir, int) and 0 <= reservoir <= 50:
            self.__reservoir = reservoir

    # Assesseurs
    def get_marque(self):
        return self.__marque

    def get_modele(self):
        return self.__modele

    def get_annee(self):
        return self.__annee

    def get_kilometrage(self):
        return self.__kilometrage

    def get_en_marche(self):
        return self.__en_marche

    def demarrer(self):
        if self.__verifier_plein() > 5:
            self.__en_marche = True
            return "La voiture démarre."
        else:
            return "Le réservoir est trop bas pour démarrer."

    def arreter(self):
        self.__en_marche = False
        return "La voiture s'arrête."

    def __verifier_plein(self):
        return self.__reservoir

    def afficher_informations(self):
        return f'Marque: {self.__marque}, Modèle: {self.__modele}, Année: {self.__annee}, Kilométrage: {self.__kilometrage}, En marche: {"Oui" if self.__en_marche else "Non"}, Réservoir: {self.__reservoir}'


ma_voiture = Voiture("Toyota", "Prius", 2020, 15000)

ma_voiture.set_marque("lamborghini")
ma_voiture.set_modele("aventador")
ma_voiture.set_annee(2022)
ma_voiture.set_kilometrage(2000)

#  voiture avec peu d'essence
ma_voiture.set_reservoir(4)  


print(ma_voiture.afficher_informations())

print(ma_voiture.demarrer())  # Essayer de démarrer avec un réservoir presque vide
print("En marche :", ma_voiture.get_en_marche())

# On Rempli le réservoir pour vérifier que la voiture peut démarrer
ma_voiture.set_reservoir(10)
print(ma_voiture.demarrer())
print("En marche :", ma_voiture.get_en_marche())
