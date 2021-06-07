import sqlite3
conn = sqlite3.connect('base.db')
cursor = conn.cursor()

class Client():
    def __init__(self,id,nom,prenom,adresse,numeroAgence):
        self.__nom = nom
        self.__prenom = prenom
        self.__adresse = adresse
        self.__numeroAgence = numeroAgence
        self.__id = id

    def get_id(self):
        return self.__id

    def get_nom(self) ->str:
        return self.__nom

    def set_nom(self,nom,numero):
        cursor.execute("""UPDATE client SET nom = ? WHERE id ="""+str(numero), (nom,))
        conn.commit()

    def get_prenom(self) ->str:
        return self.__prenom

    def set_prenom(self,prenom,numero):
        cursor.execute("""UPDATE client SET prenom = ? WHERE id ="""+str(numero), (prenom,))
        conn.commit()

    def get_adresse(self) ->str:
        return self.__adresse

    def set_adresse(self,adresse,numero) :
        cursor.execute("""UPDATE client SET adresse = ? WHERE id =""" + str(numero), (adresse,))
        conn.commit()



    def get_numeroAgence(self) ->int:
        return self.__numeroAgence


    def clientDB(self):
        cursor.execute("""INSERT INTO client(id,nom,prenom,adresse,idAgence) VALUES(?,?,?,?,?)""",(self.get_id(),self.get_nom(), self.get_prenom(),self.get_adresse(),self.get_numeroAgence()))
        conn.commit()


