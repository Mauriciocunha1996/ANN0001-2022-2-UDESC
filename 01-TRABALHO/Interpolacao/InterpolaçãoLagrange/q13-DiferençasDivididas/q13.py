def dif_div(x, y):
    num = len(x)
    Y = [yi for yi in y]
    coefs = [y[0]]
    for j in range(num -1):
        for i in range(num - 1 - j):
            numerador = Y[i + 1] - Y[i]
            denominador = x[i + 1 + j] - x[i]
            div = numerador / denominador
            Y[i] = div
        coefs.append(Y[0])
    return coefs

def poly(t, x, coefs):
    val = 0
    num = len(coefs)
    for i in range(num):
        prod = 1
        for j in range(i):
            prod *= (t - x[j])
        val += coefs[i] * prod
    return val

def build_func(x, coefs):
    def temp(t):
        return poly(t, x, coefs)
    return temp


if __name__ == '__main__':

    #ex
    x = [0.316, 0.587, 1.014, 1.795, 2.16, 2.5, 3.051, 3.498, 4.001, 4.345, 4.974, 5.297, 5.789, 6.28, 6.707]
    y = [4.855, 4.541, 3.886, 2.818, 2.454, 2.201, 2.004, 2.063, 2.347, 2.641, 3.259, 3.552, 3.88, 4.0, 3.912]
    coefs = dif_div(x, y)

    #polinomio interpolador da lista de pontos
    p = build_func(x, coefs)

    print(coefs)

    #print(p(1), p(3), p(3), p(4))
   # print(f'{p(0.97244)}')


    #visu
    #import matplotlib.pyplot as plt
    #import numpy as np

    #t = np.linspace(min(x), max(x), 100)
    #pt = [p(ti) for ti in t]

    #plt.scatter(x, y)
    #plt.plot(t, pt)

    #plt.savefig('dif_div.png')