

class Livre:
    def __init__(self, titre, auteur, nombre_de_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombre_de_pages = nombre_de_pages
        self.__disponible = True  

    # Accesseurs
    def get_titre(self):
        return self.__titre

    def get_auteur(self):
        return self.__auteur

    def get_nombre_de_pages(self):
        return self.__nombre_de_pages

    # Mutateurs
    def set_titre(self, titre):
        self.__titre = titre

    def set_auteur(self, auteur):
        self.__auteur = auteur

    def set_nombre_de_pages(self, nombre_de_pages):
        if isinstance(nombre_de_pages, int) and nombre_de_pages > 0:
            self.__nombre_de_pages = nombre_de_pages
    

    def verification(self):
        return self.__disponible

    
    def emprunter(self):
        if self.verification():
            self.__disponible = False
            return True
        else:
            return False

    
    def rendre(self):
        if not self.verification():
            self.__disponible = True
            return True
        else:
            return False

    
    def afficher_informations(self):
        return f'Titre: {self.__titre}, Auteur: {self.__auteur}, Nombre de pages: {self.__nombre_de_pages}, Disponible: {"Oui" if self.__disponible else "Non"}'


livre = Livre('voyage au centre de la terre', 'Jules Verne', 96)
print(livre.afficher_informations())  
print(livre.verification())  
print(livre.emprunter())  
print(livre.afficher_informations())  
print(livre.rendre())  
print(livre.afficher_informations())

