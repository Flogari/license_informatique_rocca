from datetime import date
from dateutil.relativedelta import relativedelta

def date_est_valide (jour, mois, annee): #Vérification si la date est valide
    if (0<jour<31) and (0<mois<12):
        return 1
    else:
        return 0

def saisie_date_de_naissance(): #L'utilisateur saisie sa date de naissance
    jour = input("Entrez une date en commençant par le jour \n jour = \n")
    jour = int(jour)
    mois = input("mois = \n")
    mois = int(mois)
    annee = input("annee = \n")
    annee = int(annee)
    if date_est_valide(jour, mois, annee):
        return date(annee, mois, jour)
    else:
        return 0

def age(date_naissance): #Calcul de l'âge
    today = date.today()
    jour = relativedelta(today, date_naissance)
    return jour.years

def est_majeur(date_naissance): #Vérification de la majorité
    #ages = age(date_naissance)
    today = date.today()
    jour = relativedelta(today, date_naissance)
    ages = jour.years
    if ages>=18:
        return True
    else:
        return False

date_de_naissance = saisie_date_de_naissance() 
if date_de_naissance != 0:   
    age = age(date_de_naissance)
    acces = est_majeur(date_de_naissance)
    if acces == True:
     print("Bonjour, votre age est ", age, 'ans\n')
     print("Accès autorisé")
    else:
     print("Bonjour, nous sommes désolé mais votre age est ", age, 'ans\n')
     print("Accès refusé, revenez plus tard")
else:
    print("Erreur dans la saisie de la date de naissance")