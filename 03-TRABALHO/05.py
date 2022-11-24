

from math import cos, sin, exp, pi, ceil
import numpy as np


a = -3.141592653589793
b = 3.141592653589793
n = 1024
xs = [-2.088, 0.8, 1.383]

def f(x):
    return x * sin(6 * exp(-x**2))

def trapz(f, a, b, n):
    h = abs(b - a) / n
    sum_fx = 0

    for i in range(1, n):
        sum_fx += f(a + i * h)

    return (f(a) + 2 * sum_fx + f(b)) * h / 2


def trapz_romberg(f, a, b, h):
    n = int((b - a) / h)
    soma = 0

    for k in range(1, n):
        soma += f(a + k * h)

    return (h / 2) * (f(a) + 2 * soma + f(b))


def romberg(coluna_f1):
    coluna_f1 = [i for i in coluna_f1]
    n = len(coluna_f1)
    for j in range(n - 1):
        temp_col = [0] * (n - 1 - j)
        for i in range(n - 1 - j):
            power = j + 1
            temp_col[i] = (4 ** power * coluna_f1[i + 1] - coluna_f1[i]) / (4 ** power - 1)
        coluna_f1[:n - 1 - j] = temp_col
        # print(f'F_{j+2} = {temp_col}')
    return coluna_f1[0]


def best_func(f, funcs, a, b, method: ['trapz', 256]):
    k = len(funcs)

    A = [[0 for _ in range(k)] for _ in range(k)]
    B = []

    for i in range(k):
        for j in range(k):
            if j >= i:
                def f_ij(x):
                    return funcs[j](x) * funcs[i](x)

                if method[0] == 'trapz':
                    A[i][j] = trapz(f_ij, a, b, method[1])
                elif method[0] == 'romberg':
                    tam = int(method[1] / 2)
                    hs = [method[2] / 2 ** ki for ki in range(tam)]
                    coluna_f1 = [trapz_romberg(f_ij, a, b, hi) for hi in hs]
                    A[i][j] = romberg(coluna_f1)

            else:
                A[i][j] = A[j][i]

        def ffi(x):
            return f(x) * funcs[i](x)

        if method[0] == 'trapz':
            B.append(trapz(ffi, a, b, method[1]))
        elif method[0] == 'romberg':
            tam = int(method[1] / 2)
            hs = [method[2] / 2 ** ki for ki in range(tam)]
            coluna_f1 = [trapz_romberg(ffi, a, b, hi) for hi in hs]
            B.append(romberg(coluna_f1))

    A = np.array(A, dtype=float)
    B = np.array(B, dtype=float)

    return np.linalg.solve(A, B)



def simps(f, a, b, n):
    if (n % 2 != 0):
        raise ValueError("O número de subintervalos deve ser par")
    soma = 0
    numParabolas = int(n/2)
    h = (b-a) / n
    for k in range(numParabolas):
        x0 = a + (2 * k) * h
        x1 = a + (2 * k + 1) * h
        x2 = a + (2 * k + 2) * h
        soma += (f(x0) + 4 * f(x1) + f(x2))
    soma *= h/3.0
    return soma
    
coeffs = []

c = (1/(2 * pi)) * simps(f, a, b, n)
coeffs.append(c)

for m in range(1, 6):
    am = (1/pi) * simps(lambda x: f(x) * cos(m * x), a, b, n)
    coeffs.append(am)
    bm = (1/pi) * simps(lambda x: f(x) * sin(m * x), a, b, n)
    coeffs.append(bm)
    
for i in range(len(coeffs)):
    print(f"c{i+1} = {coeffs[i]}")
print("-------------------\n")
    
def g(x, coeffs):
    soma = coeffs[0]
    for i in range(1, len(coeffs), 2):
        soma += coeffs[i] * cos(ceil(i/2)*x)
        soma += coeffs[i+1] * sin(ceil(i/2)*x)
    return soma

for xi in xs:
    print(f"x{xi} = {g(xi, coeffs)}")
    
# calculando o erro com o método da quadratura gaussiana: 
# com 10 nós (mudar se necessário)
pontos_n10 = [-0.14887433898163122, 0.14887433898163122, -0.4333953941292472, 0.4333953941292472, -0.6794095682990244, 0.6794095682990244, -0.8650633666889845, 0.8650633666889845, -0.9739065285171717, 0.9739065285171717]
pesos_n10 = [0.29552422471475287, 0.29552422471475287, 0.26926671930999635, 0.26926671930999635, 0.21908636251598204, 0.21908636251598204, 0.1494513491505806, 0.1494513491505806, 0.06667134430868814, 0.06667134430868814]
n10 = zip(pontos_n10, pesos_n10)

# MUDAR a função do erro para a função que está dentro da integral
def func_erro(x):
    return pow((f(x) - g(x, coeffs)), 2)

def quadratura_zip(func_erro, pontos_e_pesos):
    soma = 0
    for x_k, c_k in pontos_e_pesos:
        soma += c_k * func_erro(x_k)
    return soma
    
def change_zip(func_erro, a, b, u):
    return func_erro((b+a)/2 + (b-a)*u/2) * (b-a)/2
    
def g_erro(u):
    return change_zip(func_erro, a, b, u)
    
erro = quadratura_zip(g_erro, n10)

#imprimindo o erro:
print("-------------------\n")
print("Erro: ", erro)