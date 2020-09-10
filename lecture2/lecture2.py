# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 13:25:01 2020

@author: Baby
Good code don't need to explain but this is good code but still need to explain
##############################CODE IS MY CADIO#################################
"""


import numpy
import math
import matplotlib.pyplot as plt


# find factorial
def fac(n):
    if n == 0:
        return 1
    else:
        return n*fac(n-1)


# find e^0.2
def task1():
    # Code AJ
    x = 0.2
    ex = 0
    for i in range(0, 10):
        ex += x**i/fac(i)
    print(ex)


# find ln(x) ex. ln(0.2) ln(4.7)
def task2(n):
    # find ln(x)
    x = n
    # count how many ln(e)
    counter = 0
    while True:
        x = x/math.e
        counter += 1
        # to make ln(1+x) form.
        if (x > 1 and x < 2) or x < 1:
            x = x-1
            break
        # end if
    # end loop
    # Code AJ
    logx = 0
    i = 1
    prev_logx = 0
    approx_error_pct = 100
    while (approx_error_pct > 0.0005):
        logx = logx + (((-1)**(i+1))*(x**i)/i)
        approx_error_pct = (abs(logx - prev_logx)/abs(logx)) * 100
        prev_logx = logx
        i += 1
    # end while

    # print('log({}) = {}+log({}) ='.format(n,counter,x),counter+logx)
    # print('The actual log({}) = '.format(n),math.log(n))
    return counter+logx


# find log2(10), sin(60), tan-1(0.4), ln(0.6)
def task3():
    # find log2(10)
    # so we know lo2(x) = log10(x)/log10(2)
    # and log10(x) = ln(x)/ln(10)
    # step 1 find log10(10) = ln(10)/ln(10)
    log10_10 = task2(10)/task2(10)
    # step 2 find log10(2) = ln(2)/ln(10)
    log10_2 = task2(2)/task2(10)
    print('======================== log2(10) ================================')
    print('log2(10) =', log10_10/log10_2)
    print('The actual log2(10) =', math.log2(10))

    # find sin(60)
    # convert 60 to um idk degrees radians what's ever
    # Code AJ
    # convert 60 degrees to radians.
    x = 60 * math.pi/180  # math.pi/3 -> radians to degrees
    ex = 0
    i = 0
    prev_ex = 0
    approx_error_pct = 100
    while (approx_error_pct > 0.0005):
        # taylor series formula
        ex = ex + (((-1)**i)*((x**((2*i)+1))/fac((2*i)+1)))
        approx_error_pct = (abs(ex - prev_ex)/ex) * 100
        prev_ex = ex
        i += 1
    # end while
    print('======================== sin(60) ================================')
    print('sin(60) =', ex)
    print('The actual sin(60) =', numpy.sin(numpy.radians(60)))

    # find tan-1(0.4) ;x = [-1,1] so it's fine
    # Code AJ
    x = 0.4
    tan = 0
    i = 0
    prev_ex = 0
    approx_error_pct = 100
    while (approx_error_pct > 0.0005):
        # taylor series formula
        tan = tan + (((-1)**i)/((2*i)+1)) * (x**((2*i)+1))
        approx_error_pct = (abs(tan - prev_ex)/tan) * 100
        prev_ex = tan
        i += 1
    # end while
    print('======================== arctan(0.4) =============================')
    print('arctan(0.4) =', tan)
    print('The actual arctan(0.4) =', numpy.arctan(0.4))
    print('======================== ln(0.6) =================================')
    # find ln(0.6)
    print('ln(0.6) =', task2(0.6))
    print('The actual log2(10) =', math.log(0.6))


def f(x):
    # x**2-2*x-3
    # numpy.sin((10*x)) + numpy.cos((3*x))
    # numpy.sin(numpy.degrees(10*x))+numpy.cos(numpy.degrees(3*x))
    # numpy.sin(numpy.radians(10*x))+ numpy.cos(numpy.radians(3*x))
    # numpy.sin(2*numpy.pi*x)+numpy.e**(2*x)+x-2.5
    return numpy.sin(2*numpy.pi*x)+numpy.e**(2*x)+x-2.5


def task4():
    # Prepare the data
    x = numpy.linspace(0, 10, 101)
    y = f(x)

    # Plot the data
    plt.plot(x, y, label='y = f(x)')

    # Add a legend
    plt.legend()

    # Show the plot
    plt.show()


# Task5
def is_square(a):
    # use numpy library
    rows, colums = a.shape
    if rows == colums:
        return True
    else:
        return False


def is_symmetrical(a):
    if is_square(a):
        rows, colums = a.shape
        for i in range(0, rows):
            for j in range(0, colums):
                # it's not symmectric
                if not a[i, j] == a[j, i]:
                    return False
                # end if
            # end for
        # end for
        return True
    else:
        return False


# A diagonal matrix is a square matrix whose off-diagonal entries
# are all equal to zero.
def is_diagonal(a):
    if is_square(a):
        rows, colums = a.shape
        for i in range(0, rows):
            for j in range(0, colums):
                if (a[i, j] != 0 and i != j):
                    print(i, j)
                    return False
                # end if
            # end for
        # end for
        return True
    else:
        return False


def is_identity(a):
    if is_diagonal(a):
        rows, colums = a.shape
        for i in range(0, rows):
            for j in range(0, colums):
                if (a[i, j] != 1 and i == j):
                    print(i, j)
                    return False
                # end if
            # end for
        # end for
        return True
    else:
        return False
    


def is_zero(a):
    rows, colums = a.shape
    for i in range(0, rows):
        for j in range(0, colums):
            if a[i, j] != 0:
                return False
            # end if
        # end for
    # end for
    return True


def transpose(a):
    rows, colums = len(a),len(a)
    temp = numpy.empty((rows,colums),dtype=int)
    for i in range(rows):
        for j in range(colums):
            temp[i][j] = a[j][i]
        # end for
    # end for
    return temp

# task6
def dot_product(a,b):
    rows = len(a)
    colums = len(a[0])
    c = numpy.empty((rows,colums),dtype=int)
    if rows == colums:
        i = 0
        while i < rows:
            j = 0
            while j < colums:
                product_sum = 0
                k = 0
                while k < len(a[0]):
                    product_sum += a[i,k] * b[k,j]
                    k += 1
                # end  k loop
                c[i,j] = product_sum
                j += 1
            # end j loop
            i += 1
        # end i loop
        return c
    else:
        return 'Error'


# task7 find determinate
# minor(a,r,c) just use to find minor of n-1 x n-1
# return in array
def minor(a, r, c):
    l = len(a)
    temp = []
    # run loop through colum 
    for j in range(l):
            temp2 = []
            # run loop through row
            for i in range(l):
                # cut the row and colum to get minor
                if  j != c and i != r :
                    temp2.append(a[i][j])
                # end if
            # end for j
            # if temp2 is not empty
            if temp2:
                temp.append(temp2)
        #end if
    #end for i
    return temp      

# find determinate of 3x3 matrix.
def det3x3(a):
    d = 0 # result
    if len(a) == 1 :return a[0][0]
    else:
        for c in range(0,len(a)):
            # det use only 1st row of minor
            temp = minor(a, 0, c)
            b = temp[0][0]*temp[1][1] - temp[0][1]*temp[1][0]
            d = d + (-1)**c * a[0][c] * b
        # end loop
        return d


# task8 find minor cofactor adjoint and inverse
# find determinate for NxN useing recursion
def det(a):
    d = 0
    if len(a) == 1 :return a[0][0]
    else:
        for c in range(0,len(a)):
            temp = minor(a, 0, c)
            d = d + (-1)**c * a[0][c] * det(temp)
        # end loop
        return d


# find complete minor.
def find_minor(a):
    # normaly we have to check square matrix first.
    m = []
    for i in range(len(a)):
        for j in range(len(a)):
            # find det of small minor
            x = det(minor(a,i,j))
            m.append(x)
        # end j loop
    # end i loop
    # return in 2d matrix.
    return numpy.array(m).reshape(len(a),len(a))

# find cofactor from complete minor
def cofactor(a):
    a = find_minor(a)
    for i in range(len(a)):
       for j in range(len(a)):
           a[i][j] = (-1)**(i+j) * a[i][j]
       # end j loop
    # end i loop
    return a

# find adjoint from transposed matrix of the cofactor of matrix
def adjoint(a):
    return transpose(cofactor(a))

# find inverse from adjoint/determinate
def inverse(a):
    # normaly check square matrix
    # determinate must not equal 0
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
            # end j loop
            inv.append(temp)
        # end i loop
    return numpy.array(inv)


# task 9 do by hand
# Driver code
if __name__ == '__main__':

    # task1()
    # print('ln(0.2) =', task2(0.2))
    # print('ln(4.7) =', task2(4.7))
    # task3()
    # task4()
    a = numpy.array([
        [3, -2, 4],
        [-2, 6, 2],
        [4, 2, 3],
        ])
    b = numpy.array([
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        ])
    c = numpy.zeros((2, 2),int)
    d = [[1,2,3],
         [4,5,6],
         [7,8,9]]
    e = numpy.array([
        [3,4,2],
        [13,26,75],
        [9,5,3]
        ])
    g = [
    	  [1, 1, -1, -2],
    	  [0, 2, 1, 3],
    	  [0, 1, 1, 3],
    	  [0, 2, 1, 4]
    	 ]
    
    # print(is_square(a))
    # print(is_symmetrical(a))
    # print(is_diagonal(a))
    # print(is_identity(a))
    # print(is_zero(c))
    # print(transpose(e))
    # print(dot_product(a, e))
    
    # find det 3x3
    # print(det3x3(a))
    # print(numpy.linalg.det(a))
    
    # find minor
    # print(find_minor(g))
    
    # find cofactor
    # print(cofactor(g))
    
    # find adjoint
    # print(adjoint(g))
    
    # find inverse
    # print(inverse(g))
    # print(numpy.linalg.inv(g))
    

    
    
    
