import json

class professeur:
    def __init__(self, N, p, a, s):
        self.nom = N
        self.prenom = p
        self.tel = ""
        self.specialite = ""
        self.salaire = s
        self.anciennete = 0
        self.etat_familial = ""
        self.dateNaissance = ""
        self.adresse = a
        self.email = ""

    def calculsalairetotal(self):
        return self.salaire + (self.anciennete // 5) * 2000

    def toDictr(self):
        dictprofesseur = {
            "nom": self.nom,
            "prenom": self.prenom,
            "tel": self.tel,
            "specialite": self.specialite,
            "salaire": self.salaire,
            "anciennete": self.anciennete,
            "etat_familial": self.etat_familial,
            "dateNaissance": self.dateNaissance,
            "adresse": self.adresse,
            "email": self.email
        }
        return dictprofesseur

    @staticmethod
    def fromDictr(dictprofesseur):
        N = dictprofesseur.get("nom", "")
         
        
      
