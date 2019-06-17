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

ligne_moi=ligne_de_base(l)

print(ligne_moi[1])


for i in range(9):
    print(decalage_ligne(ligne_moi,i))

print(" ")

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

grille[0][0]=[1,1,1,1,1,1,1,1,1]
grille[0][1]=[1,1,1,1,1,1,1,1,1]



for i in range(9):
    print(grille[i])

print(initialisation_liste_indice_a_tester(grille))


print(nombre_solution(grille))



#print(solution_grille(grille))




#print("|| {} | {} | {} || {} | {} | {} || {} | {} | {} ||"
      #.format(*(cell or ' ' for cell in line)))
      #pour imprimer les cases en une sule ligne de commande !