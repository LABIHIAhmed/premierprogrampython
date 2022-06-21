print("Debut de programme")

def calcul_factorielle(nombre) :
    if nombre<2 : 
        return 1;
    else :
       return nombre*calcul_factorielle(nombre-1);

print(calcul_factorielle(1));
print(calcul_factorielle(2));
print(calcul_factorielle(7));
print(calcul_factorielle(20));
print(calcul_factorielle(200));
print("Fin de programme")
