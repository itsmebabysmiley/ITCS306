# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 13:10:23 2020

@author: -

"""
import numpy
def f(x):
    # (-1)*(x**2)+(3*x)+2
    # task1 x*(1-x)*numpy.e**x
    # x**5 - 3*x**4 + 5
    # x**2 / 10 - (2*numpy.sin(x))
    return x**5 - 3*x**4 + 5

# Task1 find maximum
def max_interval(f,a,b,p):
    ep = 0.1
    ea = 100
    es = 0.5 * 10**(2-p)
    px = b
    while ea > es:
        l = (a+b)/2 - ep/2
        u = (a+b)/2 + ep/2
        if f(l) > f(u):
            b = u
        else:
            a = l
        xmax = (a+b)/2
        ea = abs((xmax - px)/xmax) * 100
        px = xmax
        print('({},{}) xmax = {} ea = {}'.format(a,b,xmax,ea))


#Task2 find minimum
def min_interval(f,a,b,p):
    ep = 0.1
    ea = 100
    es = 0.5 * 10**(2-p)
    px = b
    while ea > es:
        l = (a+b)/2 + ep/2
        u = (a+b)/2 - ep/2
        if f(l) > f(u):
            b = u
        else:
            a = l
        xmax = (a+b)/2
        ea = abs((xmax - px)/xmax) * 100
        px = xmax
    print('({},{}) xmin = {} ea = {}'.format(a,b,xmax,ea))
        

#Task3 find minimum
def min_goldensearch(f,xL,xU,p):
    phi = (1+numpy.sqrt(5))/2 
    ea = 100
    es = 0.5 * 10**(2-p)
    while ea > es:
        d = (phi - 1)*(xU-xL)
        x1 = xL+d
        x2 = xU-d
        if f(x1) > f(x2):
            xmin = x2
            xU = x1
        else:
            xmin = x1
            xL = x2
        ea = (2-phi)*abs((xU-xL)/xmin)*100
    print('({},{}) xmin = {} ea = {}'.format(xL,xU,xmin,ea))


#Task4 find maximum
def max_goldensearch(f,xL,xU,p):
    phi = (1+numpy.sqrt(5))/2 
    ea = 100
    es = 0.5 * 10**(2-p)
    while ea > es:
        d = (phi - 1)*(xU-xL)
        x1 = xL+d
        x2 = xU-d
        if f(x1) < f(x2):
            xmin = x2
            xU = x1
        else:
            xmin = x1
            xL = x2
        ea = (2-phi)*abs((xU-xL)/xmin)*100
        print('({},{}) xmin = {} ea = {}'.format(xL,xU,xmin,ea))


#Task 5 find minimum
def min_parabolic(f,x1,x2,x3,p):
    ea = 100
    es = 0.5 * 10**(2-p)
    px = x3
    
    while ea > es:
        
        alpha1 = (x2-x1)*(x2-x1)*(f(x2)-f(x3));
        alpha2 = (x2-x3)*(x2-x3)*(f(x2)-f(x1));
        beta1 = (x2-x1)*(f(x2)-f(x3));
        beta2 = (x2-x3)*(f(x2)-f(x1));
        
        gamma = (alpha1 - alpha2)/(beta1 - beta2);
        x4 = x2 - (0.5 * gamma);
        if x3 > x2:
            x1 = x2
            x2 = x4
        else:
            x3 = x2
            x2 = x4
        xopt = x4
        ea = abs((xopt - px)/xopt) * 100
        px = xopt
        # print(x1,x2,x3,x4)
    print('({},{}) xmin = {} ea = {}'.format(x1,x2,xopt,ea))


#Task 5 find minimum
def max_parabolic(f,x1,x2,x3,p):
    ea = 100
    es = 0.5 * 10**(2-p)
    px = x3
    
    while ea > es:
        
        alpha1 = (x2-x1)*(x2-x1)*(f(x2)-f(x3));
        alpha2 = (x2-x3)*(x2-x3)*(f(x2)-f(x1));
        beta1 = (x2-x1)*(f(x2)-f(x3));
        beta2 = (x2-x3)*(f(x2)-f(x1));
        
        gamma = (alpha1 - alpha2)/(beta1 - beta2);
        x4 = x2 - (0.5 * gamma);
        if x4 < x2:
            x1 = x2
            x2 = x4
        else:
            x3 = x2
            x2 = x4
        xopt = x4
        print(xopt)
        ea = abs((xopt - px)/xopt) * 100
        px = xopt
        # print(x1,x2,x3,x4)
        print('({},{}) xmax = {} ea = {}'.format(x1,x2,xopt,ea))
# max_interval(f,0,2,4)
# max_goldensearch2(f,0,2,4)
# max_parabolic(f,0,1,2,4)

# min_interval(f,0,4,4)
# min_goldensearch(f,0,4,4)
# min_parabolic(f, 0, 1, 4, 4)

        