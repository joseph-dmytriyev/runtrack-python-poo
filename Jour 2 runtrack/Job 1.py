


class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
    
    # Accesseurs
    def get_longueur(self):
        return self.__longueur
    
    def get_largeur(self):
        return self.__largeur
    
    # Mutateurs
    def set_longueur(self, longueur):
        self.__longueur = longueur
    
    def set_largeur(self, largeur):
        self.__largeur = largeur


rectangle = Rectangle(10, 5)


print("Longueur initiale:", rectangle.get_longueur())
print("Largeur initiale:", rectangle.get_largeur())


rectangle.set_longueur(15)
rectangle.set_largeur(8)


print("Nouvelle longueur:", rectangle.get_longueur())
print("Nouvelle largeur:", rectangle.get_largeur())
