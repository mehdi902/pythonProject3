from Agence import *
from Client import *
from compteCourant import *
from CompteEpargne import *
from Transaction import *
from random import *
import sqlite3
from tkinter import *
conn = sqlite3.connect('base.db')
cursor = conn.cursor()

listedescomptes2 = [cursor.execute("""SELECT id FROM compte """)]
compteDb2 = cursor.fetchall()

listedesagences = [cursor.execute("""SELECT libelle,numeroAgence FROM agence""")]
agenceDb = cursor.fetchall()

listedestransactions = [cursor.execute("""SELECT idCompteCourant,idCompteEpargne, montant FROM transactionBancaire""")]
transactionDB = cursor.fetchall()
conn.commit()


def ajoutClient(agence):
    numero = randint(0, 1000000)
    nom = input("entrez le nom du client")
    prenom =input("entrez prenom")
    adresse = input("entrez adresse")
    cursor.execute("""SELECT id FROM compte Where utilise=?""", ("non",))
    compteDb = cursor.fetchall()
    nombreDeCompte = input("combien la personne a de comptes")
    print(compteDb)
    if len(compteDb) < int(nombreDeCompte):
        nouveauCompte = input("pas de compte ou tous les comptes sont utilisés? 1 ajouter un compte courant,2 ajouter un compte epargne")
        if nouveauCompte =="1":
            compteCourant()
        elif nouveauCompte =="2":
            compteEpargne()
    else:
        for i in range(int(nombreDeCompte)):
            compte = input("entrez un compte parmis ceux indiqués")
            cursor.execute("""UPDATE compte SET utilise = ? WHERE id ="""+compte, ("oui",))
            cursor.execute("""UPDATE compte SET idClient = ? WHERE id =""" + compte, (numero,))
            conn.commit()
        client = Client(numero,nom,prenom,adresse,agence)
        client.clientDB()
        conn.commit()
        print("client bien ajouté")
        refaire = input("1 ajouter un autre client, 2 retour au menu principal")
        if refaire == "1":
            ajoutClient()
        elif refaire == "2":
            accueil()


def supprimerClient():
    supprimer = input("quel client voulez vous supprimer")
    cursor.execute("DELETE from client WHERE id = {}".format(supprimer))
    print("client bien supprimé")
    conn.commit()
    refaire = input("1 supprimer un autre client, 2 retour au menu principal")
    if refaire == "1":
        supprimerClient()
    elif refaire == "2":
        accueil()


def modifierunclient():
        client = Client("","","",5000)
        idclient = input("quel client voulez vous modifier")
        modifClient = input("quel client voulez vous modifier entre le nom le prenom et l'adresse?")
        if modifClient =="nom":
            nouveaunom =input("Nouveau nom")
            client.set_nom(nouveaunom,idclient)
        elif modifClient =="prenom":
            nouveauprenom=input("Nouveau prenom")
            client.set_prenom(nouveauprenom,idclient)
        elif modifClient =="adresse":
            nouvelleAdresse = input("Nouvelle Adresse")
            client.set_adresse(nouvelleAdresse,idclient)



def transaction():
    print(compteDb2)
    premierCompte = input("selectionnez un compte donneur")
    deuxiemeCompte = input("selectionnez un compte bénéficiaire")
    if premierCompte == deuxiemeCompte:
        return "vous avez rentrer deux fois le même compte"
    else:
        montant = input("montant de la transaction")
        transaction = Transaction(premierCompte,deuxiemeCompte,montant)
        transaction.transactionDB()
        print("transaction effectuée")

def liste_transaction():
    print(transactionDB)
    refaire = input(" 1 retour au menu principal")
    if refaire == "1":
        accueil()


def compteCourant():
    numero = randint(0,1000000)
    frais = input("frais de transfert")
    solde = input("soldeMinimum")
    compte = CompteCourant(numero,50,solde,frais)
    compte.compteCourantDB()
    print("compte courant ajouté")
    refaire = input("1 ajouter un autre compte courant, 2 retour au menu principal")
    if refaire == "1":
        compteCourant()
    elif refaire == "2":
        accueil()

def compteEpargne():
    numero = randint(0,1000000)
    plafond = input("plafond")
    tauxInteret = input("taux d'interet")
    compte = CompteEpargne(numero,50,plafond,tauxInteret)
    compte.compteEpargneDB()
    print("compte épargne ajouté")
    refaire = input("1 ajouter un autre compte épargne, 2 retour au menu principal")
    if refaire == "1":
        compteEpargne()
    elif refaire == "2":
        accueil()

def liste_client(agence):
    cursor.execute("""SELECT id,nom, prenom, adresse FROM client WHERE idAgence="""+agence)
    clientDb = cursor.fetchall()
    print(clientDb)
    action = input("1 modifier un client,2 supprimer un client,3 retourner au menu?")
    if action =="1":
        modifierunclient()
    elif action == "2":
        supprimerClient()
    elif action=="3":
        accueil()

def liste_comptes():
    print(compteDb2)
    action = input("1 modifier un compte,2 supprimer un compte,3 accueil")
    if action=="1":
        modifier_compte()
    elif action=="2":
        supprimer_compte()
    elif action=="3":
        accueil()

def modifier_compte():
    comptemodif = CompteCourant(0,0,0,0)
    comptemodifepargne = CompteEpargne(0,0,0,0)
    compte = input("quel compte voulez vous modifier")
    modifcompte = input("quel client voulez vous modifier entre le montant le solde minimum et les frais de transfert, le plafond ou le taux?")
    if modifcompte == "montant":
        nouveaumontant = input("Nouveau nom")
        comptemodif.set_montant(nouveaumontant,compte)
    elif modifcompte == "solde minimum":
        nouveausoldeminimum= input("Nouveau solde minimum")
        comptemodif.set_soldeMinimum(nouveausoldeminimum, compte)
    elif modifcompte == "frais de transfert":
        nouveaufrais = input("Nouveau frais de transfert")
        comptemodif.set_fraisDeTransfert(nouveaufrais, compte)
    elif modifcompte == "plafond":
        nouveauplafond = input("Nouveau plafond")
        comptemodifepargne.set_plafond(nouveauplafond, compte)
    elif modifcompte == "taux":
        nouveautaux = input("Nouveau taux")
        comptemodifepargne.set_plafond(nouveautaux, compte)


def supprimer_compte():
    compte = input("quel compte voulez vous supprimer")
    cursor.execute("DELETE from compte WHERE id = {}".format(compte))
    print("compte bien supprimé")
    conn.commit()



def accueil():
        print(agenceDb)
        agence = input("quel agence êtes vous?")
        menu = input("1 ajouter un client, 2 voir la liste des clients,3 liste des comptes, 4 ajouter un compte courant,\n 5 ajouter un compte epargne,6 effectuer une transaction,7 voir les transactions ")
        if menu =="1":
            ajoutClient(agence)
        elif menu =="2":
            liste_client(agence)
        elif menu=="3":
            liste_comptes()
        elif menu=="4":
            compteCourant()
        elif menu == "5":
            compteEpargne()
        elif menu == "6":
            transaction()
        elif menu == "7":
            liste_transaction()





accueil()
conn.close()



