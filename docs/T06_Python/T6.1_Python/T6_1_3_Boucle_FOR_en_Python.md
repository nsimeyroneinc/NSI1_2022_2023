
{% set num = 3 %}
{% set titre = "Les boucles FOR en Python"%}
{% set theme = "python" %}
{% set niveau = "premiere"%} 


{{ titre_chapitre(num,titre,theme,niveau)}}

![python_logo1.png](data/python_logo1.png){:.center}

##  Les énumérables ou itérables


En mathématiques, on dit qu'un ensemble est *dénombrable* lorsqu'on peut associer à chaque élément de l'ensemble un nombre (traditionnellement 1, 2, 3 ...)

- les voitures qui roulent sur l'autoroute sont dénombrables.
- l'eau qui coule d'un robinet n'est pas dénombrable.

En informatique, il existe un concept similaire qui va désigner les objets que l'on peut **énumérer**, c'est-à-dire les décomposer en une succession ordonnée d'éléments. On les appelle les **énumérables** ou les **itérables** (Python utilise le mot anglais ```iterable```).

- la variable ```NSI``` (qui est de type ```String```) est énumérable : on peut la décomposer en  ```N```,  ```S```, ```I```.
- la variable ```[4, 3, 17]```  (qui est de type ```List```) est énumérable : on peut la décomposer en  ```4```,  ```3```, ```17```.
- la variable ```5```  (qui est de type ```Int```) n'est PAS énumérable : on ne peut pas la décomposer. 



###  Itérer sur les itérables : la boucle `for`

#### &#x2712; Itérer sur une chaîne de caractères

Il existe donc une instruction permettant de faire une (ou plusieurs) action(s) à chaque itération sur un élément énumérable.

**Exemple :**  
Le programme suivant :
```python linenums='1'
for k in 'NSI':
    print(k)
```
va donner ceci :
```python
N
S
I
```

**Analyse grâce à PythonTutor**
Étudions, grâce à PythonTutor, le détail de cette exécution.

Cliquez sur Next et observez bien l'évolution de la variable ```k```. 




```
from tutor import tutor
for k in 'NSI':
    print(k)
tutor()
```

    N
    S
    I



<iframe id="basthon-pythontutor-iframe-0" style="width: 100%; height: 400px;" frameborder="0" src="data:text/html;charset=utf-8,%3C%21DOCTYPE%20html%3E%0A%3Chtml%3E%0A%20%20%3Chead%3E%0A%20%20%20%20%3Clink%20rel%3D%22stylesheet%22%20href%3D%22https%3A//capytale2.ac-paris.fr/basthon/notebook/assets/0.41.11/modules/extern/pytutor-main.min.css%22/%3E%0A%20%20%20%20%3Cscript%20src%3D%22https%3A//capytale2.ac-paris.fr/basthon/notebook/assets/0.41.11/modules/extern/pytutor-main.min.js%22%3E%3C/script%3E%0A%20%20%20%20%3Cscript%3E%0A%20%20%20%20%20%20let%20sent_height%3B%0A%20%20%20%20%20%20%24%28document%29.ready%28function%28%29%20%7B%0A%20%20%20%20%20%20%20%20%20%20//%20managing%20iframe%20resize%0A%20%20%20%20%20%20%20%20%20%20const%20send%20%3D%20%28%29%20%3D%3E%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20const%20new_height%20%3D%20document.body.offsetHeight%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20if%20%28sent_height%20%3D%3D%3D%20new_height%29%20return%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20sent_height%20%3D%20new_height%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20window.parent.postMessage%28%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20type%3A%20%22pytutor-iframe-resize%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20target%3A%20%22basthon-pythontutor-iframe-0%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20height%3A%20sent_height%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7D%2C%20%27%2A%27%29%3B%0A%20%20%20%20%20%20%20%20%20%20%7D%3B%0A%20%20%20%20%20%20%20%20%20%20const%20o%20%3D%20new%20ResizeObserver%28send%29%3B%0A%20%20%20%20%20%20%20%20%20%20o.observe%28document.body%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20const%20t%20%3D%20%7B%22code%22%3A%20%22for%20k%20in%20%27NSI%27%3A%5Cn%20%20%20%20print%28k%29%22%2C%20%22trace%22%3A%20%5B%7B%22line%22%3A%201%2C%20%22event%22%3A%20%22step_line%22%2C%20%22func_name%22%3A%20%22%3Cmodule%3E%22%2C%20%22globals%22%3A%20%7B%7D%2C%20%22ordered_globals%22%3A%20%5B%5D%2C%20%22stack_to_render%22%3A%20%5B%5D%2C%20%22heap%22%3A%20%7B%7D%2C%20%22stdout%22%3A%20%22%22%7D%2C%20%7B%22line%22%3A%202%2C%20%22event%22%3A%20%22step_line%22%2C%20%22func_name%22%3A%20%22%3Cmodule%3E%22%2C%20%22globals%22%3A%20%7B%22k%22%3A%20%22N%22%7D%2C%20%22ordered_globals%22%3A%20%5B%22k%22%5D%2C%20%22stack_to_render%22%3A%20%5B%5D%2C%20%22heap%22%3A%20%7B%7D%2C%20%22stdout%22%3A%20%22%22%7D%2C%20%7B%22line%22%3A%201%2C%20%22event%22%3A%20%22step_line%22%2C%20%22func_name%22%3A%20%22%3Cmodule%3E%22%2C%20%22globals%22%3A%20%7B%22k%22%3A%20%22N%22%7D%2C%20%22ordered_globals%22%3A%20%5B%22k%22%5D%2C%20%22stack_to_render%22%3A%20%5B%5D%2C%20%22heap%22%3A%20%7B%7D%2C%20%22stdout%22%3A%20%22N%5Cn%22%7D%2C%20%7B%22line%22%3A%202%2C%20%22event%22%3A%20%22step_line%22%2C%20%22func_name%22%3A%20%22%3Cmodule%3E%22%2C%20%22globals%22%3A%20%7B%22k%22%3A%20%22S%22%7D%2C%20%22ordered_globals%22%3A%20%5B%22k%22%5D%2C%20%22stack_to_render%22%3A%20%5B%5D%2C%20%22heap%22%3A%20%7B%7D%2C%20%22stdout%22%3A%20%22N%5Cn%22%7D%2C%20%7B%22line%22%3A%201%2C%20%22event%22%3A%20%22step_line%22%2C%20%22func_name%22%3A%20%22%3Cmodule%3E%22%2C%20%22globals%22%3A%20%7B%22k%22%3A%20%22S%22%7D%2C%20%22ordered_globals%22%3A%20%5B%22k%22%5D%2C%20%22stack_to_render%22%3A%20%5B%5D%2C%20%22heap%22%3A%20%7B%7D%2C%20%22stdout%22%3A%20%22N%5CnS%5Cn%22%7D%2C%20%7B%22line%22%3A%202%2C%20%22event%22%3A%20%22step_line%22%2C%20%22func_name%22%3A%20%22%3Cmodule%3E%22%2C%20%22globals%22%3A%20%7B%22k%22%3A%20%22I%22%7D%2C%20%22ordered_globals%22%3A%20%5B%22k%22%5D%2C%20%22stack_to_render%22%3A%20%5B%5D%2C%20%22heap%22%3A%20%7B%7D%2C%20%22stdout%22%3A%20%22N%5CnS%5Cn%22%7D%2C%20%7B%22line%22%3A%201%2C%20%22event%22%3A%20%22step_line%22%2C%20%22func_name%22%3A%20%22%3Cmodule%3E%22%2C%20%22globals%22%3A%20%7B%22k%22%3A%20%22I%22%7D%2C%20%22ordered_globals%22%3A%20%5B%22k%22%5D%2C%20%22stack_to_render%22%3A%20%5B%5D%2C%20%22heap%22%3A%20%7B%7D%2C%20%22stdout%22%3A%20%22N%5CnS%5CnI%5Cn%22%7D%2C%20%7B%22line%22%3A%201%2C%20%22event%22%3A%20%22return%22%2C%20%22func_name%22%3A%20%22%3Cmodule%3E%22%2C%20%22globals%22%3A%20%7B%22k%22%3A%20%22I%22%7D%2C%20%22ordered_globals%22%3A%20%5B%22k%22%5D%2C%20%22stack_to_render%22%3A%20%5B%5D%2C%20%22heap%22%3A%20%7B%7D%2C%20%22stdout%22%3A%20%22N%5CnS%5CnI%5Cn%22%7D%5D%7D%3B%0A%20%20%20%20%20%20%20%20%20%20function%20redraw%28%29%20%7B%20if%20%28window.v%29%20window.v.redrawConnectors%28%29%3B%20%7D%0A%20%20%20%20%20%20%20%20%20%20window.v%20%3D%20new%20ExecutionVisualizer%28%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%27main%27%2C%20t%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7BembeddedMode%3A%20false%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20heightChangeCallback%3A%20redraw%7D%0A%20%20%20%20%20%20%20%20%20%20%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20//%20message%20of%20type%20%27redraw%27%20from%20parent%20triggers%20a%20full%20redraw%0A%20%20%20%20%20%20%20%20%20%20//%20%28usefull%20when%20iframe%20is%20added%20to%20a%20non%20visible%20parent%29%0A%20%20%20%20%20%20%20%20%20%20window.addEventListener%28%27message%27%2C%20function%20%28event%29%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20const%20data%20%3D%20event.data%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20if%28%20data.type%20%3D%3D%3D%20%27redraw%27%20%29%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20window.v.updateOutput%28%29%3B%0A%20%20%20%20%20%20%20%20%20%20%7D%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%24%28window%29.resize%28redraw%29%3B%0A%20%20%20%20%20%20%20%20%20%20redraw%28%29%3B%0A%20%20%20%20%20%20%7D%29%3B%0A%20%20%20%20%3C/script%3E%0A%20%20%3C/head%3E%0A%20%20%3Cbody%20style%3D%22overflow-y%3A%20hidden%3B%22%3E%0A%20%20%20%20%3Cdiv%20id%3D%22main%22%3E%3C/div%3E%0A%20%20%3C/body%3E%0A%3C/html%3E%0A"></iframe>


La variable ```k``` prend donc **successivement** toutes les lettre de la chaîne de caractère ```"NSI"```. 

Pour chaque valeur de ```k```, la ou les instruction(s) situées **de manière indentée** sous la ligne du ```for``` seront exécutées. 

Ici, il y a simplement un ```print(k)```, donc chaque lettre de ```"NSI"``` s'affiche l'une après l'autre.



!!! exo "Exercice 1 :"
    Que donne le script suivant ?
    ```python
    for m in 'NASA':
        print("bonjour")
    ``` 


Dans cet exercice, la **variable de boucle** ```m``` est **muette** : elle n'apparaît dans les instructions indentées sous le ```for```. 

La variable ```m``` prend successivement les valeurs ```'N```, ```'A'```, ```'S'``` et ```'A'```, mais on ne le voit pas.

!!! savoir "&#x1F4DA;  A retenir :"
    **&#x26A0; Comment éviter les erreurs classiques**  
    Quand vous écrivez une boucle ```for```, veillez bien à :

    - finir la ligne du ```for``` par les deux points ```:```  
    - indenter sous le ```for``` les instructions qui doivent être répétées. 

    ```python
    for ........ :
        instructions à répéter
    ```

#### &#x2712; Itérer sur une liste

**Exemple :**
Le programme suivant :
```python
for jour in ["lundi", "mardi", "mercredi", "jeudi", "vendredi"]:
    print(f"je vais au lycée le {jour}")
```
va donner ceci :
```python
je vais au lycée le lundi
je vais au lycée le mardi
je vais au lycée le mercredi
je vais au lycée le jeudi
je vais au lycée le vendredi
```



```
from tutor import tutor
for jour in ["lundi", "mardi", "mercredi", "jeudi", "vendredi"]:
    print(f"je vais au lycée le {jour}")
tutor()
```

    je vais au lycée le lundi
    je vais au lycée le mardi
    je vais au lycée le mercredi
    je vais au lycée le jeudi
    je vais au lycée le vendredi



<iframe id="basthon-pythontutor-iframe-1" style="width: 100%; height: 400px;" frameborder="0" src="data:text/html;charset=utf-8,%3C%21DOCTYPE%20html%3E%0A%3Chtml%3E%0A%20%20%3Chead%3E%0A%20%20%20%20%3Clink%20rel%3D%22stylesheet%22%20href%3D%22https%3A//capytale2.ac-paris.fr/basthon/notebook/assets/0.41.11/modules/extern/pytutor-main.min.css%22/%3E%0A%20%20%20%20%3Cscript%20src%3D%22https%3A//capytale2.ac-paris.fr/basthon/notebook/assets/0.41.11/modules/extern/pytutor-main.min.js%22%3E%3C/script%3E%0A%20%20%20%20%3Cscript%3E%0A%20%20%20%20%20%20let%20sent_height%3B%0A%20%20%20%20%20%20%24%28document%29.ready%28function%28%29%20%7B%0A%20%20%20%20%20%20%20%20%20%20//%20managing%20iframe%20resize%0A%20%20%20%20%20%20%20%20%20%20const%20send%20%3D%20%28%29%20%3D%3E%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20const%20new_height%20%3D%20document.body.offsetHeight%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20if%20%28sent_height%20%3D%3D%3D%20new_height%29%20return%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20sent_height%20%3D%20new_height%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20window.parent.postMessage%28%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20type%3A%20%22pytutor-iframe-resize%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20target%3A%20%22basthon-pythontutor-iframe-1%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20height%3A%20sent_height%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7D%2C%20%27%2A%27%29%3B%0A%20%20%20%20%20%20%20%20%20%20%7D%3B%0A%20%20%20%20%20%20%20%20%20%20const%20o%20%3D%20new%20ResizeObserver%28send%29%3B%0A%20%20%20%20%20%20%20%20%20%20o.observe%28document.body%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20const%20t%20%3D%20%7B%22code%22%3A%20%22for%20jour%20in%20%5B%5C%22lundi%5C%22%2C%20%5C%22mardi%5C%22%2C%20%5C%22mercredi%5C%22%2C%20%5C%22jeudi%5C%22%2C%20%5C%22vendredi%5C%22%5D%3A%5Cn%20%20%20%20print%28f%5C%22je%20vais%20au%20lyc%5Cu00e9e%20le%20%7Bjour%7D%5C%22%29%22%2C%20%22trace%22%3A%20%5B%7B%22line%22%3A%201%2C%20%22event%22%3A%20%22step_line%22%2C%20%22func_name%22%3A%20%22%3Cmodule%3E%22%2C%20%22globals%22%3A%20%7B%7D%2C%20%22ordered_globals%22%3A%20%5B%5D%2C%20%22stack_to_render%22%3A%20%5B%5D%2C%20%22heap%22%3A%20%7B%7D%2C%20%22stdout%22%3A%20%22%22%7D%2C%20%7B%22line%22%3A%202%2C%20%22event%22%3A%20%22step_line%22%2C%20%22func_name%22%3A%20%22%3Cmodule%3E%22%2C%20%22globals%22%3A%20%7B%22jour%22%3A%20%22lundi%22%7D%2C%20%22ordered_globals%22%3A%20%5B%22jour%22%5D%2C%20%22stack_to_render%22%3A%20%5B%5D%2C%20%22heap%22%3A%20%7B%7D%2C%20%22stdout%22%3A%20%22%22%7D%2C%20%7B%22line%22%3A%201%2C%20%22event%22%3A%20%22step_line%22%2C%20%22func_name%22%3A%20%22%3Cmodule%3E%22%2C%20%22globals%22%3A%20%7B%22jour%22%3A%20%22lundi%22%7D%2C%20%22ordered_globals%22%3A%20%5B%22jour%22%5D%2C%20%22stack_to_render%22%3A%20%5B%5D%2C%20%22heap%22%3A%20%7B%7D%2C%20%22stdout%22%3A%20%22je%20vais%20au%20lyc%5Cu00e9e%20le%20lundi%5Cn%22%7D%2C%20%7B%22line%22%3A%202%2C%20%22event%22%3A%20%22step_line%22%2C%20%22func_name%22%3A%20%22%3Cmodule%3E%22%2C%20%22globals%22%3A%20%7B%22jour%22%3A%20%22mardi%22%7D%2C%20%22ordered_globals%22%3A%20%5B%22jour%22%5D%2C%20%22stack_to_render%22%3A%20%5B%5D%2C%20%22heap%22%3A%20%7B%7D%2C%20%22stdout%22%3A%20%22je%20vais%20au%20lyc%5Cu00e9e%20le%20lundi%5Cn%22%7D%2C%20%7B%22line%22%3A%201%2C%20%22event%22%3A%20%22step_line%22%2C%20%22func_name%22%3A%20%22%3Cmodule%3E%22%2C%20%22globals%22%3A%20%7B%22jour%22%3A%20%22mardi%22%7D%2C%20%22ordered_globals%22%3A%20%5B%22jour%22%5D%2C%20%22stack_to_render%22%3A%20%5B%5D%2C%20%22heap%22%3A%20%7B%7D%2C%20%22stdout%22%3A%20%22je%20vais%20au%20lyc%5Cu00e9e%20le%20lundi%5Cnje%20vais%20au%20lyc%5Cu00e9e%20le%20mardi%5Cn%22%7D%2C%20%7B%22line%22%3A%202%2C%20%22event%22%3A%20%22step_line%22%2C%20%22func_name%22%3A%20%22%3Cmodule%3E%22%2C%20%22globals%22%3A%20%7B%22jour%22%3A%20%22mercredi%22%7D%2C%20%22ordered_globals%22%3A%20%5B%22jour%22%5D%2C%20%22stack_to_render%22%3A%20%5B%5D%2C%20%22heap%22%3A%20%7B%7D%2C%20%22stdout%22%3A%20%22je%20vais%20au%20lyc%5Cu00e9e%20le%20lundi%5Cnje%20vais%20au%20lyc%5Cu00e9e%20le%20mardi%5Cn%22%7D%2C%20%7B%22line%22%3A%201%2C%20%22event%22%3A%20%22step_line%22%2C%20%22func_name%22%3A%20%22%3Cmodule%3E%22%2C%20%22globals%22%3A%20%7B%22jour%22%3A%20%22mercredi%22%7D%2C%20%22ordered_globals%22%3A%20%5B%22jour%22%5D%2C%20%22stack_to_render%22%3A%20%5B%5D%2C%20%22heap%22%3A%20%7B%7D%2C%20%22stdout%22%3A%20%22je%20vais%20au%20lyc%5Cu00e9e%20le%20lundi%5Cnje%20vais%20au%20lyc%5Cu00e9e%20le%20mardi%5Cnje%20vais%20au%20lyc%5Cu00e9e%20le%20mercredi%5Cn%22%7D%2C%20%7B%22line%22%3A%202%2C%20%22event%22%3A%20%22step_line%22%2C%20%22func_name%22%3A%20%22%3Cmodule%3E%22%2C%20%22globals%22%3A%20%7B%22jour%22%3A%20%22jeudi%22%7D%2C%20%22ordered_globals%22%3A%20%5B%22jour%22%5D%2C%20%22stack_to_render%22%3A%20%5B%5D%2C%20%22heap%22%3A%20%7B%7D%2C%20%22stdout%22%3A%20%22je%20vais%20au%20lyc%5Cu00e9e%20le%20lundi%5Cnje%20vais%20au%20lyc%5Cu00e9e%20le%20mardi%5Cnje%20vais%20au%20lyc%5Cu00e9e%20le%20mercredi%5Cn%22%7D%2C%20%7B%22line%22%3A%201%2C%20%22event%22%3A%20%22step_line%22%2C%20%22func_name%22%3A%20%22%3Cmodule%3E%22%2C%20%22globals%22%3A%20%7B%22jour%22%3A%20%22jeudi%22%7D%2C%20%22ordered_globals%22%3A%20%5B%22jour%22%5D%2C%20%22stack_to_render%22%3A%20%5B%5D%2C%20%22heap%22%3A%20%7B%7D%2C%20%22stdout%22%3A%20%22je%20vais%20au%20lyc%5Cu00e9e%20le%20lundi%5Cnje%20vais%20au%20lyc%5Cu00e9e%20le%20mardi%5Cnje%20vais%20au%20lyc%5Cu00e9e%20le%20mercredi%5Cnje%20vais%20au%20lyc%5Cu00e9e%20le%20jeudi%5Cn%22%7D%2C%20%7B%22line%22%3A%202%2C%20%22event%22%3A%20%22step_line%22%2C%20%22func_name%22%3A%20%22%3Cmodule%3E%22%2C%20%22globals%22%3A%20%7B%22jour%22%3A%20%22vendredi%22%7D%2C%20%22ordered_globals%22%3A%20%5B%22jour%22%5D%2C%20%22stack_to_render%22%3A%20%5B%5D%2C%20%22heap%22%3A%20%7B%7D%2C%20%22stdout%22%3A%20%22je%20vais%20au%20lyc%5Cu00e9e%20le%20lundi%5Cnje%20vais%20au%20lyc%5Cu00e9e%20le%20mardi%5Cnje%20vais%20au%20lyc%5Cu00e9e%20le%20mercredi%5Cnje%20vais%20au%20lyc%5Cu00e9e%20le%20jeudi%5Cn%22%7D%2C%20%7B%22line%22%3A%201%2C%20%22event%22%3A%20%22step_line%22%2C%20%22func_name%22%3A%20%22%3Cmodule%3E%22%2C%20%22globals%22%3A%20%7B%22jour%22%3A%20%22vendredi%22%7D%2C%20%22ordered_globals%22%3A%20%5B%22jour%22%5D%2C%20%22stack_to_render%22%3A%20%5B%5D%2C%20%22heap%22%3A%20%7B%7D%2C%20%22stdout%22%3A%20%22je%20vais%20au%20lyc%5Cu00e9e%20le%20lundi%5Cnje%20vais%20au%20lyc%5Cu00e9e%20le%20mardi%5Cnje%20vais%20au%20lyc%5Cu00e9e%20le%20mercredi%5Cnje%20vais%20au%20lyc%5Cu00e9e%20le%20jeudi%5Cnje%20vais%20au%20lyc%5Cu00e9e%20le%20vendredi%5Cn%22%7D%2C%20%7B%22line%22%3A%201%2C%20%22event%22%3A%20%22return%22%2C%20%22func_name%22%3A%20%22%3Cmodule%3E%22%2C%20%22globals%22%3A%20%7B%22jour%22%3A%20%22vendredi%22%7D%2C%20%22ordered_globals%22%3A%20%5B%22jour%22%5D%2C%20%22stack_to_render%22%3A%20%5B%5D%2C%20%22heap%22%3A%20%7B%7D%2C%20%22stdout%22%3A%20%22je%20vais%20au%20lyc%5Cu00e9e%20le%20lundi%5Cnje%20vais%20au%20lyc%5Cu00e9e%20le%20mardi%5Cnje%20vais%20au%20lyc%5Cu00e9e%20le%20mercredi%5Cnje%20vais%20au%20lyc%5Cu00e9e%20le%20jeudi%5Cnje%20vais%20au%20lyc%5Cu00e9e%20le%20vendredi%5Cn%22%7D%5D%7D%3B%0A%20%20%20%20%20%20%20%20%20%20function%20redraw%28%29%20%7B%20if%20%28window.v%29%20window.v.redrawConnectors%28%29%3B%20%7D%0A%20%20%20%20%20%20%20%20%20%20window.v%20%3D%20new%20ExecutionVisualizer%28%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%27main%27%2C%20t%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7BembeddedMode%3A%20false%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20heightChangeCallback%3A%20redraw%7D%0A%20%20%20%20%20%20%20%20%20%20%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20//%20message%20of%20type%20%27redraw%27%20from%20parent%20triggers%20a%20full%20redraw%0A%20%20%20%20%20%20%20%20%20%20//%20%28usefull%20when%20iframe%20is%20added%20to%20a%20non%20visible%20parent%29%0A%20%20%20%20%20%20%20%20%20%20window.addEventListener%28%27message%27%2C%20function%20%28event%29%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20const%20data%20%3D%20event.data%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20if%28%20data.type%20%3D%3D%3D%20%27redraw%27%20%29%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20window.v.updateOutput%28%29%3B%0A%20%20%20%20%20%20%20%20%20%20%7D%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%24%28window%29.resize%28redraw%29%3B%0A%20%20%20%20%20%20%20%20%20%20redraw%28%29%3B%0A%20%20%20%20%20%20%7D%29%3B%0A%20%20%20%20%3C/script%3E%0A%20%20%3C/head%3E%0A%20%20%3Cbody%20style%3D%22overflow-y%3A%20hidden%3B%22%3E%0A%20%20%20%20%3Cdiv%20id%3D%22main%22%3E%3C/div%3E%0A%20%20%3C/body%3E%0A%3C/html%3E%0A"></iframe>


!!! warning "**&#x26A0; Attention:**"
    Très souvent, l'objet itérable que la boucle va parcourir aura été **au préalable** stocké dans une variable :

**Exemple :**
Le programme précédent est équivalent à :
```python
semaine = ["lundi", "mardi", "mercredi", "jeudi", "vendredi"]
for jour in semaine:
    print("je vais au lycée le", jour)
```

Notez l'importance d'avoir choisi des noms de variables explicites : ils aident grandement à la lisibilité du code.



*Trailer : Dans le cours spécifique sur les listes, nous verrons une toute autre manière de parcourir une liste.*


```
semaine = ["lundi", "mardi", "mercredi", "jeudi", "vendredi"]
for jour in semaine:
    print("je vais au lycée le", jour)
```

    je vais au lycée le lundi
    je vais au lycée le mardi
    je vais au lycée le mercredi
    je vais au lycée le jeudi
    je vais au lycée le vendredi


###  &#x2712; Comment répéter ```n``` fois la même action ?

Comment répéter 10 fois la phrase ```"Hasta la vista, baby"``` ?

!!! note "&#x1F4CC; Note : range"

Le programme suivant :
```python
for i in range(5):
    print("Hasta la vista, baby")
```

va donner ceci :  

```python
Hasta la vista, baby
Hasta la vista, baby
Hasta la vista, baby
Hasta la vista, baby
Hasta la vista, baby
```

Là encore, le ```i``` est une variable muette.


```
for i in range(5):
    print("Hasta la vista, baby")
```

    Hasta la vista, baby
    Hasta la vista, baby
    Hasta la vista, baby
    Hasta la vista, baby
    Hasta la vista, baby


#### Utilisation minimale de l'objet ```range()```  


**Syntaxe minimale de ```range()```  :**
Le programme suivant :
```python
for k in range(4):
    print(k)
```
va donner ceci :
```python
0
1
2
3
```

!!! savoir "&#x1F4DA;  A retenir :"
    Faire parcourir à une variable ```k``` l'ensemble **```range(n)```** va faire prendre à ```k``` les valeurs 0, 1, 2, ..., n-1. 


#### Utilisation avancée de l'objet ```range()```  

**Syntaxe complète de ```range()```  :**
Le programme suivant :
```python
for k in range(5, 15, 2):
    print(k)
```
va donner ceci :
```python
5
7
9
11
13
```    

!!! savoir "&#x1F4DA;  A retenir :"
    faire parcourir à ```k``` l'ensemble `range(start, stop, step)` fait :

    - démarrer ```k``` à la valeur ```start```   
    - progresser ```k```  de ```step``` en ```step```   
    - tant que ```k``` est **rictement inférieur** ```stop```   


**Remarques** :

- si le ```step``` est omis, il vaut 1 par défaut.
- l'objet ```range(5)``` n'est pas «techniquement» égal à la liste ```[0, 1, 2, 3, 4]```, car ce n'est pas un objet de type ```List```:



!!! exo "&#x1F4BB;   Exercice 1 :"
    Faire afficher les séries de nombres suivantes.
        
    On utilisera la syntaxe ```print(k, end = ' ')``` ) pour afficher les nombres horizontalement.

    A. ```0 1 2 3 4 5```   
    B. ```10 11 12 13 14 15 ```  
    C. ```3 6 9 12 ```  
    D. ```10 9 8 7 6 5 4 3 2 1 0  ``` 



### &#x2712; Une situation classique : la double boucle

Il est très souvent utile d'imbriquer une boucle dans une autre, notamment lors du parcours de tous les pixels d'une image. Prenons pour l'instant un exemple numérique.

!!! exo "&#x1F4BB;  Exercice 2 :"
    Ecrire un script permettant d'afficher

    ```python
    1 * 1 = 1
    1 * 2 = 2
    1 * 3 = 3
    2 * 1 = 2
    2 * 2 = 4
    2 * 3 = 6
    3 * 1 = 3
    3 * 2 = 6
    3 * 3 = 9
    4 * 1 = 4
    4 * 2 = 8
    4 * 3 = 12
    ```


!!! savoir "&#x1F4DA; A retenir :"  
    - La boucle `for` s'utilise lorsque :  
        - on veut parcourir un à un les éléments d'un objet itérable (une chaîne de caractère, une liste...)  
        - on veut répéter une action un nombre de fois **connu à l'avance**. On parle de boucle **bornée**.  
    - Les instructions répétées peuvent - mais ce n'est pas obligatoire - faire appel à la variable de boucle, mais il ne faut pas que ces instructions la modifient.  
    - Ne pas oublier les `:` et l'indentation !  
    - `range(n)` génère une séquence de `n` nombres entiers: on s'en servira dès qu'on aura besoin de répéter `n` fois des instructions.

## Exercices 

!!! exo "&#x1F4BB;  Exercice 3 :"
    Dans l'extrait de code suivant:

    - `chaine` est une variable initialisée avec un `str` vide : `""`;  
    - on veut qu'en sortie de programme cette variable contienne la valeur `'bravo'`.  

    L'idée est d'ajouter une par une les lettres à la variable `chaine`.

    Compléter le code.

    ```python
    chaine = ""
    for ... in ['b', 'r', 'a', 'v', 'o']:
        ...
    ```

Cette variable `chaine` est appelée un **accumulateur**.



!!! exo "&#x1F4BB; Exercice 4 :"
    En Python, la fonction `ord` renvoie le code Unicode d'un caractère et la fonction `chr` le contraire: elle renvoie le caractère correspondant à un code Unicode.

    Par exemple:
    ```python 
    >>> ord('a')
    97
    >>> chr(97)
    'a'
    ```

    Voici une liste contenant les codes Unicode des lettres d'un mot secret...  
    À vous d'écrire un programme où en sortie, la variable `mot_secret` contiendra la chaîne de caractères de ce mot.   


    ```python
    mystere = [111, 107, 44, 32, 98, 105, 101, 110, 32, 106, 111, 117, 233]
    mot_secret = ""
    ```


    ok, bien joué


!!! exo "&#x1F4BB; Exercice 5 :"
    On souhaite calculer la somme des 1000 premiers nombres entiers naturels, c'est-à-dire:

    $1+2+3+4+5+ \dots +999+1000$

    Écrire un programme avec une variable `somme` **accumulateur** (comme à l'exercice 3) qui contiendra la valeur souhaitée en fin de programme.




!!! exo "&#x1F4BB; Exercice 6 :"
    Ecrire un programme permettant de calculer 

    $1\times 2 \times 3 \times \dots 99 \times 100$.

!!! exo "&#x1F4BB; Exercice 7 :"
    Proposer un code qui écrit la **table de multiplication** de 7, de 8 et de 9.

