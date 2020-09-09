# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy

# lecture 3 is about to find root of xr where is xr = [xl,xu] maybe
# code AJ
# =============================================================================
# def interval_search_normal(l, u, n):
#     x = numpy.linspace(l, u, n)
#     for i in range(n-1):
#         xl = x[i]
#         xu = x[i+1]
#         print('interval ({},{})' .format(xl, xu))
#         if f(xl) * f(xu) < 0:
#             xr = (xl+xu)/2
#             print('found root in ({},{}) = {}'.format(xl, xu, xr))
# =============================================================================
# code AJ
# =============================================================================
# def bisection(l, u, n):
#     xl = l
#     xu = u
#     for i in range(n):
#         mid = (xl+xu)/2
#         if f(xl)*f(mid) < 0:
#             xu = mid
#         else:
#             xl = mid
#         xr = (xl+xu)/2
#         print('root xr =',xr)
# =============================================================================


def f(x):
    return x**3 - 6*x**2 + 4*x + 12
# task3.1 
# find root xr 4 significant 
def interval_search(l, u, n):
    xr = 0
    es =0.005
    prev_xr = 0
    ea = 100
    while ea > es:
        x = numpy.linspace(l, u, n)
        for i in range(n-1):
            xl = x[i]
            xu = x[i+1]
            if f(xl) * f(xu) < 0:
                xr = (xl+xu)/2
                # print('found root in ({},{}) = {}'.format(xl, xu, xr))
                l = xl
                u = xu
                break
        ea = abs((xr-prev_xr)/xr) * 100
        prev_xr = xr
        # print('approxmate error =',ea)
    print('found root in [{},{}] xr = {}'.format(xl, xu, xr))
    print('approxmate error =',ea)

# task3.2
def bisection(l, u):
    xl = l
    xu = u
    xr = 0
    es =0.005
    prev_xr = 0
    ea = 100
    while ea > es:
        mid = (xl+xu)/2
        if f(xl)*f(mid) < 0:
            xu = mid
        else:
            xl = mid
        xr = (xl+xu)/2
        # print('found root in ({},{}) = {}'.format(xl, xu, xr))
           
        ea = abs((xr-prev_xr)/xr) * 100
        prev_xr = xr
        # print('approxmate error =',ea)
    print('found root in [{},{}] xr = {}'.format(xl, xu, xr))
    print('approxmate error =',ea)

# task3.3
def false_position(l, u):
    xl = l
    xu = u
    xr = 0
    es =0.005
    prev_xr = 0
    ea = 100
    while ea > es:
        # another fomula
        # xr = xl -(xu-xl) * f(xl)/(f(xu) - f(xl))
        xr = xu - f(xu) * ( (xu - xl) / ( f(xu) - f(xl) ) )
        if f(xl)*f(xr) < 0:
            xu = xr
        else:
            xl = xr
        # print('found root in ({},{}) = {}'.format(xl, xu, xr))
        ea = abs((xr-prev_xr)/xr) * 100
        prev_xr = xr
        # print('approxmate error =',ea)
    print('found root in [{},{}] xr = {}'.format(xl, xu, xr))
    print('approxmate error =',ea)


if __name__ == '__main__':
    print('--------------interval search--------------')
    interval_search(2,3,11)
    print('--------------bisection search--------------')
    bisection(2,3)
    print('--------------false position search--------------')
    false_position(2,3)