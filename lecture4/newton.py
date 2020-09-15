#just python3 newton.py
from scipy import optimize as o
import numpy 
def f(x):
	return numpy.sin(numpy.sqrt(x)) - x

root = float(input('Input: '))
print('root is {}'.format(o.newton(f,root)))
