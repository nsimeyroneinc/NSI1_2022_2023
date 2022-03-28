---
#title : Exercice Révision - Codage de caractères
subtitle: Représentation des données
author : M.Meyroneinc-Condy
numbersections: true
fontsize: 11pt
geometry:
- top=12mm
- left=12mm
- right=12mm
- heightrounded    
output:
  pdf_document:
    toc: yes
    toc_depth: 3
    number_sections: yes
    highlight: tango
  blogdown::html_page:
    toc: yes
    toc_depth: 3
    number_sections: yes
    highlight: tango
--- 


<table  style="table-layout: fixed; border:solid;color:black;width:100%;">
        <tr>
            <th colspan=2; style="background-color: #3B444B;color:white;text-align:center;border:none;font-size:12pt;width:100%;">
           Thème 1 : Types de bases
            </th>
        </tr>
</table>

<table  style="table-layout: fixed;border:solid;color:black;width:100%;">
        <tr >
            <th width="30%"; style="background-color: #3B444B;color:white;text-align:center;border:none;font-size:20pt;">
            DS
            </th>
            <th  width="70%"; style="text-align:center;background-color:#99BADD;border:none;font-size:20pt;"> Codage des caractères</th>
        </tr>
</table>


<div style="page-break-after: always;"></div>

![](data/ascii.png){:.center width=350px}  
*Table ASCII*

!!! exo "Exercice 1 :"
   Décoder l'expression suivante, écrite en ASCII :  

    ```01010000 01100101 01110010 01110011 01101111 01101110 01101110 01100101 00100000 01110000 01100001 01110010 00100000 01101100 01100001 00100000 01100111 01110101 01100101 01110010 01110010 01100101 00100000 01101110 01100101 00100000 01100100 01100101 01110110 01101001 01100101 01101110 01110100 00100000 01100111 01110010 01100001 01101110 01100100 00101110 00001101 00001010 00001101 00001010 ```

    Yoda

??? tip "Correction"

    - Première méthode en passant par les binaires : 

    |128  | 64  |32   |16   |8    |4    |2    |1    |dec  |lettre ASCII|
    |:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
    |0|1|0|1|0|0|0|0| 80 | P |
    |0|1|1|0|0|1|0|1| 101 | e |


    - Deuxième méthode en passant par l'hexadécimal en découpant 4 par 4 :  
    - pour 01010000 -> 0101 soit 5 et 0000 soit 0 donc en hexadécimal 50 donc la lettre P

    - pour 01100101 -> 0110 soit 6 et 0101 soit 5 donc en héxadécimal 65 donc la lettre e

    - etc ...

    Au final, on obtient une citation de Yoda :  
    "Personne par la guerre ne devient grand"



![](data/iso-latin.png){:.center width=300px}
*Latin-9*

!!! exo "Exercice 2 :"
    **Q.1.** Le mot représenté par les octets ci-dessous est-il codé en ASCII ou en Latin 9 ? Donner ce mot :   
    ![](data/DS_mot.png){width=200px}  
    **Q.2.** Représenter `goûté` en Latin-9

??? tip "Correction"
    1. Le mot codé est déçus!  
    2. goûté : 67 6F FB 74 E9

![](data/cap_utf8.png){:.center  width=800px}

!!! exo "Exercice 3 : "
    ![](data/LatinB.png){width=300px}  
    Donner le codage Unicode la lettre &#586; puis son codage en UTF-8


??? tip "Correction"
     &#586;  - -> Unicode : +U024A

     - -> sur 11 bits :  
        - A en binaire -> <span style="color:red">1010</span>   (4 bits)
        - 4 en binaire -> <span style="color:green">0100</span>   (4 bits)
        - 2 en binaire -> <span style="color:blue">010</span>   (3 bits restants)

    - -> on remplie les 2 octects :  
        - 110<span style="color:blue">010</span><span style="color:green">01</span>  
        - 10<span style="color:green">00</span><span style="color:red">1010</span>

    - -> en repassant à l'hexadécimal :  
        - 12 soit C et 9
        - 8 et A

    - -> en UTF-8  :  C9 8A


!!! exo "Exercice 4"
    Décoder le message suivant :  
    ![](data/DS_parachute_GP2.png){:.center  width=600px}

??? tip "Correction"
    ![](data/DS_Parachute_Gpe2_Cor.png)

!!! exo "Exercice 5"
    Le défi du cours : codage UTF-8 (Latin-9), décoder le texte ci-dessous :  

    `56 65 72 73 20 6C 27 69 6E 66 69 6E 69 20 65 74 20 6C 27 61 75 2D 64 65 6C C3 A0``

??? tip "Correction"
    Vers l'infin et l'au-del&#195;   

!!! exo "Exercice 4 :"
    Codage XOR : 

**Q.1.** Le nombre 65, donné ici en écriture décimale, s’écrit 01000001 en notation binaire. En détaillant la méthode utilisée, donner l’écriture binaire du nombre 86.

??? tip "Correction"
    86 en binaire : 0101 0110

**Q.2.** La fonction logique **OU EXCLUSIF**, appelée **XOR** et représentée par le symbole ⊕, fournit une sortie égale à 1 si l’une ou l’autre des deux entrées vaut 1 mais pas les deux. 

On donne ci-dessous la table de vérité de la fonction XOR

|A|B|A XOR B|
|:---:|:---:|:---:|
|0|0|0|
|0|1|1|
|1|0|1|
|1|1|0|

Poser et calculer l’opération : 11011101 ⊕ 01101011

On donne, ci-dessous, un extrait de la table ASCII qui permet d’encoder les caractères de A à Z.  
On peut alors considérer l’opération XOR entre deux caractères en effectuant le XOR entre les codes ASCII des deux caractères.  
Par exemple : 'F' XOR 'S' sera le résultat de 01000110 ⊕ 01010011.

??? tip "Correction"  
      11011101  
    ⊕ 01101011  
    ---  
      10110110  

![](data/ascii_Exo.png){:.center width=350px}  

On souhaite mettre au point une méthode de cryptage à l’aide de la fonction XOR.  
Pour cela, on dispose d’un message à crypter et d’une clé de cryptage de même longueur que ce message. Le message et la clé sont composés uniquement des caractères du tableau ci-dessus et on applique la fonction XOR caractère par caractère entre les lettres du message à crypter et les lettres de la clé de cryptage.

**Question 3.**
Chiffrer **ALPHA** avec la clé **NSI**. Pour cela recopier et compléter le tableau ci-dessous : 

![](data/DS_XOR.png){:.center width=300px}  


??? tip "Correction"
    ![](data/DS_XOR_Cor_Gpe2.png)

**Q.4.**  
Recopier et compléter la table de vérité de (𝑬𝟏 ⊕ 𝑬𝟐) ⊕ 𝑬𝟐.

![](data/Table_XOR_XOR.png){:.center width=300px}  

??? tip "Correction"
    ![](data/DS_XOR_XOR_Cor.png){:.center width=300px}  

A l’aide de ce résultat, proposer une démarche pour décrypter un message crypté.

??? tip "Correction"  
    Pour décoder le message, on a juste à refaire la fonction XOR sur le message codé avec la clé.

**Q.5** Décoder le message suivant : 
`12 1 8 24 28 105 15 115 29 1 6 26`

??? tip "Correction"  
    Bravo à tous
