# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 21:46:00 2020

@author: User
"""

import numpy


def minor(a, r, c):
    l = len(a)
    temp = []
    for j in range(l):
            temp2 = []
            for i in range(l):
                if  j != c and i != r :
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
    else:
        for c in range(0,len(a)):
            temp = minor(a, 0, c)
            d = d + (-1)**c * a[0][c] * det(temp)
        return d


def find_minor(a):
    # fi a is square matrix
    m = []
    for i in range(len(a)):
        for j in range(len(a)):
            x = det(minor(a,i,j))
            m.append(x)
        pass
    return numpy.array(m).reshape(len(a),len(a))
        
def transpose(a):
    rows, colums = len(a),len(a)
    temp = numpy.empty((rows,colums),dtype=int)
    for i in range(rows):
        for j in range(colums):
            temp[i][j] = a[j][i]
        # end for
    # end for
    return temp


def cofactor(a):
    for i in range(len(a)):
           for j in range(len(a)):
                   a[i][j] = (-1)**(i+j) * a[i][j]
                   
    return a


def adjoint(a):
    return transpose(cofactor(find_minor(a)))


def inverse(a):
        deter = det(a)
        if deter == 0:
            return False
        else:
            inv = []
            adj = adjoint(a)
            for i in range(len(a)):
                temp = []
                for j in range(len(a)):
                    temp.append(adj[i][j] / deter)
                inv.append(temp)
        return numpy.array(inv)
    
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
    mm = [
        [2,1,3],
        [1,1,3],
        [2,1,4]]
    print(adjoint(g))
    

    
# M = numpy.array([
#      [1, 3, 2],
#      [-3, -1, -3],
#      [2, 3, 1]])
# print(numpy.linalg.det(M))