
import matplotlib.pyplot as plt
import csv

fichier = open('pokemons.csv', 'r', encoding = 'UTF-8')
t = csv.DictReader(fichier, delimiter=';')
pokemons = [dict(ligne) for ligne in t] # création et construction du tableau par compréhension
fichier.close()
