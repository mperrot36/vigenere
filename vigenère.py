
def chiffrement(texteEntrée: str, clé: str)->str:
    texteSortie:str
    compteurClé:int
    compteurClé=0
    lettre:str
    nouvelleLettre:str
    nouvelleLettre=""
    texteSortie=""
    for lettre in texteEntrée:
        if lettre>="a" and lettre<="z":
            nouvelleLettre=chr(ord(lettre)+(ord(clé[compteurClé])-(ord("a"))))
            if ord(nouvelleLettre)>ord("z"):
                nouvelleLettre=chr(ord(nouvelleLettre)-26)
            texteSortie+=nouvelleLettre
        else:
            if lettre>="A" and lettre<="Z":
                nouvelleLettre=chr(ord(lettre)+(ord(clé[compteurClé])-(ord("A"))))
                if ord(nouvelleLettre)>ord("Z"):
                    nouvelleLettre=chr(ord(nouvelleLettre)-26)
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
demanderChiffrement()