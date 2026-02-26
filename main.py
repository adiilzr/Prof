from file1 import professeur
import json  
with open("professeurs.json", mode="r", encoding="utf-8") as f:    lista=json.load(f)


listprofs=[]
for dicto in lista:
    listprofs.append(professeur.fromDictr(dicto))

print("nombre de professeurs:",len(lista))
print("le professur 89 est:",listprofs[89].nom,listprofs[89].prenom)
