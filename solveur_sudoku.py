# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 13:40:58 2019

@author: Nicolas

"""
import itertools


def initialisation_valeur_a_tester(grille):
    valeur_a_tester= [[0] *len(grille) for _ in range(len(grille))]
    for i, j in itertools.product(range(len(grille)), repeat=2):
        if grille[i][j].count(1)!=1:
            valeur_a_tester[i][j]=[1,0,0,0,0,0,0,0,0]
    return valeur_a_tester

def initialisation_liste_indice_a_tester(grille):
    liste_indice_trou=[]
    for i, j in itertools.product(range(len(grille)), repeat=2):
            if grille[i][j].count(1)!=1:
                liste_indice_trou.append([i,j])
    return liste_indice_trou


            
def chgt_nombre_utilise(valeur_a_tester,indice_case):
    indice=valeur_a_tester[indice_case].index(1)
    if indice !=len(valeur_a_tester):
        valeur_a_tester[indice_case]=[0]*(len(valeur_a_tester)-1)
        valeur_a_tester[indice_case].append(1,indice+1)
    return valeur_a_tester


    
    
    
