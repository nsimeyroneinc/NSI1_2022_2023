---
marp: true
paginate: true
theme: gaia
size: 16:9
---


# Problème du sac à dos - Exercice

Un cambrioleur ne peut emporter que 40 kg sur son dos dans son sac. Il a le choix d'emporter certains des objets suivants :

---

|         | Poids (masse en kg) | Valeur (prix de revente) |
|---------|:-----:|:------:|
| objet A |   15  |   500  |
| objet B |   24  |   400  |
| objet C |   9   |   350  |
| objet D |   25  |   750  |
| objet E |   5   |   400  |
| objet F |   12  |   800  |
| objet G |   2   |  1400  |
| objet H |   18  |   550  |


---

## Q1
Classer ces objets par valeur décroissante et donner la solution de l'algorithme glouton avec ce critère de classement.

|objet|G|F|D|H|A|B|E|C|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|Valeur |1400|800|750|550|500|400|400|350|
|Poids|2|12|25|18|15|24|5|9|



Avec l'algorithme glouton et cette stratégie : 
- on prend les objets G - F et D soit une valeur de 2950 et un poids de 39 kg.

---

## Q2
Même question avec un classement par poids croissant.

|objet|G|E|C|F|A|H|B|D|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|Valeur |1400|400|350|800|500|550|400|750|
|Poids|2|5|9|12|15|18|24|25|


Avec l'algorithme glouton et cette stratégie : 
- on prend les objets G - E - C et F soit une valeur de 2950 et un poids de 29 kg.
---

## Q3
Même question avec un classement par valeur/poids (valeur massique) croissant.

|objet|G|E|F|C|A|H|D|B|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|Valeur |1400|400|800|350|500|550|750|400|
|Poids|2|5|12|9|15|18|25|24|
|valeur massique|700|80|66.7|38.9|33.3|30.7|30|16.7|

Avec l'algorithme glouton et cette stratégie : 
- on prend les objets G - E - F et C soit une valeur de 2950 et un poids de 29 kg.


Avec l'algorithme glouton et cette stratégie : 
- on prend les objets 3 - 1 - 2 et 7 pour un poids de 5.5 kg et une valeur de 20.

---

!!! question "Q4"  
    A-t-on obtenu la solution optimale ?
