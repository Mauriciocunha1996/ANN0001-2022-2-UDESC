from cmath import exp
from math import pi

def f(m):
    return (((9.81*m)/21.09)*(1-exp(-((21.09/m)*8.58))))-30.93
def df(m):
    return (327*(1-exp(-904761/(5000*m))))/703-(420849*exp(-904761/(5000*m)))/(5000*m) # derivada de f

def newton(x0,n):
    for i in range(0,n):
        x1 = x0-(f(x0)/df(x0))
        print(f'x_{i+1} = {x1:.16f}')
        x0=x1

def main():
    x0=22.14
    n=5
    newton(x0,n)
    
main()


