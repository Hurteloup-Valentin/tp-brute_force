#Exo5, Palindrome choisi = Kayak

def est_palindrome(mot):
    longeur = len(mot)
    for i in range(0,4):
        test = mot[-i]
        Test1 = mot[i]
        if mot[i] != mot[-i]:
            return False
    return True

est_palindrome("kayak") #Aifficher True
