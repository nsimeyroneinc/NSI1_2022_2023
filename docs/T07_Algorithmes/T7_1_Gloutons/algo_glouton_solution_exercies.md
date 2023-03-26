---
marp: true
paginate: true
theme: gaia
---


# Problème du sac à dos - Exercice


Dans un jeu vidéo, le héros dispose d'un sac à dos lui permettant de porter les objets collectés au fil du jeu, avec une capacité maximale de 10 kg.  
Le héros souhaite maximiser la valeur en pièces d'or des objets contenus dans le sac à dos, qui varie de 3 à 15 pièces d'or selon l'objet.  
L'objectif est d'aider le héros à effectuer cette optimisation.

---

|Objet|Anti.|Bag. mag.|Cape d'invis.|Diad.|Epée|Horloge|Miroir|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|Numéro objet|1|2|3|4|5|6|7|
|Valeur (pièces d'or)|3|5|12|15|9|10|12|
|Masse (kg)|0.5|1|1|5|6|5|3|
|Valeur massique||||||||

---

## Q1
Classer ces objets par valeur décroissante et donner la solution de l'algorithme glouton avec ce critère de classement.

|Numéro objet|4|3|7|6|5|2|1|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|Valeur (pièces d'or)|15|12|12|10|9|5|3|
|Masse (kg)|5|1|3|5|6|1|0.5|



Avec l'algorithme glouton et cette stratégie : 
- on prend les objets 4 - 3 et 7 soit (Diadème - Cape et Miroir) pour un poids de 9 kilos et une valeur de 39.

---

## Q2
Même question avec un classement par poids décroissant.

|Numéro objet|5|6|4|7||||
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|Valeur (pièces d'or)|3|12|5|12|10|15|9|
|Masse (kg)|0.5|1|1|3|5|5|6|

Avec l'algorithme glouton et cette stratégie : 
- on prend les objets 1 - 2 - 3 et 6 pour un poids de 5.5 kget une valeur de 20.

---

## Q3
Même question avec un classement par valeur/poids (valeur massique) croissant.

|Numéro objet|3|1|2|7|4|6|5|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|Valeur (pièces d'or)|12|3|5|12|15|10|9|
|Masse (kg)|1|0.5|1|3|5|5|6|
|valeur massique|12|6|5|4|3|2|1.5|

Avec l'algorithme glouton et cette stratégie : 
- on prend les objets 3 - 1 - 2 et 7 pour un poids de 5.5 kg et une valeur de 20.

---

!!! question "Q4"  
    A-t-on obtenu la solution optimale ?
