#au moins majuscule et minuscule
#au moins un chiffre
#au moins un caractere spécial [!, @, #, $, %, ^, &, *]
#au moins 8 caracteres 

import hashlib
import json

mot_de_passe = input("Donnez un mot de passe")

def validateur(passeword):
    if len(passeword) <8:
        print("Le mot de passe doit contenir au moins 8 caracteres")
        
    minuscule = False
    majuscule = False
    chiffre = False
    special = False
    
    for i in range(len(passeword)):
        if passeword[i]>="a" and passeword[i]<="z":
            minuscule = True
        
        if passeword[i]>="a" and passeword[i]<="z":
             majuscule = True
             
        if passeword[i]>="a" and passeword[i]<="z":
             chiffre = True
        
        if passeword[i]=="@" or passeword[i]=="!" or passeword[i]=="#" or passeword[i]=="$" or passeword=="%" or passeword[i]=="*" or passeword[i]=="^" or passeword[i]=="&":
            special = True
            
    if minuscule==False:
        print("Le mot de passe doit comporter au moins une minuscule")
        
    if majuscule==False:
        print("Le mot de passe doit comporter une majsucule")
        
    if chiffre==False:
        print("Le mot de passe doit comporter un chiffre")
        
    if special==False:
        print("Le mot de passe doit comporter un caractere special")
        
    if (minuscule, majuscule, chiffre, special):
        print("Le mot de passe est correct")
    
    #La chaine de caractere a hasher    
    string_to_hash = "validateur_string"
    
    # Creation d'un objet hash SHA-256
    hash_object = hashlib.sha256()
    
    #Mise a jour de l'objet hash avec la chaine de caractere a hasher
    hash_object.update(string_to_hash.encode())
    
    # Recuperation du hash en hexadecimal
    hex_hash = hash_object.hexdigest()
    
    print(f"hash de la chaine '{string_to_hash}' : {hex_hash}")
    
    Donnee = {
        "mdp": "Azerty12345?", 
        "mdp2": "Salut1278!"
    }
    #Cree un fichier et stocker les donnees ecrite
    with open("donnees.json","w") as f:
        json.dump(Donnee,f)
        
    #Serialiser les donnees
    j = json.dumps(Donnee)
    print(j)
    {"mdp": "Azerty12345?",
     "mdp2": "Salut1278!"}

validateur(mot_de_passe)
                