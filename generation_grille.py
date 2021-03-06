# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 12:02:07 2019

@author: Nicolas
"""

import random
import copy 
from solveur_sudoku import *

def unique_solution(case:list):
    assert case.count(1)==1
    
    
def contenu_case(indice,premiere_ligne,grille):
    if unique_solution(grille.index(indice)):
        case=premiere_ligne[indice.index(1)]
    else:
        case=[]
    return case

def ligne_de_base(ligne_reference:list):
    random.shuffle(ligne_reference)
    return ligne_reference




    
def decalage_ligne(ligne,decalage):
    ligne_decalee=[]
    for i in range(9):
        ligne_decalee.append([0]*9)
    for i in range(9):
        #decalage=(i//3)+3*(i%3)
        if i+decalage<9:
            ligne_decalee[i]=ligne[i+decalage]
        else :
            ligne_decalee[i]=ligne[i+decalage-9]
    return ligne_decalee

def decalage_colonne(colonne,decalage):
    colonne_decalee=[]
    for i in range(9):
        #decalage=(i//3)+3*(i%3)
        if i+decalage<9:
            colonne_decalee[i]=colonne[i+decalage]
        else :
            colonne_decalee[i]=colonne[i+decalage-9]
    return colonne_decalee       



def grille_de_reference(premiere_ligne):
    grille=[]
    for i in range(9):
        grille.append(decalage_ligne(premiere_ligne,(i%3)*3+(i//3)))
    return grille


def melange_lignes(grille):
    for k in range(3):
        ordre=[0,1,2]
        random.shuffle(ordre)
        ligne1_temp=copy.deepcopy(grille[3*k]) 
        ligne2_temp=copy.deepcopy(grille[3*k+1]) 
        ligne3_temp=copy.deepcopy(grille[3*k+2]) 
        grille[k*3+ordre[0]]=ligne1_temp
        grille[k*3+ordre[1]]=ligne2_temp
        grille[k*3+ordre[2]]=ligne3_temp        
    return grille


def symetrie_grille(grille):
    grille_temp=copy.deepcopy(grille)
    for i in range(9):
        for j in range(9):
            grille[i][j]=grille_temp[j][i]
    return grille

def melange_colonnes(grille):
    colonnes=copy.deepcopy(symetrie_grille(grille))
    melange_lignes(colonnes)
    grille=symetrie_grille(colonnes)
    return grille

def melange_par_bloc_ligne(grille):
    ordre_bloc=[0,1,2]# attention shuffle melange sur place il faut donc donner un nom à la liste
    random.shuffle(ordre_bloc)
    grille_temp=copy.deepcopy(grille)
    for k in range(3):
        grille[(k%3)*3:(k%3+1)*3]=grille_temp[(ordre_bloc[k]%3)*3:(ordre_bloc[k]%3+1)*3]
    return grille

def melange_par_bloc_colonne(grille):
    grille_temp=copy.deepcopy(symetrie_grille(grille))
    melange_par_bloc_ligne(grille_temp)
    grille=symetrie_grille(grille_temp)
    return grille


    
    
def grille_aleatoire(grille):
    grille=melange_lignes(grille)
    grille=melange_colonnes(grille)
    grille=melange_par_bloc_ligne(grille)
    grille=melange_par_bloc_colonne(grille)
    return grille


def transformation_chiffre(liste):
    if liste.count(1)==1:
        return liste.index(1)+1
    else :
        return 0
    
    
def grille_incomplete(grille,nb_trous):
    k=0
    while k < nb_trous:
        i=random.randint(0,8)
        j=random.randint(0,8)
        if grille[i][j]!=[1]*9:
            grille[i][j]=[1]*9
            k+=1
    return grille


def grille_a_une_solution(grille):
    grille_a_trou=grille_incomplete(grille,1)
    while solution_unique(grille_a_trou):
        grille_a_trou=grille_incomplete(grille_a_trou,1)
    return grille_a_trou

    
