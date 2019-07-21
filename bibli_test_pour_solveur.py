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
    if grille[indice_case[0]][indice_case[1]].count(1)==1:
        for i in range(9):
            if grille[indice_case[0]][i].count(1)!=1:
                grille[indice_case[0]][i][grille[indice_case[0]][indice_case[1]].index(1)]=0
    return grille


def exclusion_colonne(grille,indice_case):
    if grille[indice_case[0]][indice_case[1]].count(1)==1:
        for i in range(9):
            if grille[i][indice_case[1]].count(1)!=1:
                grille[i][indice_case[1]][grille[indice_case[0]][indice_case[1]].index(1)]=0
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
    if grille[indice_case[0]][indice_case[1]].count(1)==1:
        for indice in indices_bloc(indice_case):
            if grille[indice[0]][indice[1]].count(1)!=1:
                grille[indice[0]][indice[1]][grille[indice_case[0]][indice_case[1]].index(1)]=0
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
    for indice in indices_ligne(indice_case):
        if grille[indice_case[0]][indice_case[1]]==grille[indice[0]][indice[1]]:
            nb+=1
    return nb
    

def exclusion_par_paire(grille):
    for i in range(9):
        for j in range(9):
            if grille[i][j].count(1)==2:
                for indice in indices_ligne([i,j]):
                    if indice != [i,j] and grille[i][j]==grille[indice[0]][indice[1]]:
                        paire=[]
                        for k in range(9):
                            if grille[i][j][k]!=0:
                                paire.append(k)
                        for indice2 in indices_ligne(indice):
                            if indice2!=indice and indice2!= [i,j]:
                                grille[indice2[0]][indice2[1]][paire[0]]=0
                                grille[indice2[0]][indice2[1]][paire[1]]=0
                for indice in indices_colonne([i,j]):
                    if indice != [i,j] and grille[i][j]==grille[indice[0]][indice[1]]:
                        paire=[]
                        for k in range(9):
                            if grille[i][j][k]!=0:
                                paire.append(k)
                        for indice2 in indices_colonne(indice):
                            if indice2!=indice and indice2!= [i,j]:
                                grille[indice2[0]][indice2[1]][paire[0]]=0
                                grille[indice2[0]][indice2[1]][paire[1]]=0
                for indice in indices_bloc([i,j]):
                    if indice != [i,j] and grille[i][j]==grille[indice[0]][indice[1]]:
                        paire=[]
                        for k in range(9):
                            if grille[i][j][k]!=0:
                                paire.append(k)
                        for indice2 in indices_bloc(indice):
                            if indice2!=indice and indice2!= [i,j]:
                                grille[indice2[0]][indice2[1]][paire[0]]=0
                                grille[indice2[0]][indice2[1]][paire[1]]=0
    return grille

def intersection_non_vide(ensemble1,ensemble2):
    for element in ensemble1:
        if element in ensemble2:
            return True
    return False

def valeurs_possibles(indice,grille):
    valeurs_possibles_indice=[]
    for i in range(9):
        if grille[indice[0]][indice[1]][i]==1:
            valeurs_possibles_indice.append(i)
    return valeurs_possibles_indice


    
    
    
def triplet_ligne(grille,indice_case):
    liste_indices_triplet=[]
    liste_indice_max3=[]
    for indice in indices_ligne(indice_case):
        if grille[indice[0]][indice[1]].count(1)==2  or  grille[indice[0]][indice[1]].count(1)==3:
            liste_indice_max3.append(indice)     
    for i in range(len(liste_indice_max3)-2):
        for j in range(i+1,len(liste_indice_max3)-1) :
                if intersection_non_vide(valeurs_possibles(liste_indice_max3[i],grille),valeurs_possibles(liste_indice_max3[i],grille)):
                    for k in range(j+1,len(liste_indice_max3)):
                        if intersection_non_vide(valeurs_possibles(liste_indice_max3[k],grille),valeurs_possibles(liste_indice_max3[i],grille)) and intersection_non_vide(valeurs_possibles(liste_indice_max3[k],grille),valeurs_possibles(liste_indice_max3[j],grille)):
                            liste_indices_triplet.append([liste_indice_max3[i],liste_indice_max3[j],liste_indice_max3[k]])
    return liste_indices_triplet

def union_valeurs_possibles(indice1,indice2,indice3,grille):
    union_des_valeurs_possibles=[]
    for i in range(9):
        if grille[indice1[0]][indice1[1]][i]!=0 or grille[indice2[0]][indice2[1]][i]!=0 or grille[indice3[0]][indice3[1]][i]!=0:
            union_des_valeurs_possibles.append(i)
    return union_des_valeurs_possibles

def exclusion_triplet_ligne(grille,indice_case):
    for i in len(triplet_ligne(grille,indice_case)):
        for indice in indices_ligne(triplet_ligne(grille,indice_case)[i][0]):
            if indice!=triplet_ligne(grille,indice_case)[i][0] and indice!=triplet_ligne(grille,indice_case)[i][1] and indice!=triplet_ligne(grille,indice_case)[i][2]:
                for valeur in union_valeurs_possibles(triplet_ligne(grille,indice_case)[i][0],triplet_ligne(grille,indice_case)[i][1],triplet_ligne(grille,indice_case)[i][2],grille):
                    grille[indice[0]][indice[1]][valeur]=0
    return grille

def triplet_colonne(grille,indice_case):
    liste_indices_triplet=[]
    liste_indice_max3=[]
    for indice in indices_colonne(indice_case):
        if grille[indice[0]][indice[1]].count(1)==2  or  grille[indice[0]][indice[1]].count(1)==3:
            liste_indice_max3.append(indice)     
    for i in range(len(liste_indice_max3)-2):
        for j in range(i+1,len(liste_indice_max3)-1) :
                if intersection_non_vide(valeurs_possibles(liste_indices_triplet[i],grille),valeurs_possibles(liste_indices_triplet[j],grille)) :
                    for k in range(j+1,len(liste_indice_max3)):
                        if intersection_non_vide(valeurs_possibles(liste_indices_triplet[k],grille),valeurs_possibles(liste_indices_triplet[i],grille)) and intersection_non_vide(valeurs_possibles(liste_indices_triplet[k],grille),valeurs_possibles(liste_indices_triplet[j],grille)):
                            liste_indices_triplet.append([indice1,indice2,indice3])
    return liste_indices_triplet


def exclusion_triplet_colonne(grille,indice_case):
    if len(triplet_colonne(grille,indice_case))!=0:
        for i in range(len(triplet_colonne(grille,indice_case))):
            for indice in indices_colonne(indice_case):
                if indice!=triplet_colonne(grille,indice_case)[i][0] and indice!=triplet_colonne(grille,indice_case)[i][1] and indice!=triplet_colonne(grille,indice_case)[i][2]:
                    for valeur in union_valeurs_possibles(triplet_colonne(grille,indice_case)[i][0],triplet_colonne(grille,indice_case)[i][1],triplet_colonne(grille,indice_case)[i][2],grille):
                        grille[indice[0]][indice[1]][valeur]=0
    return grille


def triplet_bloc(grille,indice_case):
    liste_indices_triplet=[]
    liste_indice_max3=[]
    for indice in indices_bloc(indice_case):
        if grille[indice[0]][indice[1]].count(1)==2  or  grille[indice[0]][indice[1]].count(1)==3:
            liste_indice_max3.append(indice)  
    if len(liste_indice_max3)>=3:
        for i in range(len(liste_indice_max3)-2):
            for j in range(i+1,len(liste_indice_max3)-1):
                    if intersection_non_vide(valeurs_possibles(liste_indice_max3[i],grille),valeurs_possibles(liste_indice_max3[j],grille)):
                        for k in range(j+1,len(liste_indice_max3)):
                            if intersection_non_vide(valeurs_possibles(liste_indice_max3[k],grille),valeurs_possibles(liste_indice_max3[i],grille)) and intersection_non_vide(valeurs_possibles(liste_indice_max3[k],grille),valeurs_possibles(liste_indice_max3[j],grille)):
                                    liste_indices_triplet.append([liste_indice_max3[i],liste_indice_max3[j],liste_indice_max3[k]])
    return liste_indices_triplet


def exclusion_triplet_bloc(grille,indice_case):
    if len(triplet_bloc(grille,indice_case))!=0:
        for i in range(len(triplet_bloc(grille,indice_case))):
            for indice in indices_bloc(indice_case):
                if indice!=triplet_bloc(grille,indice_case)[i][0] and indice!=triplet_bloc(grille,indice_case)[i][1] and indice!=triplet_bloc(grille,indice_case)[i][2]:
                    for valeur in union_valeurs_possibles(triplet_bloc(grille,indice_case)[i][0],triplet_bloc(grille,indice_case)[i][1],triplet_bloc(grille,indice_case)[i][2],grille):
                        grille[indice[0]][indice[1]][valeur]=0
    return grille  

def paire_associee_colonne(grille,nombre):# pas sur que cela marche
    combien_de_fois_ce_nombre=[0]*9
    colonne_contenant_deux_occurences=[]
    for colonne in range(9):
        for ligne in range(9):   
            if grille[ligne][colonne][nombre]==1:
                combien_de_fois_cenombre[nombre]+=1
                if combien_de_fois_ce_nombre[nombre]==2:
                    colonne_contenant_deux_occurences.append(colonne)
                if combien_de_fois_ce_nombre[nombre]>2:
                    colonne_contenant_deux_occurences.remove(colonne)
    if len(colonne_contenant_deux_occurences)==2:
        liste_indice_case=[]
        for ligne in range(9):
            if grille[ligne][colonne_contenant_deux_occurences[0]][nombre]==1 :
                liste_indice_case.append(ligne,colonne_contenant_deux_occurences[0])
        for ligne in range(9):
            if grille[ligne][colonne_contenant_deux_occurences[1]][nombre]==1 :
                liste_indice_case.append(ligne,colonne_contenant_deux_occurences[1])    
        if (colonne_contenant_deux_occurences[0]%3)==(colonne_contenant_deux_occurences[1]%3): #même bloc
            if indices_bloc(liste_indice_case[0])==indices_bloc(liste_indice_case[2]) and indices_bloc(liste_indice_case[1])==indices_bloc(liste_indice_case[3]):
                for indice in indices_bloc(liste_indice_case[0]):
                    if indice!= liste_indice_case[0] and indice!= liste_indice_case[2]:
                        grille[indice[0]][indice[1]][nombre]=0
                for indice in indices_bloc(liste_indice_case[1]):
                    if indice!= liste_indice_case[1] and indice!= liste_indice_case[3]:
                        grille[indice[0]][indice[1]][nombre]=0   
        else : #pas les mêmes blocs 
            if liste_indice_case[0][0]==liste_indice_case[2][0] and liste_indice_case[1][0]==liste_indice_case[3][0]:#mêmes lignes
                for indice in indices_ligne(liste_indice_case[0]):
                    if indice!= liste_indice_case[0] and indice!= liste_indice_case[2]:
                        grille[indice[0]][indice[1]][nombre]=0
                for indice in indices_ligne(liste_indice_case[1]):
                    if indice!= liste_indice_case[1] and indice!= liste_indice_case[3]:
                        grille[indice[0]][indice[1]][nombre]=0    
    return grille

def paire_associee_ligne_bloc(grille,nombre):
    combien_de_fois_ce_nombre=[0]*9
    ligne_contenant_deux_occurences=[]
    for ligne in range(9):
        for colonne in range(9):   
            if grille[ligne][colonne][nombre]==1:
                combien_de_fois_cenombre[nombre]+=1
                if combien_de_fois_ce_nombre[nombre]==2:
                    ligne_contenant_deux_occurences.append(ligne)
                if combien_de_fois_ce_nombre[nombre]>2:
                    ligne_contenant_deux_occurences.remove(ligne)
    if len(ligne_contenant_deux_occurences)==2:
        liste_indice_case=[]
        for colonne in range(9):
            if grille[ligne_contenant_deux_occurences[0]][colonne][nombre]==1 :
                liste_indice_case.append(ligne_contenant_deux_occurences[0],colonne)
        for colonne in range(9):
            if grille[ligne_contenant_deux_occurences[1]][colonne][nombre]==1 :
                liste_indice_case.append(ligne_contenant_deux_occurences[1],colonne)    
        if (ligne_contenant_deux_occurences[0]%3)==(ligne_contenant_deux_occurences[1]%3): #même bloc
            if indices_bloc(liste_indice_case[0])==indices_bloc(liste_indice_case[2]) and indices_bloc(liste_indice_case[1])==indices_bloc(liste_indice_case[3]):
                for indice in indices_bloc(liste_indice_case[0]):
                    if indice!= liste_indice_case[0] and indice!= liste_indice_case[2]:
                        grille[indice[0]][indice[1]][nombre]=0
                for indice in indices_bloc(liste_indice_case[1]):
                    if indice!= liste_indice_case[1] and indice!= liste_indice_case[3]:
                        grille[indice[0]][indice[1]][nombre]=0     
    return grille
            
    
def difficulte_grille_exclusion(grille,difficulte):
    difficulte_a_ajouter=1
    nb_cases_a_trouver=81- nb_cases_remplies(grille)
    nouvelle_difficulte_a_ajouter=0
    while difficulte_a_ajouter!=nouvelle_difficulte_a_ajouter:
        difficulte_a_ajouter=nouvelle_difficulte_a_ajouter
        for i in range(9):
            for j in range(9):
                exclusion_bloc(grille,[i,j])
                exclusion_colonne(grille,[i,j])
                exclusion_ligne(grille, [i,j])
        nouvelle_difficulte_a_ajouter+=nb_cases_a_trouver-(81-nb_cases_remplies(grille))
        nb_cases_a_trouver=81-nb_cases_remplies(grille)
    return difficulte+difficulte_a_ajouter
    
def difficulte_grille_exclusion_par_paire(grille,difficulte):
    difficulte_a_ajouter=1
    nb_cases_a_trouver=81- nb_cases_remplies(grille)
    nouvelle_difficulte_a_ajouter=0
    while difficulte_a_ajouter!=nouvelle_difficulte_a_ajouter:
        difficulte_a_ajouter=nouvelle_difficulte_a_ajouter
        exclusion_par_paire(grille)
        nouvelle_difficulte_a_ajouter+=(nb_cases_a_trouver-(81-nb_cases_remplies(grille)))*3
    return difficulte+difficulte_a_ajouter

def difficulte_grille_exclusion_par_triplet(grille,difficulte):
    difficulte_a_ajouter=1
    nb_cases_a_trouver=81- nb_cases_remplies(grille)
    nouvelle_difficulte_a_ajouter=0
    while difficulte_a_ajouter!=nouvelle_difficulte_a_ajouter:
        difficulte_a_ajouter=nouvelle_difficulte_a_ajouter
        for i in range(9):
            for j in range(9):
                exclusion_triplet_bloc(grille, [i,j])
                exclusion_triplet_colonne(grille, [i,j])
                exclusion_triplet_ligne(grille, [i,j])
                nouvelle_difficulte_a_ajouter+=(nb_cases_a_trouver-(81-nb_cases_remplies(grille)))*7
    return difficulte+difficulte_a_ajouter
def difficulte_grille(grille):
    difficulte=-1
    nouvelle_difficulte=0
    while nb_cases_remplies(grille)!=81:
        difficulte=nouvelle_difficulte
        nouvelle_difficulte+=difficulte_grille_exclusion(grille,difficulte)
        if nouvelle_difficulte== difficulte:
            nouvelle_difficulte+=difficulte_grille_exclusion_par_paire(grille, nouvelle_difficulte)
            if nouvelle_difficulte==difficulte:
                nouvelle_difficulte+=difficulte_grille_exclusion_par_triplet(grille, nouvelle_difficulte)
        difficulte=nouvelle_difficulte
    return difficulte


        