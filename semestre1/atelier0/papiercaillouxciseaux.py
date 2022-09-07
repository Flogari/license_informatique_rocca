import random

joueur2=0

reponse = input("Bonjour, pour jouer contre l'ordinateur tapez 1, \nPour jouer contre un autre joueur tapez 2 ")
if reponse != '1' and reponse != '2':
        print("Je n'ai pas compris votre réponse")
if reponse == '1':
    nom_j1 = input("Quel est votre nom ? ")
    print("Bienvenue, ",nom_j1, " nous allons jouer ensemble \n")
    nom_j2 = 'ROB'
nb_pt_j1 = 0
nombre_partie = 0
if reponse == '2':
    joueur2=1
    nom_j1 = input("Quel est votre nom ? ")
    print("Bienvenue, ",nom_j1, " nous allons jouer ensemble")
    nom_j2 = input("Quel est le nom du deuxième joueur ?")
    print("Bienvenue, ",nom_j2, " nous allons jouer ensemble \n")

continuer = True
nb_pt_j2 = 0
while continuer == True:
    nombre_partie += 1 
    choix_j1 = input("\n\n\n\n\n\n\n\n\n\n\n\n\n{nom} faîtes votre choix parmi (pierre, papier, ciseaux, puits): ".format(nom=nom_j1))
    choix_j1 = choix_j1.lower()
    if choix_j1 != 'pierre' and choix_j1 != 'papier' and choix_j1 != 'ciseaux' and choix_j1 != 'puits':
                choix_j1ok = False
                print("Je n'ai pas compris votre réponse")
                while choix_j1ok == False :
                    print("Joueur ", nom_j1)
                    choix_j1 = input("\nFaîtes votre choix parmi (pierre, papier, ciseaux, puits): ")
                    choix_j1ok = True
                    if choix_j1 != 'pierre' and choix_j1 != 'papier' and choix_j1 != 'ciseaux' and choix_j1 != 'puits':
                                choix_j1ok = False

    if joueur2 == 0:
        choix_j2 = ['papier','pierre','ciseaux','puits'][random.randint(0, 3)]


    else:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\nJoueur", nom_j2)
        choix_j2 = input("faîtes votre choix parmi (pierre, papier, ciseaux, puits): ")
        choix_j2 = choix_j2.lower()
        if choix_j2 != 'pierre' and choix_j2 != 'papier' and choix_j2 != 'ciseaux' and choix_j2 != 'puits':
                    j2bon = False
                    print("Je n'ai pas compris votre réponse")
                    while not j2bon :
                        print("Joueur ", nom_j2)
                        choix_j2 = input("\nFaîtes votre choix parmi (pierre, papier, ciseaux, puits): ")
                        j2bon = True
                        if choix_j2 != 'pierre' and choix_j2 != 'papier' and choix_j2 != 'ciseaux' and choix_j2 != 'puits':
                                    j2bon = False

    print("Si on récapitule :",nom_j1, choix_j1, "et", nom_j2, choix_j2,"\n")

    if choix_j1 == choix_j2: #Si il y a égalité, on attribut directement 0 points à chaque joueurs
        nb_pt_j1 = nb_pt_j1 + 0
        nb_pt_j2 = nb_pt_j2 + 0
        print("le gagnant est aucun de vous, vous être ex æquo")
        print("Les scores à l'issue de cette manche sont donc",nom_j1, nb_pt_j1, "et", nom_j2, nb_pt_j2, "\n")


    elif choix_j1 =='pierre': #Si le joueur 1 fait pierre, le seul coup contre lequel il gagne est le ciseaux.
        if choix_j2 =='ciseaux':
            nb_pt_j1= nb_pt_j1+1
            nb_pt_j2=nb_pt_j2+0
            print("Le gagnant est ",nom_j1)
            print("Les scores à l'issue de cette manche sont donc",nom_j1, nb_pt_j1, "et", nom_j2, nb_pt_j2, "\n")
        else: #Le joueur 2 joue papier ou puits
            nb_pt_j1= nb_pt_j1+0
            nb_pt_j2=nb_pt_j2+1
            print("Le gagnant est ",nom_j2)
            print("Les scores à l'issue de cette manche sont donc",nom_j1, nb_pt_j1, "et", nom_j2, nb_pt_j2, "\n")
            

    elif choix_j1 =='papier': #Si le joueur 1 fait papier, il gagne contre pierre et puits
        if choix_j2 =='pierre' or 'puits':
            nb_pt_j1= nb_pt_j1+1
            nb_pt_j2=nb_pt_j2+0
            print("Le gagnant est ",nom_j1)
            print("Les scores à l'issue de cette manche sont donc",nom_j1, nb_pt_j1, "et", nom_j2, nb_pt_j2, "\n")
        else: #Le joueur 2 joue ciseaux
            nb_pt_j1= nb_pt_j1+0
            nb_pt_j2=nb_pt_j2+1
            print("Le gagnant est ",nom_j2)
            print("Les scores à l'issue de cette manche sont donc",nom_j1, nb_pt_j1, "et", nom_j2, nb_pt_j2, "\n")


    elif choix_j1 =='ciseaux': #Si le joueur 1 fait ciseaux, le seul coup contre lequel il gagne est le papier.
        if choix_j2 =='papier':
            nb_pt_j1= nb_pt_j1+1
            nb_pt_j2=nb_pt_j2+0
            print("Le gagnant est ",nom_j1)
            print("Les scores à l'issue de cette manche sont donc",nom_j1, nb_pt_j1, "et", nom_j2, nb_pt_j2, "\n")
        else: #Le joueur 2 joue pierre ou puits, et donc, bats le ciseaux.
            nb_pt_j1= nb_pt_j1+0
            nb_pt_j2=nb_pt_j2+1
            print("Le gagnant est ",nom_j2)
            print("Les scores à l'issue de cette manche sont donc",nom_j1, nb_pt_j1, "et", nom_j2, nb_pt_j2, "\n")


    else: #Le joueur 1 joue puits, il ne perd que contre la feuille.
        if choix_j2 =='pierre' or 'ciseaux':
            nb_pt_j1= nb_pt_j1+1
            nb_pt_j2=nb_pt_j2+0
            print("Le gagnant est ",nom_j1)
            print("Les scores à l'issue de cette manche sont donc",nom_j1, nb_pt_j1, "et", nom_j2, nb_pt_j2, "\n")
        else: #Le jouer 2 fait papier
            nb_pt_j1= nb_pt_j1+0
            nb_pt_j2=nb_pt_j2+1
            print("Le gagnant est ",nom_j2)
            print("Les scores à l'issue de cette manche sont donc",nom_j1, nb_pt_j1, "et", nom_j2, nb_pt_j2, "\n")


    if nombre_partie!=5:
        continuer = True
        recommencer = input("Souhaitez vous refaire une partie {} contre {} ? (1 = oui/2 = non) ".format(nom_j1,nom_j2))
        if recommencer == '1':
            continuer = True
        elif recommencer == '2':
            continuer = False
        else:
            print("Je n'ai pas compris votre réponse\n")
            while recommencer !='1'and recommencer !='0' :
                recommencer = input("\n\nSouhaitez vous refaire une partie {} contre {} ? (1 = oui/2 = non) ".format(nom_j1,nom_j2))
        if recommencer == '1':
            continuer = True
        else:
            continuer = False
    else: continuer = False
  
        
if continuer == False :
    print("Merci d'avoir joué ! A bientôt")