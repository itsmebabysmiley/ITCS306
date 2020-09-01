# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 09:25:23 2020

@author: User
"""

import math
# task10
def task10():
    # find Es
    Es = 0.5*pow(10, 2-7)
    print('Es=', Es)
    # ture value is 2.449489742783178
    # initialize x = 1
    MAX_iterations = 10
    N = 6
    prev_x = 1
    x = 1
    turevalue = 2.449489742783178
    for i in range(0, MAX_iterations):
        x = (1/2)*(prev_x + N/prev_x)
        prev_x = x
        # find Et
        print('Et(%d) =' % i, (abs((turevalue-x)/turevalue)*100), end=' ')
        # find Ea
        print('Ea(%d) =' % i, (abs(x-prev_x)/x)*100)
    # end for
    print('The Approximated value of sqrt(6) =', x)


# task11
def bin_to_dec(bin):
    # find length of string
    length = len(bin)
    # reverse string
    revbin = bin[::-1]
    R = 0
    for i in range(0, length):
        # calculate only '1' power of i++
        if '1' == revbin[i]:
            R = R + 2**i
    # end for
    return R


def bin_to_dec2(bin):
    temp = bin.split('.')
    # call bin_to_dec to calculate interger.
    R = bin_to_dec(temp[0])
    # just rename it haha
    decimal_part = temp[1]
    counter = -1
    for i in decimal_part:
        if i == '1':
            R = R + 2**counter
            counter -= 1
        else:
            counter -= 1
        # end if
    # end for
    return R


def dec_to_bin(dec):
    dec = '5.75'
    temp = dec.split('.')
    integer = int(temp[0])
    result = ''
    # Convert integer to binay
    while integer > 0:
        Remainder = integer%2
        integer = integer//2
        result += str(Remainder)
    # End loop
    # revese the binary
    result = result[::-1]+"."
    # Convert floating-point to binary

    # check length of floating part
    length = len(temp[1])
    # Convert string to float.
    floating = int(temp[1])/10**length
    old_value = floating
    # Convert floating-point to binary
    for i in range(0,24):
        floating = floating * 2
        result +=str(int(floating//1))
        floating = round(floating%1,2)
        if floating == old_value:
            break
    # end loop
    return


# task12
def square_root():
    N = int(input('Input number: '))
    # initialize x = 1
    prev_x = 1
    x = 1
    for i in range(0, N):
        x = (1/2)*(prev_x + N/prev_x)
        prev_x = x
    # end for
    print('Square root of {} : {}' .format(N, x))
# code AJ


def cube_root():
    N = int(input('Input number: '))
    # initialize x = 1
    prev_x = 1
    x = 1
    for i in range(0, N):
        x = (1/4)*(3*prev_x + N/prev_x**2)
        prev_x = x
    # end for
    print('Cube root of {} : {}' .format(N, x))
# code AJ


def dec_iee():
    # won't work every number just 0.096
    N = 0.096
    # check sign
    if N > 0:
        sign = 0
    else:
        sign = 1
    # find mantissa
    R = '0.'
    for i in range(0, 27):
        N = N * 2
        if N >= 1:
            R = R + '1'
        else:
            R = R + '0'
        # end if
        # mod to get 0.xx
        N = N % 1
        # round to 2 decimals place
        N = round(N, 3)
        # if repeat number stop
    # end for
    # shifting the decimal to the right so that only one non zero digit remains
    # to the left of it
    # find how many digits have to shift(exponent)
    # minus '.'
    counter = -1  # exponent
    for i in R:
        counter += 1
        if i == '1':
            break
        # end if
    # end for
    # print(R[counter+1::])
    # calculate exponent
    exponent = -(counter-1) + 127
    # change exponent to binay base
    exponent = str(dec_to_bin(exponent))
    # print(exponent.zfill(8))
    print('sign: {} exponent: {} fraction: {}'.format(sign, exponent.zfill(8),
                                                      R[counter+1::]))


def iee_dec(sign, exponent, fraction):
    # convert exponent to decimal
    exponent = bin_to_dec(exponent)
    # adjust exponent -bias(127/1023)
    exponent = exponent - 127
    #convert fraction
    counter = -1
    R = 0
    x = 0
    getcontext().prec = 24
    for i in fraction:
        x = float(i) * 2**counter
        counter -= 1
        R+=x
        # end if
    # end for
    # calculate floating-point
    f = (math.pow(-1,int(sign)) * (1+R) * math.pow(2,exponent))
    return f
    
# Driver code
if __name__ == "__main__":
    binary = '110110'
    float_binary = '10.1001'
    task10()
    print('-----------------------------------')
    print('{} in decimal: {}' .format(binary, bin_to_dec(binary)))
    print('{} in decimal: {}' .format(float_binary,
                                      bin_to_dec2(float_binary)))
    print('-----------------------------------')
    dec_to_bin(10)
    print('{} in binary: {}' .format(10, dec_to_bin(10)))
    fdec_to_bin2(0.36)
    print('{} in binary: {}' .format(0.36, fdec_to_bin2(0.36)))
    print('-----------------------------------')
    square_root()
    cube_root()
    print('-----------------------------------')
    dec_iee()
    dec = iee_dec('0', '01111011', '10001001001101110100101')
    print('0-01111011-10001001001101110100101 is %.3f' %(dec))
