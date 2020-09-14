# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 15:22:31 2020

@author: User
"""


import math as m

def f(x):
    return x**3 - 4*x**2 - 4*x + 16


def df(x):
    return 3*x**2 - 8*x -4


def g(x):
    # f(x) = e^(-x) - x
    # x = e^(-x)
    return m.e**(-x)


def newton(f,df,x0,p):
    es = 0.5 *(10**(2-p))
    x = prev_x = x0
    i = 0
    ea = 100
    while ea > es:
        x = x - (f(x)/df(x))
        ea = abs((x-prev_x)/x) * 100
        prev_x = x
        i += 1
        print(x)


def fixedpoint(g,x0,p):
    es = 0.5 *(10**(2-p))
    x = prev_x = x0
    i = 0
    ea = 100
    while ea > es:
        x = g(x)
        ea = abs((x-prev_x)/x) * 100
        prev_x = x
        i += 1
        print(x)


# newton(f,df,4.2,4)
# fixedpoint(g,df,2,4)

    
