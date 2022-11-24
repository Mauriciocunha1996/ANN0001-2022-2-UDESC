from math import pow, sqrt, tanh
from mpmath import sech

def f(h):
    return (sqrt(2*9.81*h)*(tanh(((sqrt(2*9.81*h))/(2*5.82))*5.45)))-6.51 # function

def df(h):
    return (3*sqrt(109)*tanh((109**(3/2)*sqrt(h))/(97*2**(5/2))))/(5*2**(3/2)*sqrt(h))+(35643*sech((109**(3/2)*sqrt(h))/(97*2**(5/2)))**2)/7760 # derivada de f

def newton(x0,n):
    for i in range(0,n):
        x1 = x0-(f(x0)/df(x0))
        print('x_{} = {}'.format(i+1,x1))
        #print(f'x_{i+1} = {x1:.16f}')
        x0=x1



def main():
    x0=1.37 
    n=5
    newton(x0,n)



main()