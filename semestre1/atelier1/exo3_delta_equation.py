from math import sqrt
import random

def discriminant(a, b, c):
    """Permet de calculer delta

    Args:
        a (float): coefficient pour le x²
        b (float): coefficient pour le x
        c (float): coefficient directeur

    Returns:
        float: valeur de delta, le discriminant
    """
    return b*b-4*a*c

def racine_unique(a,b):
    """Permet de calculer la racine unique dans le cas delta=0

    Args:
        a (float): coefficient pour le x²
        b (float): coefficient pour le x

    Returns:
        float: La racine unique, solution pour l'équation ax²+bx+c=0, avec delta=0
    """
    if a!=0:
        return -b/(2*a)
    else:
        return 0


def racine_double(a,b,delta,num):
    """Permet de calculer les racines dans le cas delta > 0

    Args:
        a (float): coefficient pour le x²
        b (float): coefficient pour le x
        delta (float): discriminant
        num (float): Permet de choisir quel racine on veut calculer

    Returns:
        float: return une solution de l'équation dans le cas delta > 0
    """
    if a!=0:
        if num == 1:
            return (-b+sqrt(delta))/(2*a)
        else:
            return (-b-sqrt(delta))/(2*a)
    else:
        return 0

def str_equation(a, b, c):
    """Permet de changer les différent coefficient en chaîne de caractère pour mettre sous la forme ax²+bx+c

    Args:
        a (float): coefficient pour le x²
        b (float): coefficient pour le x
        c (float): coefficient directeur

    Returns:
        str: return l'équation sous la fourme ax²+bx+c, pour plus de clarté pour l'utilisateur
    """
    a = str(a)
    b = str(b)
    c = str(c)
    equation = a+"x2+"+b+"x+"+c
    return equation

def solution_equation(a, b, c):
    """fonction qui permet de données les solution de l'équation

    Args:
        a (float): coefficient pour le x²
        b (float): coefficient pour le x
        c (float): coefficient directeur

    Returns:
        str: return une chaîne de caractère qui donne les solution de l'équation de ax²+bx+c
    """
    delta = discriminant(a, b, c)
    equation = str_equation(a, b, c)
    print("\n")
    print("Delta = ")
    print(delta)
    print("\n")
    if delta<0:
        equation = equation+"=0\nPas de racine réel, l'équation n'a pas de solution dans R"
    elif delta == 0:
        if racine_unique(a, b) != 0:
            equation = equation+"=0\nRacine unique\nx="+str(racine_unique(a, b))
        else:
            return "Erreur, a = 0, ce n'est pas une équation du second degrés"
    else:
        if (racine_double(a,b,delta,1) and racine_double(a,b,delta,2)) !=0:
            equation = equation+"=0\nRacine double\nx1="+str(racine_double(a,b,delta,1))+"\nx2="+str(racine_double(a,b,delta,2))+"\n"
        else:
            return "Erreur, a = 0, ce n'est pas une équation du second degrés"
    return equation


a = input("Entrez 3 nombres a, b et c, nous calculerons ensuite les solution de l'équation ax²+bx+c :\n a= \n")
a = float(a)
b = input("b = \n")
b = float(b)
c = input("c = \n")
c = float(c)
calcul = solution_equation(a, b, c)
print(calcul)

i=0
for i in range(1, 10):
    a=random.randint(2, 8)
    b=random.randint(5, 11)
    c=random.randint(2, 10)
    reponse = solution_equation(a, b, c)
    print(reponse)