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
    rows, colums = a.shape
    temp = numpy.empty((rows,colums),dtype=int)
    for i in range(rows):
        for j in range(colums):
            temp[i,j] = a[j,i]
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


# task7
def deter(a):
    det = 0
    if len(a) == 1 and is_square(a):
        return a[0][0]
    else:
        for i in range(3):
            det = det + (a[0][i]*(a[1][(i+1)%3]*a[2][(i+2)%3] - a[1][(i+2)%3]*a[2][(i+1)%3]));
    return det


# task8


# task8
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
    # print(is_square(a))
    # print(is_symmetrical(a))
    # print(is_diagonal(a))
    # print(is_identity(a))
    # print(is_zero(c))
    # print(numpy.array(transpose(d)))
    # print(transpose(e))
    # print(dot_product(a, e))
    # print(numpy.dot(a,e))
    # find det
    print(numpy.linalg.det(a))
    print(deter(a))
