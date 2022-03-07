<table  style="table-layout: fixed;background-color:#87A96B; border:solid;color:black;width:100%;">
        <tr>
            <th colspan=2; style="background-color: #3B444B;color:white;text-align:center;border:none;font-size:12pt;">
           Thème : Traitement des données
            </th>
        </tr>
</table>
<table  style="table-layout: fixed;background-color:#87A96B; border:solid;color:black;width:100%;">
        <tr >
            <th width="25%"; style="background-color: #3B444B;color:white;text-align:center;border:none;font-size:50pt;">
            20
            </th>
            <th  width="75%"; style="text-align:center;background-color:#99BADD;border:none;font-size:25pt;">Manipulation de fichiers CSV avec une bibliothèque</th>
        </tr>
</table>


# Utilisation du module Pandas
Le module `csv` utilisé précédemment se contente de lire les données structurées. Il ne fait aucun effort particulier pour analyser les données. Nous nous en sommes aperçus lorsqu'il a fallu convertir par `int()` toutes les valeurs numériques, qui étaient interprétées comme des chaînes de caractères.  
La bibliothèque `pandas` est par contre spécialement conçue pour l'analyse des données (*data analysis*) : elle est donc naturellement bien plus performante.

On allons utiliser une base de données sur les joueurs NBA.


```python
import pandas as pd #import du module pandas, abrégé classiquement par "pd"
```


```python
df = pd.read_csv('data/players.csv', encoding = 'utf-8')
```

La variable est nommée classiquement `df` pour *dataframe* (que l'on peut traduire par *table de données*)

## Premiers renseignements sur les fichiers de données  

Que contient la variable `df`?


```python
df
```

Les données sont présentées dans l'ordre originel du fichier.  
Il est possible d'avoir uniquement les premières lignes du fichier avec la commande `head()` et les dernières du fichier avec la commande `tail()`. Ces commandes peuvent recevoir en paramètre un nombre entier.


```python
df.head()
```


```python
df.tail()
```


```python
df.head(3)
```


```python
df.tail(5)
```

Pour avoir des renseignements globaux sur la structure de notre fichier, on peut utiliser la commande `df.info()`


```python
df.info()
```

## Extraction de colonnes, création de graphiques 

Pour accéder à une fiche particulière de joueur avec sa position, on peut utiliser la fonction `loc()` :


```python
df.loc[45]
```

Pour accéder à un joueur avec son nom : 


```python
df.loc[df['Name']=='Jaylen Brown']
```

Pour accéder à des données avec une contrainte (Joueurs touchant plus de 40 millions de dollars par an):


```python
df.loc[df['Salary']>=40000000]
```

Pour faire afficher une colonne de données :


```python
df.loc[:,"Salary"]
```


```python
df.loc[:10,"Salary"]  # les 10 premiers dans la liste
```

On peut calculer la moyenne des salaires : 


```python
df["Salary"].mean()
```

le maximum


```python
df["Salary"].max()
```

Le minimum


```python
df["Salary"].min()
```

On peut également faire afficher le salaire max et le nom du joueur correspondant :


```python
result = df[df["Salary"].max() == df["Salary"]]["Name"].iloc[0]
print(result)
```

**Question 1.**  
Faites de même pour faire apparaitre le nom du joueur ayant le salaire minimum.


```python

```

**Question 2.**  
Faire apparaitre le poste de Kemba Walker


```python
result = df[df["Name"] == "Kemba Walker"]["Position"].iloc[0]
print(result)
```

**Question 3.**  
Faire apparaitre le plus grand joueur


```python
result = df[df["Height"].max() == df["Height"]]["Name"].iloc[0]
print(result)
```

**Question 4.**  
Faire apparaitre le plus petit joueur


```python
result = df[df["Height"].min() == df["Height"]]["Name"].iloc[0]
print(result)
```


```python
df.loc[df['Name']=='Jared Harper']
```

**Question 5.**  
Donner le nom du meilleur marqueur ainsi que sa moyenne de points


```python
pointsmax=df["Points"].max()
result = df[df["Points"].max() == df["Points"]]["Name"].iloc[0]
print(result,pointsmax)
```


```python
result = df[df["Points"].max() == df["Points"]][["Name","Points"]].iloc[0]
print(result)
```

## Création de graphique


```python
%matplotlib inline
import matplotlib.pyplot as plt
X = df['Weight']
Y = df['Height_i']

plt.plot(X,Y,'ro') # r pour red, o pour un cercle. voir https://matplotlib.org/api/markers_api.html
plt.show()
```

L'interprétation numérique permet à `pandas` d'analyser automatiquement les données, avec notamment la fonction `describe()`.


```python
df['Height_i'].describe()
```


```python
df.boxplot('Height_i')
```

Donner les joueurs des Brooklyn Nets


```python
test=df[['Name','Points']][df['Team']=='Brooklyn Nets']
print(test)
```


```python
df[['Name','Team']]
```

## Rajout d'une colonne
Afin de pouvoir trier les joueurs suivant de nouveaux critères, nous allons rajouter un champ pour chaque joueur.
Prenons un exemple stupide : fabriquons un nouveau champ `'Taille en cm'` qui contiendra la taille des joueurs aprés conversion en cm. 
Ceci se fera simplement par :


```python
df['Taille'] = round(df['Height_i'] * 0.3048,2)
```


```python
df
```

Faite de même pour convertir le poid en kg.


```python
df['Poids'] = round(df['Weight'] * 0.45359 ,0)
```


```python
df
```

Faire afficher la répartition des tailles (Voir plus haut)


```python
df['Taille'].describe()
```


```python
df.boxplot('Taille')
```

Trier les joueurs par ordre décroissant de poids


```python
p=df.sort_values(by=['Poids'], ascending = False)
p
```

Faire de même pour la taille, les scoreurs et rebondeurs


```python
scoreur=df.sort_values(by=['Points'], ascending = False)
scoreur
```

1. Créer une colonne contenant l'IMC de chaque joueur
2. Créer une nouvelle dataframe contenant tous les joueurs du top14 classés par ordre d'IMC croissant.


```python

```

Créer une dataframe contenant les joueurs en provenance de Duke


```python
dfduke=df[df['College']=='Duke']
```


```python
dfduke
```


```python

```
