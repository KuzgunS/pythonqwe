
from sympy import *
import numpy as np
# Accept integer n as a command-line argument. Write to standard
# output the prime factors of n.
EPSILON = 1e-15

def root(a):
    x_n=a
    i=0
    x=Symbol('x')
    f=x**2-11*x+28
    fPrime=f.diff()
    
    f_value = lambdify(x, f, 'numpy')
    fPrime_value = lambdify(x, fPrime, 'numpy')
    
    while abs(f_value(x_n)/fPrime_value(x_n)) > EPSILON:    
        x_n=x_n-(f_value(x_n)/fPrime_value(x_n))
        i=i+1

    return x_n,i

def main():
    x=int(input('Enter x'))
    result, iteration = root(x)
    print(x)
    print(result)
    print(iteration)
    
main()



