class Ville:
    def __init__(self, nom, population):
        self.__nom = nom
        self.__population = population

    def get_nom(self):
        return self.__nom

    def get_population(self):
        return self.__population

    def ajouter_habitant(self):
        self.__population += 1


class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville
        self.ajouter_population()

    def ajouter_population(self):
        self.__ville.ajouter_habitant()


# objet
paris = Ville("Paris", 1000000)
marseille = Ville("Marseille", 861635)


print(f"Le nombre d'habitants de {paris.get_nom()} est {paris.get_population()}.")
print(f"Le nombre d'habitants de {marseille.get_nom()} est {marseille.get_population()}.")

# objets Personne
johnny = Personne("Johnny", 45, paris)
marie = Personne("marie", 4, paris)
claire = Personne("Claire", 18, marseille)


print(f"Le nombre d'habitants de {paris.get_nom()} après l'arrivée de Johnny et marie est {paris.get_population()}.")
print(f"Le nombre d'habitants de {marseille.get_nom()} après l'arrivée de claire est {marseille.get_population()}.")
