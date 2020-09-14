from scipy import optimize as o
import math as m
def g(x):
	return m.e**(-x)

root = float(input('Input'))
print('root is {}'.format(o.fixed_point(g,root)))
