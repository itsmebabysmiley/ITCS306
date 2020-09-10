# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 19:54:38 2020

@author: User
"""

import numpy

def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]
def det(a):
    d = 0
    if len(a) == 1:
        return a[0][0]
    else:
        for c in range(0,len(a)):
            temp = getMatrixMinor(a, 0, c)
            print(temp)
            d += (-1)**c * a[0][c] * det(temp)
        return d
    


a = [
        [3, -2, 4],
        [-2, 6, 2],
        [4, 2, 3],
        ]

g = [
    	  [1, 1, -1, -2],
    	  [0, 2, 1, 3],
    	  [0, 1, 1, 3],
    	  [0, 2, 1, 4]
    	 ]
r = [
     [5	,7	,1],
    [-4	,1	,0],
    [2	,0	,3]
     ]
for i in range(len(g)):
    
    print(numpy.array(getMatrixMinor(g,0,i)))