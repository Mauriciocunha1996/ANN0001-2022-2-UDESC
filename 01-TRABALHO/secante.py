"""Encontre as aproximações para a raiz da função
	f(x)=πx-ex
obtidas pelo método da Secante com estimativas iniciais x0=0.83403 e x1=2.08037, após 1, 3 e 5 iterações.from cmath import cos, sqrt"""

from cmath import exp, pi


def f(x):
    return pi*x-exp(x) #funcao

def secante(x0,x1,n):
    for i in range(0,n):
        fx0 = f(x0)
        fx1 = f(x1)
        if fx0 ==fx1:
            print(f'Divisao por zero na iterazao {i+1}')
        x2 = ((x0*fx1)-(x1*fx0))/(fx1-fx0)
        print(f'x_{i+1} = {x2:.16f}')
        x0=x1
        x1=x2

def main():
    x0=0.1 # inicio intervalo
    x1=1.33 #fim intervalo
    n=5 #quantidade de iteracoes
    secante(x0,x1,n)

main()
