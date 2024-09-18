#Exo 2

def somme_liste(liste):
    somme = 0
    addition = 0
    for abcd in liste:
        somme += liste[addition]
        addition = addition + 1
    return somme

print(somme_liste([1, 2, 3, 4])) #Affiche 10

#Plus court :

def somme_liste(liste):
    somme = 0
    for abcd in liste:
        somme += abcd
    return somme

print(somme_liste([1, 2, 3, 4])) #Affiche 10

#Sans boucle :

#Bémol avec cette méthode en ce qui concerne le fait d'ajouter des valeur dans la liste,
#car le programme ne detecteras pas les nouvelles entrée

def somme_liste(liste):
    somme = 0
    somme = somme + liste[0]
    somme = somme + liste[1]
    somme = somme + liste[2]
    somme = somme + liste[3]
    somme = somme + liste[4]
    return somme

print(somme_liste([1, 2, 3, 4])) #Affiche 10

