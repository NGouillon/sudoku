# -*- coding: utf-8 -*-

"""
Created on Thu Apr 11 13:40:58 2019

@author: Nicolas
"""

import random
from bibli_test_pour_solveur import *#importe tous les fichiers avec leurs noms rÃ©els
from generation_grille import *


#print(indices_bloc([5,8]))
#print(indices_ligne([5,8]))
#print(indices_colonne([5,8]))
l=[1,2,3,4,5,6,7,8,9]
ligne_moi=ligne_de_base(l)

grille=grille_de_reference(ligne_moi)

print (grille)

print(grille_aleatoire(grille))
