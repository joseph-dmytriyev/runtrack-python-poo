import mysql.connector

# Connexion base de données
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="godsAvou1r",
    database="Laplateforme"
)

cursor = db.cursor()

#  première requête SQL
cursor.execute("SELECT * FROM etudiant")
resultats_etudiant = cursor.fetchall()


for etudiant in resultats_etudiant:
    print(etudiant)

# deuxième requête SQL
cursor.execute("SELECT nom, capacite FROM salle")
resultats_salle = cursor.fetchall()


for salle in resultats_salle:
    print(f"Nom : {salle[0]}, Capacité : {salle[1]}")

#  requête SQL superficie total 
cursor.execute("SELECT SUM(superficie) FROM etage")


resultat = cursor.fetchone()

# Affichage du résultat
print(f"La superficie de La Plateforme est de {resultat[0]} m2")

# requête SQL calcul capacité totale
cursor.execute("SELECT SUM(capacite) FROM salle")


resultat = cursor.fetchone()


print(f"La capacité totale des salles est de {resultat[0]}")

# Requête SQL afficher les employés avec leur service respectif

cursor.execute("SELECT employe.nom, employe.prenom, service.nom AS service FROM employe JOIN service ON employe.id_service = service.id")


resultats = cursor.fetchall()


for employe in resultats:
    print(f"Nom : {employe[0]}, Prénom : {employe[1]}, Service : {employe[2]}")


cursor.close()
db.close()
