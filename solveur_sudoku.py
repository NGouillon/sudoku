# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 13:40:58 2019

@author: Nicolas

"""
import itertools
import copy
from bibli_test_pour_solveur import *

def initialisation_liste_indice_a_tester(grille):
    liste_indice_ou_la_grille_est_vide=[]
    for i, j in itertools.product(range(len(grille)), repeat=2):
            if grille[i][j].count(1)!=1:
                liste_indice_ou_la_grille_est_vide.append([i,j])
    return liste_indice_ou_la_grille_est_vide

def initialisation_valeur_a_tester():
    valeur_a_tester=[]
    for i in range(9):
        valeur_a_tester.append([[1,0,0,0,0,0,0,0,0]]*9)
    return valeur_a_tester

def valeur_possible(grille,indice_case,valeur):
    for indice in indices_ligne(indice_case):
        if grille[indice[0]][indice[1]]== valeur[indice_case[0]][indice_case[1]] and indice!=indice_case:
            return False
    for indice in indices_colonne(indice_case):
        if grille[indice[0]][indice[1]]== valeur[indice_case[0]][indice_case[1]] and indice!=indice_case:
            return False        
    for indice in indices_bloc(indice_case):
        if grille[indice[0]][indice[1]]== valeur[indice_case[0]][indice_case[1]] and indice!=indice_case:
            return False 
    return True

            
def chgt_valeur_test(valeur_a_tester,liste_indice,increment,grille):
    if increment <0:
        return valeur_a_tester, increment,grille
    indice_valeur_a_tester=valeur_a_tester[liste_indice[increment][0]][liste_indice[increment][1]].index(1)
    if indice_valeur_a_tester !=8:
        valeur_a_tester[liste_indice[increment][0]][liste_indice[increment][1]]=[0]*8
        valeur_a_tester[liste_indice[increment][0]][liste_indice[increment][1]].insert(indice_valeur_a_tester+1,1)
        return valeur_a_tester,increment,grille
    else :
        while indice_valeur_a_tester ==8 and increment>=0:
            valeur_a_tester[liste_indice[increment][0]][liste_indice[increment][1]]=[1,0,0,0,0,0,0,0,0]
            grille[liste_indice[increment][0]][liste_indice[increment][1]]=[1]*9
            increment-=1
            indice_valeur_a_tester=valeur_a_tester[liste_indice[increment][0]][liste_indice[increment][1]].index(1)
        return valeur_a_tester,increment,grille
        
    
    

def Resolution(grille,increment,liste_indice,valeur_a_tester):
    if increment >len(liste_indice)-1:
        return grille
    if increment <0:
        return False
    grille[liste_indice[increment][0]][liste_indice[increment][1]]=valeur_a_tester[liste_indice[increment][0]][liste_indice[increment][1]]
    if valeur_possible(grille,liste_indice[increment],valeur_a_tester):
        Resolution(grille, increment+1, liste_indice, valeur_a_tester)
    else :
        chgt_valeur_test(valeur_a_tester, liste_indice, increment,grille)
        Resolution(grille, increment, liste_indice, valeur_a_tester)
        
def solution_grille_recursif(grille):
    liste_indice=initialisation_liste_indice_a_tester(grille)
    valeurs_de_test=initialisation_valeur_a_tester()
    increment=0
    Resolution(grille, increment, liste_indice, valeurs_de_test)


def solution_grille(grille):
    liste_indice=initialisation_liste_indice_a_tester(grille)
    valeurs_a_tester=initialisation_valeur_a_tester()
    increment=0
    while increment<len(liste_indice):
        if increment <0:
            return False
        grille[liste_indice[increment][0]][liste_indice[increment][1]]=valeurs_a_tester[liste_indice[increment][0]][liste_indice[increment][1]]
        if valeur_possible(grille,liste_indice[increment],valeurs_a_tester):
            increment+=1
        else :
            chgt_valeur_test(valeurs_a_tester, liste_indice, increment,grille)     
    return grille
    
def nombre_solution(grille):
    nombre_de_solution=0
    liste_indice=initialisation_liste_indice_a_tester(grille)
    valeurs_a_tester=initialisation_valeur_a_tester()
    increment=0
    while increment<len(liste_indice):
        if increment <0:
            return nombre_de_solution
        grille[liste_indice[increment][0]][liste_indice[increment][1]]=valeurs_a_tester[liste_indice[increment][0]][liste_indice[increment][1]]
        if valeur_possible(grille,liste_indice[increment],valeurs_a_tester):
            increment+=1
        else :
            chgt_valeur_test(valeurs_a_tester, liste_indice, increment,grille)     
        if increment ==len(liste_indice):
            nombre_de_solution+=1
            increment-=1
            chgt_valeur_test(valeurs_a_tester, liste_indice, increment,grille)
            









    
    
    
