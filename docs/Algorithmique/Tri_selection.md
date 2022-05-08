---
title : Tri par insertion
author : M.Meyroneinc-Condy - Lycée Murat Issoire
date : 28/11/2021
---

<table  class="blueTable">
        <tr>
            <th>
            Thème 7 : Algorithmique
            </th>
        </tr>
</table>
<br>
<table  class="blueTable">
        <tr >
            <th width="20%"; style="background-color: #3B444B;color:white;text-align:center;border:none;font-size:40pt;">
            24
            </th>
            <th  width="80%"; style="text-align:center;border:none;font-size:25pt;">Tri par selection</th>
        </tr>
</table>
<br>



## Tri par sélection


### Animation
Considérons la liste `[8,5,2,6,9,3,1,4,8,7]`  
Voici le fonctionnement de l'algorithme :  
![](data/Selection-Sort-Animation.gif){: .center}

!!! lien "Vidéo Tri par sélection"
    [Tri par sélection](http://lwh.free.fr/pages/algo/tri/tri_selection.html)

### Principe

!!! note "description de l'algorithme"
    Le travail se fait essentiellement sur les **indices**.
    
    - du premier élément jusqu'à l'avant-dernier :
        - on considère que cet élément est l'élément minimum, on stocke donc son indice dans une variable *indice du minimum*.
        - on parcourt les éléments suivants, et si on repère un élémént plus petit que notre mininum on met à jour notre *indice du minimum*.
        - une fois le parcours fini, on échange l'élément de travail avec l'élément minimum qui a été trouvé.
 




### Implémentation de l'algorithme

!!! abstract "Tri par sélection :heart: "
    ```python
    def tri_selection(lst) :
        for k in range(len(lst)-1):
            indice_min = k
            for i in range(k+1, len(lst)) :
                if lst[i] < lst[indice_min]:
                    indice_min = i
            lst[k], lst[indice_min] = lst[indice_min], lst[k]
    ```

*Vérification :*

```python
>>> ma_liste = [7, 5, 2, 8, 1, 4]
>>> tri_selection(ma_liste)
>>> ma_liste
[1, 2, 4, 5, 7, 8]
```

    


### Complexité de l'algorithme




#### Calcul du nombre d'opérations
Dénombrons le nombre d'opérations, pour une liste de taille $n$.

- boucle `for` : elle s'exécute $n-1$ fois.
- deuxième boucle `for` imbriquée : elle exécute d'abord 1 opération, puis 2, puis 3... jusqu'à $n-1$. 

Or 
$1+2+3+\dots+n-1=\dfrac{n \times (n-1)}{2}$

Ceci est bien un polynôme du second degré, ce qui confirme que la complexité de ce tri est quadratique.


### Preuve de la terminaison de l'algorithme

**Est-on sûr que notre algorithme va s'arrêter ?**

À l'observation du programme, constitué de deux boucles `for` imbriquées, il n'y a pas d'ambiguïté : on ne peut pas rentrer dans une boucle infinie. Le programme s'arrête forcément au bout de d'un nombre fixe d'opérations. 
D'après nos calculs sur la complexité, ce nombre de tours de boucles est égal à $\dfrac{n \times (n-1)}{2}$.

Ceci prouve que l'algorithme se terminera.


### Pour aller plus loin : Preuve de la correction de l'algorithme

**Est-on sûr que notre algorithme va bien trier notre liste ?**

Les preuves de correction sont des preuves théoriques. La preuve ici s'appuie sur le concept mathématique de **récurrence**. 
Principe du raisonnement par récurrence : 
une propriété $P(n)$ est vraie si :

- $P(0)$ (par exemple) est vraie
- Pour tout entier naturel $n$, si $P(n)$ est vraie alors $P(n+1)$ est vraie.

Ici, la propriété serait : « Quand $k$ varie entre 0 et `longueur(liste) -1`, la sous-liste de longueur $k$ est triée dans l'ordre croissant.» On appelle cette propriété un **invariant de boucle** (sous-entendu : elle est vraie pour chaque boucle)

- quand $k$ vaut 0, on place le minimum de la liste en l[0], la sous-liste l[0] est donc triée.
-  si la sous-liste de $k$ éléments est triée, l'algorithme rajoute en dernière position de la liste le minimum de la sous-liste restante, dont tous les éléments sont supérieurs au maximum de la sous-liste de $k$ éléments. La sous-liste de $k+1$ éléments est donc aussi triée.

