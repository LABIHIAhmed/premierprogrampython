# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Debut de programme")
nom ="LABIHI"
prenom ="Ahmed"
def afficher(chaine) :
    print(chaine);
    
def trouver_le_prenom(age) : 
    if age>14 :
        #afficher("Ahmed");
        return "Ahmed";
    if age<4 :
        prenom="Youness"
        return prenom;
    if 4<age<8 :
        prenom="OMAR"
       
        return prenom;
    if age ==10 :
        prenom="Maroua & Safae"
       # print(prenom);
        return prenom;
    else :
        print("en attente du bébé")
        return "n'exite pas"

print(trouver_le_prenom(15));
print(trouver_le_prenom(10));
print(trouver_le_prenom(2));
print(trouver_le_prenom(8));
print(trouver_le_prenom(6));

print("Fin de programme")


