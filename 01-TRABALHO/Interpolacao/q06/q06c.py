import numpy as np


def f(x):
    return (np.cos(x)**3)+(2*np.cos(x)**2)+1


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
    x = [-2.908, -1.671, -1.163, -0.098, 0.836, 1.778, 2.25, 2.931, 4.211]
    y = []

    for i in x:
        y.append(f(i))

    np.set_printoptions(suppress=True)
    coefs = poly(x, y)
    print(coefs)

print(abs(f(-0.638) - p(-0.638, coefs)))
print(abs(f(2.272) - p(2.272, coefs)))
print(abs(f(2.389) - p(2.389, coefs)))
print(abs(f(3.001) - p(3.001, coefs)))
print(abs(f(3.684) - p( 3.684, coefs)))#pontos
	