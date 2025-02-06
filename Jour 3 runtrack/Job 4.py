class Joueur:
    def __init__(self, nom, numero, position):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts = 0
        self.passes_decisives = 0
        self.cartons_jaunes = 0
        self.cartons_rouges = 0

    def marquer_un_but(self):
        self.buts += 1

    def effectuer_une_passe_decisive(self):
        self.passes_decisives += 1

    def recevoir_un_carton_jaune(self):
        self.cartons_jaunes += 1

    def recevoir_un_carton_rouge(self):
        self.cartons_rouges += 1

    def afficher_statistiques(self):
        print(f"{self.nom} (N°{self.numero}, {self.position}):")
        print(f"Buts marqués: {self.buts}")
        print(f"Passes décisives: {self.passes_decisives}")
        print(f"Cartons jaunes: {self.cartons_jaunes}")
        print(f"Cartons rouges: {self.cartons_rouges}")

class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.joueurs = []

    def ajouter_joueur(self, joueur):
        self.joueurs.append(joueur)

    def afficher_statistiques_joueurs(self):
        print(f"Statistiques des joueurs de l'équipe {self.nom}:")
        for joueur in self.joueurs:
            joueur.afficher_statistiques()

    def mettre_a_jour_statistiques_joueur(self, nom, buts=2, passes_decisives=0, cartons_jaunes=0, cartons_rouges=0):
        for joueur in self.joueurs:
            if joueur.nom == nom:
                joueur.buts += buts
                joueur.passes_decisives += passes_decisives
                joueur.cartons_jaunes += cartons_jaunes
                joueur.cartons_rouges += cartons_rouges
                break


joueur1 = Joueur("Pierre", 9, "Attaquant")
joueur2 = Joueur("Luc", 10, "Milieu")
joueur3 = Joueur("Jean", 4, "Défenseur")

# Création de l'équipe
equipe1 = Equipe("Marseille")

# Ajout des joueurs à l'équipe
equipe1.ajouter_joueur(joueur1)
equipe1.ajouter_joueur(joueur2)
equipe1.ajouter_joueur(joueur3)

# Présentation des joueurs de l'équipe
equipe1.afficher_statistiques_joueurs()

# Simulation d'un match
joueur1.marquer_un_but()
joueur1.marquer_un_but()
joueur2.effectuer_une_passe_decisive()
joueur2.effectuer_une_passe_decisive()
joueur3.recevoir_un_carton_jaune()
joueur1.recevoir_un_carton_rouge()

# Afficher les statistiques des joueurs après le match
print("Statistiques des joueurs après le match:")
equipe1.afficher_statistiques_joueurs()
