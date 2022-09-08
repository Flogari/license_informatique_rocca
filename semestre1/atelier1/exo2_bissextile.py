def est_bissextile(annee):
    if (annee%4 == 0 and annee%100 != 0) or (annee%400 == 0):
        return "L'année est bissextile\n"
    else:
        return "L'année n'est pas bissextile\n"

annee = input("Veuillez entrer une année pour vérifier si elle est bissextile (à partir de l'année 1)\n")
annee = int(annee)
reponse = est_bissextile(annee)
print(reponse)

test = [2000,2002,2004,2006,2008,2010,2012]

i=0
for i in test:
    reponse = est_bissextile(i)
    print(i)
    print(" ")
    print(reponse)