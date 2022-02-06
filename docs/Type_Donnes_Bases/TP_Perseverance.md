<table  style="table-layout: fixed;background-color:#87A96B; border:solid;color:black;width:100%;">
        <tr>
            <th colspan=2; style="background-color: #3B444B;color:white;text-align:center;border:none;font-size:12pt;">
           Thème 1 : Types de bases
            </th>
        </tr>
</table>
<table  style="table-layout: fixed;background-color:#87A96B; border:solid;color:black;width:100%;">
        <tr >
            <th width="20%"; style="background-color: #3B444B;color:white;text-align:center;border:none;font-size:50pt;">
            17
            </th>
            <th  width="80%"; style="text-align:center;background-color:#99BADD;border:none;font-size:25pt;">TP : Message caché sur le Rover Perseverance</th>
        </tr>
</table>

# TP 17 Cachez ce que je ne saurais voir !

**Un message caché sur le rover Perseverance.**

Ce que le rover cache, ne se trouve pas en dessous mais plutôt au dessus, rires !

![perseverance_rover_pillars.jpg](data/perseverance_rover_pillars.jpg){:.center width=500px}

Source : ESA


# Plan

* [1. easter egg by NASA](#1.-easter-egg-by-NASA)
   
* [2. Un écho de 1899](#2.-Un-écho-de-1899)


## 1. easter egg by NASA

Vous avez déjà probablement regardé la vidéo vertigineuse de [l’atterrissage](https://youtu.be/4czjS9h4Fpg) du rover Perseverance sur la planète rouge.

Mais avez-vous remarqué le parachute ?

**Sa conception esthétique n’a rien d’anodin :**

un message est encodé dans le motif, il était sous vos yeux durant toute la vidéo.


## Mais comment ce message est-il encodé ?

Si vous observez bien la conception du parachute, vous verrez qu’il est constitué de colonnes verticales, entièrement blanches, entièrement rouges, ou blanches et rouges.

![eu4f4esuyae939y.jpg](data/eu4f4esuyae939y.jpg)

Source : NASA


### Question 1 :

+ Par groupe, essayez de décomposer les zones décrites.
+ Que peuvent représenter les couleurs blanches, rouges ?
+ Les colonnes verticales peuvent être découpées en cercle de diamètres différents. Trouvez en combien de cercles le parachute est constitué.


### Réponse 1 :

...
Inscrire ici votre réponse
...


### Question 2 :

+ Avec vos constations, quel est la base de l'encodage ?
+ Sur combien de bits le message est-il encodé ?


### Réponse 2 :

...
Inscrire ici votre réponse
...


### Question 3 :

+ A partir du shéma ci dessous, Positionnez les valeurs binaires dans chaques des cases du parachute.

![eu4f4esuyae939y_eleve.jpg](data/eu4f4esuyae939y_eleve.jpg)


Source : Twitter, Adam Steltzner.

![](data/cercle_perseverance.png)




### Réponse 3 :

...
Inscrire ici votre réponse
...


### Question 4 :

Décodez les valeurs binaires trouvés en valeurs décimales : 
- soit à partir d'un programma Python, 
- soit à la main

Attention : Le bit de poids faible est à droite.


```python
# Votre programme ici
```

### Question 5 :

Pour que le message puisse être entièrement décodé, les valeurs trouvées en décimal vont être maintenant converties en texte par la convertion suivante: 
+ 00 0000 0001 : 'A'
+ 00 0001 1010 : 'Z'

Modifiez votre programme pour convertir la valeur binaire en une lettre de l'alphabet.



```python
# Votre programme ici
```

### Question 6 :

Avez vous décodez le message après déchiffrage des cercles 1 à 3 ?

Si oui quel est sa signification ?

### Réponse 6 :

...
Inscrire ici votre réponse
...


## Vérifiez votre déchiffrage.

Un internaute a rebondi sur l’idée pour mettre en ligne « Msg2Mars » via GitHub, le 23 février : cette page permet à chacune et chacun de concevoir son propre parachute, en y encodant un message.

Il suffit de renseigner les champs à droite du parachute qui s’affiche, et vous verrez le motif évoluer. Une fois le message entré, il est possible de télécharger un visuel du parachute, au format PNG.

https://sjwarner.github.io/perseverance-parachute-generator/


### Question 7 :

Vous avez aussi décodé le 4e cercle (le cercle en périphérie).
Que représente le message sur ce 4e cercle ?


### Réponse 7 :

...
Inscrire ici votre réponse
...


## 2. Un écho de 1899

Avant de savoir comment il est parvenu à trouver le résultat de l'énigme, on remarque que cette phrase a de profondes résonances dans l'histoire aérospatiale américaine, comme l'a détaillé le quotidien britannique The Guardian. Cette phrase, qu'on peut traduire par "Osez le sublime" ("mighty" signifie littéralement "puissant"), est le slogan du laboratoire Jet Propulsion de la NASA, qui a réalisé le gros du travail autour du rover Perseverance.

Elle prend racine dans la mémoire politique états-unienne. Lors d'un discours prononcé en avril 1899 devant le Hamilton Club de Chicago, le président américain, et Prix Nobel de la paix, Theodore Roosevelt avait ainsi lancé:

***"Mieux vaut, et de loin, oser le sublime, remporter de glorieux triomphes, même si nous sommes bousculés par l'échec, que de rentrer dans le rang de ces tristes sires qui n'exultent jamais ni ne souffrent beaucoup car ils vivent dans un crépuscule gris qui ne connaît ni la victoire ni la défaite".***

Le site du quotidien britannique note que le robot dépêché sur Mars est porteur de deux autres signes discrets. D'abord, il comporte des puces contenant 10,9 millions de textes ou propositions de noms envoyées à l'agence au moment où celle-ci cherchait à en choisir un pour son nouveau rover. Se trouve également sur le rover américain une assiette en aluminium où se dessine le caducée du dieu gréco-romain de la médecine Esculape (le même symbole que celui indiquant nos pharmacies) soutenant la Terre. Un hommage à l'action des soignants face aux ravages du Covid-19.

Le centre de recherche n’a pas seulement personnalisé le parachute qui a permis à Perseverance de ralentir sa course vers Mars. Sur le rover lui-même, le JPL a apposé une plaque avec un code Morse signifiant « Explore as One » (« Explorer comme un »), une phrase que la Nasa avait déjà employée auparavant. L’astromobile arbore également un portrait de famille avec plusieurs robots martiens, ainsi qu’un cadran solaire truffé de symboles sur l’histoire du système solaire et de la Terre.

À l’heure qu’il est, le véritable parachute de Perseverance gît à la surface de Mars, là où il est allé finir sa course une fois sa tâche accomplie pendant l’atterrissage. Il sera peu à peu recouvert par la poussière martienne, effaçant ainsi sa trace sur les images des orbiteurs.

# Fin ... 

A bientôt.

Auteurs :
    laura.fleron@ac-reims.fr

Fait le 23/02/2021

Version 2

Source :  Marcus Dupont-Besnard 23 février 2021 - Numérama.


```python

```
