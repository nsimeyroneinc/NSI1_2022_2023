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



Le module `csv` utilisé précédemment se contente de lire les données structurées. Il ne fait aucun effort particulier pour analyser les données. Nous nous en sommes aperçus lorsqu'il a fallu convertir par `int()` toutes les valeurs numériques, qui étaient interprétées comme des chaînes de caractères.  
La bibliothèque `pandas` est par contre spécialement conçue pour l'analyse des données (*data analysis*) : elle est donc naturellement bien plus performante.

Nous allons utiliser une base de données sur les joueurs NBA.


```python
import pandas as pd #import du module pandas, abrégé classiquement par "pd"
```


```python
df = pd.read_csv('data/players.csv', encoding = 'utf-8')
```

La variable est nommée classiquement `df` pour *dataframe* (que l'on peut traduire par *table de données*)

# Premiers renseignements sur les fichiers de données  

Que contient la variable `df`?


```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Position</th>
      <th>Team</th>
      <th>Age</th>
      <th>Height</th>
      <th>Height_i</th>
      <th>Weight</th>
      <th>College</th>
      <th>Salary</th>
      <th>Points</th>
      <th>Rebounds</th>
      <th>Assists</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Juhann Begarin</td>
      <td>SG</td>
      <td>Boston Celtics</td>
      <td>19</td>
      <td>6' 5"</td>
      <td>6.50</td>
      <td>185</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Jaylen Brown</td>
      <td>SG</td>
      <td>Boston Celtics</td>
      <td>24</td>
      <td>6' 6"</td>
      <td>6.60</td>
      <td>223</td>
      <td>California</td>
      <td>26758928.0</td>
      <td>24.7</td>
      <td>6.0</td>
      <td>3.4</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Kris Dunn</td>
      <td>PG</td>
      <td>Boston Celtics</td>
      <td>27</td>
      <td>6' 3"</td>
      <td>6.30</td>
      <td>205</td>
      <td>Providence</td>
      <td>5005350.0</td>
      <td>1.3</td>
      <td>1.5</td>
      <td>0.5</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Carsen Edwards</td>
      <td>PG</td>
      <td>Boston Celtics</td>
      <td>23</td>
      <td>5' 11"</td>
      <td>5.11</td>
      <td>200</td>
      <td>Purdue</td>
      <td>1782621.0</td>
      <td>4.0</td>
      <td>0.8</td>
      <td>0.5</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Tacko Fall</td>
      <td>C</td>
      <td>Boston Celtics</td>
      <td>25</td>
      <td>7' 5"</td>
      <td>7.50</td>
      <td>311</td>
      <td>UCF</td>
      <td>NaN</td>
      <td>2.5</td>
      <td>2.7</td>
      <td>0.2</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>553</th>
      <td>Juwan Morgan</td>
      <td>SF</td>
      <td>Utah Jazz</td>
      <td>24</td>
      <td>6' 7"</td>
      <td>6.70</td>
      <td>232</td>
      <td>Indiana</td>
      <td>NaN</td>
      <td>1.2</td>
      <td>1.0</td>
      <td>0.3</td>
    </tr>
    <tr>
      <th>554</th>
      <td>Royce O'Neale</td>
      <td>PF</td>
      <td>Utah Jazz</td>
      <td>28</td>
      <td>6' 4"</td>
      <td>6.40</td>
      <td>226</td>
      <td>Baylor</td>
      <td>8800000.0</td>
      <td>7.0</td>
      <td>6.8</td>
      <td>2.5</td>
    </tr>
    <tr>
      <th>555</th>
      <td>Olumiye Oni</td>
      <td>SG</td>
      <td>Utah Jazz</td>
      <td>24</td>
      <td>6' 5"</td>
      <td>6.50</td>
      <td>206</td>
      <td>Yale</td>
      <td>1782621.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>556</th>
      <td>Eric Paschall</td>
      <td>F</td>
      <td>Utah Jazz</td>
      <td>24</td>
      <td>6' 6"</td>
      <td>6.60</td>
      <td>255</td>
      <td>Villanova</td>
      <td>1782621.0</td>
      <td>9.5</td>
      <td>3.2</td>
      <td>1.3</td>
    </tr>
    <tr>
      <th>557</th>
      <td>Hassan Whiteside</td>
      <td>C</td>
      <td>Utah Jazz</td>
      <td>32</td>
      <td>7' 0"</td>
      <td>7.00</td>
      <td>265</td>
      <td>Marshall</td>
      <td>1669178.0</td>
      <td>8.1</td>
      <td>6.0</td>
      <td>0.6</td>
    </tr>
  </tbody>
</table>
<p>558 rows × 12 columns</p>
</div>



Les données sont présentées dans l'ordre originel du fichier.  
&#x27A1; Il est possible d'avoir uniquement les premières lignes du fichier avec la commande `head()` et les dernières du fichier avec la commande `tail()`. Ces commandes peuvent recevoir en paramètre un nombre entier.


```python
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Position</th>
      <th>Team</th>
      <th>Age</th>
      <th>Height</th>
      <th>Height_i</th>
      <th>Weight</th>
      <th>College</th>
      <th>Salary</th>
      <th>Points</th>
      <th>Rebounds</th>
      <th>Assists</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Juhann Begarin</td>
      <td>SG</td>
      <td>Boston Celtics</td>
      <td>19</td>
      <td>6' 5"</td>
      <td>6.50</td>
      <td>185</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Jaylen Brown</td>
      <td>SG</td>
      <td>Boston Celtics</td>
      <td>24</td>
      <td>6' 6"</td>
      <td>6.60</td>
      <td>223</td>
      <td>California</td>
      <td>26758928.0</td>
      <td>24.7</td>
      <td>6.0</td>
      <td>3.4</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Kris Dunn</td>
      <td>PG</td>
      <td>Boston Celtics</td>
      <td>27</td>
      <td>6' 3"</td>
      <td>6.30</td>
      <td>205</td>
      <td>Providence</td>
      <td>5005350.0</td>
      <td>1.3</td>
      <td>1.5</td>
      <td>0.5</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Carsen Edwards</td>
      <td>PG</td>
      <td>Boston Celtics</td>
      <td>23</td>
      <td>5' 11"</td>
      <td>5.11</td>
      <td>200</td>
      <td>Purdue</td>
      <td>1782621.0</td>
      <td>4.0</td>
      <td>0.8</td>
      <td>0.5</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Tacko Fall</td>
      <td>C</td>
      <td>Boston Celtics</td>
      <td>25</td>
      <td>7' 5"</td>
      <td>7.50</td>
      <td>311</td>
      <td>UCF</td>
      <td>NaN</td>
      <td>2.5</td>
      <td>2.7</td>
      <td>0.2</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.tail()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Position</th>
      <th>Team</th>
      <th>Age</th>
      <th>Height</th>
      <th>Height_i</th>
      <th>Weight</th>
      <th>College</th>
      <th>Salary</th>
      <th>Points</th>
      <th>Rebounds</th>
      <th>Assists</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>553</th>
      <td>Juwan Morgan</td>
      <td>SF</td>
      <td>Utah Jazz</td>
      <td>24</td>
      <td>6' 7"</td>
      <td>6.7</td>
      <td>232</td>
      <td>Indiana</td>
      <td>NaN</td>
      <td>1.2</td>
      <td>1.0</td>
      <td>0.3</td>
    </tr>
    <tr>
      <th>554</th>
      <td>Royce O'Neale</td>
      <td>PF</td>
      <td>Utah Jazz</td>
      <td>28</td>
      <td>6' 4"</td>
      <td>6.4</td>
      <td>226</td>
      <td>Baylor</td>
      <td>8800000.0</td>
      <td>7.0</td>
      <td>6.8</td>
      <td>2.5</td>
    </tr>
    <tr>
      <th>555</th>
      <td>Olumiye Oni</td>
      <td>SG</td>
      <td>Utah Jazz</td>
      <td>24</td>
      <td>6' 5"</td>
      <td>6.5</td>
      <td>206</td>
      <td>Yale</td>
      <td>1782621.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>556</th>
      <td>Eric Paschall</td>
      <td>F</td>
      <td>Utah Jazz</td>
      <td>24</td>
      <td>6' 6"</td>
      <td>6.6</td>
      <td>255</td>
      <td>Villanova</td>
      <td>1782621.0</td>
      <td>9.5</td>
      <td>3.2</td>
      <td>1.3</td>
    </tr>
    <tr>
      <th>557</th>
      <td>Hassan Whiteside</td>
      <td>C</td>
      <td>Utah Jazz</td>
      <td>32</td>
      <td>7' 0"</td>
      <td>7.0</td>
      <td>265</td>
      <td>Marshall</td>
      <td>1669178.0</td>
      <td>8.1</td>
      <td>6.0</td>
      <td>0.6</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.head(3)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Position</th>
      <th>Team</th>
      <th>Age</th>
      <th>Height</th>
      <th>Height_i</th>
      <th>Weight</th>
      <th>College</th>
      <th>Salary</th>
      <th>Points</th>
      <th>Rebounds</th>
      <th>Assists</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Juhann Begarin</td>
      <td>SG</td>
      <td>Boston Celtics</td>
      <td>19</td>
      <td>6' 5"</td>
      <td>6.5</td>
      <td>185</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Jaylen Brown</td>
      <td>SG</td>
      <td>Boston Celtics</td>
      <td>24</td>
      <td>6' 6"</td>
      <td>6.6</td>
      <td>223</td>
      <td>California</td>
      <td>26758928.0</td>
      <td>24.7</td>
      <td>6.0</td>
      <td>3.4</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Kris Dunn</td>
      <td>PG</td>
      <td>Boston Celtics</td>
      <td>27</td>
      <td>6' 3"</td>
      <td>6.3</td>
      <td>205</td>
      <td>Providence</td>
      <td>5005350.0</td>
      <td>1.3</td>
      <td>1.5</td>
      <td>0.5</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.tail(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Position</th>
      <th>Team</th>
      <th>Age</th>
      <th>Height</th>
      <th>Height_i</th>
      <th>Weight</th>
      <th>College</th>
      <th>Salary</th>
      <th>Points</th>
      <th>Rebounds</th>
      <th>Assists</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>553</th>
      <td>Juwan Morgan</td>
      <td>SF</td>
      <td>Utah Jazz</td>
      <td>24</td>
      <td>6' 7"</td>
      <td>6.7</td>
      <td>232</td>
      <td>Indiana</td>
      <td>NaN</td>
      <td>1.2</td>
      <td>1.0</td>
      <td>0.3</td>
    </tr>
    <tr>
      <th>554</th>
      <td>Royce O'Neale</td>
      <td>PF</td>
      <td>Utah Jazz</td>
      <td>28</td>
      <td>6' 4"</td>
      <td>6.4</td>
      <td>226</td>
      <td>Baylor</td>
      <td>8800000.0</td>
      <td>7.0</td>
      <td>6.8</td>
      <td>2.5</td>
    </tr>
    <tr>
      <th>555</th>
      <td>Olumiye Oni</td>
      <td>SG</td>
      <td>Utah Jazz</td>
      <td>24</td>
      <td>6' 5"</td>
      <td>6.5</td>
      <td>206</td>
      <td>Yale</td>
      <td>1782621.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>556</th>
      <td>Eric Paschall</td>
      <td>F</td>
      <td>Utah Jazz</td>
      <td>24</td>
      <td>6' 6"</td>
      <td>6.6</td>
      <td>255</td>
      <td>Villanova</td>
      <td>1782621.0</td>
      <td>9.5</td>
      <td>3.2</td>
      <td>1.3</td>
    </tr>
    <tr>
      <th>557</th>
      <td>Hassan Whiteside</td>
      <td>C</td>
      <td>Utah Jazz</td>
      <td>32</td>
      <td>7' 0"</td>
      <td>7.0</td>
      <td>265</td>
      <td>Marshall</td>
      <td>1669178.0</td>
      <td>8.1</td>
      <td>6.0</td>
      <td>0.6</td>
    </tr>
  </tbody>
</table>
</div>



&#x27A1; Pour avoir des renseignements globaux sur la structure de notre fichier, on peut utiliser la commande `df.info()`


```python
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 558 entries, 0 to 557
    Data columns (total 12 columns):
     #   Column    Non-Null Count  Dtype  
    ---  ------    --------------  -----  
     0   Name      558 non-null    object 
     1   Position  558 non-null    object 
     2   Team      558 non-null    object 
     3   Age       558 non-null    int64  
     4   Height    558 non-null    object 
     5   Height_i  558 non-null    float64
     6   Weight    558 non-null    int64  
     7   College   485 non-null    object 
     8   Salary    445 non-null    float64
     9   Points    476 non-null    float64
     10  Rebounds  476 non-null    float64
     11  Assists   476 non-null    float64
    dtypes: float64(5), int64(2), object(5)
    memory usage: 52.4+ KB


# Extraction de colonnes

## Pour accéder aux information d'une colonne

### Filter les lignes en appliquant une condition aux colonnes à l'aide de  `.loc` 

&#x27A1; Pour faire afficher une colonne de données :


```python
df.loc[:,"Salary"]
```




    0             NaN
    1      26758928.0
    2       5005350.0
    3       1782621.0
    4             NaN
              ...    
    553           NaN
    554     8800000.0
    555     1782621.0
    556     1782621.0
    557     1669178.0
    Name: Salary, Length: 558, dtype: float64



&#x27A1;  On peut rajouter une contrainte avec, par exemple; uniquement les 10 premiers de la liste


```python
df.loc[:10,"Salary"]  # les 10 premiers dans la liste
```




    0            NaN
    1     26758928.0
    2      5005350.0
    3      1782621.0
    4            NaN
    5      1782621.0
    6     27000000.0
    7      1669178.0
    8            NaN
    9      3804360.0
    10     3631200.0
    Name: Salary, dtype: float64




```python
df.loc[]  # les 10 premiers dans la liste
```

**&#x1F58B; A vous**  
Faite apparaitre la colonne correspondant au âge des joueurs, puis faite apparaitre les 15 premiers de la liste.


```python
df.loc[:15,"Salary"]  
```




    0            NaN
    1     26758928.0
    2      5005350.0
    3      1782621.0
    4            NaN
    5      1782621.0
    6     27000000.0
    7      1669178.0
    8            NaN
    9      3804360.0
    10     3631200.0
    11     2283034.0
    12     2137440.0
    13    11615328.0
    14     5890000.0
    15    14339285.0
    Name: Salary, dtype: float64



&#x27A1; Pour accéder à une fiche particulière de joueur avec sa position, on peut utiliser la fonction `loc()` :


```python
test=df.loc[45]
print(test)
test1=df.loc[45,['Name','Position']]
print(test1)
```

    Name             RJ Barrett
    Position                 SG
    Team        New York Knicks
    Age                      21
    Height                6' 6"
    Height_i                6.6
    Weight                  214
    College                Duke
    Salary            8623920.0
    Points                 17.6
    Rebounds                5.8
    Assists                 3.0
    Name: 45, dtype: object
    Name        RJ Barrett
    Position            SG
    Name: 45, dtype: object


### Extraire des informations selon des critères  `loc()`

Cette méthode nécessite de savoir la position du joueur voulu, pour accéder à un joueur avec son nom : 


```python
df.loc[df['Name']=='Kevin Durant']   # ou df.loc[df.Name=='Kevin Durant']
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Position</th>
      <th>Team</th>
      <th>Age</th>
      <th>Height</th>
      <th>Height_i</th>
      <th>Weight</th>
      <th>College</th>
      <th>Salary</th>
      <th>Points</th>
      <th>Rebounds</th>
      <th>Assists</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>25</th>
      <td>Kevin Durant</td>
      <td>PF</td>
      <td>Brooklyn Nets</td>
      <td>32</td>
      <td>6' 10"</td>
      <td>6.1</td>
      <td>240</td>
      <td>Texas</td>
      <td>42018900.0</td>
      <td>26.9</td>
      <td>7.1</td>
      <td>5.6</td>
    </tr>
  </tbody>
</table>
</div>



&#x27A1; Pour accéder à des données avec une contrainte (Joueurs touchant plus de 40 millions de dollars par an):


```python
df.loc[df.Salary>=40000000]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Position</th>
      <th>Team</th>
      <th>Age</th>
      <th>Height</th>
      <th>Height_i</th>
      <th>Weight</th>
      <th>College</th>
      <th>Salary</th>
      <th>Points</th>
      <th>Rebounds</th>
      <th>Assists</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>25</th>
      <td>Kevin Durant</td>
      <td>PF</td>
      <td>Brooklyn Nets</td>
      <td>32</td>
      <td>6' 10"</td>
      <td>6.1</td>
      <td>240</td>
      <td>Texas</td>
      <td>42018900.0</td>
      <td>26.9</td>
      <td>7.1</td>
      <td>5.6</td>
    </tr>
    <tr>
      <th>29</th>
      <td>James Harden</td>
      <td>SG</td>
      <td>Brooklyn Nets</td>
      <td>32</td>
      <td>6' 5"</td>
      <td>6.5</td>
      <td>220</td>
      <td>Arizona State</td>
      <td>44310840.0</td>
      <td>24.6</td>
      <td>7.9</td>
      <td>10.8</td>
    </tr>
    <tr>
      <th>287</th>
      <td>Stephen Curry</td>
      <td>PG</td>
      <td>Golden State Warriors</td>
      <td>33</td>
      <td>6' 3"</td>
      <td>6.3</td>
      <td>185</td>
      <td>Davidson</td>
      <td>45780966.0</td>
      <td>32.0</td>
      <td>5.5</td>
      <td>5.8</td>
    </tr>
    <tr>
      <th>331</th>
      <td>LeBron James</td>
      <td>SF</td>
      <td>Los Angeles Lakers</td>
      <td>36</td>
      <td>6' 9"</td>
      <td>6.9</td>
      <td>250</td>
      <td>NaN</td>
      <td>41180544.0</td>
      <td>25.0</td>
      <td>7.7</td>
      <td>7.8</td>
    </tr>
    <tr>
      <th>336</th>
      <td>Russell Westbrook</td>
      <td>PG</td>
      <td>Los Angeles Lakers</td>
      <td>32</td>
      <td>6' 3"</td>
      <td>6.3</td>
      <td>200</td>
      <td>UCLA</td>
      <td>44211146.0</td>
      <td>22.2</td>
      <td>11.5</td>
      <td>11.7</td>
    </tr>
    <tr>
      <th>408</th>
      <td>John Wall</td>
      <td>PG</td>
      <td>Houston Rockets</td>
      <td>31</td>
      <td>6' 3"</td>
      <td>6.3</td>
      <td>210</td>
      <td>Kentucky</td>
      <td>44310840.0</td>
      <td>20.6</td>
      <td>3.2</td>
      <td>6.9</td>
    </tr>
  </tbody>
</table>
</div>



**&#x1F58B; A vous**  
Donner les joueurs marquant plus de 25 points par match.


```python
df.loc[df.Points>=27]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Position</th>
      <th>Team</th>
      <th>Age</th>
      <th>Height</th>
      <th>Height_i</th>
      <th>Weight</th>
      <th>College</th>
      <th>Salary</th>
      <th>Points</th>
      <th>Rebounds</th>
      <th>Assists</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>69</th>
      <td>Joel Embiid</td>
      <td>C</td>
      <td>Philadelphia Sixers</td>
      <td>27</td>
      <td>7' 0"</td>
      <td>7.00</td>
      <td>280</td>
      <td>Kansas</td>
      <td>31579390.0</td>
      <td>28.5</td>
      <td>10.6</td>
      <td>2.8</td>
    </tr>
    <tr>
      <th>113</th>
      <td>Zach LaVine</td>
      <td>SG</td>
      <td>Chicago Bulls</td>
      <td>26</td>
      <td>6' 5"</td>
      <td>6.50</td>
      <td>200</td>
      <td>UCLA</td>
      <td>19500000.0</td>
      <td>27.4</td>
      <td>5.0</td>
      <td>4.9</td>
    </tr>
    <tr>
      <th>171</th>
      <td>Giannis Antetokounmpo</td>
      <td>PF</td>
      <td>Milwaukee Bucks</td>
      <td>26</td>
      <td>6' 11"</td>
      <td>6.11</td>
      <td>242</td>
      <td>NaN</td>
      <td>39344970.0</td>
      <td>28.1</td>
      <td>11.0</td>
      <td>5.9</td>
    </tr>
    <tr>
      <th>267</th>
      <td>Bradley Beal</td>
      <td>SG</td>
      <td>Washington Wizards</td>
      <td>28</td>
      <td>6' 3"</td>
      <td>6.30</td>
      <td>207</td>
      <td>Florida</td>
      <td>33724200.0</td>
      <td>31.3</td>
      <td>4.7</td>
      <td>4.4</td>
    </tr>
    <tr>
      <th>287</th>
      <td>Stephen Curry</td>
      <td>PG</td>
      <td>Golden State Warriors</td>
      <td>33</td>
      <td>6' 3"</td>
      <td>6.30</td>
      <td>185</td>
      <td>Davidson</td>
      <td>45780966.0</td>
      <td>32.0</td>
      <td>5.5</td>
      <td>5.8</td>
    </tr>
    <tr>
      <th>378</th>
      <td>Luka Doncic</td>
      <td>PG</td>
      <td>Dallas Mavericks</td>
      <td>22</td>
      <td>6' 7"</td>
      <td>6.70</td>
      <td>230</td>
      <td>NaN</td>
      <td>10174391.0</td>
      <td>27.7</td>
      <td>8.0</td>
      <td>8.6</td>
    </tr>
    <tr>
      <th>449</th>
      <td>Zion Williamson</td>
      <td>PF</td>
      <td>New Orleans Pelicans</td>
      <td>21</td>
      <td>6' 7"</td>
      <td>6.70</td>
      <td>284</td>
      <td>Duke</td>
      <td>10733400.0</td>
      <td>27.0</td>
      <td>7.2</td>
      <td>3.7</td>
    </tr>
    <tr>
      <th>529</th>
      <td>Damian Lillard</td>
      <td>PG</td>
      <td>Portland Trail Blazers</td>
      <td>31</td>
      <td>6' 2"</td>
      <td>6.20</td>
      <td>195</td>
      <td>Weber State</td>
      <td>39344900.0</td>
      <td>28.8</td>
      <td>4.2</td>
      <td>7.5</td>
    </tr>
  </tbody>
</table>
</div>



**&#x1F58B; A vous**  
Donner les joueurs provenant du collège du Kentuchy.


```python
df.loc[df.College=='Kentucky']
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Position</th>
      <th>Team</th>
      <th>Age</th>
      <th>Height</th>
      <th>Height_i</th>
      <th>Weight</th>
      <th>College</th>
      <th>Salary</th>
      <th>Points</th>
      <th>Rebounds</th>
      <th>Assists</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>7</th>
      <td>Enes Kanter</td>
      <td>C</td>
      <td>Boston Celtics</td>
      <td>29</td>
      <td>6' 10"</td>
      <td>6.10</td>
      <td>250</td>
      <td>Kentucky</td>
      <td>1669178.0</td>
      <td>11.2</td>
      <td>11.0</td>
      <td>1.2</td>
    </tr>
    <tr>
      <th>51</th>
      <td>Kevin Knox II</td>
      <td>SF</td>
      <td>New York Knicks</td>
      <td>22</td>
      <td>6' 7"</td>
      <td>6.70</td>
      <td>215</td>
      <td>Kentucky</td>
      <td>5845979.0</td>
      <td>3.9</td>
      <td>1.5</td>
      <td>0.5</td>
    </tr>
    <tr>
      <th>53</th>
      <td>Nerlens Noel</td>
      <td>C</td>
      <td>New York Knicks</td>
      <td>27</td>
      <td>6' 11"</td>
      <td>6.11</td>
      <td>220</td>
      <td>Kentucky</td>
      <td>8000000.0</td>
      <td>5.1</td>
      <td>6.4</td>
      <td>0.7</td>
    </tr>
    <tr>
      <th>57</th>
      <td>Immanuel Quickley</td>
      <td>SG</td>
      <td>New York Knicks</td>
      <td>22</td>
      <td>6' 3"</td>
      <td>6.30</td>
      <td>190</td>
      <td>Kentucky</td>
      <td>2210640.0</td>
      <td>11.4</td>
      <td>2.1</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>58</th>
      <td>Julius Randle</td>
      <td>PF</td>
      <td>New York Knicks</td>
      <td>26</td>
      <td>6' 8"</td>
      <td>6.80</td>
      <td>250</td>
      <td>Kentucky</td>
      <td>21780000.0</td>
      <td>24.1</td>
      <td>10.2</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>75</th>
      <td>Tyrese Maxey</td>
      <td>PG</td>
      <td>Philadelphia Sixers</td>
      <td>20</td>
      <td>6' 2"</td>
      <td>6.20</td>
      <td>200</td>
      <td>Kentucky</td>
      <td>2602920.0</td>
      <td>8.0</td>
      <td>1.7</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>136</th>
      <td>Hamidou Diallo</td>
      <td>SG</td>
      <td>Detroit Pistons</td>
      <td>23</td>
      <td>6' 5"</td>
      <td>6.50</td>
      <td>202</td>
      <td>Kentucky</td>
      <td>5200000.0</td>
      <td>11.6</td>
      <td>5.2</td>
      <td>1.9</td>
    </tr>
    <tr>
      <th>146</th>
      <td>Trey Lyles</td>
      <td>PF</td>
      <td>Detroit Pistons</td>
      <td>25</td>
      <td>6' 9"</td>
      <td>6.90</td>
      <td>234</td>
      <td>Kentucky</td>
      <td>2500000.0</td>
      <td>5.0</td>
      <td>3.7</td>
      <td>0.6</td>
    </tr>
    <tr>
      <th>158</th>
      <td>Isaiah Jackson</td>
      <td>PF</td>
      <td>Indiana Pacers</td>
      <td>19</td>
      <td>6' 10"</td>
      <td>6.10</td>
      <td>205</td>
      <td>Kentucky</td>
      <td>2451240.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>222</th>
      <td>Nick Richards</td>
      <td>C</td>
      <td>Charlotte Hornets</td>
      <td>23</td>
      <td>7' 0"</td>
      <td>7.00</td>
      <td>245</td>
      <td>Kentucky</td>
      <td>1517981.0</td>
      <td>0.8</td>
      <td>0.6</td>
      <td>0.1</td>
    </tr>
    <tr>
      <th>227</th>
      <td>P.J. Washington</td>
      <td>PF</td>
      <td>Charlotte Hornets</td>
      <td>23</td>
      <td>6' 7"</td>
      <td>6.70</td>
      <td>230</td>
      <td>Kentucky</td>
      <td>4215120.0</td>
      <td>12.9</td>
      <td>6.5</td>
      <td>2.5</td>
    </tr>
    <tr>
      <th>228</th>
      <td>Bam Adebayo</td>
      <td>C</td>
      <td>Miami Heat</td>
      <td>24</td>
      <td>6' 9"</td>
      <td>6.90</td>
      <td>255</td>
      <td>Kentucky</td>
      <td>28103500.0</td>
      <td>18.7</td>
      <td>9.0</td>
      <td>5.4</td>
    </tr>
    <tr>
      <th>233</th>
      <td>Tyler Herro</td>
      <td>PG</td>
      <td>Miami Heat</td>
      <td>21</td>
      <td>6' 5"</td>
      <td>6.50</td>
      <td>195</td>
      <td>Kentucky</td>
      <td>4004280.0</td>
      <td>15.1</td>
      <td>5.0</td>
      <td>3.4</td>
    </tr>
    <tr>
      <th>295</th>
      <td>Mychal Mulder</td>
      <td>SG</td>
      <td>Golden State Warriors</td>
      <td>27</td>
      <td>6' 3"</td>
      <td>6.30</td>
      <td>184</td>
      <td>Kentucky</td>
      <td>1782621.0</td>
      <td>5.6</td>
      <td>1.0</td>
      <td>0.4</td>
    </tr>
    <tr>
      <th>304</th>
      <td>Eric Bledsoe</td>
      <td>SG</td>
      <td>Los Angeles Clippers</td>
      <td>31</td>
      <td>6' 1"</td>
      <td>6.10</td>
      <td>214</td>
      <td>Kentucky</td>
      <td>18125000.0</td>
      <td>12.2</td>
      <td>3.4</td>
      <td>3.8</td>
    </tr>
    <tr>
      <th>306</th>
      <td>DeMarcus Cousins</td>
      <td>C</td>
      <td>Los Angeles Clippers</td>
      <td>31</td>
      <td>6' 10"</td>
      <td>6.10</td>
      <td>270</td>
      <td>Kentucky</td>
      <td>NaN</td>
      <td>8.9</td>
      <td>6.4</td>
      <td>1.9</td>
    </tr>
    <tr>
      <th>316</th>
      <td>Patrick Patterson</td>
      <td>PF</td>
      <td>Los Angeles Clippers</td>
      <td>32</td>
      <td>6' 8"</td>
      <td>6.80</td>
      <td>235</td>
      <td>Kentucky</td>
      <td>NaN</td>
      <td>5.2</td>
      <td>2.0</td>
      <td>0.8</td>
    </tr>
    <tr>
      <th>326</th>
      <td>Anthony Davis</td>
      <td>PF</td>
      <td>Los Angeles Lakers</td>
      <td>28</td>
      <td>6' 10"</td>
      <td>6.10</td>
      <td>253</td>
      <td>Kentucky</td>
      <td>35361360.0</td>
      <td>21.8</td>
      <td>7.9</td>
      <td>3.1</td>
    </tr>
    <tr>
      <th>333</th>
      <td>Malik Monk</td>
      <td>SG</td>
      <td>Los Angeles Lakers</td>
      <td>23</td>
      <td>6' 3"</td>
      <td>6.30</td>
      <td>200</td>
      <td>Kentucky</td>
      <td>1669178.0</td>
      <td>11.7</td>
      <td>2.4</td>
      <td>2.1</td>
    </tr>
    <tr>
      <th>335</th>
      <td>Rajon Rondo</td>
      <td>PG</td>
      <td>Los Angeles Lakers</td>
      <td>35</td>
      <td>6' 1"</td>
      <td>6.10</td>
      <td>180</td>
      <td>Kentucky</td>
      <td>1669178.0</td>
      <td>5.4</td>
      <td>2.4</td>
      <td>4.4</td>
    </tr>
    <tr>
      <th>338</th>
      <td>Devin Booker</td>
      <td>SG</td>
      <td>Phoenix Suns</td>
      <td>24</td>
      <td>6' 5"</td>
      <td>6.50</td>
      <td>206</td>
      <td>Kentucky</td>
      <td>31650600.0</td>
      <td>25.6</td>
      <td>4.2</td>
      <td>4.3</td>
    </tr>
    <tr>
      <th>357</th>
      <td>De'Aaron Fox</td>
      <td>PG</td>
      <td>Sacremento Kings</td>
      <td>23</td>
      <td>6' 3"</td>
      <td>6.30</td>
      <td>185</td>
      <td>Kentucky</td>
      <td>28103550.0</td>
      <td>25.2</td>
      <td>3.5</td>
      <td>7.2</td>
    </tr>
    <tr>
      <th>377</th>
      <td>Willie Cauley-Stein</td>
      <td>C</td>
      <td>Dallas Mavericks</td>
      <td>28</td>
      <td>7' 0"</td>
      <td>7.00</td>
      <td>240</td>
      <td>Kentucky</td>
      <td>4100000.0</td>
      <td>5.3</td>
      <td>4.5</td>
      <td>0.7</td>
    </tr>
    <tr>
      <th>408</th>
      <td>John Wall</td>
      <td>PG</td>
      <td>Houston Rockets</td>
      <td>31</td>
      <td>6' 3"</td>
      <td>6.30</td>
      <td>210</td>
      <td>Kentucky</td>
      <td>44310840.0</td>
      <td>20.6</td>
      <td>3.2</td>
      <td>6.9</td>
    </tr>
    <tr>
      <th>434</th>
      <td>Wenyen Gabriel</td>
      <td>PF</td>
      <td>New Orleans Pelicans</td>
      <td>24</td>
      <td>6' 9"</td>
      <td>6.90</td>
      <td>205</td>
      <td>Kentucky</td>
      <td>1762796.0</td>
      <td>3.4</td>
      <td>2.6</td>
      <td>0.5</td>
    </tr>
    <tr>
      <th>456</th>
      <td>Keldon Johnson</td>
      <td>SF</td>
      <td>San Antonio Spurs</td>
      <td>21</td>
      <td>6' 5"</td>
      <td>6.50</td>
      <td>220</td>
      <td>Kentucky</td>
      <td>2145720.0</td>
      <td>12.8</td>
      <td>6.0</td>
      <td>1.8</td>
    </tr>
    <tr>
      <th>482</th>
      <td>Jamal Murray</td>
      <td>PG</td>
      <td>Denver Nuggets</td>
      <td>24</td>
      <td>6' 3"</td>
      <td>6.30</td>
      <td>215</td>
      <td>Kentucky</td>
      <td>29467800.0</td>
      <td>21.2</td>
      <td>4.0</td>
      <td>4.8</td>
    </tr>
    <tr>
      <th>499</th>
      <td>Karl-Anthony Towns</td>
      <td>C</td>
      <td>Minnesota Timberwolves</td>
      <td>25</td>
      <td>6' 11"</td>
      <td>6.11</td>
      <td>248</td>
      <td>Kentucky</td>
      <td>31650600.0</td>
      <td>24.8</td>
      <td>10.6</td>
      <td>4.5</td>
    </tr>
    <tr>
      <th>500</th>
      <td>Jarred Vanderbilt</td>
      <td>PF</td>
      <td>Minnesota Timberwolves</td>
      <td>22</td>
      <td>6' 9"</td>
      <td>6.90</td>
      <td>214</td>
      <td>Kentucky</td>
      <td>NaN</td>
      <td>5.4</td>
      <td>5.8</td>
      <td>1.2</td>
    </tr>
    <tr>
      <th>508</th>
      <td>Shai Gilgeous-Alexander</td>
      <td>SG</td>
      <td>Oklahoma City Thunder</td>
      <td>23</td>
      <td>6' 6"</td>
      <td>6.60</td>
      <td>180</td>
      <td>Kentucky</td>
      <td>5495532.0</td>
      <td>23.7</td>
      <td>4.7</td>
      <td>5.9</td>
    </tr>
  </tbody>
</table>
</div>



### Opération classique : Moyenne, maximum et minimum

&#x27A1; On peut calculer la moyenne des salaires : 


```python
df["Salary"].mean()   # ou df.Salary.mean()
```




    8813695.5752809



&#x27A1; le maximum


```python
df["Salary"].max()
```




    45780966.0



&#x27A1; le minimum


```python
df["Salary"].min()
```




    925258.0



### Filtrer les lignes avec des indices en utilisant `iloc`

&#x27A1; On peut également faire afficher le salaire max et le nom du joueur correspondant :


```python
result = df[df["Salary"].max() == df["Salary"]]["Name"].iloc[0]
print(result)
```

    Stephen Curry


**&#x1F58B; A vous**  
Faites de même pour faire apparaitre le nom du joueur ayant le salaire minimum.


```python

```

**&#x1F58B; A vous**  
Faire apparaitre le poste de Kemba Walker


```python
result = df[df["Name"] == "Kemba Walker"]["Position"].iloc[0]
print(result)
```

**&#x1F58B; A vous**  
Faire apparaitre le plus grand joueur


```python
result = df[df["Height"].max() == df["Height"]]["Name"].iloc[0]
print(result)
```

**&#x1F58B; A vous**  
Faire apparaitre le plus petit joueur


```python
result = df[df["Height"].min() == df["Height"]]["Name"].iloc[0]
print(result)
```


```python
df.loc[df['Name']=='Jared Harper']
```

**&#x1F58B; A vous**  
Faire apparaitre le meilleur rebondeur


```python

```

**&#x1F58B; A vous**   
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

**&#x1F58B; A vous**   
Donner les joueurs des Brooklyn Nets


```python

```

# Création de graphique


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


```python
df[['Name','Team']]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Team</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Juhann Begarin</td>
      <td>Boston Celtics</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Jaylen Brown</td>
      <td>Boston Celtics</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Kris Dunn</td>
      <td>Boston Celtics</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Carsen Edwards</td>
      <td>Boston Celtics</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Tacko Fall</td>
      <td>Boston Celtics</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>553</th>
      <td>Juwan Morgan</td>
      <td>Utah Jazz</td>
    </tr>
    <tr>
      <th>554</th>
      <td>Royce O'Neale</td>
      <td>Utah Jazz</td>
    </tr>
    <tr>
      <th>555</th>
      <td>Olumiye Oni</td>
      <td>Utah Jazz</td>
    </tr>
    <tr>
      <th>556</th>
      <td>Eric Paschall</td>
      <td>Utah Jazz</td>
    </tr>
    <tr>
      <th>557</th>
      <td>Hassan Whiteside</td>
      <td>Utah Jazz</td>
    </tr>
  </tbody>
</table>
<p>558 rows × 2 columns</p>
</div>



# Rajout d'une colonne
Afin de pouvoir trier les joueurs suivant de nouveaux critères, nous allons rajouter un champ pour chaque joueur.   
Prenons un exemple stupide : fabriquons un nouveau champ `'Taille en cm'` qui contiendra la taille des joueurs aprés conversion en cm. 
Ceci se fera simplement par :


```python
df['Taille'] = round(df['Height_i'] * 0.3048,2)
```


```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Position</th>
      <th>Team</th>
      <th>Age</th>
      <th>Height</th>
      <th>Height_i</th>
      <th>Weight</th>
      <th>College</th>
      <th>Salary</th>
      <th>Points</th>
      <th>Rebounds</th>
      <th>Assists</th>
      <th>Taille</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Juhann Begarin</td>
      <td>SG</td>
      <td>Boston Celtics</td>
      <td>19</td>
      <td>6' 5"</td>
      <td>6.50</td>
      <td>185</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.98</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Jaylen Brown</td>
      <td>SG</td>
      <td>Boston Celtics</td>
      <td>24</td>
      <td>6' 6"</td>
      <td>6.60</td>
      <td>223</td>
      <td>California</td>
      <td>26758928.0</td>
      <td>24.7</td>
      <td>6.0</td>
      <td>3.4</td>
      <td>2.01</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Kris Dunn</td>
      <td>PG</td>
      <td>Boston Celtics</td>
      <td>27</td>
      <td>6' 3"</td>
      <td>6.30</td>
      <td>205</td>
      <td>Providence</td>
      <td>5005350.0</td>
      <td>1.3</td>
      <td>1.5</td>
      <td>0.5</td>
      <td>1.92</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Carsen Edwards</td>
      <td>PG</td>
      <td>Boston Celtics</td>
      <td>23</td>
      <td>5' 11"</td>
      <td>5.11</td>
      <td>200</td>
      <td>Purdue</td>
      <td>1782621.0</td>
      <td>4.0</td>
      <td>0.8</td>
      <td>0.5</td>
      <td>1.56</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Tacko Fall</td>
      <td>C</td>
      <td>Boston Celtics</td>
      <td>25</td>
      <td>7' 5"</td>
      <td>7.50</td>
      <td>311</td>
      <td>UCF</td>
      <td>NaN</td>
      <td>2.5</td>
      <td>2.7</td>
      <td>0.2</td>
      <td>2.29</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>553</th>
      <td>Juwan Morgan</td>
      <td>SF</td>
      <td>Utah Jazz</td>
      <td>24</td>
      <td>6' 7"</td>
      <td>6.70</td>
      <td>232</td>
      <td>Indiana</td>
      <td>NaN</td>
      <td>1.2</td>
      <td>1.0</td>
      <td>0.3</td>
      <td>2.04</td>
    </tr>
    <tr>
      <th>554</th>
      <td>Royce O'Neale</td>
      <td>PF</td>
      <td>Utah Jazz</td>
      <td>28</td>
      <td>6' 4"</td>
      <td>6.40</td>
      <td>226</td>
      <td>Baylor</td>
      <td>8800000.0</td>
      <td>7.0</td>
      <td>6.8</td>
      <td>2.5</td>
      <td>1.95</td>
    </tr>
    <tr>
      <th>555</th>
      <td>Olumiye Oni</td>
      <td>SG</td>
      <td>Utah Jazz</td>
      <td>24</td>
      <td>6' 5"</td>
      <td>6.50</td>
      <td>206</td>
      <td>Yale</td>
      <td>1782621.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.98</td>
    </tr>
    <tr>
      <th>556</th>
      <td>Eric Paschall</td>
      <td>F</td>
      <td>Utah Jazz</td>
      <td>24</td>
      <td>6' 6"</td>
      <td>6.60</td>
      <td>255</td>
      <td>Villanova</td>
      <td>1782621.0</td>
      <td>9.5</td>
      <td>3.2</td>
      <td>1.3</td>
      <td>2.01</td>
    </tr>
    <tr>
      <th>557</th>
      <td>Hassan Whiteside</td>
      <td>C</td>
      <td>Utah Jazz</td>
      <td>32</td>
      <td>7' 0"</td>
      <td>7.00</td>
      <td>265</td>
      <td>Marshall</td>
      <td>1669178.0</td>
      <td>8.1</td>
      <td>6.0</td>
      <td>0.6</td>
      <td>2.13</td>
    </tr>
  </tbody>
</table>
<p>558 rows × 13 columns</p>
</div>



**&#x1F58B; A vous**   
Faite de même pour convertir le poid en kg.


```python
df['Poids'] = round(df['Weight'] * 0.45359 ,0)
```


```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Position</th>
      <th>Team</th>
      <th>Age</th>
      <th>Height</th>
      <th>Height_i</th>
      <th>Weight</th>
      <th>College</th>
      <th>Salary</th>
      <th>Points</th>
      <th>Rebounds</th>
      <th>Assists</th>
      <th>Taille</th>
      <th>Poids</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Juhann Begarin</td>
      <td>SG</td>
      <td>Boston Celtics</td>
      <td>19</td>
      <td>6' 5"</td>
      <td>6.50</td>
      <td>185</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.98</td>
      <td>84.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Jaylen Brown</td>
      <td>SG</td>
      <td>Boston Celtics</td>
      <td>24</td>
      <td>6' 6"</td>
      <td>6.60</td>
      <td>223</td>
      <td>California</td>
      <td>26758928.0</td>
      <td>24.7</td>
      <td>6.0</td>
      <td>3.4</td>
      <td>2.01</td>
      <td>101.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Kris Dunn</td>
      <td>PG</td>
      <td>Boston Celtics</td>
      <td>27</td>
      <td>6' 3"</td>
      <td>6.30</td>
      <td>205</td>
      <td>Providence</td>
      <td>5005350.0</td>
      <td>1.3</td>
      <td>1.5</td>
      <td>0.5</td>
      <td>1.92</td>
      <td>93.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Carsen Edwards</td>
      <td>PG</td>
      <td>Boston Celtics</td>
      <td>23</td>
      <td>5' 11"</td>
      <td>5.11</td>
      <td>200</td>
      <td>Purdue</td>
      <td>1782621.0</td>
      <td>4.0</td>
      <td>0.8</td>
      <td>0.5</td>
      <td>1.56</td>
      <td>91.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Tacko Fall</td>
      <td>C</td>
      <td>Boston Celtics</td>
      <td>25</td>
      <td>7' 5"</td>
      <td>7.50</td>
      <td>311</td>
      <td>UCF</td>
      <td>NaN</td>
      <td>2.5</td>
      <td>2.7</td>
      <td>0.2</td>
      <td>2.29</td>
      <td>141.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>553</th>
      <td>Juwan Morgan</td>
      <td>SF</td>
      <td>Utah Jazz</td>
      <td>24</td>
      <td>6' 7"</td>
      <td>6.70</td>
      <td>232</td>
      <td>Indiana</td>
      <td>NaN</td>
      <td>1.2</td>
      <td>1.0</td>
      <td>0.3</td>
      <td>2.04</td>
      <td>105.0</td>
    </tr>
    <tr>
      <th>554</th>
      <td>Royce O'Neale</td>
      <td>PF</td>
      <td>Utah Jazz</td>
      <td>28</td>
      <td>6' 4"</td>
      <td>6.40</td>
      <td>226</td>
      <td>Baylor</td>
      <td>8800000.0</td>
      <td>7.0</td>
      <td>6.8</td>
      <td>2.5</td>
      <td>1.95</td>
      <td>103.0</td>
    </tr>
    <tr>
      <th>555</th>
      <td>Olumiye Oni</td>
      <td>SG</td>
      <td>Utah Jazz</td>
      <td>24</td>
      <td>6' 5"</td>
      <td>6.50</td>
      <td>206</td>
      <td>Yale</td>
      <td>1782621.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.98</td>
      <td>93.0</td>
    </tr>
    <tr>
      <th>556</th>
      <td>Eric Paschall</td>
      <td>F</td>
      <td>Utah Jazz</td>
      <td>24</td>
      <td>6' 6"</td>
      <td>6.60</td>
      <td>255</td>
      <td>Villanova</td>
      <td>1782621.0</td>
      <td>9.5</td>
      <td>3.2</td>
      <td>1.3</td>
      <td>2.01</td>
      <td>116.0</td>
    </tr>
    <tr>
      <th>557</th>
      <td>Hassan Whiteside</td>
      <td>C</td>
      <td>Utah Jazz</td>
      <td>32</td>
      <td>7' 0"</td>
      <td>7.00</td>
      <td>265</td>
      <td>Marshall</td>
      <td>1669178.0</td>
      <td>8.1</td>
      <td>6.0</td>
      <td>0.6</td>
      <td>2.13</td>
      <td>120.0</td>
    </tr>
  </tbody>
</table>
<p>558 rows × 14 columns</p>
</div>



**&#x1F58B; A vous**   
Faire afficher la répartition des tailles (Voir plus haut)


```python
df['Taille'].describe()
```




    count    558.000000
    mean       1.977419
    std        0.101202
    min        1.550000
    25%        1.890000
    50%        1.980000
    75%        2.040000
    max        2.290000
    Name: Taille, dtype: float64




```python
df.boxplot('Taille')
```




    <AxesSubplot:>




    
![png](TP_Pandas_Prof_files/TP_Pandas_Prof_72_1.png)
    


&#x27A1; Trier les joueurs par ordre décroissant de poids


```python
p=df.sort_values(by=['Poids'], ascending = False)
p
```

**&#x1F58B; A vous**  
Faire de même pour la taille, les scoreurs et rebondeurs


```python
scoreur=df.sort_values(by=['Points'], ascending = False)
scoreur
```

**&#x1F58B; A vous**  

1. Créer une colonne contenant l'IMC de chaque joueur
2. Créer une nouvelle dataframe contenant tous les joueurs du top14 classés par ordre d'IMC croissant.


```python

```

**&#x1F58B; A vous**  
Créer une dataframe contenant les joueurs en provenance de Duke


```python
dfduke=df[df['College']=='Duke']
```


```python
dfduke
```


```python

```

**&#x1F58B; A vous**   
Déterminer les joueurs gagnat plus de 15 millions de dollars et marquant moins de 10 points par match (le ET : &)


```python
df.loc[(df.Points<10) & (df.Salary>=15000000)]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Position</th>
      <th>Team</th>
      <th>Age</th>
      <th>Height</th>
      <th>Height_i</th>
      <th>Weight</th>
      <th>College</th>
      <th>Salary</th>
      <th>Points</th>
      <th>Rebounds</th>
      <th>Assists</th>
      <th>Taille</th>
      <th>Poids</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>128</th>
      <td>Ricky Rubio</td>
      <td>G</td>
      <td>Cleveland Cavaliers</td>
      <td>30</td>
      <td>6' 3"</td>
      <td>6.30</td>
      <td>190</td>
      <td>NaN</td>
      <td>17800000.0</td>
      <td>8.6</td>
      <td>3.3</td>
      <td>6.4</td>
      <td>1.92</td>
      <td>86.0</td>
    </tr>
    <tr>
      <th>255</th>
      <td>Gary Harris</td>
      <td>SG</td>
      <td>Orlando Magic</td>
      <td>26</td>
      <td>6' 4"</td>
      <td>6.40</td>
      <td>210</td>
      <td>Michigan State</td>
      <td>20482143.0</td>
      <td>9.9</td>
      <td>2.0</td>
      <td>2.0</td>
      <td>1.95</td>
      <td>95.0</td>
    </tr>
    <tr>
      <th>271</th>
      <td>Spencer Dinwiddie</td>
      <td>PG</td>
      <td>Washington Wizards</td>
      <td>28</td>
      <td>6' 5"</td>
      <td>6.50</td>
      <td>215</td>
      <td>Colorado</td>
      <td>17142857.0</td>
      <td>6.7</td>
      <td>4.3</td>
      <td>3.0</td>
      <td>1.98</td>
      <td>98.0</td>
    </tr>
    <tr>
      <th>288</th>
      <td>Draymond Green</td>
      <td>PF</td>
      <td>Golden State Warriors</td>
      <td>31</td>
      <td>6' 6"</td>
      <td>6.60</td>
      <td>230</td>
      <td>Michigan State</td>
      <td>24026712.0</td>
      <td>7.0</td>
      <td>7.1</td>
      <td>8.9</td>
      <td>2.01</td>
      <td>104.0</td>
    </tr>
    <tr>
      <th>411</th>
      <td>Steven Adams</td>
      <td>C</td>
      <td>Memphis Grizzlies</td>
      <td>28</td>
      <td>6' 11"</td>
      <td>6.11</td>
      <td>265</td>
      <td>Pittsburgh</td>
      <td>17073171.0</td>
      <td>7.6</td>
      <td>8.9</td>
      <td>1.9</td>
      <td>1.86</td>
      <td>120.0</td>
    </tr>
  </tbody>
</table>
</div>



**&#x1F58B; A vous**    
Créer une dictionnaire avec les divers colléges comme clé et le nombre de joueurs comme valeur.


```python
dico={}
for k in df.College:
    if k not in dico:
        if k !="nan":
            dico[k]=1
    else:
        dico[k]+=1
print(dico)
```

    {nan: 73, 'California': 1, 'Providence': 1, 'Purdue': 2, 'UCF': 1, 'Maryland': 6, 'Florida': 7, 'Kentucky': 30, 'Vanderbilt': 5, 'Indiana': 8, 'Duke': 27, 'Oregon': 8, 'Tennessee': 6, 'Oklahoma State': 2, 'Texas A&M': 4, 'Texas': 14, "Saint Joseph's": 4, 'Miami (FL)': 2, 'West Virginia': 2, 'Georgia': 3, 'Pepperdine': 1, 'Florida State': 11, 'Oklahoma': 3, 'Arizona State': 3, 'Virginia': 8, 'Eastern Arizona Coll. (J.C.)': 1, 'Missouri State': 1, 'Wake Forest': 7, 'Fresno State': 2, "Saint Mary's": 2, 'Louisiana Tech': 1, 'Mississippi State': 3, 'North Carolina': 13, 'LSU': 6, 'Creighton': 3, 'Colorado': 3, 'USC': 10, 'Houston': 4, 'Auburn': 5, "St. John's": 3, 'Memphis': 4, 'Dayton': 2, 'Connecticut': 5, 'Western Kentucky': 1, 'Cincinnati': 1, 'Kansas': 12, 'Michigan State': 8, 'Arkansas': 5, 'SMU': 3, 'Iowa State': 5, 'Gonzaga': 9, 'DePaul': 2, 'Charleston': 2, 'Washington': 8, 'Nebraska': 2, 'UNLV': 3, 'New Mexico JC': 1, 'Wisconsin': 2, 'San Diego State': 3, 'Baylor': 5, 'Louisville': 6, 'Arizona': 11, 'New Mexico State': 1, 'Wichita State': 2, 'George Washington': 1, 'Villanova': 9, 'UCLA': 13, 'Illinois': 2, 'Radford': 1, 'Alabama': 5, 'Penn State': 2, 'Truman State': 1, 'Kansas State': 3, 'Belmont': 1, 'Iowa': 2, 'Syracuse': 5, 'Michigan': 11, 'North Carolina State': 2, 'USC Upstate': 1, 'Butler': 3, 'Xavier': 2, 'BYU': 1, 'Notre Dame': 1, 'IUPUI': 1, 'Stanford': 7, 'Seton Hall': 1, 'Florida Gulf Coast': 1, 'Utah': 3, 'Delaware': 1, 'Nevada': 3, 'Pittsburgh': 2, 'Marquette': 5, 'TCU': 3, 'UC Santa Barbara': 3, 'Georgetown': 3, 'Rhode Island': 1, 'Long Beach State': 1, 'South Carolina': 3, 'Liberty': 1, 'David Lipscomb University': 1, 'Davidson': 1, 'Drexel': 1, 'Salt Lake CC UT': 1, 'Washington State': 2, 'Minnesota': 2, 'Boston College': 1, 'Ohio': 1, 'John A. Logan College': 1, 'Old Dominion': 1, 'North Carolina-Wilmington': 1, 'Boise State': 1, 'Murray State': 2, 'Louisiana-Lafayette': 1, 'Ole Miss': 1, 'Bowling Green': 1, 'Wyoming': 2, 'Utah State': 2, 'Texas Tech': 2, 'Vermont': 1, 'Cal Poly': 1, 'Ohio State': 4, 'Loyola (MD)': 1, 'Missouri': 3, 'Virginia Tech': 1, 'Oregon State': 1, 'Cleveland State': 1, 'Western Texas Coll. (J.C.)': 1, 'Georgia Tech': 3, 'Tulsa': 1, 'Virginia Commonwealth': 1, 'William & Mary': 1, 'Moravian': 1, 'Bucknell': 1, 'Montana State': 1, 'Tennessee State': 1, 'Weber State': 1, 'Lehigh': 1, 'New Mexico': 1, 'Yale': 1, 'Marshall': 1}


**&#x1F58B; A vous**   


