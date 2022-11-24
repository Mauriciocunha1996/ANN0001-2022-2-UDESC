from cmath import sin
import numpy as np



def f(x):
    return np.sin(x)**3- 3*np.sin(x)**2+np.sin(pow(x,2)) + 4


def poly(x, y):
    n = len(x) - 1
    A = []
    for xi in x:
        row = [1]
        for j in range(1, n + 1):
            row.append(xi**j)
        A.append(row)
    return np.linalg.solve(A, y)


def p(x, coefs):
    first = coefs[0]
    return first + sum([ai*x**j for j, ai in enumerate(coefs[1:], 1)])


if __name__ == '__main__':
    x = [-3.024, -1.855, -0.47, 1.627, 3.318]
    y = []

    for i in x:
        y.append(f(i))

    np.set_printoptions(suppress=True)
    coefs = poly(x, y)
    print(coefs)
print(abs(f(-2.789) - p(-2.789, coefs)))
print(abs(f(-2.543) - p(-2.543, coefs)))
print(abs(f(-1.421) - p(-1.421, coefs))) #pontos
	