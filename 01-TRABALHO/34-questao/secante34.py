from math import pi, pow

def f(h):
	#return pi*pow(h,2)*((3*7.33-h)/3)-213.02
    #return ((((9.81*83.19)/c)*(1-(exp(-((c/83.19)*8.3)))))-48.83);#funcao
	#return (((9.81*m)/21.09)*(1-exp(-((21.09/m)*8.58))))-30.93
	r1 = 2.33
	r2 = 5.71
	pt = 470.47
	pw = 1000.0
	H = 7.63
	x = H*r1/(r2-r1)
	return pt * ((H) * (pow(r2, 2) + pow(r1, 2) + r1 * r2)) - pw * (H - h) * ((pow(r1, 2) + (2* (pow(r1, 2) * h)/ x) + pow(h,2)*pow(r1,2)/pow(x,2)+ pow(r2,2) + r2*r1 + h*r2*r1/x))


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
    x0= 0.36  # inicio intervalo
    x1= 6.89 #fim intervalo
    n=5 #quantidade de iteracoes
    secante(x0,x1,n)

main()