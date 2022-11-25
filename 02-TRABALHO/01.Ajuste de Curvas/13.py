import numpy as np

#a*2^(bx)

def best_poly(x, y, grau = 1):
    k = grau + 1
    A = [[0 for _ in range(k)] for _ in range(k)]
    B = [sum(y)]
    n = len(x)
    cache = {}
    for i in range(k):
        for j in range(k):
            p = i + j
            if (p == 0):
                A[0][0] = n
                continue
            if p not in cache:
                cache[p] = sum([xi ** p for xi in x])
            A[i][j] = cache[p]
        if i > 0:
            B.append(sum([yi * xi ** i for xi, yi in zip(x, y)]))
    return np.linalg.solve(A, B)

def poly(x, a, b):
    return a * 2 ** (b * x)

def build_func(a, b):
    def temp(x):
        return poly(x, a, b)
    return temp

if __name__ == '__main__':
    x = [0.0086, 0.0589, 0.1564, 0.2008, 0.2483, 0.2902, 0.3376, 0.4143, 0.4462, 0.5451, 0.5842, 0.6362, 0.7146, 0.7644, 0.8085, 0.8825, 0.9362, 0.9831, 1.0476, 1.0697, 1.157, 1.17, 1.227, 1.281, 1.3735, 1.4245, 1.4478, 1.5373, 1.5778, 1.6546, 1.7064, 1.7275, 1.7903, 1.8857, 1.8898, 1.9718]
    y = [4.9464, 7.8116, 6.441, 6.5787, 5.9823, 6.7021, 7.0066, 6.545, 8.4708, 8.6355, 8.4441, 8.1603, 13.5913, 11.9899, 13.8446, 12.7251, 13.7423, 15.2408, 15.5823, 17.4124, 17.7482, 17.7981, 18.4494, 20.9402, 22.6807, 23.9732, 24.9297, 27.8104, 29.2137, 29.8556, 35.0688, 34.1774, 37.0202, 41.0611, 41.0775, 45.0906]
    values = [0.3299, 0.672, 0.7473, 1.1852, 1.9439]
    y_ = np.log(y)
 
    grau = 1

    a0, a1 =  best_poly(x, y_, grau)

   # print(f'{a0 = } e {a1 = }')

    a = np.exp(a0)
    b = a1/np.log(2)

    print(f'{a = } e {b = }')

    p = build_func(a, b)


    
    for xi_v in values:
        print(f'{p(xi_v)}, ')
        
        
"""Encontre os coeficientes a e b da função exponencial y=a2bx que melhor se aproxima da seguinte lista de 36 pontos
(0.0338,4.8525), (0.0911,5.1324), (0.1412,4.5248), (0.2002,5.3759), (0.2519,6.0774), (0.2944,7.2223), (0.3631,6.1928), (0.4003,7.165), (0.455,7.2011), (0.5036,4.9567), (0.586,8.3868), (0.6294,8.1903), (0.7162,9.1576), (0.7225,9.63), (0.7947,10.2223), (0.8579,9.2097), (0.9166,13.4057), (0.9991,12.2236), (1.004,12.7509), (1.063,11.0904), (1.146,13.9157), (1.1966,15.7055), (1.2518,17.125), (1.3027,16.8769), (1.3728,21.9679), (1.4045,19.9439), (1.4949,22.2668), (1.5352,24.8677), (1.5889,21.5155), (1.6627,26.5412), (1.6715,26.1364), (1.7357,29.2421), (1.8123,30.8769), (1.847,31.6285), (1.9148,34.422) e (1.9704,36.5564)
Em seguida, calcule o valor de y para os seguintes valores de x:
x=0.4607, x=0.9263, x=0.9461, x=1.2634  e  x=1.938"""