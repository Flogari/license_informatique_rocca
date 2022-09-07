from math import sqrt

def discriminant(a, b, c):
    delta=b*b-4*a*c
    return delta

def racine_unique(a,b):
    x=-b/(2*a)
    return x

def racine_double(a,b,delta,num):
    if num == 1:
        x1= (-b+sqrt(delta))/(2*a)
        return x1
    else:
        x2= (-b-sqrt(delta))/(2*a)
        return x2

def str_equation(a, b, c):
    a = str(a)
    b = str(b)
    c = str(c)
    equation = a+"x2+"+b+"x+"+c
    return equation

def solution_equation(a, b, c):
    delta = discriminant(a, b, c)
    equation = str_equation(a, b, c)
    print("\n")
    print("Delta = ")
    print(delta)
    print("\n")
    if delta<0:
        equation = equation+"=0\nPas de racine réel, l'équation n'a pas de solution dans R"
    elif delta == 0:
        equation = equation+"=0\nRacine unique\nx="+str(racine_unique(a, b))
    else:
        equation = equation+"=0\nRacine double\nx1="+str(racine_double(a,b,delta,1))+"\nx2="+str(racine_double(a,b,delta,2))+"\n"
    return equation


a = input("Entrez 3 nombres a, b et c, nous calculerons ensuite les solution de l'équation ax²+bx+c :\n a= \n")
a = float(a)
b = input("b = \n")
b = float(b)
c = input("c = \n")
c = float(c)
calcul = solution_equation(a, b, c)
print(calcul)
