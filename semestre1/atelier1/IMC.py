def message_imc(imc):
    i = 0
    Liste_ref = [16.5, 18.5, 25, 30, 35, 1000]
    Liste_inter = ["Dénutrinion ou famine", "maigreur", "Corpulence normale", "Surpoids", "Obésité modérée", "Obésité sévère", "Obésité morbide"]
    Liste = Liste_ref
    Liste.append(imc)
    Liste = sorted(Liste)
    while Liste_ref[i] == Liste[i]:
        i=i+1
    reponse = Liste_inter[i]
    return reponse

imc =0
retour='\0'
imc = input("Veuillez entrez votre IMC\n")
imc = float(imc)
retour = message_imc(imc)
print(retour)

test = [15,21,28,32,40,60,0.5]

i=0
for i in test:
    retour = message_imc(i)
    print(i)
    print(" ")
    print(retour)