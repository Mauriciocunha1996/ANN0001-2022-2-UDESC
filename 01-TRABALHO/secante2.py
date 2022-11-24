


def f(x):
    return 2*(x+1)*(x-0.5)*(x-1) #funcao

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
    x0=0.15735 # inicio intervalo
    x1= 0.69731 #fim intervalo
    n=5 #quantidade de iteracoes
    secante(x0,x1,n)

main()
