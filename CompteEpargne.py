from Compte import *
import sqlite3
conn = sqlite3.connect('base.db')
cursor = conn.cursor()

class CompteEpargne(Compte):
    def __init__(self,numeroDeCompte, montant, plafond, tauxDinteret ):
        super().__init__(numeroDeCompte,montant)
        self.__plafond = plafond
        self.__tauxDinteret = tauxDinteret

    def get_numeroDeCompte(self) -> int:
        return self._numeroDeCompte

    def set_numeroDeCompte(self, numeroDeCompte) -> int:
        self._numeroDeCompte = numeroDeCompte


    def get_montant(self) -> int:
        return self._montant

    def set_montant(self, montant,numero) :
        cursor.execute("""UPDATE compte SET solde = ? WHERE id =""" + str(numero), (montant,))
        conn.commit()

    def get_tauxDinteret(self):
        return self.__tauxDinteret

    def set_tauxDinteret(self,tauxDinteret,numero):
        cursor.execute("""UPDATE compteEpargne SET tauxInteret = ? WHERE id =""" + str(numero), (tauxDinteret,))
        conn.commit()

    def get_plafond(self):
        return self.__plafond

    def set_plafond(self,plafond,numero):
        cursor.execute("""UPDATE compteEpargne SET plafond = ? WHERE id =""" + str(numero),(plafond,))
        conn.commit()


    def compteEpargneDB(self):
        cursor.execute("""INSERT INTO compte(id,solde,utilise) VALUES(?,?,?)""",(self.get_numeroDeCompte(), self.get_montant(),"non"))
        cursor.execute("""INSERT INTO compteEpargne(idCompte,plafond,tauxInteret) VALUES(?,?,?)""", (self.get_numeroDeCompte(), self.get_plafond(),self.get_tauxDinteret()))
        conn.commit()
