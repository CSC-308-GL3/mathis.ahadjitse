from Employe import Employe
from Grade import Grade
from Intervention import Intervention
from Contrat import Contrat
from Client import Client

grade = Grade('G1', 'Grade 2', 50)
employe = Employe(1, 'AHADJITSE Mathis', grade, '2010-01-01')
client = Client(1, 'TOBGE Yawa', 'Lomé-TOGO', '75000', 'TOGI', 10)
intervention1 = Intervention(1, '2022-01-01', 3, 0.5, employe)
intervention2 = Intervention(2, '2022-01-02', 2, 0.5, employe)
intervention3 = Intervention(3, '2022-01-03', 1, 0.5, employe)
contrat = Contrat(1, '2022-01-01', client, 2000, [intervention1, intervention2, intervention3])

ecart = contrat.ecart()

print("L'écart entre le montant du contrat et le coût des interventions est de : ", ecart)
