<table  style="background-color:  #66CC33; width:100%;">
    <thead>
        <tr>
            <th style="text-align:center;border:solid;border-width:1px;font-size:20pt;width:70%;">TD n°11 : HTML et CSS</th>
            <th style="text-align:center;border:solid;border-width:1px;font-size:12pt;width:30%">Thème  : INTERACTIONS ENTRE HOMME ET LA MACHINE</th>
        </tr>
                    <tr>
            <th style="text-align:center;border:solid;border-width:1px;font-size:20pt;width:70%;"></th>
            <th style="text-align:center;border:solid;border-width:1px;font-size:12pt;width:30%">COURS</th>
        </tr>
    </thead>
</table>

<iframe width="640" height="360" src="https://www.youtube.com/embed/8FqZZrbnwkM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>




Les langages informatique HTML et CSS sont les langages des pages Web. Ce sont deux langages com- plémentaires compris par les navigateurs. Ce ne sont pas des langages de programmation mais des langages de description.


# I. Qu'est ce que le HTML ?

Quand on consulte un site web, notre ordinateur se connecte à un serveur distant et celui-ci lui envoie une page web, que le navigateur va pouvoir afficher. En général la page est constituée de plusieurs fichiers :

- un fichier HTML (il existe d’autres formats qui seront étudiés plus tard : php, jsp, asp, ...)
- un fichier CSS
- un fichier JS
- des images, du sons, ...

Le format HTML (de l’anglais HyperText Markup Language, ou « langage de balisage hypertexte ») est un format textuel qui permet de décrire le contenu et la structure d’une page Web.  
Plusieurs versions du langage HTML se sont succédées depuis la première en 1992, celle utilisée actuellement est HTML5.

<blockquote style="background-color: #DAF7A6; border-left: 7px solid rgb(0 0 0);">
    <span style="font-size:25px">&#x1F4D8;   Un peu d’histoire: </span> <br>

<img src="imagesWEB/Tim_Berners-Lee.jpg">

**TimBerners-Lee** est considéré comme l’inventeur du HTML en1992. C’est un informaticien britannique, qui a aussi inventé le Web (World Wide Web ou WWW) en 1989 lors de ses travaux au CERN. En juillet 2004, il est fait chevalier par la reine Élisa- beth II pour ce travail et son nom officiel devient Sir Timothy John Berners-Lee. Depuis 1994, il préside le World Wide Web Consortium (W3C), organisme qu’il a fondé et qui est en charge de promouvoir la compatibilité des technologies du Web. Il est également lauréat du prix Turing 2016.
</blockquote>

 

**LeLangageHTMLetCSS**

La description du contenu et de la structure d’une page Cette description se fait en utilisant ce qu’on appelledesbalises. Cesontcesbalisesquivontindiquersitellepartiedudocumentestuntitre, oubien un paragraphe, ou bien une image, ...

**Lesbalises**

Une balise est un mot-clef permettant d’indiquer au navigateur ce qu’il doit faire avec le contenu. Les balises contrôlent tout. Elles permettent de gérer la structure, les images, les liens, la police d’affichage utilisée, les titres, ¢¢¢

On écrit <balise> pour ouvrir une balise (appelée **balise ouvrante**) et </balise> pour la fermer appelée **balisefermante**). De manière générale, toute balise ouverte doit être fermée.



Voici la structure minimale (squelette) de toute page HTML : 

<!DOCTYPE html> <!-- langage utilisé, html pour html5 --> 

<html lang="fr"> <!-- début de la page web --> 

<head> <!-- En tête de la page, la balise n ' est pas affiché, mais elle permet ,! de donner des informations telles que le titre de la page ou la police de ,! caractères utilisée --> 

<title> Le html en 1ère NSI</title> 

<meta charset="utf-8"/> 

</head> 

<body> <!-- Corps de la page, c ' est ici que l ' on écrit tout ce qui doit être 

,! affiché --> 

<h1> COURS de NSI 

</h1> <!-- balise de titre de niveau 1, il y 6 niveaux possibles--> 

<p> 

Bienvenue en cours de NSI. 

</p> </body> 

</html> 

On retrouve toujours : 

- une première ligne <!DOCTYPE html>qui indique que le fichier texte qui suit et écrit dans le lan- gage HTML 
- La balise <html> </html> , qui est la balise principale du code , elle englobe tout le contenu écrit en HTML du fichier. Dans cette balise, on distingue deux partie différentes : 

ç La balise <head></head> qui est la balise d’en-tête du document et qui donne les informa- 

tions générales sur la page Web : on peut y idiquer son titre, l’encodage des caractères, les mots-clés, son auteur, etc. 

ç La balise <body></body> qui est la balise du corps de la page : elle encadre tout le contenu 

que le navigateur doit affihcer à l’écran. 

Ces balises sont obligatoires dans tout document HTML. **LeLangage**

On peut remarquer que certaines balises particulières ne se ferment pas (comme la balise <meta/> ). Dans ce cas il y a un “/” avant le “>” ? 

**Définition**

Le nom d’une balise s’appelle un **élément** (exemple ici body, p ou meta). Certainsélémentspeuventavoirdesattributspourdéfinirdesparamètres. Danscecaslesattributs sont toujours donnés entre guillemets " " ou apostrophes ‘ ’. 

De plus des balises peuvent être imbriquées les une dans les autres mais pas se chevaucher ! 

**Remarque** 

Les commentaires sont délimités par les caractères <!-- et --> , ils ne sont pas interprétés par le navigateur et servent à l’auteur pour écrire des notes (destinées à lui-même ou à d’autres person- nes). 




**Exemple 6. 1:**

<p>

Bienvenue en <em> cours </em> de NSI.<br/>

Ici les balises sont correctement imbriquées </p>

<p>

Bienvenue en <em> cours de NSI.<br/>

Problème, la balise em est fermé après la balise p !! </p></em>

3. ` `**Inline**

Voici les éléments les plus courants mais il en existe d’autres. Ils peuvent être regroupées en deux caté- gories :

- lesélémentsdebloc(**block** enanglais)quis’affichentcommeunbloc(sautdeligneavantetaprès automatiquement),
- les éléments en ligne (**inline** en anglais) qui s’affichent dans la ligne courante. Un élément inline doit obligatoirement être à l’intérieur d’un bloc.

**Balises detypeblock** :

...

<body>

<p>

Un paragraphe

**LeLangageHTMLetCSS** </p>

<h1>

Un titre de premier niveau

</h1>

<h2> Un titre de niveau 2

</h2>

<ul> <!-- une liste à puce (Unordered List) -->

<li> Premier élément de la liste à puce </li>

<li> Deuxième élément de la liste à puce </li> </ul>

<ol> <!-- une liste numérotée (Ordered List) --> <li> Premier élément de la liste numérotée </li>

<li> Deuxième élément de la liste numérotée </li> </ol>

<div>

Un bloc quelconque, utile pour la mise en forme

</div> </body> </html>

 **Balises type inline** :



|Balise|Fonction|Attributs utiles|
| - | - | - |
|<br/>|Retour à la ligne||
|<img/>|Permet d’insérer une image|<p>- src = ’emplacement de l’image’</p><p>- alt = ’texte à afficher si problème’</p>|
|<a>|Ancre, permet de créer un lien|<p>- name = ’nom de l’ancre’</p><p>&emsp;- href = ’lien’</p>|
**Exemple 6. 2:**

...

<body>

<h1>

Un exemple avec des éléments inline

</h1>

<p>

Voici un paragraphe. Pas d ' élément &lt; br/&gt; donc pas de retour à la ,! ligne.<br/>

Après la balise une nouvelle ligne commence.<br/>

Une ligne avec une image : <img src= ' adresse image ' alt= ' Mon image' /><br/ >

,!

Et maintenant un lien vers un autre site : <a href= ' url souhaitée ' > Le site du prof ! </a>

,!

</p>

</body>

</html>

4. ` `**le  LeLangage**

**LangageCSS**

LeformatCSS(del’anglaisCascadingStyleSheets,ou«feuillesdestylesencascade»)estunformat textuelquipermetdedécrirelamiseenformedesdocumentsHTML(etXML).Lapremièreversion du langage CSS date de 1996. Celui-ci est pris en charge par tous les navigateurs depuis les années 2000. La version utilisée actuellement est CSS3.

**Unlangagedestyle**

Le langage CSS permet de définir les propriétés graphiques des éléments HTML constituant une page Web : les polices utilisées, leurs tailles, les couleurs utilisées, la position des éléments dans la page, etc. Ce langage permet de séparer le contenu (décrit en HTML) de la forme (décrit en CSS) d’une page Web. En pratique, le fichier CSS sera associé au fichier HTML et le navigateur pourra alors savoir comment il doit mettre en forme le contenu de la page Web.

Le fichier ‘.css’ (cascading style sheet) qui accompagne souvent une page html sert à définir tout ce qui concernelaformedudocument(làoùlapartieHTMLs’occupeplutôtducontenu). Ilgèredonclataille de la police, la couleur, le positionnement des blocs, des images, ...



Exemple de page internet san[s CSS](https://jsfiddle.net/meyroneinc/skp8c3u5/2/) et avec[ CSS.](https://jsfiddle.net/meyroneinc/dkswnha8/)

Un fichier contenant du code CSS permet de donner des informations sur la forme que doit avoir une page internet (couleur de la police, position et taille des images, fond de page, menus, ...). Ce fichier peutavoirlenomquel’onsouhaite(onutiliseranéanmoinspréféremmentl’extension.css). Dansnotre exemple ce fichier s’appellera “style.css”.

**Cequ’ilfautretenir**

**ModificationsàapporterdanslefichierHTML:**

- il faut donner le nom (et le chemin si nécessaire) du(des) fichier(s) CSS à utiliser. Cela se fait à l’aide de la balise suivante dans l’en-tête : <link href="style.css" rel="stylesheet" type="text/css">
- on peut maintenant utiliser 2 nouveaux attributs dans les balises HTML,
  - id="nomUnique" : permet de donner un nom unique à un élément pour lui appliquer un style particulier,
  - class="nom" : permet de donner le même nom à un ensemble d’éléments auxquels on veut appliquer le même style.

DanslefichierCSSonpeutmaintenantcréerunensemblederèglesàappliquer. Unerègleestcomposée d’unsélecteur(l’objetauquellarègledoits’appliquer)etdedéclarationsdepropriétés. Lesdéclarations se trouvent entre accolades et les propriétés sont séparées par des points-virgules.

**LeLangageHTMLetCSS**

Il y a beaucoup de sélecteurs différents, les plus courants sont :

- lenomd’untyped’éléments(ex: html, p, body, h1, img, ... ): larègles’appliqueàtousles éléments de la page de ce type,
- le nom d’un id précédé d’un # : la règle s’applique au seul élément ayant cet id,
- le nom d’une classe précédé d’un point : la règle s’applique à tous les éléments ayant cette classe, qu’importe le type.

On peut mélanger plusieurs sélecteurs pour une même règle.

Il existe une très grande variété de propriétés, la liste dépendant du sélecteur choisi ! **Exemple 6. 3:**



<!DOCTYPE html> <!-- langage utilisé, html pour html5 -->

<html lang="fr"> <!-- début de la page web -->

<head> <!-- En tête de la page, la balise n ' est pas affiché, mais ,! elle permet de donner des informations telles que le titre de la page ou ,! la police de caractères utilisée -->

<title> Le CSS en 1ère NSI</title>

<meta charset="utf-8"/>

<link rel="stylesheet" href="style.css"> <!-- import le CSS de la ,! page cible -->

</head>

<body>

<h1>Un joli titre centrée, en rouge et en italique.</h1>

<p>

Un beau paragraphe générique.

</p>

<p class="important">

Un paragraphe de la classe "important" que je vais faire apparaitre en gras.

,!

</p>

<p>

Un paragraphe normal dans lequel <a href="https://sites. ,! google.com/view/nsi-premiere/accueil?authuser=1" class="important"> le ,! lien est important </a>.

</p>

<p id="fin">

Un paragraphe unique avec le texte en bleu.

</p>

<img src= ' https://drive.google.com/uc?

,! id=1Ec6yGZA5tHZnJoujwsfjwKKuOfeYJkR6' style= ' height: 150px ' alt= ' image mac ,! ' id=' logo ' />

</body>

</html>

**LeLangage**



body{

font-family: helvetica, arial, sans-serif; margin: 2em;

background-color: beige;

}

h1{ /\* tous les titres h1 \*/

font-style: italic;

text-align: center;

color: red;

}

p{ /\* tous les paragraphes \*/

margin-left: 280px;

}

#fin{ /\* l ' unique élément d ' id fin \*/

color: darkblue;

}

.important{ /\* tous les éléments de la classe important \*/

font-weight: bold;

}

img#logo{ /\* élément img avec l ' id logo \*/

display: block;

border-radius: 20px;

width: 150px;

margin-left: auto;

left: 20px;

top: 20px;

position: fixed;

}

Rendu des pages sa[ns CS](https://jsfiddle.net/meyroneinc/a2tgu8bo/)S et av[ec CSS.](https://jsfiddle.net/meyroneinc/9z86kprh/1/)

**LeLangageHTMLetCSS**



5. ` `**boites**

TouslesélémentsHTMLdetypeblocksontmanipulésentantqueboitesparCSS.Ilexisteunepropriété display en CSS pour transformer n’importe quel élément en type block (ou autre) si on le souhaite.

Voici les différentes propriétés d’une boite en CSS : 

right top

 margin-top border-top

padding-top

height

width

margin-left border-left

padding-left border-right margin-rpadding-right

padding-bottom

border-bottom

margin-bottom bottom

left 
La zone centrale représente le contenu, le padding <header>![](Aspose.Words.4f226f03-13bc-47a4-84e3-08978a8a61fb.022.png)

est l’écart entre le contenu et la bordure, le margin **LeLangage **est l’écart avec le bord extérieur de la boite. <nav>

La position d’un élément peut être définie avec la 

propriété position. Elle peut être relative à la place <section> <aside> del’élémentdanslefluxdelapageouabsolute,c’est

à dire définie directement par rapport au bord de la

fenêtre. <article>

L’ensemble de ces propriétés, associées aux élé-

ments div, header, nav, section, article, aside et <article>

footer permet de construire une belle mise en page

en HTML.

Voiciunexempleavecunen-têtedepage,unebarre <article>

de navigation, un pied de page et une colonne de

menus (à droite de la page dans cet exemple). 

<footer>

**Exemple 6. 4:**

Une version sans la barre de navigation :


Et le code HTML associé :

Le code CSS correspondant : <!DOCTYPE html>

<html lang="fr">

html { <head>

height: 100%; <title>NSI : CSS</title>

box-sizing: border-box; <meta charset="utf-8" />

} <link rel="stylesheet" href="style1.css" body {

box-sizing: border-box; ,! />

</head>

font-family: helvetica, 

<body>

arial, sans-serif;

,! <header>

margin: 0em;

background-color: beige; </headerUne jolie> bannière, un menu, ... min-height: 100%; <section>

padding-bottom: 30px; <article>

} <h1>Contenu 1</h1>

section { Voici le contenu de la page, on peut 

padding: 20px; le faire changer grâce aux liens

height: auto; ,!

par exemple.

float: left;

</article>

width: 85%;

<article>

}

<h1>Contenu 2</h1>

header {

Il peut y a voir plusieurs articles height : 5%;

</article>

padding: 20px;

<article>

text-align: center;

<h1>Contenu 3</h1> background-color: grey;

L' informaticien logiciel et 

}

footer { ,! programmation.<br />

height : 30px; Le travail d ' un ...

padding: 10px; Il propose également des ... text-align: center; <br />

<br />

**LeLangageHTMLetCSS** positionbackground-co: absolutelor:; grey; Source : wikipédia

</article>

rightleft: :0;0; </section>

bottom: 0; <aside>

clear: both; <h4>Un menu</h4>

} <ul>

aside { <li><a href="">Page 1</a></li> <li><a href="">Page 2</a></li>

paddingfloat: right: 10; px; <li><a href="">Page 3</a></li>

width: 10%; </ul>

</aside>

h4} { <footer>

Un pied de page ...

} text-align: center; </footer>

</body>

</html>

