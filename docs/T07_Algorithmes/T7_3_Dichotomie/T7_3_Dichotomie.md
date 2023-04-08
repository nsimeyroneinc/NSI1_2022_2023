{% set num = 16%}
{% set titre = "Dichotomie"%}
{% set theme = "algorithmique" %}
{% set niveau = "premiere"%} 

## Activité 

{{ titre_activite("Recherche dichotomique",[]) }}


1. Copier et exécuter le programme du jeu du nombre mystère.  
```python
import random

NB_MIN=1
NB_MAX=100

print(f"Choisir un nombre entre {NB_MIN} et {NB_MAX}, je vais tenter de le deviner en vous posant des questions")
debut = NB_MIN
fin = NB_MAX
while fin-debut>0:
    milieu = (fin+debut)//2
    reponse = input(f"Le nombre est-il strictement plus grand que {milieu} ?")
    if reponse=='O':
        debut=milieu+1
    else:
        fin=milieu
print(f"Le nombre était : {debut}")
```
    1. Faire quelques parties, expliquer la stratégie de l'ordinateur pour trouver le nombre mystère.
    2. Lorsque le nombre est compris entre 1 et 100, en combien d'essais au maximum l'ordinateur trouve-t-il la solution ?
    3. Et si le nombre mystère est compris entre 1 et 200 ?
2. En s'inspirant de cette stratégie de recherche appelée **dichotomie** (*couper en deux*), on cherche un algorithme pour déterminer si un élément se trouve ou non dans une liste. Par exemple, si on recherche $\color{red}{28}$ dans $[14, 15, 17, 22, 23, 25, 29, 34, 38]$, le tableau ci-dessous représente les étapes de la méthode :

    |Etape | Liste | Milieu|Comparaison |
    |------|-------|--------------|------------|
    |:one:|$\underbrace{[\overset{\textcolor{red}{_\wedge^{0}}}{14}, 15, 17, 22,}_{ } \underset{_4^\uparrow}{\textcolor{darkblue}{23}} , \overbrace{25, 29, 34, \underset{\textcolor{red}{_8^{\vee}}}{38}]}_{ }$| $(0+8)//2 = 4$ |$\textcolor{darkblue}{23} <\textcolor{red}{28}$ |
    |:two:|$[\colorbox{lightgray}{14, 15, 17, 22,23} , \underbrace{\overset{\textcolor{red}{_\wedge^{5}}}{25}} \underset{_6^\uparrow}{\textcolor{darkblue}{29}}, \overbrace{34, \underset{\textcolor{red}{_8^{\vee}}}{38}]}_{ }$ | $(5+8)//2=6$|$\textcolor{darkblue}{29} \geq \textcolor{red}{28}$.|
    |:three:|$[\colorbox{lightgray}{14, 15, 17, 22,23} , \underset{_5^\uparrow}{\overset{\textcolor{red}{_\wedge^{5}}}{25}}, \underset{\textcolor{red}{_6^{\vee}}}{29} \colorbox{lightgray}{34,38}]$ | $(5+6)//2=5$ |$\textcolor{darkblue}{25} < \textcolor{red}{28}$.|
    |:four:|$[\colorbox{lightgray}{14, 15, 17, 22,23,25} \underset{\textcolor{red}{_6^{\vee}}}{\overset{\textcolor{red}{_\wedge^6}}{29}} \colorbox{lightgray}{34,38}]$ | - | - |

    Arrêt de l'algorithme, $28$ n'est pas dans la liste.

    1. Dès l'étape 2, on a grisé les éléments situés avant 23 pour indiquer que 28 ne s'y trouve pas. Quelle propriété de la liste le permet ?
    2. Que représente les nombres situés en rouge au-dessus (ou au-dessous) des éléments de la liste ?
    3. Quelle est la condition d'arrêt de cet algorithme ?
    4. Si la liste contenait 100 éléments, en combien d'étapes cet algorithme se terminerait-il ? Justifier.
    
3. Recopier et compléter le fonctionnement de cet algorithme pour chercher si $\textcolor{red}{4}$ est dans la liste $[1, 4, 7, 12, 13, 14]$ :

    |Etape | Liste | Milieu|Comparaison |
    |------|-------|--------------|------------|
    |1|$\underbrace{[\overset{\textcolor{red}{_\wedge^{...}}}{1}, 4,}_{ } \underset{_2^\uparrow}{\textcolor{darkblue}{7}} , \overbrace{12, 13, \underset{\textcolor{red}{_{...}^{\vee}}}{14}]}_{ }$| $(...+...)//2 = ...$ |$\textcolor{darkblue}{...} \geq \textcolor{red}{4}$ |
    |2|  ...  |  ...     |    ...          |   ...         |
    |3|  ...  |  ...     |    ...          |   ...         |
    |4|  ...  |  ...     |    ...          |   ...         |

4. Recopier et compléter la fonction Python suivante qui implémente l'algorithme de recherche par dichotomie.

```python linenums="1"
def recherche_dichotomie(element,liste):
    debut = ...
    fin = ...
    while ....:
        milieu = ...
        if element>liste[milieu]:
            debut=.....
        else:
            fin=.....
    if element==.....:
        return True
    else:
        return False
```

!!! aide "Aide"
    * Les variables `debut` (ligne 2) et `fin` (ligne 3) contiennent les indices de la liste entre lesquels on recherche.
    * La condition d'arrêt (ligne 4) est que l'écart entre ces deux indices est égale à 0.
    * Si `element>liste[milieu]` (condition ligne 6), alors on peut restreindre la recherche à droite de milieu (exclu).
    * Sinon on restreint la recherche à gauche de milieu (inclus)