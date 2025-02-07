class Forme:
    def aire(self):
        return 0
         
    
class Rectangle(Forme):
    def __init__(self,largeur,hauteur):
        
        self.largeur = largeur
        self.hauteur = hauteur
        
    def aire(self):
        return self.largeur * self.hauteur

rectangle1 = Rectangle(3, 4)
print(f"Aire du rectangle : {rectangle1.aire()}")  

rectangle2 = Rectangle(5, 6)
print(f"Aire du rectangle : {rectangle2.aire()}") 
        
    
    
    