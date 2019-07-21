# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 12:02:07 2019

@author: Nicolas
"""

import csv


def mise_sous_dictionnaire_des_grilles(chemin_fichier):
    toutes_les_grilles=[]
    fichier= open('chemin_fichier','r')
    lecture_du_fichier=csv.DictReader(fichier,delimiter=';')
    for ligne in lecture_du_fichier :
        toutes_les_grilles.append({'numero_grille' : int(row['numero_grille']),
                                   'grille': list(row['grille']), 
                                   'difficulte' : row['difficulte'],
                                   'solution': row['solution']})
    fichier.close()
    return toutes_les_grilles
    
def creation_js(dictionnaire):
    fichier_js = open("les_grilles.js", "w")
    liste_grille=[]
    for i in len(dictionnaire):
        liste_grille.append([dictionnaire])
        
    fichier_js.write(line)
    


