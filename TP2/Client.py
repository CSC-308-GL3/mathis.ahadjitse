class Client:

    def __init__(self, numero, nom, adresse, codePostale, ville, nbKm):
        self.__numero = numero
        self.__nom = nom
        self.__adresse = adresse
        self.__codePostale = codePostale
        self.__ville = ville
        self.__nbKm = nbKm

    def distance(self):
        return self.__nbKm
