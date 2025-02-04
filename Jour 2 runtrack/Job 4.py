

class Student:
    def __init__(self, nom, prenom, numero_etudiant):
        self.__nom = nom
        self.__prenom = prenom
        self.__numero_etudiant = numero_etudiant
        self.__credits = 0
        self.__level = self.__student_eval()
    
    # Accesseurs
    def get_nom(self):
        return self.__nom
    
    def get_prenom(self):
        return self.__prenom
    
    def get_numero_etudiant(self):
        return self.__numero_etudiant
    
    def get_credits(self):
        return self.__credits

    def get_level(self):
        return self.__level
    
    # Mutateurs
    def set_nom(self, nom):
        self.__nom = nom
    
    def set_prenom(self, prenom):
        self.__prenom = prenom
    
    def set_numero_etudiant(self, numero_etudiant):
        self.__numero_etudiant = numero_etudiant
    
    def add_credits(self, credits):
        if credits > 0:
            self.__credits += credits
            self.__level = self.__student_eval()
        else:
            print("Erreur : le nombre de crédits doit être supérieur à zéro.")
    
    
    def __student_eval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"
    
    
    def student_info(self):
        print(f"Nom : {self.__nom}")
        print(f"Prénom : {self.__prenom}")
        print(f"Numéro d'étudiant : {self.__numero_etudiant}")
        print(f"Niveau : {self.__level}")

# Instanciation
etudiant = Student("Doe", "John", 145)


etudiant.add_credits(30)
etudiant.add_credits(40)
etudiant.add_credits(25)

# total de crédits 
print("Total de crédits :", etudiant.get_credits())

# informations de l'étudiant
etudiant.student_info()

        