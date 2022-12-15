import math
import numpy as np


def trapz(f, a, b, n):
    sum = f(a)/2 + f(b)/2
    base = (b-a)/n
    # Lembre-se que x0 = a e xn = b, por isso no seguinte loop k varia de 1 até n-1:
    for k in range(1, n):
        sum += f(a + k*base)
    area = base*sum
    return area


def coef(f,g, a, b, numero_intervalo):
    numer = trapz(
        lambda x: f(x) * g(x),
        a,
        b,
        numero_intervalo
                  )
    denom = trapz(
        lambda x: g(x) * g(x),
        a,
        b,
        numero_intervalo
                  )
    return numer/denom
def coefs_comb(f, funcs, a, b, numero_intervalo):
    list_coefs = []
    for gk in funcs:
        numer = trapz(
            lambda x: f(x) * gk(x),
            a,
            b,
            numero_intervalo
            )
        denom = trapz(
            lambda x: gk(x) * gk(x),
            a,
            b,
            numero_intervalo
                    )
        ck = numer/denom
        list_coefs.append(ck)
    return list_coefs
        
if __name__ == '__main__':
    
    # Exemplo 01:
    a = -1.02966
    b=1.07575
    n = 256

    def f1(x): return 1
    def f2(x): return x
    def f3(x): return x**2
    def f4(x): return x**3
    
    def g1(x): return f1(x)

    a_21 =  coef(f2, g1, a, b, n)
    print(f'{a_21},')
    def g2(x): return f2(x) - a_21*g1(x)
    
    a_31 = coef(f3, g1, a, b, n)
    a_32 = coef(f3, g2, a, b, n)
    print(f'{a_31},')
    print(f'{a_32},')
    def g3(x): return f3(x) - a_31*g1(x) - a_32*g2(x)
    
    a_41 = coef(f4, g1, a, b, n)
    a_42 = coef(f4, g2, a, b, n)
    a_43 = coef(f4, g3, a, b, n)
    print(f'{a_41},')
    print(f'{a_42},')
    print(f'{a_43},')
   
    def g4(x): return f4(x) - a_41*g1(x) - a_42*g2(x) - a_43*g3(x)
    
    
        
        