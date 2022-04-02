---
title : TD - Les dictionnaires
---

<table  class="blueTable">
        <tr>
            <th>
            Thème 3 : Traitement des données
            </th>
        </tr>
</table>
<br>
<table  class="blueTable">
        <tr >
            <th width="20%"; style="background-color: #3B444B;color:white;text-align:center;border:none;font-size:40pt;">
            19
            </th>
            <th  width="80%"; style="text-align:center;border:none;font-size:25pt;">Manipulation de fichiers CSV</th>
        </tr>
</table>
<br>



**Programme N.S.I**

|Contenus| Capacités attendues | Commentaires|
|:---|:---|:---|
|Indexation de tables| Importer une table depuis un fichier texte tabulé ou un fichier CSV. | Est utilisé un tableau doublement indexé ou un tableau de p-uplets  qui partagent les mêmes descripteurs. | 
|Recherche dans une table | Rechercher les lignes d’une table vérifiant des critères exprimés en logique propositionnelle | La recherche de doublons, les tests de cohérence d’une  table sont présentés | 

> Les fichiers **CSV (pour Comma Separated Values)** sont des fichiers-texte (ils ne contiennent aucune mise en forme) utilisés pour stocker des données, séparées par des virgules (ou des points-virgules, ou des espaces...). Il n'y a pas de norme officielle du CSV.  


# Ouverture d'un fichier CSV par des logiciels classiques
- Ouvrir avec le Bloc-Notes le fichier `Les colleges_Puy_De_dome_2022.csv`.
- Ouvrir le fichier avec LibreOffice.

# Exploitation avec Python



## Exercice n°1 : Exploitation d'un fichier CSV en Python avec le module CSV

L'utilisation d'un tableur peut être délicate lorsque le fichier CSV comporte un très grand nombre de lignes. 
Python permet de lire et d'extraire des informations d'un fichier CSV même très volumineux, grâce à des modules dédiés, comme le bien-nommé `csv` (utilisé ici) ou bien `pandas` (qui sera vu plus tard).


```python
import csv                          
f = open('Les_colleges_Puy_De_Dome_2022.csv', "r", encoding = 'utf-8') # le "r" signifie "read", le fichier est ouvert en lecture seule
donnees = csv.reader(f)  # donnees est un objet (spécifique au module csv) qui contient des lignes

for ligne in donnees:               
    print(ligne)
    
f.close()    # toujours fermer le fichier !
```

### Problèmes :  

1. Les données ne sont pas structurées : la première ligne est la ligne des «descripteurs» (ou des «champs»), alors que les lignes suivantes sont les valeurs de ces descripteurs.
2. La variable `donnees` n'est pas exploitable en l'état.


### Améliorations
Au lieu d'utiliser la fonction `csv.reader()`, utilisons `csv.DictReader()`. Comme son nom l'indique, elle renverra une variable contenant des dictionnaires.


```python
import csv
f = open('Les_colleges_Puy_De_Dome_2022.csv', "r", encoding = 'utf-8')
donnees = csv.DictReader(f)

for ligne in donnees:
    print(ligne)

f.close()
```

C'est mieux ! Les données sont maintenant des dictionnaires. Comment ré-accéder au premier d'entre eux ?


```python
donnees[0]
```

Erreur normal, nous allons donc créer une liste de dictionnaires.


```python
import csv
global colleges
f = open('Les_colleges_Puy_De_Dome_2022.csv', "r", encoding = 'utf-8')
donnees = csv.DictReader(f)
colleges = []
for ligne in donnees:
    colleges.append(dict(ligne))
    
    
descripteurs=colleges[0]  # on stocke les descripteurs dans une variable

colleges.pop(0)   # on enlève les descripteurs
    
f.close()    # toujours fermer le fichier
```


```python
descripteurs
```


```python
print(colleges[1]['Nom du Canton'])
```

    LES MONTS-DU-LIVRADOIS



```python
print(colleges[2]['Nom'])
```

    Collège Liziniat



```python
print(colleges[2]['Nom du (de la) Principal(e)'])
```

    M. FAURE Michel


**Question 1 :** Compléter la fonction `plus_grand_college(colleges)` qui renvoie la commune, le nom du collège et le nom du (de la) principal(e)


```python
def plus_grand_college():
    maxi=0
    nom=''
    commune=''
    principal=''
    for col in colleges:
        if int(col['Effectif'])>maxi:
            maxi=int(col['Effectif'])
            nom=col['Nom']
            commune=col['Commune']
            principal=col['Nom du (de la) Principal(e)']
    return nom,commune,principal,maxi

plus_grand_college()

```




    ('Collège I. et F. Joliot Curie', 'AUBIERE', 'Mr COMMEAU Richard', 858)



**Question  2 :** Ecrire une fonction `plus_petit_college(colleges)` qui renvoie la commune, le nom du collège et le nom du (de la) principal(e)


```python
def plus_petit_college():
    mini=1E99
    nom=''
    commune=''
    principal=''
    for col in colleges:
        if int(col['Effectif'])<mini:
            mini=int(col['Effectif'])
            nom=col['Nom']
            commune=col['Commune']
            principal=col['Nom du (de la) Principal(e)']
    return nom,commune,principal,mini


plus_petit_college()



```




    ('Collège Alexandre Vialatte', 'SAINT-AMANT-ROCHE-SAVINE', 'Plus de poste de Principal', 24)



**Question  3 :** 
Ecrire une fonction `moyenne()` qui renvoie le nombre d'èléves moyen dans les collèges.


```python
def moyenne():
    somme=0
    nb2colleges=len(colleges)
    for col in colleges:
        somme+=int(col['Effectif'])
    moy=somme/nb2colleges
    return moy
    

round(moyenne(),1)
```




    388.7



**Question 4 :**  Ecrire une fonction `renseignement(college)` qui renvoie les renseignements sur le collége choisi.


```python
def renseignement(college):
    for col in colleges:
        if col['Nom']==college:
            return col
    return "Pas dans la base"

renseignement('Collège I. et F. Joliot Curie')
```




    {'Code Education nationale': '0631451K', 'Type de collège': 'Public', 'Nom': 'Collège I. et F. Joliot Curie', 'Adresse': 'Avenue Charles de Gaulle - 63170 AUBIERE', 'Code Poste': '63170', 'Commune': 'AUBIERE', 'Téléphone': '04 73 26 02 25', 'adresse e-mail': 'Ce.0631451K@ac-clermont.fr', 'Nom du (de la) Principal(e)': 'Mr COMMEAU Richard', 'Effectif': '858', 'année scolaire': '2021/2022', 'Code INSEE de la commune': '63014', 'Coordonnée X GPS': '3,119102', 'Coordonnée Y GPS': '45,751291', 'Date de début': '01/09/2021', 'Date de fin': '01/07/2022', "Identifiant de l'opération de chargement": '927', 'Code INSEE du Canton': '6303', 'Nom du Canton': 'AUBIERE', "numero de SIREN de l'EPCI": '246300701', "Nom de l'EPCI": 'Clermont Auvergne Métropole', 'Année de référence': '2021', 'Identifiant interne': '565'}



**Question 5 :**  Ecrire une fonction `renseignement(commune)` qui renvoie les renseignements sur le(s) colléges de la commune ainsi que leur nombre.


```python
def renseignement_commune(commune):
    rep=[]
    nb=0
    for col in colleges:
        if col['Commune']==commune:
            rep.append(col['Nom'])
            nb+=1
    
    return nb,rep

renseignement_commune('ISSOIRE')
```




    (3, ['Collège Verrière', 'Collège Les Prés', 'Collège Sévigné-Saint-Louis'])



## Exercice n°2 : les joueurs de rugby du TOP14



Le fichier `Top14.csv ` contient tous les joueurs du Top14 de rugby, avec : 

- ID  
- Nom  
- Âge, Taille, Poids  
- Nationalité  
- Poste  
- Matchs  
- E, T, P, D, J, R  
- Temps de jeu  
- Club    
. 

Ce fichier a été généré sur le site _[https://www.allrugby.com/stats/moteur.html](https://www.allrugby.com/stats/moteur.html)


**Question 1.** Stocker dans  une variable `joueurs`  les renseignements de tous les joueurs présents dans ce fichier csv.


```python
import csv
f = open('Top14.csv', "r", encoding = 'utf-8')
donnees = csv.DictReader(f)
joueurs=[]
for ligne in donnees:
    joueurs.append(ligne)
    
f.close()

```

**Question 2.** Combien de joueurs sont présents dans ce fichier ?


```python
nb2joueurs=len(joueurs)
nb2joueurs
```




    618



**Question 3.** Quel est le nom prénom du joueur n°486 ?


```python
joueurs[485]['Nom']
```




    'KHARAISHVILI Gia'



**Question 4.** Ecrire une fonction permettant d'obtenir le numero d'un joueur connaissant son nom.


```python
def numero(nom):
    pos=0
    for jo in joueurs:
        if jo['Nom']==nom:
            return pos
        pos+=1
    
numero('SERIN Baptiste')
```




    89



### Extraction de données particulières

**Question 5.** 
Ecrire une fonction `clubJoueur(joueur)` permettant de savoir où joue un joueur ?  
A appliquer avec Baptiste SERIN ?  
La méthode la plus naturelle est de parcourir toute la liste jusqu'à trouver le bon joueur, puis d'afficher son équipe :


```python
def clubJoueur(joueur):
    club=''
    for jo in joueurs:
        if jo['Nom']==joueur:
            return jo['Club']
        
clubJoueur('SERIN Baptiste')
```




    'Toulon'



Une méthode plus efficace est d'utiliser une liste par compréhension incluant un test. 
Rappel : 


```python
exemple = [k for k in range(1,50) if k % 3 == 0]
print(exemple)
```

    [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48]


Procéder de même pour retrouver le club de Baptiste SERIN.


```python
clubSerin = [k['Club'] for k in joueurs if k['Nom'] == 'SERIN Baptiste']
print(clubSerin)
```

    ['Toulon']


**Question 6.** 
Ecrire une fonction `joueurPoid(poid)` qui renvoie la liste des joueurs de plus de poid kg ?  
A tester avec les joueurs de plus de 140 kg


```python
def joueurPoid(poid):
    liste=[]
    for jo in joueurs:
        if int(jo['Poids']) >=poid:
            liste.append(jo['Nom'])
    return liste

joueurPoid(140)
```




    ['HAMADACHE Malik', 'ATONIO Uini', 'TAMEIFUNA Ben', 'SKELTON Will', 'OZ Ali', 'SCLAVI Joel', 'MEAFOU Emmanuel']



Il est impératif de convertir la chaine de caractère renvoyée par `k['Poids']` en entier, par la fonction `int()`.

**Question 7.** Ecrire une fonction `taille_moyenne(poste)` renvoyant la taille moyenne des joueurs en fonction du poste.


```python
def taille_moyenne(poste):
    somme=0
    nb=0
    for jo in joueurs:
        if jo['Poste']==poste:
            somme=somme+int(jo['Taille'])
            nb+=1
    return somme/nb

taille_moyenne('Centre')
```




    184.33823529411765



**Question 8.** Ecrire une fonction `poid_moyenne(poste)` renvoyant le poid moyen des joueurs en fonction du poste.


```python
def poid_moyenne(poste):
    somme=0
    nb=0
    for jo in joueurs:
        if jo['Poste']==poste:
            somme=somme+int(jo['Poids'])
            nb+=1
    return somme/nb

poid_moyenne('Centre')
```




    97.16176470588235



**Question 9.** Ecrire une fonction renvoyant la taille et le poid moyen des joueurs par équipe.


```python
def listejoueur(club):
    liste=[]
    for jo in joueurs:
        if jo['Club']==club:
            liste.append(jo)
    return liste

def taille_moyenne_joueur(liste):
    somme=0
    for jo in liste:
        somme+=int(jo['Taille'])
    return somme/len(liste)
    
def poids_moyen_joueur(liste):
    somme=0
    for jo in liste:
        somme+=int(jo['Poids'])
    return somme/len(liste)

def taille_poid_moyen_club(club):
    liste=listejoueur(club)
    return poids_moyen_joueur(liste),taille_moyenne_joueur(liste)
        

taille_poid_moyen_club('Toulon')
```




    (104.06122448979592, 185.46938775510205)



### Exploitation graphique
Nous allons utiliser le module Matplotlib pour illustrer les données de notre fichier csv.

### Exemple 


```python
import matplotlib.pyplot as plt
plt.close()
X = [0,1,3,6,8]
Y = [12,10,7,15,11]
plt.plot(X,Y,'gs') # r pour red, o pour un cercle. voir https://matplotlib.org/api/markers_api.html
plt.show()
```



### Application

**Question 10.** Afficher sur un graphique tous les joueurs de rugby du top14, en mettant le poids en abscisse et la taille en ordonnée.



```python
plt.close()
X=[]
Y=[]
for k in joueurs:
    p=int(k['Poids'])
    X.append(p)
    t=int(k['Taille'])
    Y.append(t)

plt.plot(X,Y,'ro') # r pour red, o pour un cercle. voir https://matplotlib.org/api/markers_api.html
plt.show()

```



**Question 11.** Faire apparaître ensuite les joueurs évoluant au poste de Centre en bleu (b), les 2ème lignes en vert (g), les demis de Mêlée en magenta (m), les Piliers en jaune et les Arrières en cyan (c).


```python
plt.close()
#tous les joueurs
X = [int(k['Poids']) for k in joueurs]
Y = [int(k['Taille']) for k in joueurs]
plt.plot(X,Y,'ro') 

#on recolorie les Centres en bleu
X = [int(k['Poids']) for k in joueurs if k['Poste'] == 'Centre']
Y = [int(k['Taille']) for k in joueurs if k['Poste'] == 'Centre']
plt.plot(X,Y,'bo')

#on recolorie les 2ème ligne en vert
X = [int(k['Poids']) for k in joueurs if k['Poste'] == '2ème ligne']
Y = [int(k['Taille']) for k in joueurs if k['Poste'] == '2ème ligne']
plt.plot(X,Y,'go')

#on recolorie les Pilier en jaune
X = [int(k['Poids']) for k in joueurs if k['Poste'] == 'Pilier']
Y = [int(k['Taille']) for k in joueurs if k['Poste'] == 'Pilier']
plt.plot(X,Y,'yo')

#on recolorie les demi de Mêlée en magenta
X = [int(k['Poids']) for k in joueurs if k['Poste'] == 'Mêlée']
Y = [int(k['Taille']) for k in joueurs if k['Poste'] == 'Mêlée']
plt.plot(X,Y,'mo')

#on recolorie les Arrières en cyan
X = [int(k['Poids']) for k in joueurs if k['Poste'] == 'Arrière']
Y = [int(k['Taille']) for k in joueurs if k['Poste'] == 'Arrière']
plt.plot(X,Y,'co')
plt.show()

```



# Trier des données

**Programme N.S.I**

|Contenus| Capacités attendues | Commentaires|
|:---|:---|:---|
|Tri d'une table| Trier une table suivant une colonne | Une fonction de tri intégrée au système ou à une bibliothèque peut être utilisée | 

### Créer une fonction filtre
**Question 12.**  
L'objectif est de créer une fonction `joueursClub(equipe)` qui renvoie une liste contentant tous les joueurs de l'équipe `equipe`.   
Le paramètre `equipe` sera donnée sous forme de chaîne de caractères.  
La valeur renvoyée sera de type liste.


```python
def joueursClub(equipe):
    ret = []
    
    for k in joueurs :
        if k['Club'] == equipe :
            ret.append(k)
    
    return ret

joueursClub("Clermont")
```

**Question 13.**  
Ecrire une fonction `nomJoueursClub(equipe)` qui cette fois ne renvoie que les noms des joueurs pour le club.


```python
def nomJoueursClub(equipe):
    """
    The function nomJoueursClub(equipe) takes as input the name of a team and returns the list of the
    names of the players of the team
    
    :param equipe: the name of the team you want to get the players of
    :return: A list of strings
    """
    rep=joueursClub(equipe)
    jrs=[]
    for k in rep:
        jrs.append(k['Nom']) 
            
    
    return jrs

print(len(nomJoueursClub("Clermont")))
nomJoueursClub("Clermont")
```

    45





    ['PARRA Morgan', 'FOFANA Wesley', 'BÉZY Sébastien', 'BARRAQUE Jean-Pascal', 'JEDRASIAK Paul', "O'CONNOR Marvin", 'SLIMANI Rabah', 'VAHAAMAHINA Sébastien', 'LOPEZ Camille', 'PÉLISSIÉ Adrien', 'LEE Fritz', 'FALGOUX Etienne', 'YATO Peceli', 'HANRAHAN JJ', 'LAVANINI Tomás', 'POURAILLY Bastien', 'CANCORIET Judicaël', 'ITURRIA Arthur', 'PENAUD Damian', 'RAKA Alivereti', 'NAQALEVU Apisai', 'RAVAI Peni', 'MATSUSHIMA Kotaro', 'FOURCADE Etienne', 'BEHEREGARAY Yohan', 'MOALA George', 'VILI Tani', 'FALATEA Sipili', 'OJOVAN Cristian', 'FISCHER Alexandre', 'VAN TONDER Jaco', 'VIALLARD Kévin', 'BIBI BIZIWU Daniel', 'BERIA Giorgi', 'TIBERGHIEN Cheikh', 'LANEN Clément', 'LANEN Thibault', 'DESSAIGNE Lucas', 'BOUDOU Benjamin', 'MICHET Gabin', 'AMATOSERO Miles', 'ANNANDALE Edward', 'JAUNEAU Baptiste', 'ROZIÈRE Thomas', 'MAGURANYANGA TJ']



**Question 14.**  
Définir de la même manière une fonction `joueursPoste(poste)`. pour l'ensemble des joueurs puis écrire une fonction pour le nom des joueurs club par poste.


```python
def joueursPoste(poste):
    jrs=[]
    for k in joueurs:
        if k['Poste']==poste:
            jrs.append(k['Nom']) 
    return jrs

joueursPoste('Mêlée')


```




    ['PARRA Morgan', 'LESGOURGUES Yann', 'BÉZY Sébastien', 'MACHENAUD Maxime', 'PÉLISSIÉ Jonathan', 'PAILLAUGUE Benoît', 'ECOCHARD Tom', 'HART James', 'KOCKOTT Rory', 'SERIN Baptiste', 'DAUBAGNA Thibault', 'BALÈS Alexi', 'ABADIE Paul', 'IRIBAREN Teddy', 'DARBO Clément', 'LE BAIL Jules', 'LUCU Maxime', 'DUPONT Antoine', 'TAKULUA Tane', 'BLANC Julien', 'SANGA Enzo', 'LOBZHANIDZE Vasil', 'LANDAJO Martín', 'CUBELLI Tomás', 'KERR-BARLOW Tawera', 'LE BAIL Clovis', 'COUILLOUD Baptiste', 'COVILLE Arthur', 'HALL James', 'DEGHMACHE Sadek', 'APRASIDZE Gela', 'FERNANDEZ Jérémy', 'REINACH Cobus', 'VIALLARD Kévin', 'SHORT Mitch', 'BERJON Thomas', 'PAGE-RELO Martin', 'ARATA Santiago', 'RODOR Matteo', 'GERMAIN Baptiste', 'AURREKOETXEA Kerman', 'PERCILLIER Will', 'COUILLOUD Barnabé', 'IDJELLIDAINE Théo', 'LE GARREC Nolann', 'LEVRON Alexis', 'JAUNEAU Baptiste', 'DANGLOT Jules', 'DOAN Martin', 'EYMERI Aubin', 'RIMET Liam']




```python
def joueursPosteClub(poste,equipe):
    jrs=[]
    for k in joueurs:
        if k['Poste']==poste and k['Club']==equipe:
            jrs.append(k['Nom']) 
    return jrs


joueursPosteClub('Mêlée','Clermont')
```




    ['PARRA Morgan', 'BÉZY Sébastien', 'VIALLARD Kévin', 'JAUNEAU Baptiste']



## Utilisation d'une fonction de tri

Comment classer les joueurs suivant leur taille ?  
La fonction `sorted(liste)` est efficace sur les listes : elle renvoie une nouvelle liste triée dans l'ordre croissant.


```python
mylist = [4,2,8,6]
mynewlist = sorted(mylist)
print(mynewlist)
```

    [2, 4, 6, 8]


Mais comment trier un dictionnaire ? 


```python
test = sorted(joueurs)
```

    Traceback (most recent call last):
      File "<input>", line 1, in <module>
    TypeError: '<' not supported between instances of 'dict' and 'dict'


Il est normal que cette tentative échoue : un dictionnaire possède plusieurs clés différentes.
Ici, plusieurs clés peuvent être des critères de tri : la taille, le poids.

### Un exemple de tri de dictionnaire


```python
global Simpsons

Simpsons = [{"Prenom" : "Bart", "age estimé": "10"},
           {"Prenom" : "Lisa", "age estimé": "8"},
           {"Prenom" : "Maggie", "age estimé": "1"},
           {"Prenom" : "Homer", "age estimé": "38"},
           {"Prenom" : "Marge", "age estimé": "37"}]
```


```python
#Fonction pour le tri du dictionnaire

def age(personnage):
    return int(personnage["age estimé"])
```


```python
age(Simpsons[0])
```




    10



On va créer une nouvelle fonction `ageP(nom)` permettant de renvoyer l'age du personnage directement.

```python
def ageP(nom):
    for n in Simpsons:
        if n['Prenom']==nom:
            return age(n)

ageP('Bart')
```



```python
def ageP(nom):
    for n in Simpsons:
        if n['Prenom']==nom:
            return age(n)

ageP('Homer')

```




    38



La création de cette fonction `age()` va nous permettre de spécifier une clé de tri, par le paramètre `key` :


```python
triSimpsons = sorted(Simpsons, key = age)
```


```python
triSimpsons
```




    [{'Prenom': 'Maggie', 'age estimé': '1'}, {'Prenom': 'Lisa', 'age estimé': '8'}, {'Prenom': 'Bart', 'age estimé': '10'}, {'Prenom': 'Marge', 'age estimé': '37'}, {'Prenom': 'Homer', 'age estimé': '38'}]




```python
triSimpsons = sorted(Simpsons, key = age, reverse = True)
```


```python
triSimpsons
```




    [{'Prenom': 'Homer', 'age estimé': '38'}, {'Prenom': 'Marge', 'age estimé': '37'}, {'Prenom': 'Bart', 'age estimé': '10'}, {'Prenom': 'Lisa', 'age estimé': '8'}, {'Prenom': 'Maggie', 'age estimé': '1'}]



**Question 15.**
Trier les joueurs du top14 par taille.  
Adapter ensuite pour afficher que certains renseignements.


```python
def taillePlayer(player) :
    return int(player['Taille'])
```


```python
joueurs_taille_croissant = sorted(joueurs, key = taillePlayer)
print(joueurs_taille_croissant)
```


```python
for nom in  joueurs_taille_croissant:
    print(nom['Nom'],nom['Taille'])
```

**Question 16.**
Trier les joueurs de Clermont par taille.



```python
for nom in  joueurs_taille_croissant:
    if nom['Club']=='Clermont':
        print(nom['Nom'],nom['Taille'])
```

**Question 17.**  
Trier les joueurs de Clermont suivant leur Indice de Masse Corporelle ([IMC](https://fr.wikipedia.org/wiki/Indice_de_masse_corporelle) )


```python
def IMC(player):
    """
    The function IMC(player) takes a player dictionary as input and returns the player's IMC
    
    :param player: a dictionary containing the stats of a given player
    :return: The IMC of the player
    """
    masse = int(player['Poids'])
    taille_m = int(player['Taille']) / 100
    return masse / taille_m**2
    
joueursASM = [k for k in joueurs if k['Club'] == 'Clermont']
joueursASM 

def IMCJoueur(player):
    n1=numero(player)
    j=joueurs[n1]
    imc=IMC(j)
    return imc

joueursASM_tri = sorted(joueurs, key = IMC)
joueursASM_tri
```

**Question 18.**  
En s'inspirant de l'exemple, écrire une fonction permettant d'avoir l'IMC d'un joueur à l'aide de sons nom et prénom


```python
def IMCJoueur(player):
    n1=numero(player)
    j=joueurs[n1]
    imc=IMC(j)
    return imc
IMCJoueur('PARRA Morgan')
```




    25.61728395061728



 ## Recherche des joueurs de profil  physique similaire

### Distance entre deux joueurs
Construire une fonction `distance(joueur1,joueur2)` qui renvoie la somme des carrés des différences de tailles et de poids entre les joueurs `joueur1` et `joueur2` : 
$$ d = (p_1-p_2)^2 + (t_1-t_2)^2$$


```python
def distance(joueur1,joueur2):
    p1 = int(joueur1['Poids'])
    p2 = int(joueur2['Poids'])
    t1 = int(joueur1['Taille'])
    t2 = int(joueur2['Taille'])
    return (p1-p2)**2+(t1-t2)**2

```

Ecrire une fonction permettant de claculer la distance entre deux joueurs


```python
def distanceJ(joueur1,joueur2):
    n1=numero(joueur1)
    n2=numero(joueur2)
    d=distance(joueurs[n1],joueurs[n2])
    return d
distanceJ('PARRA Morgan','SERIN Baptiste')
```




    16



### Distance des joueurs avec Baptiste Serin



```python
def distanceSerin(joueur2):
    p1 = int(joueurs[89]['Poids'])
    p2 = int(joueur2['Poids'])
    t1=int(joueurs[89]['Taille'])
    t2 = int(joueur2['Taille'])
    return (p1-p2)**2+(t1-t2)**2
  


```


```python
joueurs_VS_Serin = sorted(joueurs, key = distanceSerin)
```


```python
joueurs_VS_Serin
```


```python
for j in joueurs_VS_Serin:
    print(j['Nom'],distanceSerin(j))
```

**Question 19.**  
Ecrire une fonction qui renvoie un dictionnaire de la forme `dico={'France':nb de joueurs, ...}`


```python
def paysJoueurs():
    dico={}
    for jrs in joueurs:
        if jrs['Nationalité'] not in dico:
            dico[jrs['Nationalité']]=1
        else:
            dico[jrs['Nationalité']]+=1
    return dico

paysJoueurs()
            
```




    {'France': 379, 'Italie': 4, 'Argentine': 24, 'Samoa': 15, 'Fidji': 37, 'Géorgie': 27, 'Afrique du sud': 30, 'Angleterre': 11, 'Nouvelle-Zélande': 26, 'Australie': 24, 'Irlande': 8, 'Ecosse': 2, 'Tonga': 10, 'Cameroun': 1, 'Canada': 3, 'Moldavie': 3, 'Namibie': 1, 'Portugal': 1, 'Japon': 1, 'Etats-Unis': 4, 'Colombie': 1, 'Îles Cook': 1, 'Allemagne': 1, 'Uruguay': 1, 'Espagne': 2, 'Zimbabwe': 1}




```python

```
