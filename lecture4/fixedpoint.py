#just python3 fixedpoint.py
from scipy import optimize as o
import math as m
def g(x):
	return m.sin(m.sqrt(x))

# root = float(input('Input: '))
print('root is {}'.format(o.fixed_point(g,1)))

