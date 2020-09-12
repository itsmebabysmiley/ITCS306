from scipy import optimize as o

def f(x):
	return x**3 - 4*x**2 - 4*x + 12

root = o.newton(f,-1.5)
