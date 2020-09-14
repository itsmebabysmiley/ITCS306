#just python3 newton.py
from scipy import optimize as o

def f(x):
	return x**3 - 4*x**2 - 4*x + 16

root = float(input('Input'))
print('root is {}'.format(o.newton(f,root)))
