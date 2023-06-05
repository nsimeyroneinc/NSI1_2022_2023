def creation_alphabet():
    alpha=[]
    for i in range(26):
        alpha.append(chr(65+i))
    return alpha

def creation_crypto(alphabet):
    import random
    random.shuffle(alphabet)
    return alphabet

def dico_crypto():
    import copy
    alpha=creation_alphabet()
    copie_alpha = copy.deepcopy(alpha)
    crypto=creation_crypto(alpha)
    dico_crypto=dict(zip(copie_alpha,crypto))
    return dico_crypto

def CryptoLettre(Lettre,Dico):
    Lettre=Lettre.upper()
    return Dico[Lettre]

def CryptoTexte(Texte,Dico):
    Texte=Texte.upper()
    T=""
    for Lettre in Texte:
        if Lettre==" ":
            T+=" "
        elif Lettre==",":
            T+=","
        elif Lettre==".":
            T+="."
        else:
            T+=CryptoLettre(Lettre,Dico)
    return T

def DecrypteTexte(Texte,Dico):
    T=""
    for Lettre in Texte:
        if Lettre==" ":
            T+=" "
        elif Lettre==",":
            T+=","
        else:
            for Lorigine,Lcrypte in Dico.items():
                if Lettre==Lcrypte:
                    T+=Lorigine
    return T

def Occurrence(Texte):
    Texte=Texte.upper()
    Dico={}
    for lettre in Texte:
        if lettre != ' ' and lettre !=',' and lettre != '.':
            if lettre in Dico:
                Dico[lettre]+=1
            else:
                Dico[lettre]=1
    print(Dico)

    return Dico

def Max(Dico):
    maxi=-1
    for cle,val in Dico.items():
        if val>maxi:
            maxi=val
            Lettre=cle
    return Lettre

def propose(Texte):
    F={'A':8.15,'B':0.97,'C':3.15,'D':3.73,'E':17.39,'F':1.12,'G':0.97,'H':0.85,'I':7.31,'J':0.45,'K':0.02,'L':5.69,'M':2.87,'N':7.12,'O':5.28,'P':2.80,'Q':1.21,'R':6.64,'S':8.14,'T':7.22,'U':6.38,'V':1.64,'W':0.03,'X':0.41,'Y':0.28,'Z':0.15}
    occ=Occurrence(Texte)
    Dico={}
    mini=min(len(F),len(occ))
    for i in range(mini):
        LettreTexte=Max(occ)
        LettreFranc=Max(F)
        Dico[LettreFranc]=LettreTexte
        occ[LettreTexte]=-1
        F[LettreFranc]=-1
    t=DecrypteTexte(Texte,Dico)

    return Dico

crypto={'A': 'X', 'B': 'K', 'C': 'O', 'D': 'Y', 'E': 'D', 'F': 'F', 'G': 'I', 'H': 'M', 'I': 'L', 'J': 'H', 'K': 'Z', 'L': 'G', 'M': 'B', 'N': 'C', 'O': 'U', 'P': 'T', 'Q': 'V', 'R': 'P', 'S': 'E', 'T': 'J', 'U': 'W', 'V': 'S', 'W': 'A', 'X': 'R', 'Y': 'N', 'Z': 'Q'}

textedepart="On ne connaissait a Phileas Fogg ni femme ni enfants, ce qui peut arriver aux gens les plus honnetes, ni parents ni amis, ce qui est plus rare en verite. Phileas Fogg vivait seul dans sa maison de Saville row, o u personne ne penetrait. De son interieur, jamais il n etait question. Un seul domestique suffisait a le servir. Dejeunant, dinant au club a des heures chronometriquement determinees, dans la meme salle, a la meme table, ne traitant point ses collegues, n invitant aucun etranger, il ne rentrait chez lui que pour se coucher, a minuit precis, sans jamais user de ces chambres confortables que le Reform Club tient a la disposition des membres du cercle. Sur vingt quatre heures, il en passait dix a son domicile, soit qu il dormit, soit qu il s occupat de sa toilette. S il se promenait, c etait invariablement, d un pas egal, dans la salle d entree parquetee en marqueterie, ou sur la galerie circulaire, au dessus de laquelle s arrondit un dome a vitraux bleus, que supportent vingt colonnes ioniques en porphyre rouge. S il dinait ou dejeunait, c etaient les cuisines, le garde manger, l office, la poissonnerie, la laiterie du club, qui fournissaient a sa table leurs succulentes reserves , c etaient les domestiques du club, graves personnages en habit noir, chausses de souliers a semelles de molleton, qui le servaient dans une porcelaine speciale et sur un admirable linge en toile de Saxe , c etaient les cristaux a moule perdu du club qui contenaient son sherry, son porto ou son claret melange de cannelle, de capillaire et de cinnamome , c etait enfin la glace du club    glace venue a grands frais des lacs d Amerique    qui entretenait ses boissons dans un satisfaisant etat de fraicheur."  

textefin=CryptoTexte(textedepart,crypto)

print(textefin)

D=propose(textefin)
print(D)

texteorigine=DecrypteTexte(textefin,crypto)

print(texteorigine)

