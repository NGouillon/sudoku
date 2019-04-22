# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 13:40:58 2019

@author: Nicolas
"""
def case_init(taille):
    liste=[]
    for i in range(taille):
        liste.append(1)
    return liste

def exclusion_ligne(grille,indice_case):
    if grille[indice_case].count(1)==1:
        for i in range(9):
            if grille[indice_case[0]][i].count(1)!=1:
                grille[indice_case[0]][i][grille[indice_case].index(1)]=0
    return grille


def exclusion_colonne(grille,indice_case):
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

def exclusion_bloc(grille, indice_case):
    if grille[indice_case].count(1)==1:
        for indice in indices_bloc(indice_case):
            if grille[indice].count(1)!=1:
                grille[indice][grille[indice_case].index(1)]=0
    return grille

def nb_cases_remplies(grille):
    nb=0
    for i in range(9):
        for j in range(9):
            if grille[i][j].count(1)==1:
                nb+=1
    return nb

def nb_possibilite_identique(grille,indice_case):
    nb=0
    for indice in indices_ligne:
        if grille[indice_case]==grille[indice]:
            nb+=1
    return nb
    

def exclusion_par_paire(grille):
    for i in range(9):
        for j in range(9):
            if grille[i][j].count(1)==2:
                for indice in indices_ligne([i,j]):
                    if indice != [i,j] and grille[i][j]==grille[indice]:
                        paire=[]
                        for k in range(9):
                            if grille[i][j][k]!=0:
                                paire.append(k)
                        for indice2 in indices_ligne(indice):
                            if indice2!=indice and indice2!= [i,j]:
                                grille[indice][paire[0]]=0
                                grille[indice][paire[1]]=0
                for indice in indices_colonne([i,j]):
                    if indice != [i,j] and grille[i][j]==grille[indice]:
                        paire=[]
                        for k in range(9):
                            if grille[i][j][k]!=0:
                                paire.append(k)
                        for indice2 in indices_colonne(indice):
                            if indice2!=indice and indice2!= [i,j]:
                                grille[indice][paire[0]]=0
                                grille[indice][paire[1]]=0
                for indice in indices_bloc([i,j]):
                    if indice != [i,j] and grille[i][j]==grille[indice]:
                        paire=[]
                        for k in range(9):
                            if grille[i][j][k]!=0:
                                paire.append(k)
                        for indice2 in indices_bloc(indice):
                            if indice2!=indice and indice2!= [i,j]:
                                grille[indice][paire[0]]=0
                                grille[indice][paire[1]]=0
    return grille


def exclusion_333(grille):
    
