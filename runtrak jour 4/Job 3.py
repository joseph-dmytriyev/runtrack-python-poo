class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
        
        
    def perimetre(self):
       return (self.__longueur+ self.__largeur) * 2
        
    def surface(self):
        return self.__longueur * self.__largeur
        
   
    def get_longueur(self):
        return self.__longueur 
    def get_largeur(self):
        return self.__largeur
    
    def set_longueur(self,longueur):
        self.__longueur = longueur
    def set_largeur(self,largeur):
        self.__largeur = largeur
    
class Parallepipede(Rectangle):
    def __init__(self,longueur, largeur,hauteur):
        super().__init__(longueur,largeur)
        self.hauteur = hauteur
        
    def volume(self):
       return self.get_longueur() * self.get_largeur() * self.hauteur
   
    
rect = Rectangle(10, 6)
print("Longueur:", rect.get_longueur())  
print("Largeur:", rect.get_largeur())   
print("Perimetre:", rect.perimetre())   
print("Surface:", rect.surface())       


paral = Parallepipede(10, 15, 30)
print("Volume:", paral.volume())  
    

