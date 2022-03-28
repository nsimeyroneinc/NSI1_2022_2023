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
            <th  width="75%"; style="text-align:center;background-color:#99BADD;border:none;font-size:25pt;">Manipulation de fichiers CSV avec la bibliothèque Pandas</th>
        </tr>
</table>


|Contenus| Capacités attendues | Commentaires|
|:---|:---|:---|
|Tri d'une table| Trier une table suivant une colonne | Une fonction de tri intégrée au système ou à une bibliothèque peut être  utilisée.| 


Le module `csv` utilisé précédemment se contente de lire les données structurées. Il ne fait aucun effort particulier pour analyser les données. Nous nous en sommes aperçus lorsqu'il a fallu convertir par `int()` toutes les valeurs numériques, qui étaient interprétées comme des chaînes de caractères.  
La bibliothèque `pandas` est par contre spécialement conçue pour l'analyse des données (*data analysis*) : elle est donc naturellement bien plus performante.

Nous allons utiliser une base de données sur les joueurs NBA.


```python
import pandas as pd #import du module pandas, abrégé classiquement par "pd"
```


```python
df = pd.read_csv('players.csv', encoding = 'utf-8')
```

La variable est nommée classiquement `df` pour *dataframe* (que l'on peut traduire par *table de données*)

# Premiers renseignements sur les fichiers de données  

Que contient la variable `df`?


```python
df
```

Les données sont présentées dans l'ordre originel du fichier.  

&#x27A1; Il est possible d'avoir uniquement les premières lignes du fichier avec la commande `head()` et les dernières du fichier avec la commande `tail()`. Ces commandes peuvent recevoir en paramètre un nombre entier.


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

&#x27A1; Pour avoir des renseignements globaux sur la structure de notre fichier, on peut utiliser la commande `df.info()`


```python
df.info()
```

# Extraction de colonnes

## Pour accéder aux information d'une colonne

### Filter les lignes en appliquant une condition aux colonnes à l'aide de  `.loc` 

&#x27A1; Pour faire afficher une colonne de données :


```python
df.loc[:,"Salary"]
```

&#x27A1;  On peut rajouter une contrainte avec, par exemple; uniquement les 10 premiers de la liste


```python
df.loc[:10,"Salary"]  # les 10 premiers dans la liste
```


```python
df.loc[10]  # les 10 premiers dans la liste
```

**&#x1F58B; A vous**  
Faite apparaitre la colonne correspondant au âge des joueurs, puis faite apparaitre les 15 premiers de la liste.


```python

```


```python

```

&#x27A1; Pour accéder à une fiche particulière de joueur avec sa position, on peut utiliser la fonction `loc()` :


```python
test1=df.loc[45,['Name','Position']]
print(test1)
```

### Extraire des informations selon des critères  `loc()`

&#x27A1; Cette méthode nécessite de savoir la position du joueur voulu, pour accéder à un joueur avec son nom : 


```python
df.loc[df['Name']=='Kevin Durant']   # ou df.loc[df.Name=='Kevin Durant']
```

&#x27A1; Pour accéder à des données avec une contrainte (Joueurs touchant plus de 40 millions de dollars par an):


```python
df.loc[df['Salary']>=40000000]   # ou df.loc[df.Salary>=40000000]
```


```python
df.loc[df.Salary>=40000000]
```

**&#x1F58B; A vous**  
Donner les joueurs marquant plus de 25 points par match.


```python

```


```python

```

**&#x1F58B; A vous**  
Donner les joueurs provenant du collège du Kentucky.


```python

```

### Opération classique : Moyenne, maximum et minimum

&#x27A1; On peut calculer la moyenne des salaires : 


```python
df["Salary"].mean()   # ou df.Salary.mean()
```

&#x27A1; le maximum


```python
df["Salary"].max()
```

&#x27A1; le minimum


```python
df["Salary"].min()
```

### Filtrer les lignes avec des indices en utilisant `iloc`

&#x27A1; On peut également faire afficher le salaire max et le nom du joueur correspondant :


```python
result = df[df["Salary"].max() == df["Salary"]]["Name"].iloc[0]  # 0 signifie qu'on affiche le premier joueur correspondant à la condition
print(result)
```

**&#x1F58B; A vous**  
Faire afficher uniquement le nom des joueurs gagnant plus de 40 millions de dollars par saison.


```python

```

**&#x1F58B; A vous**  
Faites de même pour faire apparaitre le nom du joueur ayant le salaire minimum.


```python

```

**&#x1F58B; A vous**  
Faire apparaitre le poste et le club de Kemba Walker


```python

```

**&#x1F58B; A vous**  
Faire apparaitre le plus grand joueur


```python

```

**&#x1F58B; A vous**  
Faire apparaitre le plus petit joueur


```python

```


```python

```

**&#x1F58B; A vous**  
Faire apparaitre le meilleur rebondeur


```python

```

**&#x1F58B; A vous**   
Donner le nom du meilleur marqueur ainsi que sa moyenne de points


```python

```

**&#x1F58B; A vous**   
Donner les joueurs des Brooklyn Nets


```python

```

&#x27A1;  On peut regrouper les informations selon un critère


```python
position_mean = df.groupby(["Position"]).mean()
result = position_mean[["Salary","Age","Points"]]
result = result.round(2)
print(result)
```

**&#x1F58B; A vous**   
Regrouper les joueurs en fonction de leur age : donner Salaires, points, rebond, assist


```python

```

# Création de graphique


```python

import matplotlib.pyplot as plt
plt.close()
X = df['Weight']
Y = df['Height_i']

plt.plot(X,Y,'ro') # r pour red, o pour un cercle. voir https://matplotlib.org/api/markers_api.html
plt.show()
```

# Rajout d'une colonne  

&#x27A1;  Afin de pouvoir trier les joueurs suivant de nouveaux critères, nous allons rajouter un champ pour chaque joueur.   

Prenons un exemple stupide : fabriquons un nouveau champ `'Taille en cm'` qui contiendra la taille des joueurs aprés conversion en cm. 
Ceci se fera simplement par :


```python
conversions = [30.48, 2.54]

df['Taille'] = df['Height_i'].str.split('-').apply(pd.Series).astype(int).dot(conversions)


```


```python
df
```


```python
import matplotlib.pyplot as plt
plt.close()
X = df['Weight']
Y = df['Taille']

plt.plot(X,Y,'ro') # r pour red, o pour un cercle. voir https://matplotlib.org/api/markers_api.html
plt.show()
```

&#x27A1;  L'interprétation numérique permet à `pandas` d'analyser automatiquement les données, avec notamment la fonction `describe()`.


```python
df['Taille'].describe()
```

On peut faire apparaitre le diagramme "boite à moustache" :


```python
plt.close()

b=df.boxplot(column=['Taille'])
b.plot()
plt.show()

```

**&#x1F58B; A vous**   
Déterminer la taille moyenne d'un joueur NBA


```python

```

**&#x1F58B; A vous**   
Déterminer les plus petits joueurs NBA ainsi que leurs moyennes de points


```python

```

**&#x1F58B; A vous**   
Convertir le poid en kg.


```python

```


```python
df
```

**&#x1F58B; A vous**   
Faire afficher la répartition des poids (Voir plus haut)


```python

```

**&#x1F58B; A vous**   
Faire afficher la boite à moustache des poids (Voir plus haut)


```python

```

&#x27A1; Trier les joueurs par ordre décroissant de poids


```python
p=df.sort_values(by=['Poids'], ascending = False)
p
```

**&#x1F58B; A vous**  
Faire de même pour la taille, les scoreurs et rebondeurs


```python

```

**&#x1F58B; A vous**  

1. Créer une colonne contenant l'IMC de chaque joueur
2. Créer une nouvelle dataframe contenant tous les joueurs NBA classés par ordre d'IMC croissant.


```python

```

**&#x1F58B; A vous**  
Créer une dataframe contenant les joueurs en provenance de Duke


```python

```


```python

```


```python

```

**&#x1F58B; A vous**   
Déterminer les joueurs gagnant plus de 15 millions de dollars et marquant moins de 10 points par match (le ET : &)


```python

```

**&#x1F58B; A vous**    
Créer une data.frame avec les divers colléges comme clé et le nombre de joueurs comme valeur.


```python


```


```python

```

**&#x1F58B; A vous**   
Donner le joueur moyenne en NBA (Age, Taille, Salaire, Points, etc)


```python

```

&#x27A1; On peut également ajouter des colonnes : 


```python
df['total_P+A'] = df[['Points','Assists']].sum(axis=1)
df_1 = df.sort_values('total_P+A',ascending=False).dropna().head(20)  #dropna() supprimme toutes les lignes avec des valeurs NULL

df_1 = df_1.drop(columns=["Height","Height_i","Weight","College","Poids"])  # on supprime certaines colonnes.
df_1
```

**&#x1F58B; A vous**   
Faire de même mais en rajoutant les rebonds, classer les 20 premiers joueurs NBA


```python

```


```python

```
