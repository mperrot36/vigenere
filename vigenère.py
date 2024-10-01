
def chiffrement(texteEntrée: str, clé: str)->str:
    texteSortie:str
    compteurClé:int
    limite: int
    compteurClé=0
    lettre:str
    nouvelleLettre:str
    nouvelleLettre=""
    texteSortie=""
    limite=0
    for lettre in texteEntrée:
        if clé[compteurClé]>="a" and clé[compteurClé]<="z":
            limite=ord("a")
        else:
            limite=ord("A")
        if lettre>="a" and lettre<="z":
            nouvelleLettre=chr(ord(lettre)+(ord(clé[compteurClé])-limite))
            if nouvelleLettre>"z":
                nouvelleLettre=chr(ord(nouvelleLettre)-26)
            texteSortie+=nouvelleLettre
            compteurClé=(compteurClé+1)%len(clé)
        else:
            if lettre>="A" and lettre<="Z":
                nouvelleLettre=chr(ord(lettre)+(ord(clé[compteurClé])-limite))
                if nouvelleLettre>"Z":
                    nouvelleLettre=chr(ord(nouvelleLettre)-26)
                texteSortie+=nouvelleLettre
                compteurClé=(compteurClé+1)%len(clé)





        
    
    return texteSortie

def dechiffrement(texteEntrée: str, clé: str)->str:
    texteSortie:str
    compteurClé:int
    limite: int
    compteurClé=0
    lettre:str
    nouvelleLettre:str
    nouvelleLettre=""
    texteSortie=""
    limite=0
    for lettre in texteEntrée:
        if clé[compteurClé]>="a" and clé[compteurClé]<="z":
            limite=ord("a")
        else:
            limite=ord("A")
        if lettre>="a" and lettre<="z":
            nouvelleLettre=chr(ord(lettre)-(ord(clé[compteurClé])-limite))
            if ord(nouvelleLettre)<ord("a"):
                nouvelleLettre=chr(ord(nouvelleLettre)+26)
            texteSortie+=nouvelleLettre
            compteurClé=(compteurClé+1)%len(clé)
            
        else:
            if lettre>="A" and lettre<="Z":
                nouvelleLettre=chr(ord(lettre)-(ord(clé[compteurClé])-limite))
                if ord(nouvelleLettre)<ord("A"):
                    nouvelleLettre=chr(ord(nouvelleLettre)+26)
                texteSortie+=nouvelleLettre
            compteurClé=(compteurClé+1)%len(clé)
    return texteSortie



def texteValide(texteAVerifier:str)->bool:
    verif:bool
    lettre:str
    verif=True
    for lettre in texteAVerifier:
        if lettre in "1234567890":
            verif=False
    return verif
    

def demanderChiffrement():
    texteEntrée : str
    clé : str
    texteSortie:str
    texteEntrée=input("Que voulez vous chiffrer ? : ")
    while texteValide(texteEntrée)!=True:
        texteEntrée=input("Caractère non reconnu, Que voulez vous chiffrer ? : ")
    clé=input("Rentrez votre clé : ")
    while texteValide(texteEntrée)!=True:
        clé=input("Caractère non reconnu, Rentrez votre clé : ")
    texteSortie=chiffrement(texteEntrée,clé)
    print(texteSortie)



def demanderDechiffrement():
    texteEntrée : str
    clé : str
    texteSortie:str
    texteEntrée=input("Que voulez vous déchiffrer ? : ")
    while texteValide(texteEntrée)!=True:
        texteEntrée=input("Caractère non reconnu, Que voulez vous déchiffrer ? : ")
    clé=input("Rentrez votre clé : ")
    while texteValide(texteEntrée)!=True:
        clé=input("Caractère non reconnu, Rentrez votre clé : ")
    texteSortie=dechiffrement(texteEntrée,clé)
    print(texteSortie)


if __name__=="__main__":
    choix:int
    choixQuitter:int
    choixQuitter=3
    choix=0
    
    while choix!=choixQuitter:
        print("1-Chiffrer")
        print("2-Déchiffrer")
        print("3-Quitter")
        choix=int(input("Que souhaitez vous faire ? : "))
        
        if choix==1:
            demanderChiffrement()
        elif choix==2:
            demanderDechiffrement()
        
    
            
            

