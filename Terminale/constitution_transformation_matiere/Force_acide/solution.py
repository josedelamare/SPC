# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 10:33:11 2020

@author: José
"""

# importing the ExerciseFunction class
from nbautoeval import ExerciseFunction, Args
from nbautoeval import CallRenderer, PPrintRenderer
from math import sqrt
from math import log10


########## step 1
# You need to define the 'correct' function
# i.e. one that would be accepted as valid for the problem

def resolution(a, b, c):
    """fonction qui résoud une équation de la forme ax² + bx + c = 0"""

    # calcul du discriminant
    delta = b**2 - 4*a*c
    solution = (-b + sqrt(delta))/(2*a)
    return solution


########## step 2
# You need to provide datasets
# This is expected to be a list of Args instances
# each one describes all the arguments to be passed
# to the function
# in this particular case we define 2 input sets, so
# the correction will have 2 meaningful rows
#
inputs_resolution = [
    Args(2, -3, 1),
    Args(2, -1, -6),
    Args(4, 19, -5),
    Args(1e-2, 1e-4, -1e-4)
]


########## step 3
# finally we create the exercise object
# NOTE: this is the only name that should be imported from this module
#
exo_resolution = ExerciseFunction(
    # first argument is the 'correct' function
    # it is recommended to use the same name as in the notebook, as the
    # python function name is used in HTML rendering 
    resolution,
    # the inputs
    inputs_resolution,
    result_renderer=PPrintRenderer(width=20),
)


def correction_KA(KA, pKA):
    assert KA == 10**(-pKA), "N'oublie pas que la relation est pKA = -log(KA).\n La puissance s'exprime par ** (x² s'exprime en python x**2)"
    
    print("Bravo !\n Tous les tests ont réussi.\n Tu as super bien travaillé pour l'instant !")
    

