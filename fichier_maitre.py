# -*- coding: utf-8 -*-

"""
Created on Thu Apr 11 13:40:58 2019

@author: Nicolas
"""

import random
from bibli_test_pour_solveur import *#importe tous les fichiers avec leurs noms rÃ©els
from generation_grille import *
from solveur_sudoku import *

#print(indices_bloc([5,8]))
#print(indices_ligne([5,8]))
#print(indices_colonne([5,8]))


#tests
l=[]
for i in range(9):
    nb=[0]*9
    nb[i]=1
    l.append(nb)

ligne_moi=l

#ligne_de_base(l)



print(ligne_moi)

print(" +")  
for i in range(9):
    print(grille_de_reference(ligne_moi)[i])

print(" +")  

grille=grille_de_reference(ligne_moi)

grille_a_resoudre=grille_a_une_solution(grille)


for i in range(9):
    for j in range(9):
        print(transformation_chiffre(grille_a_resoudre[i][j]),end='')
        print("|",end='')
    print()
print(" Stop")  
nb_solution=nb_solution(grille_a_resoudre)
print (nb_solution)

difficulte=difficulte_grille(grille_a_resoudre)
print(difficulte)



grille_a_resoudre=grille_incomplete(grille,55)


for i in range(9):
    for j in range(9):
        print(transformation_chiffre(grille_a_resoudre[i][j]),end='')
        print("|",end='')
    print()
print(" Stop")  
nb_solution=nb_solution(grille_a_resoudre)
print (nb_solution)

if nb_solution==1:
    difficulte=difficulte_grille(grille_a_resoudre)
    print(difficulte)
else:
    print("trop de solution")
    

grille_a_resoudre_melangee=grille_aleatoire(grille_a_resoudre)


for i in range(9):
    for j in range(9):
        print(transformation_chiffre(grille_a_resoudre[i][j]),end='')
        print("|",end='')
    print()
print(" Stop")  
print (nb_solution(grille_a_resoudre))
print(" +")

for i in range(9):
    print(grille_de_reference(ligne_moi)[i])

print(" ")  

grille=grille_de_reference(ligne_moi)


for i in range(9):
    print(grille[i])

print(" ")  


print('oui')
heu=grille[1][1].count(1)
print(grille[1][1])
print(heu)

grille[0][0]=[0,1,1,0,0,0,0,0,0]
grille[0][1]=[1,0,1,0,0,0,0,0,0]
grille[0][2]=[1,1,0,0,0,0,0,0,0]
grille[2][1]=[1]*9


for i in range(9):
    print(grille[i])

print(initialisation_liste_indice_a_tester(grille))



print(triplet_bloc(grille,[1,0]))

exclusion_triplet_bloc(grille,[1,0])



        
for i in range(9):
    for j in range(9):
        print(transformation_chiffre(grille[i][j]))
        

#print(solution_grille(grille))




#print("|| {} | {} | {} || {} | {} | {} || {} | {} | {} ||"
      #.format(*(cell or ' ' for cell in line)))
      #pour imprimer les cases en une sule ligne de commande !