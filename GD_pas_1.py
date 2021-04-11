# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 20:11:31 2021

@author: Desktop-sabir
"""

import numpy as np

def gradient_descent(x,y):
    w = np.array([4,4,4,4,4])
    bias = 0
    iterations = 120000

    n = len(x)
    alpha = 0.001
   
    for i in range(iterations):
        y_calculer = w * x + bias
        fonction_Erreur = (1/2*n) * sum([val**2 for val in (y-y_calculer)])
        G_w = (1/n)*sum(x*(y_calculer-y))
        G_bias = (1/n)*sum(y_calculer-y)
        w = w - alpha * G_w
        bias = bias - alpha * G_bias
        print ("w {}, bias {}, fonction_Erreur {} iteration {} y_cal {}".format(w,bias,fonction_Erreur, i,y_calculer))


x = np.array([1,2,3,4,5])

y = np.array([5,7,9,11,13])
 
gradient_descent(x,y)
