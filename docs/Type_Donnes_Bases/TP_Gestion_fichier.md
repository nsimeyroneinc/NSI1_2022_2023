
# Gestion des fichiers textes en Python  

## Ouverture et fermeture d'un fichier 

Pour sauvegarder durablement des données de session et récupérer des données d'une session précédente, les fichiers sont très utiles.

Pour accéder à un fichier, il faut d'abord le localiser. Ce point sera développer dans la partie 4. Pour simplifier, dans cette partie on considèrera que les fichiers à traiter et le script se trouvent dans le même répertoire.

La fonction open sert à ouvrir un fichier en créant une copie de ce fichier au niveau de la mémoire vive ; la copie est à affecter dans une variable.

La fonction open prend deux paramètres, le nom du fichier et le mode d'ouverture :

- 'w' pour le mode écriture (write),  
- 'r' pour le mode lecture(read)  
- et 'a' pour le mode ajout (append).

```python
fichier=open('fichier','w')  # ouverture en mode écriture : le fichier peut être modifié
fic=open('fichier','r') # ouverture en mode lecture du contenu du fichier 
fic=open('fichier','a') # ouverture en mode append : on peut ajouter en fin de fichier des chaînes de cractères.
```

Il faut systématiquement fermer le fichier :

```python
fic.close()
```