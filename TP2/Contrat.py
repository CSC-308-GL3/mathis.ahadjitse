from Client import Client

class Contrat:

    def __init__(self, numero, date, Client, montantContrat, interventions):
        self.__numero = numero
        self.__date = date
        self.__client = Client
        self.__montantContrat = montantContrat
        self.__interventions = interventions
        self.__nbIntervention = len(interventions)

    def montant(self):
        return self.__montantContrat

    def ecart(self):
        coutDesInterventions = 0
        for intervention in self.__interventions:
            coutDesInterventions += intervention.fraisKm(0) + intervention.fraisMo()
        return self.__montantContrat - coutDesInterventions
