class Tache:
    def __init__(self, titre, description, statut="à faire"):
        self.titre = titre
        self.description = description
        self.statut = statut

    def marquer_comme_finie(self):
        self.statut = "terminée"

    def __str__(self):
        return f"{self.titre}: {self.description} [{self.statut}]"

class ListeDeTaches:
    def __init__(self):
        self.taches = []

    def ajouter_tache(self, tache):
        self.taches.append(tache)

    def supprimer_tache(self, titre):
        for i, tache in enumerate(self.taches):
            if tache.titre == titre:
                del self.taches[i]
                break

    def marquer_comme_finie(self, titre):
        for tache in self.taches:
            if tache.titre == titre:
                tache.marquer_comme_finie()

    def afficher_liste(self):
        for tache in self.taches:
            print(tache)

    def filter_liste(self, statut):
        return [tache for tache in self.taches if tache.statut == statut]

# Test du code
liste = ListeDeTaches()

# Création de plusieurs instances de Tache
tache1 = Tache("Faire les courses", "Acheter des légumes et des fruits")
tache2 = Tache("Nettoyer la maison", "Passer l'aspirateur et laver le sol")
tache3 = Tache("Lire un livre", "Terminer le roman")

# Ajout des tâches à la liste
liste.ajouter_tache(tache1)
liste.ajouter_tache(tache2)
liste.ajouter_tache(tache3)

# Afficher toutes les tâches
print("Liste des tâches:")
liste.afficher_liste()

# Supprimer une tâche
liste.supprimer_tache("Nettoyer la maison")

# Changer le statut d'une tâche
liste.marquer_comme_finie("Faire les courses")

# Afficher toutes les tâches après suppression et modification du statut
print("Mis jour des tache a effectuer:")
liste.afficher_liste()

# Afficher les tâches à faire
print("Tâches à faire:")
taches_a_faire = liste.filter_liste("à faire")
for tache in taches_a_faire:
    print(tache)
