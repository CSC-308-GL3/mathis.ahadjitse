from Grade import Grade
from datetime import datetime

class Employe:

    def __init__(self, numero, nom, Grade, dateEmbauche):
        self.__numero = numero
        self.__nom = nom
        self.__qualification = Grade
        self.__dateEmbauche =  dateEmbauche
        
    def coutHoraire(self):
        taux_horaire = self.__qualification.tauxHoraire()
        anciennete = self.getAnciennete(self.__dateEmbauche)
        if anciennete >= 5 and anciennete <= 10:
            return taux_horaire * 0.05
        elif anciennete >= 11 and anciennete <=15:
            return taux_horaire * 0.08
        else:
            return taux_horaire * 0.12

    def getNumero(self):
        return self.__numero

    def getNom(self):
        return self.__nom

    def getQualification(self):
        return self.__qualification

    def getDateEmbauche(self):
        return self.__dateEmbauche

    def getAnciennete(self, date):
        now = datetime.now()
        embauche_date = datetime.strptime(self.__dateEmbauche, "%Y-%m-%d")
        duree = now - embauche_date
        return duree.days
        
