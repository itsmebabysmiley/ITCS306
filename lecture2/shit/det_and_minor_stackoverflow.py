# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 19:49:33 2020

@author: User
"""


def minor(array,i,j):
    c = array
    c = c[:i] + c[i+1:]
    for k in range(0,len(c)):
        c[k] = c[k][:j]+c[k][j+1:]
    return c
def det(array,n):
    if n == 1 :return array[0][0]
    if n == 2 :return array[0][0]*array[1][1] - array[0][1]*array[1][0]
    sum = 0
    for i in range(0,n):
        m = minor(array,0,i)
        print(m)
        sum =sum + ((-1)**i)*array[0][i] * det(m,n-1)
    return sum

def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

M = [[1, 3, 2],
     [-3, -1, -3],
     [2, 3, 1]]
import numpy
# print(numpy.linalg.det(M))
# print(det(M,3))

N = [
     [1, 1, -1, -2],
     [0, 2, 1, 3],
     [0, 1, 1, 3],
     [0, 2, 1, 4]
     ]
B = [
     [2, 3,	1],	
     [0, 5,	6],	
     [1, 1,	2], 
     ]
a = [
        [3, -2, 4],
        [-2, 6, 2],
        [4, 2, 3],
        ]
print(det(a,3))

