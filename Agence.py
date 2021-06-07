import sqlite3
conn = sqlite3.connect('base.db')
cursor = conn.cursor()
class Agence():
    def __init__(self,libelle,adresse,numeroAgence):
        self.__libelle = libelle
        self.__adresse = adresse
        self.__numeroAgence = numeroAgence

    def get_libelle(self) -> str:
        return self.__libelle

    def set_libelle(self, libelle) -> str:
        self.__libelle = libelle



    def get_adresse(self) -> str:
        return self.__adresse

    def set_adresse(self, adresse) -> str:
        self.__adresse = adresse


    def get_numeroAgence(self) -> int:
        return self.__numeroAgence

    def set_numeroAgence(self, numeroAgence) -> int:
        self.__numeroAgence = numeroAgence

    def agencebd(self):
        cursor.execute("""INSERT INTO agence(libelle,adresse,numeroAgence) VALUES(?,?,?)""", (self.get_libelle(),self.get_adresse(),self.get_numeroAgence()))
        conn.commit()

