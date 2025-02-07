import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

    def __str__(self):
        return f"{self.valeur} de {self.couleur}"


class Jeu:
    couleurs = ["Coeur", "Carreau", "Trèfle", "Pique"]
    valeurs = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Valet", "Dame", "Roi", "As"]

    def __init__(self):
        self.paquet = []
        for couleur in self.couleurs:
            for valeur in self.valeurs:
                self.paquet.append(Carte(valeur, couleur))
        random.shuffle(self.paquet)

    def distribuer_carte(self):
        return self.paquet.pop()

    def valeur_carte(self, carte):
        if isinstance(carte.valeur, int):
            return carte.valeur
        elif carte.valeur in ["Valet", "Dame", "Roi"]:
            return 10
        else:  
            return 1, 11

class JeuBlackjack(Jeu):
    def __init__(self):
        super().__init__()

    def main_valeur(self, main):
        valeur = 0
        as_compte = 0
        for carte in main:
            if isinstance(carte.valeur, int):
                valeur += carte.valeur
            elif carte.valeur in ["Valet", "Dame", "Roi"]:
                valeur += 10
            else:  
                as_compte += 1
                valeur += 11

        while valeur > 21 and as_compte > 0:
            valeur -= 10
            as_compte -= 1

        return valeur

    def jouer(self):
        joueur_main = [self.distribuer_carte(), self.distribuer_carte()]
        croupier_main = [self.distribuer_carte(), self.distribuer_carte()]

        print(f"Main du joueur: {[str(carte) for carte in joueur_main]}, valeur: {self.main_valeur(joueur_main)}")
        print(f"Main du croupier: {str(croupier_main[0])} et carte cachée")

        while self.main_valeur(joueur_main) <= 21:
            action = input("Voulez-vous 'prendre' ou 'passer'? ").lower()
            if action == 'prendre':
                joueur_main.append(self.distribuer_carte())
                print(f"Main du joueur: {[str(carte) for carte in joueur_main]}, valeur: {self.main_valeur(joueur_main)}")
            elif action == 'passer':
                break

        if self.main_valeur(joueur_main) > 21:
            print("Vous avez dépassé 21! Vous avez perdu.")
            return

        print(f"Main du croupier: {[str(carte) for carte in croupier_main]}, valeur: {self.main_valeur(croupier_main)}")
        while self.main_valeur(croupier_main) < 17:
            croupier_main.append(self.distribuer_carte())
            print(f"Main du croupier: {[str(carte) for carte in croupier_main]}, valeur: {self.main_valeur(croupier_main)}")

        joueur_valeur = self.main_valeur(joueur_main)
        croupier_valeur = self.main_valeur(croupier_main)

        if croupier_valeur > 21 or joueur_valeur > croupier_valeur:
            print("Vous avez gagné!")
        else:
            print("Le croupier a gagné.")
if __name__ == "__main__":
    jeu = JeuBlackjack()
    jeu.jouer()