def recherche_dichotomie(element,liste):
    debut = 0
    fin = len(liste)-1
    print(debut,fin)
    while debut<fin:
        milieu = (debut+fin)//2
        val=liste[milieu]
        if element==val:
            return True
        elif element>val:
            debut=milieu+1
        else:
            fin=milieu-1
    return False

L=[2, 3, 6, 7, 11, 14, 18, 19, 24]

print(recherche_dichotomie(15,L))