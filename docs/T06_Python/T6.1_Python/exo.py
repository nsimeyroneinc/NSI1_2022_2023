def nombreAnnees(capital):              # je crée un fonction nombreAnnees associé au paramétre d'entrée capital
    annee = 0                           # je crée une variable année que j'initialise à 0
    while capital<=10000:               # Je cée une boucle qui sera exécutée tant que capital est inférieur ou égal à 10 000
        capital = capital * 1.05 + 500         # J'augmente la valeur de capital
        print("Capital : ", capital)
        annee += 1                      # J'incrément de 1 la variable annee
        print('Année : ', annee)
    return annee                        # la fonction retourne la valeur de la variable année

nombreAnnees(1000)    # J'exécute la fonction nombreAnnees avec 1000 comme paramètre (correspondant au capital de départ)