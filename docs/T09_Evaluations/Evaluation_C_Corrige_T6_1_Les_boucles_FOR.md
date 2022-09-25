<table  style="border: 1px solid;  background-color: #c5ca27;  width: 100%;  color: black;  text-align: center; font-size: 18px;">
        <tr>
            <th style="background-color: #c5ca27;width: 100%; text-align:center;border:none;font-size:14pt;">
            Thème 6 - Langages et programmation
            </th>
        </tr>
</table>


<br>
<table  style="border: 1px;  background-color: #c5ca27;  width: 100%;  color: black;  text-align: center;font-size: 18px;">
        <tr >
            <th width="20%"; style="background-color: #3B444B;color:white;text-align:center;border:none;font-size:25pt;">
            Evaluation
            </th>
            <th  width="80%"; style="background-color: #c5ca27;text-align:center;border:none;font-size:25pt;">Les Boucles FOR en Python - Evaluation</th>
        </tr>
</table>
<br>

Devoir à faire avec des points bonus sur les derniers exercices.  
N'oublier pas d'enregistrer régulièrement votre travail.
A la fin penser à rendre votre travail.
Bon courage à vous.


<div class="alert alert-warning"><strong>Exercice 1 : </strong> <strong>La punition</strong><br>
    Ecrire un programme qui demande à l'utilisateur un message et le nombre de foisqu'il faut afficher ce message.   
</div>


```python
msg=input('Donner le texte à repéter : ')
nb_de_fois=int(input("donner le nombre de fois qu'il faut répéter le texte : " ))
for k in range(nb_de_fois):
    print(msg)
```

<div class="alert alert-info"><strong>Exercice 2 : </strong> Ecrire un programme qui calcule et affiche le produit 87x52 en n'effectuant que des additions.   
</div>


```python
resultat=0
for k in range(87):
    resultat+=52
print(resultat)
```

<div class="alert alert-success"><strong>Exercice 3 : </strong> Ecrire un programme qui demande à l'utilisateur de saisir un nombre entier, puis qui affiche la table de multiplication correspondande.   
    
    Quel table voulez-vous afficher ? 7 
    7 x 1 = 7
    7 x 2 = 14
    7 x 3 = 21
    ...
</div>


```python
nb=int(input("Quelle table de multiplication voulez-vous afficher ? )"))
print(f"Table de {nb} : ")
for k in range(11):
    print(f"{nb} * {k} = {nb*k}")
```

<div class="alert alert-warning"><strong>Exercice 4 :</strong>   Ecrire un programme qui affiche tous les entiers impairs de 0 à 187 inclus.
</div>


```python
for k in range(1,188,2):
    print(k, end=' ')
```

<div class="alert alert-info"><strong>Exercice 5 : </strong> Ecrire un programme qui affiche tous les carrés des nombres compris entre 0 et 29.
</div>


```python
for k in range(30):
    print(k**2, end=' ')
```

<div class="alert alert-success"><strong>Exercice 6 : </strong> <br> 1) Ecrire un programme qui affiche un rectangle de 5 lignes et 10 colonnes avec le caractère # comme ci-dessous :<br>
    ##########<br>
    ##########<br>
    ##########<br>
    ##########<br>
    ##########<br>
2) Améliorer ce programme pour qu'il demande d'abord à l'utilisateur de saisir la largeur et la hauteur du rectangle.<br>
On peut aussi lui demander avec quel caractère il souhaite remplir le rectangle.</div>


```python
# 1ère question :
for ligne in range(5):
    for colonne in range(10):
        print("#",end='')
    print("")
```


```python
# 2ème question
largeur = int(input("Veuillez saisir la largeur du rectangle : "))
hauteur = int(input("Veuillez saisir la hauteur du rectangle : "))
caractère = input("Veuillez saisir le caractère de remplissage : ")
for ligne in range(hauteur):
    for colonne in range(largeur):
        print(caractère,end='')
    print('')
```

<div class="alert alert-warning"><strong>Exercice 7 : </strong> <br>
1) Ecrire un programme qui calcule la moyenne de 7 notes. <br>
2) Améliorer ce programme pour qu'il demande d'abord à l'utilisateur de saisir le nombre de notes à rentrer puis qui calcule la moyenne de ses notes.    
</div>


```python
somme = 0
for i in range(7):
    note = float(input("Saisissez la note n°"+str(i+1)+" : "))
    somme = somme + note   # ou somme += note
moyenne = somme / 5
print(f"La moyenne des notes est {moyenne}")
```


```python
somme = 0
nb_2_notes=int(input("Combien de notes voulez-vous rentrer ? "))
for i in range(nb_2_notes):
    note = float(input("Saisissez la note n°"+str(i+1)+" : "))
    somme = somme + note   # ou somme += note
moyenne = somme / nb_2_notes
print(f"La moyenne des notes est {moyenne}")
```

<a id="partie2"></a>

<div class="alert alert-info"><strong>Exercice 8 : </strong> Ecrire un programme qui affiche le résultat suivant : <br>
36 33 30 27 24 21 18 15 12 9 6 3 0
</div>


```python
for k in range(36,-1,-3):
    print(k,end=' ')
```

<div class="alert alert-success"><strong>Exercice 9 : </strong> Ecrire un programme qui dessine un triangle comme ci-dessous avec une hauteur saisie par l'utilisateur.<br>
*****<br>
****<br>
***<br>
**<br>
*
    </div>


```python
hauteur=int(input("Veuillez saisir la hauteur du triangle : "))
for ligne in range(hauteur,0,-1):
    print("*"*ligne)
```

<div class="alert alert-warning"><strong>Exercice 10 : </strong> Ecrire un programme qui dessine une figure comme ci-dessous avec une hauteur et une largeur de 6 (on a un carré).<br>
******<br>
*****&<br>
****&&<br>
***&&&<br>
**&&&&<br>
*&&&&&<br>
&&&&&&    


```python
hauteur=int(input("Veuillez saisir la hauteur du triangle : "))
for ligne in range(0,hauteur+1):
    fin_ligne=hauteur-ligne
    print("*"*fin_ligne+"&"*ligne)

```

<div class="alert alert-info"><strong>Exercice 11 : </strong> Ecrire un programme qui dessine une figure comme ci-dessous avec une hauteur saisie par l'utilisateur.<br>
&<br>
&&<br>
&&&<br>
&&&&<br>
&&&&&<br>
&&&&&&</div>


```python
hauteur=int(input("Veuillez saisir la hauteur du triangle : "))
for ligne in range(hauteur+1):
    print("*"*ligne)
```

<a id="partie3"></a>

<div class="alert alert-warning"><strong>Exercice 12 : </strong> Ecrire un programme qui demande 7 valeurs à l'utilisateur et qui affiche la somme de ces valeurs.


```python
somme = 0
for i in range(7):
    note = float(input("Saisissez la note n°"+str(i+1)+" : "))
    somme += note   # ou somme += note
print(f"La moyenne des notes est {somme}")
```

<div class="alert alert-info"><strong>Exercice 13 : </strong> Ecrire un programme simule le lancer de 500 dés et qui affiche la moyenne des résultats obtenus.


```python
from random import *

somme = 0
for i in range(500):
    dé = randint(1,6)
    somme = somme + dé
moyenne = somme / 1000
print(f"La moyenne des 1000 lancers est {moyenne}")
```

<div class="alert alert-success"><strong>Exercice 14 : </strong> Ecrire un programme qui demande à l'utilisateur un entier a et un entier n et qui calcule $a^n$ à l'aide d'une boucle <code>for</code> (on verra plus tard un algorithme plus rapide que celui-ci).<br>
Remarque : il est interdit d'utiliser ** ici! 


```python
a = int(input("Veuillez saisir la valeurs de a (la base) : "))
n = int(input("Veuillez saisir la valeur de n (l'exponsant) : "))
puissance = 1
for i in range(n):
    puissance = puissance * a
print(f"{a} puissance {n} est égal à {puissance}")
```

<div class="alert alert-warning"><strong>Exercice 15 : </strong> Ecrire un programme qui demande de saisir un entier positif n et qui calcule la <strong>factorielle</strong> de n.<br>
    La factorielle de n, notée $n!$ est définie par $n! = 1\times 2\times 3\times...\times n$ .<br>
    On a par exemple $3! = 6$</code>.</div>


```python
n = int(input("Veuillez saisir un entier positif : "))
factorielle = 1
for i in range(1,n+1):
    factorielle *=i
print("La factorielle de ",n,"est",factorielle)
```

<div class="alert alert-info"><strong>Exercice 16 : </strong>  Ecrire un programme qui demande de saisir un entier positif n et qui calcule la <strong>somme des carrés S</strong> de 1 jusqu'à $n^2$.<br>
$S(n)=1^2 + 2^2 + 3^2 +...+ n^2$ .<br>
On a par exemple $S(3) = 14$</div>
    


```python
nb=int(input('Donner le nombre voulu : '))
resultat=0
for k in range(nb+1):
    resultat+=k**2
print(resultat)
```

<a id="partie4"></a>

<h2 style="text-decoration:underline;" id="partie4">4- Dessiner avec Turtle</h2>

La bibliothèque **turtle** permet de dessiner à l'écran.<br>
Le petit programme commenté ci-dessous permet d'obtenir un tracé intéressant :


```python
from turtle import *      # On importe la bibliothèque turtle

speed(10)                 # On règle la vitesse du tracé (un entier compris entre 1 et 10)
color('red', 'yellow')    # On fixe la couleur du tracé à 'rouge' et la couleur de rempissage à 'jaune'
begin_fill()
for i in range(36):
    forward(200)          # La tortue avance de 200 pixels 
    left(170)             # La tortue tourne vers la gauche de 170°
end_fill()
done()                    # Il faut terminer par done() pour lancer l'exécution du tracé    
```

Voici quelques fonctionnalités de turtle :

<style>
        td{
            color : green;
        }
</style>

<table>
    <tr><th style="border:1px solid #000000; background-color:pink; text-align: center;">Fonction</th><th style="text-align:center;border:1px solid #000000; background-color:pink;">Description</th></tr>
    <tr><td style="border:1px solid #000000; text-align: center;"><code>forward(x)</code></td><td style="border:1px solid #000000; text-align: center;">Déplace la tortue de x pixels en marche avant.</td></tr> 
    <tr><td style="border:1px solid #000000; text-align: center;"><code>backward(x)</code></td><td style="border:1px solid #000000; text-align: center;">Déplace la tortue de x pixels en marche arrière.</td></tr> 
    <tr><td style="border:1px solid #000000; text-align: center;"><code>left(x)</code></td><td style="border:1px solid #000000; text-align: center;">Fait pivoter la tortue d'un angle de x degrés vers la gauche.</td></tr>
    <tr><td style="border:1px solid #000000; text-align: center;"><code>right(x)</code></td><td style="border:1px solid #000000; text-align: center;">Fait pivoter la tortue d'un angle de x degrés vers la droite.</td></tr>
    <tr><td style="border:1px solid #000000; text-align: center;"><code>goto(x,y)</code></td><td style="border:1px solid #000000; text-align: center;">Déplace la tortue au point de corrdonnées (x,y). Attention, l'axe des y est orienté vers le haut de l'écran comme en mathématiques!</td></tr>
    <tr><td style="border:1px solid #000000; text-align: center;"><code>penup()</code></td><td style="border:1px solid #000000; text-align: center;">Lève le crayon (la tortue arrêtera de tracer).</td></tr>
    <tr><td style="border:1px solid #000000; text-align: center;"><code>pendown()</code></td><td style="border:1px solid #000000; text-align: center;">Abaisse le crayon. La tortue se remettra à tracer.</td></tr>
    <tr><td style="border:1px solid #000000; text-align: center;"><code>hideturtle()</code></td><td style="border:1px solid #000000; text-align: center;">Cache la tortue.</td></tr>
    <tr><td style="border:1px solid #000000; text-align: center;"><code>showturtle()</code></td><td style="border:1px solid #000000; text-align: center;">Fait réapparaitre la tortue.</td></tr>
    <tr><td style="border:1px solid #000000; text-align: center;"><code>speed(n)</code></td><td style="border:1px solid #000000; text-align: center;">Règle la vitesse du tracé. n est un entier compris entre 0 et 10. 1 correspond à une vitesse lente, 10 correspond à une vitesse rapide. 0 permet d'obtenir un tracé instantané.</td></tr>
    <tr><td style="border:1px solid #000000; text-align: center;"><code>done()</code></td><td style="border:1px solid #000000; text-align: center;">Lance l'exécution du tracé.</td></tr>
    <tr><td style="border:1px solid #000000; text-align: center;"><code>circle(r)</code></td><td style="border:1px solid #000000; text-align: center;">Trace un cercle de rayon r.<br>
        On peut ajouter une deuxième paramètre facultatif a si on souhaite tracer seulement tracer un arc de cercle d'angle a.</td></tr>
    <tr><td style="border:1px solid #000000; text-align: center;"><code>color(couleur1,couleur2)</code></td><td style="border:1px solid #000000; text-align: center;">Définir la couleur du tracé (couleur1) et la couleur de remplissage (couleur2).</td></tr>
    <tr><td style="border:1px solid #000000; text-align: center;"><code>width(n)</code></td><td style="border:1px solid #000000; text-align: center;">Règle l'épaisseur du trait à n pixels.</td></tr>
</table>

<div class="alert alert-success"><strong>Exercice 17 : </strong> Ecrire un programme qui utilise une boucle <code>for</code> pour tracer un carré de côté 100 pixels, avec un contour bleu et colorié en vert.</div>


```python

```

<div class="alert alert-warning"><strong>Exercice 18 : </strong> Ecrire un programme qui trace 10 cercles dont les rayons sont 10, 20, 30, ..., 100 et espacé de 2 fois le rayon<br>
Choisir une couleur de tracé et une couleur de remplissage.</div>




```python
from turtle import *      # On importe la bibliothèque turtle

speed(10)   
color('blue','pink')
for k in range(10,110,10):
    
    begin_fill()
    circle(k)
    forward(20)
    end_fill()

done()
```

<div class="alert alert-info"><strong>Exercice 19 : </strong> Dessiner le drapeau de l'allemagne avec Turtle.</div>


```python
from turtle import *

up()
goto(-250,0)
down()

color('black', 'black') 
begin_fill()
for i in range(2):
    forward(300)
    left(90)
    forward(75)
    left(90)
end_fill()
right(90)
forward(75)
left(90)

color('black', 'red') 
begin_fill()
for i in range(2):
    forward(300)
    left(90)
    forward(75)
    left(90)
end_fill()
right(90)
forward(75)
left(90)


color('black', 'yellow') 
begin_fill()
for i in range(2):
    forward(300)
    left(90)
    forward(75)
    left(90)
end_fill()
forward(100)

done()
```


```python
#Avec une fonction 
def rectangle(largeur,longueur,couleur1,couleur2):
    color(couleur1, couleur2) 
    begin_fill()
    for i in range(2):
        forward(longueur)
        left(90)
        forward(largeur)
        left(90)
    end_fill()

up()
goto(-250,0)
down()
largeur=75
longueur=300
rectangle(largeur,longueur,'black','black')
right(90)
forward(largeur)
left(90)

rectangle(largeur,longueur,'black','red')
right(90)
forward(largeur)
left(90)

rectangle(largeur,longueur,'black','yellow')
done()
```

<div class="alert alert-info"><strong>Exercice 20 : </strong> Ecrire un programme qui dessine le diamant ci-dessous.</div>




```python
from turtle import *

speed(10)
color('blue') 
goto(-250,0)
goto(250,0)
for i in range(11):
    goto(0,100)
    goto(i*50-250,0)   
    goto(0,-100)
done()
```


```python

```
