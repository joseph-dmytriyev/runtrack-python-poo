

class Livre:
    def __init__(self, titre, auteur, nombre_de_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombre_de_pages = nombre_de_pages
    
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
        else:
            print("non: le nombre de pages doit être un entier positif.")
# Créer un livre
livre = Livre("Tartufle", "Moliere", 330)

#
print("Titre :", livre.get_titre())
print("Auteur :", livre.get_auteur())
print("Nombre de pages :", livre.get_nombre_de_pages())

# Modifier les valeurs
livre.set_titre("Candide")
livre.set_auteur("Voltaire")
livre.set_nombre_de_pages(940)  # Changement valide
livre.set_nombre_de_pages(-5)   # Changement invalie


print("Nouveau titre :", livre.get_titre())
print("Nouvel auteur :", livre.get_auteur())
print("Nouveau nombre de pages :", livre.get_nombre_de_pages())


        
        