import math
import numpy as np

def lagrange(x, y):
    for i in range(len(x)):
        a = 1
        for j in range(len(x)):
            if i != j:
                a *= (x[i]-x[j])
        print(y[i]/a)


if __name__ == '__main__':
    # x = [-1.823, -0.45, 0.724, 1.497, 2.787, 3.853, 5.34, 6.035]  # coordenadas x do ponto
    # y = [0.564, 0.967, 0.941, 0.732, -0.161, -0.891, -0.611, 0.007]  # coordenadas y do ponto

    x = []
    y = []
    z = [0.24, 1.011, 1.522, 2.438, 3.402, 3.918, 4.438]

    def f(x):
        return  4 + math.sin(x) - x**2 / 30

    for i in z:
        x.append(i)
        y.append(f(i))

    lagrange(x, y)