class Vehicule:
    def __init__(self,marque,modele,annee,prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix
    
    def informationVehicule(self):
        print(f"Marque:{self.marque}")
        print(f"Modèle:{self.modele}")
        print(f"Année{self.annee}")
        print(f"Prix:{self.prix}")
        
class Voiture(Vehicule):
    def __init__(self,marque,modele,annee,prix,porte =4):
        super().__init__(marque,modele,annee,prix)
        self.porte = porte
        
    def informationVehicule(self):
        super().informationVehicule()
        print(f"le nombre de porte:{self.porte}")

class Moto(Vehicule):
    def __init__(self,marque,modele,annee,prix,roue = 2):
        super().__init__(marque,modele,annee,prix)       
        self.roue = roue
        
    def informationVehicule(self):
        super().informationVehicule()
        print(f"le nombre de roue est de {self.roue}")
        
voiture = Voiture("Toyota", "Corolla", 2020, 20000)
voiture.informationVehicule()

moto = Moto("Yamaha", "MT-07", 2021, 7500)
moto.informationVehicule()