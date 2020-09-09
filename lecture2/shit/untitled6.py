# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 21:46:00 2020

@author: User
"""

import numpy


def minor(a, r, c): #0,0
    l = len(a)
    temp = []
    for j in range(l):
            temp2 = []
            for i in range(l):
                if j != r and i != c :
                    temp2.append(a[i][j])
                # end if
            # end for j
            if temp2:
                temp.append(temp2)
        #end if
    #end for i
    return temp            


def det(a):
    d = 0
    if len(a) == 1 :return a[0][0]
    # if len(a) == 2 :return a[0][0]*a[1][1] - a[0][1]*a[1][0]
    else:
        for c in range(0,len(a)):
            temp = minor(a, 0, c)
            d = d + (-1)**c * a[0][c] * det(temp)
        return d

if __name__ == '__main__':

    a = [
        [3, -2, 4],
        [-2, 6, 2],
        [4, 2, 3],
        ]
    b = numpy.array([
        [3, -2, 4],
        [-2, 6, 2],
        [4, 2, 3],
        ])
    # print(numpy.linalg.det(b))
    print(det(a))
    # for i in range(0,len(a)):
    #     minor(a,0,i)

    
# M = numpy.array([
#      [1, 3, 2],
#      [-3, -1, -3],
#      [2, 3, 1]])
# print(numpy.linalg.det(M))