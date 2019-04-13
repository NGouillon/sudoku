# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 12:02:07 2019

@author: Nicolas
"""

import random

def unique_solution(case:list):
    assert case.count(1)==1

def ligne_de_base(ligne_reference:list):
    ligne=random.shuffle(ligne_reference)
    return ligne

def contenu_case(indice,premiere_ligne,grille):
    if unique_solution(grille.index(indice)):
        case=premiere_ligne[indice.index(1)]
    else:
        case=[]
    return case


    
def decalage_ligne(ligne,decalage):
    ligne_decalee=[]
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

def melange_lignes(grille):
    for k in range(3):
        grille[(k%3)*3:(k%3+1)*3]=random.shuffle(grille[(k%3)*3:(k%3+1)*3])
    return grille


def symetrie_grile(grille):
    for i in range(9):
        for j in range(9):
            grille[i,j]=grille[j,i]
    return grille

def melange_colonnes(grille):
    colonnes=symetrie_grille(grille)
    melange_lignes(colonnes)
    grille=symetrie_grille(colonnes)
    return grille

#def melange_bloc(grille):
    #ordre_bloc=random.shuffle([0,1,2])
    #for k in range(3):
        #for i in range(k*3,3*(k%3)):
            
    
        
        
        
#def grille_aleatoire(premiere_ligne):      
    
    
