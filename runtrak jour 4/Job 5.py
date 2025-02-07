import math

class Forme:
    def aire(self):
        return 0

class Cercle(Forme):
    def __init__(self, radius):
        self.radius = radius

    def aire(self):
        return math.pi * self.radius * self.radius


forme1 = Forme()
print(f"Aire de la forme : {forme1.aire()}")

cercle1 = Cercle(5)
print(f"Aire du cercle : {cercle1.aire()}")  
