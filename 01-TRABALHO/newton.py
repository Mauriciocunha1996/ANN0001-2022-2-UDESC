import math

def f(x):
    e = 2
    return x * (x - 1) * (x - 2) + 0.42 # function

def df(x):
    return 3*(x**2)-6*x+2 # derivada de f

def newton(x0,n):
    for i in range(0,n):
        x1 = x0-(f(x0)/df(x0))
        print(f'x_{i+1} = {x1:.7f}')
        x0=x1

def main():
    x0=2.7525393
    n=195
    newton(x0,n)

main()