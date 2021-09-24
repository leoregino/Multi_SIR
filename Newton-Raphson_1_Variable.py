# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 07:45:43 2021

@author: Leonardo
"""

import numpy as np 


def Newton_Raphson(x_0, f, df, tolerance):
    if abs(f(x_0)) < tolerance :
        return x_0
    else :
        return Newton_Raphson(x_0 - f(x_0)/df(x_0),f,df,tolerance)


tolerance = 1e-6
x_0 = 1.5
f = lambda x : x**2 - 2
f_prime = lambda x : 2*x

estimate = Newton_Raphson(x_0, f, f_prime, tolerance)
print("Newton-Raphson root = ", estimate)
print("sqrt(2) = " , np.sqrt(2))