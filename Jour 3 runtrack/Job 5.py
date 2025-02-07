import random

class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def attaquer(self, adversaire):
        degats = random.randint(5, 15)
        adversaire.vie -= degats
        print(f"{self.nom} attaque {adversaire.nom} et lui inflige {degats} points de dégâts !")
        print(f"Il reste {adversaire.vie} points de vie à {adversaire.nom}")

class Jeu:
    def __init__(self):
        self.niveau = None
        self.joueur = None
        self.ennemi = None

    def choisir_niveau(self):
        while True:
            try:
                niveau = int(input("Choisissez un niveau de difficulté (1, 2, 3): "))
                if niveau in [1, 2, 3]:
                    self.niveau = niveau
                    break
                else:
                    print("Veuillez choisir un niveau valide (1, 2 ou 3).")
            except ValueError:
                print("Bouge pas je vais t'acheter des lunettes.")

    def lancer_jeu(self):
        if self.niveau == 1:
            vie_joueur, vie_ennemi = 50, 30
        elif self.niveau == 2:
            vie_joueur, vie_ennemi = 50, 50
        elif self.niveau == 3:
            vie_joueur, vie_ennemi = 30, 50

        self.joueur = Personnage("Joueur", vie_joueur)
        self.ennemi = Personnage("Ennemi", vie_ennemi)

        while self.joueur.vie > 0 and self.ennemi.vie > 0:
            self.joueur.attaquer(self.ennemi)
            if self.ennemi.vie <= 0:
                print("Vous avez vaincu l'ennemi !")
                break

            self.ennemi.attaquer(self.joueur)
            if self.joueur.vie <= 0:
                print("Hommes a terre, envoyez du renfort.")
                break

        self.verifier_gagnant()

    def verifier_gagnant(self):
        if self.joueur.vie > 0:
            print("Félicitations, vous avez anihiler l'ennemi !")
        else:
            print("game over, vous etes mort !")

# Lancement du jeu
jeu = Jeu()
jeu.choisir_niveau()
jeu.lancer_jeu()
