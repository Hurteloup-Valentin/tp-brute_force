#Exo 3

def plus_grand_nombre(liste):
    max_nombre = list[0]
    for nombre in list:
        if nombre > max_nombre :
            max_nombre = nombre
    return max_nombre

print(plus_grand_nombre([3, 58, 11, 21])) # Affiche 58 en sortie

