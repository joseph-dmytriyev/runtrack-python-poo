class Personne:
    def __init__(self,age = 14):
        self.age = age
        
    def afficherAge(self):
        print(f"j'ai {self.age}")
        
    def bonjour(self):
        print("hello")
    
    def modifierAge(self,nouvelAge):
        self.age = nouvelAge
        
class Eleve(Personne):
    def allerenCours(self):
        print("Je vais en cours")
    def afficherAge(self):
        print(f"j'ai {self.age}")
        
class Professeur:
    def __init__(self, matiereEnseignee):
        self.__matiereEnseignee = matiereEnseignee  # Attribut privé

    def enseigner(self):
        print("Le cours va commencer")

    def getMatiereEnseignee(self):
        return self.__matiereEnseignee
    

#
personne = Personne(15)
personne.afficherAge()  
personne.bonjour()      
personne.modifierAge(30)
personne.afficherAge()  


eleve = Eleve()
eleve.afficherAge()     
eleve.allerenCours()    
eleve.modifierAge(18)
eleve.afficherAge()     




    