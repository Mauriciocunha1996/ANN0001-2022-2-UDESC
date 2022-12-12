import math
import numpy as np

def trapz(f, a, b, n):
    h = abs(b - a) / n
    sum_fx = 0

    for i in range(1, n):
        sum_fx += f(a + i * h)

    return (f(a) + 2 * sum_fx + f(b)) * h / 2


def dif_div(x,y):
    Y = [yi for yi in y]
    A = [y[0]] #lista de coeficientes
    n = len(x)
    for i in range(n-1):
        for j in range(n-1-i):
            numer = Y[j+1] - Y[j]
            demon = x[j+1+i] - x[j]
            y = numer/demon
            Y[j] = y
        A.append(Y[0])
    return A

def build_func(x_coord, coeffs):
    n = len(coeffs)
    def func(x): #polinomio interpolador
        soma = coeffs[0]
        for i, ci in enumerate(coeffs[1:], 1):
            prod = ci
            for j in range(i):
                prod *= (x - x_coord[j])
            soma += prod
        return soma
    return func           
    
def aprox(f, f_list):
    n = len(f_list)
    A = [[0 for _ in range(n)] for _ in range(n)]  #A é simetrica
    B = []
    for i in range(n):
        for j in range(i, n): #elementos na diagonal da matriz 
             def f_ji(x):
                return f_list[j](x) * f_list[i](x)
             #altere dependendo do metodo de integração
             a = -1 #altere dependendo do dominio
             b = 1
             num_intervals = 256 #número de subintervalos 
             a_ij = trapz(f_ji, a, b, num_intervals)
             #não altere mais
             A[i][j] = a_ij
             A[j][i] = a_ij
        def ff_i(x):
            return f(x) * f_list[i](x)
        #altere dependendo do metodo de integração
        a = -1 #altere dependendo do dominio
        b = 1
        num_intervals = 256 #número de subintervalos 
        b_i = trapz(ff_i, a, b, num_intervals)
        B.append(b_i)
    return np.linalg.solve(A,B)

def build_g(coefs, f_list):
    def func_g(x):
        return sum (ci* fi(x) for ci, fi in zip (coefs, f_list))
    return func_g

def T0(x):
    return 1


def T1(x):
    return x

def T2(x):
    return 2 * x**2 - 1

def T3(x):
    return 4 * x**3 - 2 * x - 1


def roots(n):
        if n>=1:
            return [math.cos((2*k+1)*math.pi/(2*n)) for k in range(n)]
        

def chebyshev_poly(n, x):
    # Polinômio recursivo de Chebyshev: função g_chebyshev
    
    if n < 0:
        return np.zeros(x.shape)
    elif n == 0:
        return np.ones(x.shape)
    elif n == 1:
        return x
    else:
        return 2 * x * chebyshev_poly(n - 1, x) - chebyshev_poly(n - 2, x)

if __name__=='__main__':
    
    def f(x):
        if x>=1:
            return x**2 + 1
        return math.exp(x**2)
    f_list = [T0, T1, T2, T3]
    
    coefs = aprox(f, f_list)
    g = build_g(coefs, f_list)
  
    
    # deg = 4 #grau do polinomio interpolador
    # n= deg + 1
    
    # #as raízes do polinômio de Chebyshev de grau deg +1
    # x = roots(n)
    
   
            
    
    # y = [f(xi) for xi in x]
    
    # coefs = dif_div(x, y)
    
    # p = build_func(x,  coefs)
    
    # #polinomio interpolador aleatorio
    
    # x_a = sorted([-1 + 2 * np.random.random() for _ in range(n)])
    # y_a = [f(xi) for xi in x_a]
    # coefs_a = dif_div(x_a, y_a)
    # p_a = build_func(x_a, coefs_a)
    
    
    
    
    
