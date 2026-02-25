import json
class Professeur:

    def __init__(self,n,p,a,s):
        self.nom=n
        self.prenom=p
        self.tel=""
        self.specialite=""
        self.salaire=s
        self.anciennete=0
        self.etatFAmilial=""
        self.dateNaissance=""
        self.adresse=a
        self.email=""

    def calculerSalaireTotal(self):
            return self.salaire+ (self.anciennete//5 * 2000)
    def toDict(self):
         dictprof={
             "nom":self.nom,
             "prenom":self.prenom,
             "tel":self.tel,
             "specialite":self.specialite,
             "salaire":self.salaire,
             "anciennete":self.anciennete,
             "etatFAmilial":self.etatFAmilial,
             "dateNaissance":self.dateNaissance,
             "adresse":self.adresse,
             "email":self.email
         }
         return dictprof
    def enregistrer(self):
        with open(f"prof{self.nom}_{self.prenom}.json",mode="w") as f:
            json.dump(self.toDict(),f)
          
            
         
        
      