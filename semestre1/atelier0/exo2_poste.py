POIDS_MIN = 0
POIDS_MOY1 = 20
POIDS_MOY2 = 100
POIDS_MOY3 = 250
POIDS_MOY4 = 500
POIDS_MOY5 = 1000
POIDS_MAX = 3000

def saisie_lettre():
     #L'utilisateur saisie le type de lettre, on renvoie le type de lettre choisie
     type_lettre = input("\nBonjour, bienvenue dans le service de la poste national française !\nFaite votre choix d'envoie\n-Tapez 1 pour une lettre Verte\n-Tapez 2 pour une lettre Prioritaire\n-Tapez 3 pour une lettre Eco-pli\n")
     if type_lettre != '1' and type_lettre != '2' and type_lettre != '3':
                continuer = False
                print("Je n'ai pas compris votre réponse, veuillez choisir entre 1,2 ou 3")
                while continuer == False :
                    type_lettre = input("\nBonjour, bienvenue dans le service de la poste national française !\nFaite votre choix d'envoie\n-Tapez 1 pour une lettre Verte\n-Tapez 2 pour une lettre Prioritaire\n-Tapez 3 pour une lettre Eco-pli\n")
                    continuer = True
                    if type_lettre != '1' and type_lettre != '2' and type_lettre != '3':
                                continuer = False
     return type_lettre


def saisie_poids(type_lettre):
     #L'utilisateur, en fonction du type de lettre en paramètre, va entrer un poids, la fonction retourne le poids
     if type_lettre == '1':
           poids = input("\nVeuillez saisir le poids de votre lettre en gramme (rappel : 1kg = 1000g), attention de ne pas dépasser 3kg\n")
           poids = int(poids)
           if poids < POIDS_MIN or poids > POIDS_MAX:
                continuer = False
                print("Attention, le poids ne doit pas être en dessous de 0 grammes et pas au dessus de 3000 grammes")
                while continuer == False :
                   poids = input("\nVeuillez saisir le poids de votre lettre en gramme (rappel : 1kg = 1000g), attention de ne pas dépasser 3kg\n")
                   poids = int(poids)
                   continuer = True
                   if poids < POIDS_MIN or poids > POIDS_MAX:
                                continuer = False

     elif type_lettre == '2':
          poids = input("\nVeuillez saisir le poids de votre lettre en gramme (rappel : 1kg = 1000g), attention de ne pas dépasser 1kg\n")
          poids = int(poids)
          if poids < POIDS_MIN or poids > POIDS_MOY5:
                continuer = False
                print("Attention, le poids ne doit pas être en dessous de 0 grammes et pas au dessus de 1000 grammes\n")
                while continuer == False :
                   poids = input("\nVeuillez saisir le poids de votre lettre en gramme (rappel : 1kg = 1000g), attention de ne pas dépasser 3kg\n")
                   poids = int(poids)
                   continuer = True
                   if poids < POIDS_MIN or poids > POIDS_MOY5:
                                continuer = False

     else:
          poids = input("\nVeuillez saisir le poids de votre lettre en gramme (rappel : 1kg = 1000g), attention de ne pas dépasser 250g\n")
          poids = int(poids)
          if poids < POIDS_MIN or poids > POIDS_MOY3:
                continuer = False
                print("Attention, le poids ne doit pas être en dessous de 0 grammes et pas au dessus de 250 grammes")
                while continuer == False :
                   poids = input("\nVeuillez saisir le poids de votre lettre en gramme (rappel : 1kg = 1000g), attention de ne pas dépasser 250g\n")
                   poids = int(poids)
                   continuer = True
                   if poids < POIDS_MIN or poids > POIDS_MOY3:
                                continuer = False
     return poids


def calcul_prix(type_lettre, poids):
     #En fonction du type de lettre et du poids en paramètre, la fonction calcul et renvoie le prix associé
     if type_lettre == '1':
          if poids <= POIDS_MOY1:
               prix = 1.16
          elif POIDS_MOY1 < poids <= POIDS_MOY2:
               prix = 2.32
          elif POIDS_MOY2 < poids <= POIDS_MOY3:
               prix = 4.0
          elif POIDS_MOY3 < poids <= POIDS_MOY4:
               prix = 6.0
          elif POIDS_MOY4 < poids <= POIDS_MOY5:
               prix = 7.50
          else:
               prix = 10.5
     elif type_lettre == '2':
          if poids <= POIDS_MOY1:
               prix = 1.43
          elif POIDS_MOY1 < poids <= POIDS_MOY2:
               prix = 2.86
          elif POIDS_MOY2 < poids <= POIDS_MOY3:
               prix = 5.26
          elif POIDS_MOY3 < poids <= POIDS_MOY4:
               prix = 7.89
          else:
               prix = 11.44
     else:
          if poids <= POIDS_MOY1:
               prix = 1.14
          elif POIDS_MOY1 < poids <= POIDS_MOY2:
               prix = 2.28
          else:
               prix = 3.92
     return prix


type_lettre = saisie_lettre()
poids = saisie_poids(type_lettre)
prix = calcul_prix(type_lettre, poids)

print("Récapitulatif : Vous avez choisie l'option ", type_lettre, "et un poids de ",poids,"g, le prix vous revients donc à ",prix,"€")
