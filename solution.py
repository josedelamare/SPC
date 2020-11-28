# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 10:33:11 2020

@author: José
"""

# importing the ExerciseFunction class
from nbautoeval import ExerciseFunction, Args
from nbautoeval import CallRenderer, PPrintRenderer


########## step 1
# You need to define the 'correct' function
# i.e. one that would be accepted as valid for the problem

def avant(ca, va, cb, vb):    
    nbf = 0
    naf = ca*va - cb*vb
    nab = cb*vb
    return (naf, nab, nbf)

def apres(ca, va, cb, vb):    
    nbf = cb*vb - ca*va
    naf = 0
    nab = ca*va
    return (naf, nab, nbf)

def calcul(VE, Ca, Va, Cb, Vb, nbf, naf, nab):
    for volume in Vb:
        if volume < VE:
            n_AH, n_A, n_OH = avant(Ca, Va, Cb, volume)
            nbf.append(n_OH)
            naf.append(n_AH)
            nab.append(n_A)
        else:
            n_AH, n_A, n_OH = apres(Ca, Va, Cb, volume)
            nbf.append(n_OH)
            naf.append(n_AH)
            nab.append(n_A)
    return (nbf, naf, nab)


########## step 2
# You need to provide datasets
# This is expected to be a list of Args instances
# each one describes all the arguments to be passed
# to the function
# in this particular case we define 2 input sets, so
# the correction will have 2 meaningful rows
#
inputs_avant = [
    Args(1, 10, 1, 1),
    Args(1, 10, 1, 5),
    Args(1, 10, 1, 10),
    Args(1, 10, 1, 15),
    Args(1, 10, 1, 20)    
]

inputs_apres = [
    Args(1, 10, 1, 1),
    Args(1, 10, 1, 5),
    Args(1, 10, 1, 10),
    Args(1, 10, 1, 15),
    Args(1, 10, 1, 20)    
]

inputs_calcul = [
    Args(15, 0.015, 0.02, 0.02, [1, 5, 10, 15, 20, 25], [], [], []),
]

########## step 3
# finally we create the exercise object
# NOTE: this is the only name that should be imported from this module
#
exo_avant = ExerciseFunction(
    # first argument is the 'correct' function
    # it is recommended to use the same name as in the notebook, as the
    # python function name is used in HTML rendering 
    avant,
    # the inputs
    inputs_avant,
    result_renderer=PPrintRenderer(width=20),
)

exo_apres = ExerciseFunction(
    # first argument is the 'correct' function
    # it is recommended to use the same name as in the notebook, as the
    # python function name is used in HTML rendering 
    apres,
    # the inputs
    inputs_apres,
    result_renderer=PPrintRenderer(width=20),
)

exo_calcul = ExerciseFunction(
    # first argument is the 'correct' function
    # it is recommended to use the same name as in the notebook, as the
    # python function name is used in HTML rendering 
    calcul,
    # the inputs
    inputs_calcul,
    result_renderer=PPrintRenderer(width=20),
)

def correction_volume_equivalent(V):
    assert type(V) == float, "Il faut exprimer le volume avec 3 chiffres significatifs"
    assert round(V,0) == 15, "Revois ton calcul"
    
    print("Bravo !\n Tous les tests ont réussi.\n Tu as super bien travaillé pour l'instant !")
    
def correction_append(l):
    assert l == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    print("Bravo !\n Tous les tests ont réussi.\n Tu as encore bien travaillé !")
    

