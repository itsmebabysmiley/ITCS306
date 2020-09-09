# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 20:31:29 2020

@author: Baby and BabyBoat
"""


def dec_to_ieee(N):
    print('Decimal :',N)
    sign = float(N)
    # split in integer part and float part.
    temp = N.split('.')
    # Calculate integer part to binary
    Integer = ''
    N = temp[0]
    # Convert string to positive integer
    N = abs(int(N))
    if(N != 0):
        while N > 0:
            remainder = N % 2
            N = N // 2
            Integer += str(remainder)
        # end while
    else:
        Integer = '0'
    # Reverse the binary
    Integer = Integer[::-1]
    # End calculate integer part to binary

    # Calculate floating part
    y = temp[1]
    length = len(y)
    # Convert string to floating-point
    y = float(y) / (10**length)
    Float = ''
    for i in range(0, 28):
        y = y * 2
        Float += str(int(y // 1))
        y = y % 1
    # end for
    # End calculate floating part
    #Summarizing - the positive number before normalization:
    result = Integer + Float
    counter = 0
    # Normalize the binary representation of the number..
    # find one non-zero digit stays to the left of the decimal point.
    # use counter to count the one non-zero left most
    for i in result:
        counter += 1
        if i == '1':
            break
    # end for
    # shift to the right.
    if(counter > len(Integer)+1):
        exponent = len(Integer) - counter
    # shift to the left.
    else:
        exponent = counter - len(Integer)
        exponent = abs(exponent)
    # adjusted exponent by + 127
    exponent = exponent + 127
    # Convert exponent to binary
    bin_exponent = ''
    while exponent > 0:
        remainder = exponent % 2
        exponent = exponent // 2
        bin_exponent += str(remainder)
    # End calculate exponent to binary
    print('Sign :', '0' if sign >= 0 else '1')
    print('Exponent :', bin_exponent[::-1].zfill(8))
    # Normalize the mantissa, remove the leading (leftmost) bit,
    # since it's allways '1' (and the decimal point) and adjust
    # its length to 23 bits, by removing the excess bits from
    # the right (losing precision...):
    fraction = result[counter::]
    print('Fraction :', fraction[0:23])
    if sign >= 0:
    	IEEE = '0-'
    else:
    	IEEE = '1-'
    return IEEE + bin_exponent[::-1].zfill(8) + '-' + fraction[0:23]


def iee_to_dec(S,E,F):
    Sign = int(S)
    Exponent = E
    Fraction = F
    # Sign = 0
    # Exponent = '01111010'
    # Fraction = '11000010100011110101110'
    # Convert exponent to decimal
    c = len(Exponent)-1
    dec_exponent = 0
    for i in Exponent:
        dec_exponent += int(i) * (2**c)
        c -= 1
    dec_exponent = dec_exponent - 127
    # End converter
    # Convert fraction to decimal
    c = -1
    dec_fraction = 0
    for i in Fraction:
        dec_fraction += int(i) * (2**c)
        c -= 1
    # End converter
    # Convert ieee to floating in 3 decimal points
    answer = ((-1)**Sign)*(1+dec_fraction)*(2**dec_exponent)
    print('{}-{}-{} :'.format(Sign, Exponent, Fraction), round(answer, 3))


# Driver code
print('Convert decimal to IEEE754')
IEEE = dec_to_ieee('0.055')
print('\nConvert IEEE754 to decimal')
temp = IEEE.split('-')
iee_to_dec(temp[0],temp[1],temp[2])
