from abc import ABCMeta, abstractmethod

class Compte(metaclass=ABCMeta):
    def __init__(self,numeroDeCompte,montant):
        self._numeroDeCompte = numeroDeCompte
        self._montant = montant

    @abstractmethod
    def get_numeroDeCompte(self) :
        pass

    @abstractmethod
    def set_numeroDeCompte(self,numeroDeCompte) :
        pass

    @abstractmethod
    def get_montant(self) :
        pass

    @abstractmethod
    def set_montant(self,montant,numero) :
        pass

