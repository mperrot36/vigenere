import math
def lire_fichier(chemin_fichier):
    contenu : str
    """Lit le contenu d'un fichier et le renvoie sous forme de chaîne de caractères."""
    try:
        with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
            contenu = fichier.read()
        return contenu
    except FileNotFoundError:
        return "inconnu"
    except IOError:
        return "erreur"

def trouverRepetition(texte: str, taille:int):
    compteur : int
    listeRepetition: list[str]
    listeRepetition=[]
    for compteur in range(len(texte)-taille):
        if texte[compteur:compteur + taille] in texte[compteur+taille-1:]:
            listeRepetition.append(texte[compteur:compteur + taille] )
    return listeRepetition

def distance(texte:str,listeRepetition : list[str], taille:int)->list[list[str,int]]:
    repet: list[list[str,int]]
    compteur:int
    distance:int
    distance=0
    compteur=0
    fragments: str
    repet=[]
    for fragment in listeRepetition:
        distance = -1
        for compteur in range(len(texte) - (taille-1)):
            if texte[compteur:compteur + taille] == fragment: 
                if distance != -1:  
                    repet.append([fragment, compteur - distance])  
                distance = compteur 

    
    
    return repet

def chercherEtMesurer(texte:str)->list[list[str,int]]:
    compteur:int
    occurence: list[str,int]
    repet:list[list[str,int]]
    repet=[]
    repettemp:list[list[str,int]]
    for compteur in range(13,2,-1):
        repettemp=distance(texte,trouverRepetition(texte,compteur),compteur)
        
        for occurence in repettemp:
            
            repet.append(occurence)
    return repet
def pgcd(repet:list[list[str,int]]):
    compteur:int
    pgcdTemp: int
    pgcdTemp=0
    listePGCD:list[int]
    listePGCD=[]
    for compteur in range(len(repet)):
        for compteur2 in range(len(repet)):
            pgcdTemp=math.gcd(repet[compteur][1],repet[compteur2][1])
            if pgcdTemp not in listePGCD:
                listePGCD.append(pgcdTemp)
    print(listePGCD)
    
if __name__=="__main__":
    choix: str
    texte:str
    repet: list[list[str,int]]
    choix=input("Quel fichier voulez vous lire ? : ")
    texte=lire_fichier(choix)
    candidats:list[int]
    while texte=="inconnu" or texte=="erreur":
        choix=input("Problème de lecture, quel fichier voulez vous lire ? : ")
        texte=lire_fichier(choix)
    repet=chercherEtMesurer(texte)
    if repet==[]:
        print("?")
    else:
        candidats=pgcd(repet)