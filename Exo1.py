#Exo 1 

def inverser_chaine(chaine): 
    chaine_inversee = ''
    for i in range(len(chaine) - 1, -1, -1):
        chaine_inversee += chaine[i]
    return chaine_inversee

print(inverser_chaine("Bonjour")) # Affiche "ruojnoB"
