# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 15:22:31 2020

@author: User
"""


import math as m

def f(x):
<<<<<<< HEAD
    # sin(2pix) +e^(1.2x) +x -2.5
    # x**3 - 4*x**2 - 4*x + 16
    return m.sin(2*m.pi*x) + m.e**(1.2*x) + x - 2.5


def df(x):
    # 3*x**2 - 8*x -4
=======
    # task1 x**3 - 4*x**2 - 4*x + 16
    # task2 x**2 - 2*x -3
    # task2 m.e**(-x) - x
    # task2 m.sin(2*m.pi*x) + m.e**(1.2*x) + x - 2.5
    return  m.sin(2*m.pi*x) + m.e**(1.2*x) + x - 2.5

def df(x):
    # 1.2*m.e**(1.2*x) + 2*m.pi*m.cos(2*m.pi*x)+1

    # task1 3*x**2 - 8*x -4
    # task2 2*(x-1)
    # task2 -1 * m.e**(-x) - 1
    # task2 1.2*m.e**(1.2*x) + 2*m.pi*m.cos(2*m.pi*x)+1
>>>>>>> a2effb9f739aa8c075c895aac4bb3164477b2c92
    return 1.2*m.e**(1.2*x) + 2*m.pi*m.cos(2*m.pi*x)+1


def g(x):
    # f(x) = e^(-x) - x
    # x = e^(-x)
    # m.sin(m.sqrt(x))
    # 2.5 - m.sin(2*m.pi) + m.e**(1.2*x)
<<<<<<< HEAD
    return 2.5 - m.sin(2*m.pi) - m.e**(1.2*x)

=======
    # m.sqrt(2*x+3)
    # m.e**(-x)
    return 2.5 - m.sin(2*m.pi) - m.e**(1.2*x)
>>>>>>> a2effb9f739aa8c075c895aac4bb3164477b2c92

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


newton(f,df,0,4)
# fixedpoint(g,0,4)


    
