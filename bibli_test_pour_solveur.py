# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 13:40:58 2019

@author: Nicolas
"""

def impossibilite_ligne(grille,indice_case):
    if grille[indice_case].count(1)==1:
        for i in range(9):
            if grille[indice_case[0]][i].count(1)!=1:
                grille[indice_case[0]][i][grille[indice_case].index(1)]=0
    return grille


def impossibilite_colonne(grille,indice_case):
    if grille[indice_case].count(1)==1:
        for i in range(9):
            if grille[indice_case[0]][i].count(1)!=1:
                grille[i][indice_case[1]][grille[indice_case].index(1)]=0
    return grille
 
def indices_bloc(indice_case:list):
    indices_du_bloc=[]
    ligne=indice_case[0]//3
    colonne=indice_case[1]//3
    for i in range(3*ligne,3*ligne+3):
        for j in range(3*colonne, 3*colonne+3):
            indices_du_bloc.append([i,j])
    return indices_du_bloc

def indices_ligne(indice_case):
    indices_de_la_ligne=[]
    for i in range(9):
        indices_de_la_ligne.append([indice_case[0],i])
    return indices_de_la_ligne

def indices_colonne(indice_case:list):
    indices_de_la_colonne=[]
    for i in range(9):
        indices_de_la_colonne.append([i,indice_case[1]])
    return indices_de_la_colonne

