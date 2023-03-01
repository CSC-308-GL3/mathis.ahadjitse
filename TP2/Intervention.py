from Employe import Employe

class Intervention:
    
    def __init__(self, numero, date, duree, tarifkm, Employe):
        self.__numero = numero
        self.__date = date
        self.__duree = duree
        self.__tarifkm = tarifkm
        self.__technicien = Employe
    
    def affiche(self):
        print("Numero : ", self.__numero)
        print("Date : ", self.__date)
        print("Technicien : ", self.__technicien)
        print("Durée : ", self.duree)
        print("Frais kilométriques : ", self.fraisKm(), " €")
        print("Frais de main-d'œuvre : ", self.fraisMo(), " €")
    
    def fraisKm(self, dist):
        return self.__tarifkm * dist
    
    def fraisMo(self):
        coef = 1.0 + self.__technicien.coutHoraire()
        return coef * self.__duree * self.__technicien.coutHoraire()
