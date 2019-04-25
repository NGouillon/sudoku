# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 13:40:58 2019

@author: Nicolas

"""
import itertools
import copy
from bibli_test_pour_solveur import *

def initialisation_liste_indice_a_tester(grille):
    liste_indice_trou=[]
    for i, j in itertools.product(range(len(grille)), repeat=2):
            if grille[i][j].count(1)!=1:
                liste_indice_trou.append([i,j])
    return liste_indice_trou

def initialisation_valeur_a_tester(grille):
    valeur_a_tester= [[0] *len(grille) for _ in range(len(grille))]
    for i in initialisation_liste_indice_a_tester(grille):
        valeur_a_tester[i][j]=[1,0,0,0,0,0,0,0,0]
    return valeur_a_tester

def valeur_possible(grille,indice_case,valeur):
    for indice in indices_ligne(indice_case):
        if grille[indice]== grille[indice_case] and indice!=indice_case:
            return False
    for indice in indices_colonne(indice_case):
        if grille[indice]== grille[indice_case] and indice!=indice_case:
            return False        
    for indice in indices_bloc(indice_case):
        if grille[indice]== grille[indice_case] and indice!=indice_case:
            return False 
    return True

            
def chgt_valeur_test(valeur_a_tester,liste_indice,increment,grille):
    if increment <0:
        return valeur_a_tester, increment,grille
    indice=valeur_a_tester[liste_indice[increment]].index(1)
    if indice !=8:
        valeur_a_tester[liste_indice[increment]]=[0]*7
        valeur_a_tester[liste_indice[increment]].append(1,indice+1)
        return valeur_a_tester,increment,grille
    else :
        valeur_a_tester[liste_indice[increment]]=[1,0,0,0,0,0,0,0,0]
        grille[liste_indice[increment]]=[0]*9
        chgt_valeur_test(valeur_a_tester,liste_indice, increment-1)
    
    

def Resolution(grille,increment,liste_indice,valeur_a_tester):
    grille_test=copy.deepcopy(grille)
    if increment >len(liste_indice):
        return grille
    if increment <0:
        return False
    grille_test[liste_indice[increment]]=valeur_a_tester[liste_indice[increment]]
    if valeur_possible(grille_test,liste_indice[increment],valeur_a_tester[increment]):
        Resolution(grille_test, increment+1, liste_indice, valeur_a_tester)
    else :
        chgt_valeur_test(valeur_a_tester, liste_indice, increment,grille_test)
        Resolution(grille_test, increment, liste_indice, valeur_a_tester)
        
def solution_grille(grille):
    valeurs_de_test=initialisation_valeur_a_tester(grille)
    liste_indice=initialisation_liste_indice_a_tester(grille)
    increment=0
    Resolution(grille, increment, liste_indice, valeurs_de_test)
        
    
    




    
    
    
