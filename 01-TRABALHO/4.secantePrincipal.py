from math import pi, pow, exp

def f(m):
	#return pi*pow(h,2)*((3*7.33-h)/3)-213.02
    #return ((((9.81*83.19)/c)*(1-(exp(-((c/83.19)*8.3)))))-48.83);#funcao
	return (((9.81*m)/21.09)*(1-exp(-((21.09/m)*8.58))))-30.93

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
    x0= 23.89  # inicio intervalo
    x1= 36.49 #fim intervalo
    n=5 #quantidade de iteracoes
    secante(x0,x1,n)

main()