import sqlite3
conn = sqlite3.connect('base.db')
cursor = conn.cursor()

class Transaction():
    def __init__(self,numeroCompteDonneur,numeroCompteReceveur,montant):
        self.__montant = montant
        self.__numeroCompteDonneur = numeroCompteDonneur
        self.__numeroCompteReceveur = numeroCompteReceveur


    def get_montant(self):
        return self.__montant

    def set_montant(self,montant):
        self.__montant = montant

    def get_numeroCompteDonneur(self):
        return self.__numeroCompteDonneur

    def set_numeroCompteDonneur(self, numeroCompteDonneur):
         self.__numeroCompteDonneur = numeroCompteDonneur

    def get_numeroCompteReceveur(self):
        return self.__numeroCompteReceveur

    def set_numeroCompteReceveur(self,numeroCompteReceveur):
         self.__numeroCompteReceveur = numeroCompteReceveur

    def transactionDB(self):
        cursor.execute("""INSERT INTO transactionBancaire(idCompteCourant,idCompteEpargne,montant) VALUES(?,?,?)""",
                       (self.get_numeroCompteDonneur(), self.get_numeroCompteReceveur(), self.get_montant()))
        cursor.execute("""SELECT solde FROM compte where id = {}""".format(self.get_numeroCompteDonneur()))
        montantCompteDonneur = cursor.fetchone()
        nouveauMontantCompteDonneur = montantCompteDonneur[0]-(int(self.get_montant()))
        cursor.execute("""SELECT solde FROM compte where id = {}""".format(self.get_numeroCompteReceveur()))
        montantCompteReceveur = cursor.fetchone()
        nouveauMontantCompteReceveur = montantCompteReceveur[0]+(int(self.get_montant()))
        cursor.execute("""UPDATE compte SET solde = ? WHERE id ="""+self.get_numeroCompteDonneur(), (nouveauMontantCompteDonneur,))
        cursor.execute("""UPDATE compte SET solde = ? WHERE id ="""+self.get_numeroCompteReceveur(),(nouveauMontantCompteReceveur,))
        conn.commit()



t =Transaction(1540,150,20)
print(t.get_montant())
