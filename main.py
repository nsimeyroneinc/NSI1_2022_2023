import os
import csv

# print(env.variables.config['theme']['palette']) # access palette color. Automatic toggle of color ?

def define_env(env):
    "Hook function"

    env.variables['transversal']=["histoire","projet","typesconstruits","python"]
    env.variables['projet'] = {"icone":":fontawesome-solid-lightbulb:","style":"projet"}
    env.variables['typesconstruits'] = {"icone":":fontawesome-solid-cubes:","style":"typesconstruits"}
    env.variables['python'] = {"icone":":fontawesome-brands-python:","style":"python"}
    env.variables['themes']={
        "histoire":"Histoire de l'informatique",
        "projet":"Projet",
        "devoir":"Devoir",
        "sd":"Structures de données",
        "db":"Bases de données",
        "os":"Architectures matérielles, systèmes d'exploitation et réseaux",
        "algorithmique":"Algorithmique",
        "python":"Langages et programmation",
        "typesconstruits":"Types construits",
        "typesbase":"Types de base",
        "donneestable":"Données en table",
        "web":"Le web"
    }
    env.variables['icones'] = {
        "histoire":':fontawesome-solid-building-columns:{title="'+env.variables['themes']['histoire']+'"}',
        "projet":':fontawesome-solid-lightbulb:{title="'+env.variables['themes']['projet']+'"}',
        "devoir":':fontawesome-solid-pen-to-square:{title="'+env.variables['themes']['devoir']+'"}',
        "sd":':fontawesome-solid-diagram-project:{title="'+env.variables['themes']['sd']+'"}',
        "db":':fontawesome-solid-database:{title="'+env.variables['themes']['db']+'"}',
        "os":':fontawesome-solid-microchip:{title="'+env.variables['themes']['os']+'"}',
        "algorithmique":':fontawesome-solid-gears:{title="'+env.variables['themes']['algorithmique']+'"}',
        "python":':fontawesome-brands-python:{title="'+env.variables['themes']['python']+'"}',
        "typesconstruits" : ':fontawesome-solid-cubes:{title="'+env.variables['themes']['typesconstruits']+'"}',
        "typesbase" : ':fontawesome-solid-cube:{title="'+env.variables['themes']['typesbase']+'"}',
        "donneestable" : ':fontawesome-solid-table-columns:{title="'+env.variables['themes']['donneestable']+'"}',
        "web" : ':material-web:{title="'+env.variables['themes']['web']+'"}'

    }
    env.variables['icones_exo']={
        "dur": ":fontawesome-solid-bomb:{title='Exercice difficile'}",
        "rappel": ":fontawesome-solid-clock-rotate-left:{title='Retour sur des notions antérieures'}",
        "recherche": ":fontawesome-solid-search:{title='Exercice de recherche'}",
        "capacite": ":fontawesome-solid-puzzle-piece:{title='Exercice testant une capacité du chapitre'}",
        "python": ":fontawesome-brands-python:{title='Exercice en lien avec la programmation en Python'}",
        "bac": ":fontawesome-solid-graduation-cap:{title='Exercice extrait du Bac'}",
        "maths": ":fontawesome-solid-infinity:{title='Exercice en lien avec les mathématiques'}"
    }
    env.variables['icones_act']={
        "rappel": ":material-history:{title='Retour sur des notions antérieures'}",
        "recherche": ":fontawesome-solid-search:{title='Activité de recherche'}",
        "oral": ":fontawesome-solid-comments:{title='Activité oral'}",
        "papier": ":material-file-edit-outline:{title='Activité à réaliser sur feuille'}",
        "vscode": ":material-microsoft-visual-studio-code:{title='Activité utilisant VS Code'}",
        "video": ":fontawesome-solid-film:{title='Activité utilisant un support vidéo'}",
        "notebook": ":fontawesome-solid-book:{title='Activité utilisant un jupyter notebook'}",
        "python": ":fontawesome-brands-python:{title='Activité en lien avec la programmation en Python'}",
        "maths": ":fontawesome-solid-infinity:{title='Activité en lien avec les mathématiques'}"
    }

    env.variables['devant_exo']=':black_small_square:'
    env.variables['devant_act']=':black_small_square:'
    env.variables['num_exo']=1
    env.variables['num_act']=1

    env.variables['progression_premiere']={
        0 : ["python","Introduction",0,"T06_Python/T6.1_Python/T6_1_0_Introduction.md"],
        1 : ["python","Les variables en Python",1,"T06_Python/T6.1_Python/T6_1_1_Les_Variables_en_Python.md"],
        2 : ["python","Les fonction en Python",1,"T06_Python/T6.1_Python/T6_1_2_Les_fonctions_en_Python.md"],
        3 : ["python","Les Boucles FOR",1,"T06_Python/T6.1_Python/T6_1_3_Boucle_FOR_en_Python.md"],
        4 : ["typesbase","Représentation des entiers positifs",1,"T01_TypesBase/T1.1_Bases/T1_1_Codage_Entiers.md"],
        5 : ["typesbase","Représentation des entiers négatifs",1,"T01_TypesBase/T1.2_Relatifs/T1_2_Relatifs.md"],
        6 : ["typesbase","Représentation des flottants",1,"T01_TypesBase/T1.3_Flottants/T1_3_Flottants.md"],
        7 : ["python","Les boucles WHILE",1,"T06_Python/T6.1_Python/T6_1_4_WHILE.md"],
        8 : ["python","Les instructions conditionnelles",1,"T06_Python/T6.1_Python/T6_1_5_Instructions_conditionnelles.md"],
        9 : ["python","Exercices Bilan Python",1,"T06_Python/T6.1_Python/T6_1_6_Exercices_Bilan_Bases.md"],
        10 : ["web","Le web",2,"T04_IHMWeb/T4.1_HTML_CSS/T4.1_HTML_CSS.md"],
        11: ["web","Interaction dans une page web",1,"T04_IHMWeb/T4.2_Interactions/T4.2_Js.md"],
        12 : ["typesconstruits","Les tableaux en Python",1,"T02_TypesConstruits/T2.1_Listes/T2_1_Les_tableaux.md"],
        13 : ["typesbase","Les Booleens",1,"T01_TypesBase/T1.4_Booleens/T1_4_Booleens.md"],
        14 : ["os","Architecture d'un réseau",1,"T05_Architectures/T5.3_Reseaux/T5.1_Architecture.md"],
        15 : ["python","Algorithme glouton",1,"T07_Algorithmes/T7_1_Gloutons/algo_glouton.md"]
        #9 : ["algorithmique","Algorithmes de tri",2,"algostri.md"],
        #10 : ["typesbase","Représentation des entiers négatifs",1,"negatifs.md"],
        #11: ["os","Réseau",1,"reseau.md"],
        #12: ["web","Interaction dans une page web",1,"interactionweb.md"],
        #13: ["algorithmique","Algorithmes gloutons",2,"gloutons.md"],
        #14: ["donneestable","Fusion de tables",1,"fusiontable.md"],
        #15: ["os","Interface homme-machine",2,"interface.md"],
        #16: ["typesbase","Notion de nombre flottant",1,"flottant.md"],
        #17: ["algorithmique","Algorithme des k plus proches voisins",2,"knn.md"]
    }

    env.variables['projet_premiere']={
        1 : ["projet","Défi Logo Sprint",1,"T08_Extras/5MiniProjet/logo.md"],
        2 : ["projet","Dessine ta rue","17/11/2023","T08_Extras/5MiniProjet/dessine_ta_rue.md"]
        #2 : ["python","Les fonction en Python",1,"T06_Python/T6.1_Python/T6_1_2_Les_fonctions_en_Python.md"],
        #3 : ["python","Les Boucles FOR",1,"T06_Python/T6.1_Python/T6_1_3_Boucle_FOR_en_Python.md"],
        #4 : ["typesbase","Représentation des entiers positifs",1,"T01_TypesBase/T1.1_Bases/T1_1_Codage_Entiers.md"],
        #5 : ["typesbase","Représentation des entiers négatifs",1,"T01_TypesBase/T1.2_Relatifs/T1_2_Relatifs.md"],
        #6 : ["typesbase","Représentation des flottants",1,"T01_TypesBase/T1.3_Flottants/T1_3_Flottants.md"],
        #7 : ["python","Les boucles WHILE",1,"T06_Python/T6.1_Python/T6_1_4_WHILE.md"],
        #8 : ["python","Les instructions conditionnelles",1,"T06_Python/T6.1_Python/T6_1_5_Instructions_conditionnelles.md"],
        #9 : ["python","Exercices Bilan Python",1,"T06_Python/T6.1_Python/T6_1_6_Exercices_Bilan_Bases.md"]
        #8 : ["web","Le web",2,"leweb.md"],
        #9 : ["algorithmique","Algorithmes de tri",2,"algostri.md"],
        #10 : ["typesbase","Représentation des entiers négatifs",1,"negatifs.md"],
        #11: ["os","Réseau",1,"reseau.md"],
        #12: ["web","Interaction dans une page web",1,"interactionweb.md"],
        #13: ["algorithmique","Algorithmes gloutons",2,"gloutons.md"],
        #14: ["donneestable","Fusion de tables",1,"fusiontable.md"],
        #15: ["os","Interface homme-machine",2,"interface.md"],
        #16: ["typesbase","Notion de nombre flottant",1,"flottant.md"],
        #17: ["algorithmique","Algorithme des k plus proches voisinumchapitrens",2,"knn.md"]
    }
    

    env.variables['devoir_premiere']={
     #   1 : ["projet","Défi Logo Sprint",1,"T08_Extras/5MiniProjet/logo.md"],
      #  2 : ["projet","Dessine ta rue","17/11/2023","T08_Extras/5MiniProjet/dessine_ta_rue.md"]
        #2 : ["python","Les fonction en Python",1,"T06_Python/T6.1_Python/T6_1_2_Les_fonctions_en_Python.md"],
        #3 : ["python","Les Boucles FOR",1,"T06_Python/T6.1_Python/T6_1_3_Boucle_FOR_en_Python.md"],
        #4 : ["typesbase","Représentation des entiers positifs",1,"T01_TypesBase/T1.1_Bases/T1_1_Codage_Entiers.md"],
        #5 : ["typesbase","Représentation des entiers négatifs",1,"T01_TypesBase/T1.2_Relatifs/T1_2_Relatifs.md"],
        #6 : ["typesbase","Représentation des flottants",1,"T01_TypesBase/T1.3_Flottants/T1_3_Flottants.md"],
        #7 : ["python","Les boucles WHILE",1,"T06_Python/T6.1_Python/T6_1_4_WHILE.md"],
        8 : ["devoir","Les portes Logiques",1,"T09_Evaluations/DS_portes_logiques.md"]
        #9 : ["python","Exercices Bilan Python",1,"T06_Python/T6.1_Python/T6_1_6_Exercices_Bilan_Bases.md"]
        #8 : ["web","Le web",2,"leweb.md"],
        #9 : ["algorithmique","Algorithmes de tri",2,"algostri.md"],
        #10 : ["typesbase","Représentation des entiers négatifs",1,"negatifs.md"],
        #11: ["os","Réseau",1,"reseau.md"],
        #12: ["web","Interaction dans une page web",1,"interactionweb.md"],
        #13: ["algorithmique","Algorithmes gloutons",2,"gloutons.md"],
        #14: ["donneestable","Fusion de tables",1,"fusiontable.md"],
        #15: ["os","Interface homme-machine",2,"interface.md"],
        #16: ["typesbase","Notion de nombre flottant",1,"flottant.md"],
        #17: ["algorithmique","Algorithme des k plus proches voisinumchapitrens",2,"knn.md"]
    }
    
    #titre activites 
    @env.macro
    def sc(chaine):
        return f'<span style="font-variant:small-caps;">{chaine}</span>'

    env.variables['devant_act']=':black_small_square:'
    env.variables['num_act']=1
    @env.macro
    def titre_activite(titre,licones,numero=1):
        if numero==0:
            env.variables['num_act']=1
        ligne=f"### {env.variables['devant_act']}   Activité {env.variables['num_act']} "
        if titre!="":
            ligne+=f": *{titre}*"
        if licones!=[]:
            ligne+=f"<span style='float:right;'>"
            for icone in licones:
                ligne+=f"<span style='float:right;'>&thinsp; {env.variables['icones_act'][icone]}</span>"
            ligne+="</span>"
        env.variables['num_act']=env.variables['num_act']+1
        return ligne

    # Titres des items travaillés sur l'année
    @env.macro
    def sec_titre(theme,titre):
            icone = env.variables.icones[theme]
            return f"### {icone} &nbsp; {titre}"
    
    @env.macro
    def cours(fichier):
        ccours = '''
Vous pouvez télécharger une copie au format pdf du diaporama de synthèse de cours présenté en classe :

<span class='centre'>[Diaporama de cours :fontawesome-regular-file-pdf:](../pdf/'''+fichier+'''){.md-button target=_blank}</span>
!!! warning "Attention"
    Ce diaporama ne vous donne que quelques points de repères lors de vos révisions. Il devrait être complété par la relecture attentive de vos **propres** notes de cours et par une révision approfondie des exercices.'''
        return ccours

    @env.macro
    def aff_cours(num):
        fichier=f'../../pdf/C{num}/C{num}-cours.pdf'
        return cours(fichier)

    @env.macro
    def icone(theme):
        return env.variables.icones[theme]
    
    @env.macro
    def titre_chapitre(numero,titre,theme,niveau):
        # Position de l'ancre pour repérage dans la page
        if theme=="projet":
            titre_bis = env.variables['projet_'+niveau][numero][1]
            ligne=f"# <span class='numchapitre'>Mini-Projet {numero} : </span>  {titre_bis} "
            ligne+=f"<span style='float:right;'>{env.variables.icones[theme]}</span>"
        else:
            titre_bis = env.variables['progression_'+niveau][numero][1]
            ligne=f"# <span class='numchapitre'>C{numero}</span> {titre_bis} "
            ligne+=f"<span style='float:right;'>{env.variables.icones[theme]}</span>"
        return ligne

    @env.macro
    def chapitre(num,theme,titre,duree,lien):
        icone = env.variables["icones"][theme]
        return f"|{icone}|[C{num}- {titre}]({lien}) | {duree}\n"

    @env.macro
    def projet_c(num,theme,titre,duree,lien):
        icone = env.variables["icones"][theme]
        return f"|{icone}|[Mini-Projet {num}- {titre}]({lien}) | {duree}\n"      

    @env.macro
    def liens(fichier,type=".pdf"):
        location="./pdf/"+fichier[0:2]+"/"
        return f"[:fontawesome-solid-download:]({location}{fichier}.pdf) [:fontawesome-regular-file:]({location}{fichier}.tex)"

    @env.macro
    def telecharger(description,fichier):
        liens =f"[{description} :material-download:](./{fichier})"
        liens+="{.md-button}"
        return "<span class='centre'>"+liens+"</span>"      
#--------------------------------------------
    @env.macro
    def sec_projet(theme,projet):
            icone = env.variables.icones[theme]
            return f"### {icone} &nbsp; {projet}"

    @env.macro
    def projet_chapitre(numero,projet,theme,niveau):
        # Position de l'ancre pour repérage dans la page
        titre_bis = env.variables['projet_'+niveau][numero][1]
        ligne=f"# <span class='numprojet'>Mini-projet-{numero}</span> {titre_bis} "
        ligne+=f"<span style='float:right;'>{env.variables.icones[theme]}</span>"
        return ligne

    @env.macro
    def affiche_projet(niveau):
        ret='''
| |Mini-Projet        | Pour le  |
|-|-------------|-------|
        '''
        if niveau=="premiere":
            var_projet = env.variables.projet_premiere
        else:
            var_projet = env.variables.projet_terminale
        for k in var_projet:
           ret+=projet_c(k,env.variables['projet_'+niveau][k][0],env.variables['projet_'+niveau][k][1],env.variables['projet_'+niveau][k][2],env.variables['projet_'+niveau][k][3])
        return ret
#--------------------------------------------------------

    @env.macro
    def affiche_progression(niveau):
        ret='''
| |Titre        | Durée |
|-|-------------|-------|
        '''
        if niveau=="premiere":
            var_progression = env.variables.progression_premiere

        else:
            var_progression = env.variables.progression_terminale

        for k in var_progression:
            ret+=chapitre(k,env.variables['progression_'+niveau][k][0],env.variables['progression_'+niveau][k][1],env.variables['progression_'+niveau][k][2],env.variables['progression_'+niveau][k][3])
       
        return ret
    
    @env.macro
    def genere_nav():
        ret='''```\n'''
        for k in env.variables.progression:
            da = env.variables['progression'][k]
            ret+=f'  - "C{k}-{da[1]}" : {da[3]}\n'
        return ret+'```\n'




#------------------DEVOIRS--------------------------
    @env.macro
    def devoir(num,theme,titre,duree,lien):
        icone = env.variables["icones"][theme]
        return f"|{icone}|[DS {num}- {titre}]({lien}) | {duree}\n" 


    @env.macro
    def sec_devoir(theme,devoir):
            icone = env.variables.icones[theme]
            return f"### {icone} &nbsp; {devoir}"

    @env.macro
    def devoir_chapitre(numero,devoir,theme,niveau):
        # Position de l'ancre pour repérage dans la page
        titre_bis = env.variables['devoir_'+niveau][numero][1]
        ligne=f"# <span class='numdevoir'>Devoir-{numero}</span> {titre_bis} "
        ligne+=f"<span style='float:right;'>{env.variables.icones[theme]}</span>"
        return ligne

    @env.macro
    def affiche_devoir(niveau):
        ret='''
| |Devoir       | Le  |
|-|-------------|-------|
        '''
        if niveau=="premiere":
            var_projet = env.variables.devoir_premiere
        else:
            var_projet = env.variables.devoir_terminale
        for k in var_projet:
           ret+=devoir(k,env.variables['devoir_'+niveau][k][0],env.variables['devoir_'+niveau][k][1],env.variables['devoir_'+niveau][k][2],env.variables['devoir_'+niveau][k][3])
        return ret

#--------------------------------------------------------------------------------------        

#---------------- <exo perso>-------------------- 
    with open("qcm.csv","r",encoding="utf-8") as f:
        questions = list(csv.DictReader(f,delimiter=","))
    env.variables['qcm']=questions

    @env.macro
    def affiche_question(num,index):
        lenonce = env.variables.qcm[num]["enonce"]
        # Traitement si enoncé sur plusieurs lignes
        nl = lenonce.find('\n')
        if nl>0:
            lenonce=lenonce.replace("\n",'"\n',1)
            lenonce=lenonce.replace("\n",'\n    ')
        else:
            lenonce+='"'
        # Traitement si image
        limg = env.variables.qcm[num]["image"]
        if limg!='':
            lenonce+=f'\n \t ![illustration](../../images/C{env.variables.qcm[num]["chapitre"]}/{limg})'
            lenonce+='{: .imgcentre}\n'
        modele = f'''
!!! fabquestion "**{index}.** {lenonce}
    === "Réponses"
        - [ ] a) {env.variables.qcm[num]["reponseA"]}
        - [ ] b) {env.variables.qcm[num]["reponseB"]}
        - [ ] c) {env.variables.qcm[num]["reponseC"]}
        - [ ] d) {env.variables.qcm[num]["reponseD"]}
    === "Correction"\n'''
        for rep in "ABCD":
            clerep = "reponse"+rep
            if env.variables.qcm[num]["bonne_reponse"]==rep:
                modele+=f"        - [x] {rep.lower()}) =={env.variables.qcm[num][clerep]}== \n"
            else:
                modele+=f"        - [ ] {rep.lower()}) ~~{env.variables.qcm[num][clerep]}~~ \n"
        return modele

    @env.macro
    def affiche_qcm(liste_question):
        qcm = ""
        for index in range(len(liste_question)):
            qcm+=affiche_question(liste_question[index],index+1)
        return qcm
    
    @env.macro
    def qcm_chapitre(num_chap):
        index=1
        qcmc=""
        for num in range(len(env.variables.qcm)):
            if int(env.variables.qcm[num]["chapitre"])==num_chap:
                qcmc+=affiche_question(num,index)
                index+=1
        return qcmc


#---------------------------------------------- QCM sans réponse ---------------------------

    with open("qcm_devoir.csv","r",encoding="utf-8") as f:
        questions_devoir = list(csv.DictReader(f,delimiter=","))
    env.variables['qcm_devoir']=questions_devoir

    @env.macro
    def affiche_question_devoir(num,index):
        lenonce = env.variables.qcm_devoir[num]["enonce"]
        # Traitement si enoncé sur plusieurs lignes
        nl = lenonce.find('\n')
        if nl>0:
            lenonce=lenonce.replace("\n",'"\n',1)
            lenonce=lenonce.replace("\n",'\n    ')
        else:
            lenonce+='"'
        # Traitement si image
        limg = env.variables.qcm_devoir[num]["image"]
        if limg!='':
            lenonce+=f'\n \t ![illustration](../images/C{env.variables.qcm_devoir[num]["chapitre"]}/{limg})'
            lenonce+='{: .imgcentre}\n'
        modele = f'''
!!! fabquestion "**{index}.** {lenonce}
    - [ ] a) {env.variables.qcm_devoir[num]["reponseA"]}
    - [ ] b) {env.variables.qcm_devoir[num]["reponseB"]}
    - [ ] c) {env.variables.qcm_devoir[num]["reponseC"]}
    - [ ] d) {env.variables.qcm_devoir[num]["reponseD"]}
'''
        return modele

    @env.macro
    def affiche_qcm_devoir(liste_question_devoir):
        qcm_devoir = ""
        for index in range(len(liste_question_devoir)):
            qcm_devoir+=affiche_question_devoir(liste_question_devoir[index],index+1)
        return qcm_devoir
    
    @env.macro
    def qcm_chapitre_devoir(num_chap):
        index=1
        qcmc=""
        for num in range(len(env.variables.qcm_devoir)):
            if int(env.variables.qcm_devoir[num]["chapitre"])==num_chap:
                qcmc+=affiche_question_devoir(num,index)
                index+=1
        return qcmc
#-------------------------------------    

#---------------- <exo perso>-------------------- 
    @env.macro
    def exo(titre,licones,numero=1):
        if numero==0:
            env.variables['num_exo']=1
        ligne=f"### {env.variables['devant_exo']}   Exercice {env.variables['num_exo']} "
        if titre!="":
            ligne+=f": *{titre}*"
        if licones!=[]:
            ligne+=f"<span style='float:right;'>"
            for icone in licones:
                ligne+=f"<span style='float:right;'>&thinsp; {env.variables['icones_exo'][icone]}</span>"
            ligne+="</span>"
        env.variables['num_exo']=env.variables['num_exo']+1
        return ligne

    env.variables['compteur_exo'] = 0
    @env.macro
    def exercice():
        env.variables['compteur_exo'] += 1
        return f"Exercice  { env.variables['compteur_exo']}"

    @env.macro
    def initexo(n):
        env.variables['compteur_exo'] = n
        return ""

    env.variables['compteur_exple'] = 0
    @env.macro
    def exemple():
        env.variables['compteur_exple'] += 1
        return f"Exemple  { env.variables['compteur_exple']}"

    @env.macro
    def initexple(n):
        env.variables['compteur_exple'] = n
        return ""

    @env.macro
    def correction(booleen, texte):
        if booleen == False:
            return ""
        else:
            return texte

    
    @env.macro
    def capytale(id):
        lien = "[![logo capytale](./images/capytale.png){.center width=150px border=2px}]"
        lien +=f"(https://capytale2.ac-paris.fr/web/c/{id})"
        lien += "{target=_blank}"
        return lien

#---------------- </exo perso>-------------------- 
    @env.macro
    def addition(v1, v2) -> str:
        r1='    '
        for v in v1:
            r1+=' '+v
        r2=''
        for v in v2:
            r2+=' '+v

        sum = bin(int(v1, 2) + int(v2, 2)) 
  
        resultat=sum[2:]
        rfin='    '
        for v in resultat:
            rfin+=' '+v
        return f'<center> &emsp;{r1} <br> + &nbsp;{r2} <br> <div class="trait"></div> <br>&emsp; {rfin}</center>'

    @env.macro
    def additionatrou(v1, v2,res) -> str:
        r1='    '
        for v in v1:
            r1+=' '+v
        r2=''
        for v in v2:
            r2+=' '+v

        rfin='    '
        for v in res:
            rfin+=' '+v
        return f'<center> &emsp;{r1} <br> + &nbsp;{r2} <br> <div class="trait"></div> <br>&emsp; {rfin}</center>'
        
#---------------- <PYODIDE>-------------------- 
    @env.macro
    def script(lang: str, nom: str) -> str:
        "Renvoie le script dans une balise bloc avec langage spécifié"
        return f"""```{lang}
--8<---  "docs/""" + os.path.dirname(env.variables.page.url.rstrip('/')) + f"""/{nom}"
```"""
    # f"docs/{os.path.dirname(env.variables.page.url.rstrip('/'))}/scripts/{nom}.py"
    
    @env.macro
    def py(nom: str) -> str:
        "macro python rapide"
        return script('python', "scripts/" + nom + ".py")

    env.variables['term_counter'] = 0
    env.variables['IDE_counter'] = 0

    @env.macro
    def terminal() -> str:
        """   
        Purpose : Create a Python Terminal.
        Methods : Two layers to avoid focusing on the Terminal. 1) Fake Terminal using CSS 2) A click hides the fake 
        terminal and triggers the actual Terminal.
        """        
        tc = env.variables['term_counter']
        env.variables['term_counter'] += 1
        return f"""<div onclick='start_term("id{tc}")' id="fake_id{tc}" class="terminal_f"><label class="terminal"><span>>>> </span></label></div><div id="id{tc}" class="hide"></div>"""

    def read_ext_file(nom_script : str) -> str:
        """
        Purpose : Read a Python file that is uploaded on the server.
        Methods : The content of the file is hidden in the webpage. Replacing \n by a string makes it possible
        to integrate the content in mkdocs admonitions.
        """
        short_path = f"""docs/{os.path.dirname(env.variables.page.url.rstrip('/'))}"""
        try: 
            f = open(f"""{short_path}/scripts/{nom_script}.py""")
            content = ''.join(f.readlines())
            f.close()
            content = content+ "\n"
            # Hack to integrate code lines in admonitions in mkdocs
            return content.replace('\n','backslash_newline')
        except :
            return
        
    def generate_content(nom_script : str) -> str:
        """
        Purpose : Return content and current number IDE {tc}.
        """
        tc = env.variables['IDE_counter']
        env.variables['IDE_counter'] += 1

        content = read_ext_file(nom_script)

        if content is not None :
            return content, tc
        else : return "", tc

    def create_upload_button(tc : str) -> str:
        """
        Purpose : Create upoad button for a IDE number {tc}.
        Methods : Use an HTML input to upload a file from user. The user clicks on the button to fire a JS event
        that triggers the hidden input.
        """
        return f"""<button class="emoji" onclick="document.getElementById('input_editor_{tc}').click()">⤴️</button>\
                <input type="file" id="input_editor_{tc}" name="file" enctype="multipart/form-data" class="hide"/>"""

    def create_unittest_button(tc: str, nom_script: str, mode: str) -> str:
        """
        Purpose : Generate the button for IDE {tc} to perform the unit tests if a valid test_script.py is present.
        Methods : Hide the content in a div that is called in the Javascript
        """
        stripped_nom_script = nom_script.split('/')[-1]
        relative_path = '/'.join(nom_script.split('/')[:-1])
        nom_script = f"{relative_path}/test_{stripped_nom_script}"
        content = read_ext_file(nom_script)
        if content is not None: 
            return f"""<span id="test_term_editor_{tc}" class="hide">{content}</span><button class="emoji_dark" onclick=\'executeTest("{tc}","{mode}")\'>🛂</button><span class="compteur">5/5</span>"""
        else: 
            return ''


    def blank_space() -> str:
        """ 
        Purpose : Return 5em blank spaces. Use to spread the buttons evenly
        """
        return f"""<span style="indent-text:5em"> </span>"""

    @env.macro
    def IDEv(nom_script : str ='') -> str:
        """
        Purpose : Easy macro to generate vertical IDE in Markdown mkdocs.
        Methods : Fire the IDE function with 'v' mode.
        """
        return IDE(nom_script, 'v')


    @env.macro
    def IDE(nom_script : str ='', mode : str = 'h') -> str:
        """
        Purpose : Create a IDE (Editor+Terminal) on a Mkdocs document. {nom_script}.py is loaded on the editor if present. 
        Methods : Two modes are available : vertical or horizontal. Buttons are added through functioncal calls.
        Last span hides the code content of the IDE if loaded.
        """
        content, tc = generate_content(nom_script)
        corr_content, tc = generate_content(f"""{'/'.join(nom_script.split('/')[:-1])}/corr_{nom_script.split('/')[-1]}""")
        div_edit = f'<div class="ide_classe">'
        if mode == 'v':
            div_edit += f'<div class="wrapper"><div class="interior_wrapper"><div id="editor_{tc}"></div></div><div id="term_editor_{tc}" class="term_editor"></div></div>'
        else:
            div_edit += f'<div class="wrapper_h"><div class="line" id="editor_{tc}"></div><div id="term_editor_{tc}" class="term_editor_h terminal_f_h"></div></div>'
        div_edit += f"""<button class="emoji" onclick='interpretACE("editor_{tc}","{mode}")'>▶️</button>"""
        div_edit += f"""{blank_space()}<button class="emoji" onclick=\'download_file("editor_{tc}","{nom_script}")\'>⤵️</button>{blank_space()}"""
        div_edit += create_upload_button(tc)
        div_edit += create_unittest_button(tc, nom_script, mode)
        div_edit += '</div>'

        div_edit += f"""<span id="content_editor_{tc}" class="hide">{content}</span>"""
        div_edit += f"""<span id="corr_content_editor_{tc}" class="hide">{corr_content}</span>"""
        return div_edit

#---------------- </PYODIDE>-------------------- 