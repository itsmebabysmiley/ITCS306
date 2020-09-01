# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 22:14:13 2020

@author: BaBy
"""


# Code AJ

# find es 5 sinificant figure
d = 5
es = 0.5 * 10**(2-d)

# find log(10)
x = 0.353352832366127
# initial sum
log10 = 0
i = 1  # look at the formula
prev_logx = 0
approx_error_pct = 100
while(approx_error_pct > es):
    log10 = log10 + (((-1)**(i+1))*(x**i)/i)
    approx_error_pct = (abs(log10 - prev_logx)/abs(log10))*100
    prev_logx = log10
    i += 1
# end while
print('1+1+ln(0.353352832366127) = ', 2+log10)
log10 += 2
# find log(2)
x = -0.26424111765711533
log2 = 0
i = 1
prev_logx = 0
approx_error_pct = 100
while(approx_error_pct > 0.005):
    log2 = log2 + (((-1)**(i+1))*(x**i)/i)
    approx_error_pct = (abs(log2 - prev_logx)/abs(log2))*100
    prev_logx = log2
    i += 1
# end while
print('1+ln(-0.26424111765711533) = ', 1+log2)
log2 += 1
# convert base e to base 10 from samakan log10(x) = loge(x)/loge(10)
# find log10(10) = log(10)/log(10)
log10_10 = log10/log10
# find log10(2) = log(2)/log(10)
log10_2 = log2/log10
# find log2(10) = log10(10)/log10(2)
log2 = log10_10/log10_2
print(log2)
