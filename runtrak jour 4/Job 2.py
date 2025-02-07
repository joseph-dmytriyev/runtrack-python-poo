class Personne:
    def __init__(self,nom,age = 14):
        self.age = age
        self.nom = nom
    def afficherNom(self):
        print(f"je suis {self.nom}")
        
    def afficherAge(self):
        print(f"j'ai {self.age}")
        
    def bonjour(self):
        print("Bonjour")
    
    def modifierAge(self,nouvelAge):
        self.age = nouvelAge
        
class Eleve(Personne):
    def allerenCours(self):
        print("Je vais en cours")
    def afficherAge(self):
        print(f"j'ai {self.age}")
        
class Professeur(Personne):
    def __init__(self,nom, age, matiereEnseignee):
        super().__init__(nom,age)
        self.__matiereEnseignee = matiereEnseignee  # Attribut privé

    def enseigner(self):
        print("Le cours va commencer")

    def getMatiereEnseignee(self):
        return self.__matiereEnseignee
    
eleve = Eleve("Jean", 14)
eleve.afficherNom()
eleve.bonjour()         
eleve.allerenCours()    
eleve.modifierAge(15)   
eleve.afficherAge()     

# Créer un objet Professeur
professeur = Professeur("M. Dupont", 40, "Mathématiques")
professeur.afficherNom()
professeur.bonjour()    
professeur.enseigner() 