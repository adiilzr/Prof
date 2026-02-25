from file1 import Professeur

p1=Professeur("tazi","aziz","fes",5000)
p2=Professeur("jilali","driss","tanger",4500)
p3=Professeur("amzil","foad","safrou",7000)

anc1=input(f"saisir l'anciennete de profeseur:{p1.nom} ")
anc2=input(f"saisir l'anciennete de profeseur:{p2.nom} ")
anc3=input(f"saisir l'anciennete de profeseur:{p3.nom} ")

p1.anciennete=int(anc1)
p2.anciennete=int(anc2)
p3.anciennete=int(anc3)

print(f"le salaire total de {p1.nom} : {p1.calculerSalaireTotal()} DH")
print(f"le salaire total de {p2.nom} : {p2.calculerSalaireTotal()} DH")
print(f"le salaire total de {p3.nom} : {p3.calculerSalaireTotal()} DH")

p1.enregistrer()
p2.enregistrer()
p3.enregistrer()