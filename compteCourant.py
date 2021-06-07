import sqlite3
conn = sqlite3.connect('base.db')
cursor = conn.cursor()



from Compte import *

class CompteCourant(Compte):
    def __init__(self,numeroDeCompte,montant,soldeMinimum,fraisDeTransfert):
        super().__init__(numeroDeCompte,montant)
        self.__soldeMinimum = soldeMinimum
        self.__fraisDeTransfert = fraisDeTransfert

    def get_numeroDeCompte(self) ->int:
        return self._numeroDeCompte

    def set_numeroDeCompte(self,numeroDeCompte) ->int:
        self._numeroDeCompte = numeroDeCompte

    def get_montant(self) ->int:
        return self._montant


    def set_montant(self,montant,numero):
        cursor.execute("""UPDATE compte SET solde = ? WHERE id =""" + str(numero), (montant,))
        conn.commit()

    def get_soldeMinimum(self) ->int:
        return self.__soldeMinimum

    def set_soldeMinimum(self, soldeMinimum,numero):
        cursor.execute("""UPDATE compteCourant SET soldeMinimum = ? WHERE id =""" + str(numero), (soldeMinimum,))
        conn.commit()

    def get_fraisDeTransfert(self) ->int:
        return self.__fraisDeTransfert

    def set_fraisDeTransfert(self,fraisDeTransfert,numero) :
        cursor.execute("""UPDATE compteCourant SET fraisdeTransfert = ? WHERE id =""" + str(numero), (fraisDeTransfert,))
        conn.commit()

    def compteCourantDB(self):
        cursor.execute("""INSERT INTO compte(id,solde,utilise) VALUES(?,?,?)""",(self.get_numeroDeCompte(), self.get_montant(),"non"))
        cursor.execute("""INSERT INTO compteCourant(idCompte,soldeMinimum,fraisdeTransfert) VALUES(?,?,?)""", (self.get_numeroDeCompte(), self.get_soldeMinimum(),self.get_fraisDeTransfert()))
        conn.commit()

