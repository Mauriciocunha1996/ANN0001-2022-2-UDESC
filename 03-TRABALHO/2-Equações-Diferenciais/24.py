"""Em um circuito com tensão aplicada E e com resistência R, indutância 
L e capacitância C em paralelo, a corrente i satisfaz a equação diferencial
didt=Cd2Edt2+1RdEdt+1LE.
Suponha que C=0.2311farads, R=1.3534ohm, L=1.5026henrie e que a tensão seja dada por
E(t)=e−0.0549πtsin(2t−π).
Se i(t0)=i0, com t0=0 e i0=0, use o método de Heun para encontrar estimativas
para a corrente i nos pontos
t1=0.0853, t2=0.124, t3=0.2613, t4=0.3842, t5=0.4704, t6=0.5809, t7=0.6249, 
t8=0.7385, t9=0.8313, t10=0.9542, ...... t149=14.8388 e t150=14.939."""

import numpy as np



def euler(f, x0, y0, h, n):
    vals = []
    for k in range(n):
        y0 += h*f(x0, y0)
        x0 += h
        vals.append([x0, y0])
    return vals


# b = 1
def euler_mid(f, x0, y0, h, n):
    vals = []
    for _ in range(n):
        m1 = f(x0, y0)
        m2 = f(x0 + h / 2, y0 + (h/2) * m1)
        y0 += h*m2
        x0 += h
        vals.append([x0, y0])
    return vals


# b = 1/2
def heun(f, x0, y0, h, n):
    vals = []
    for _ in range(n):
        m1 = f(x0, y0)
        m2 = f(x0 + h, y0 + h*m1)
        y0 += h*(m1+m2)/2
        x0 += h
        vals.append([x0, y0])
    return vals


# b = 2/3
# def ralston(f, x0, y0, h, n):
#     vals = []
#     for _ in range(n):
#         m1 = f(x0, y0)
#         m2 = f(x0 + 0.75*h, y0 + 0.75*h*m1)
#         y0 = h*(m1 + 2*m2)/3
#         x0 += h
#         vals.append([x0, y0])
#     return vals


# padrao = euler_mid
def rk2(f, x0, y0, h, n, b=1.0):
    # b = 1 => metodo = euler_mid
    # b = 1/2 => metodo = heun
    # b = 2/3 => metodo = ralston
    vals = []
    a = 1-b
    p = 1/(2*b)
    q = p
    for _ in range(n):
        m1 = f(x0, y0)
        m2 = f(x0 + p*h, y0 + q*h*m1)
        y0 += (a*m1 + b*m2)*h
        x0 += h
        vals.append([x0, y0])
    return vals


def rk2_h_variavel(f, x0, y0, n, b, x_values):
    # b = 1 => metodo = euler_mid
    # b = 1/2 => metodo = heun
    # b = 2/3 => metodo = ralston
    vals = []
    a = 1-b
    p = 1/(2*b)
    q = p
    for i in range(n):
        if i == 0:
            h = x_values[0] - x0
        else:
            h = x_values[i] - x_values[i-1]
        m1 = f(x0, y0)
        m2 = f(x0 + p*h, y0 + q*h*m1)
        y0 += (a*m1 + b*m2)*h
        x0 += h
        vals.append([x0, y0])
    return vals


def diff(a, b):
    return sum((ai - bi)**2 for ai, bi in zip(a, b))


def f(x, y):
    return y * (1 - x) + x + 2


def g(t, i):
    c = 0.2311
    r = 1.3534
    l = 1.5026

    # considerando a função e(t) = e^(-e_value*pi*t)*sin(2*t-pi)
    # se e^(-0.0549*pi*t) => e_value = 0.0549
    e_value = 0.0549

    def e(t):
        return np.exp(-e_value*np.pi*t)*np.sin(2*t-np.pi)

    def e_(t):
        return np.exp(-e_value*np.pi*t)*(2*np.cos(np.pi-2*t)+e_value*np.pi*np.sin(np.pi-2*t))

    def e__(t):
        return np.exp(-e_value*np.pi*t)*((4-pow(e_value, 2)*pow(np.pi, 2))*np.sin(np.pi-2*t)-4*e_value*np.pi*np.cos(np.pi-2*t))

    return c*e__(t) + (1/r)*e_(t) + (1/l)*e(t)


if __name__ == '__main__':

    x0, y0 = 0,0
    h = 0.101
    n = 150
    b = 1/2
    t_values = [0.0853, 0.124, 0.2613, 0.3842, 0.4704, 0.5809, 0.6249, 0.7385, 0.8313, 0.9542, 1.0592, 1.1208, 1.2733, 1.3709, 1.4871, 1.5453, 1.6845, 1.7398, 1.8134, 1.9715, 2.0754, 2.1341, 2.233, 2.3762, 2.4268, 2.5646, 2.6733, 2.7102, 2.8223, 2.9485, 3.0575, 3.1633, 3.2244, 3.3146, 3.4477, 3.5724, 3.6405, 3.7547, 3.8669, 3.9403, 4.0359, 4.1732, 4.2202, 4.314, 4.4484, 4.5784, 4.6576, 4.7147, 4.8381, 4.9705, 5.0663, 5.1625, 5.2509, 5.3689, 5.4424, 5.5533, 5.6507, 5.7777, 5.8778, 5.9369, 6.0876, 6.1154, 6.2669, 6.3631, 6.4553, 6.5233, 6.6627, 6.7321, 6.8601, 6.9744, 7.0745, 7.1343, 7.2402, 7.3388, 7.4389, 7.5805, 7.6757, 7.7479, 7.8129, 7.9592, 8.0449, 8.1154, 8.2778, 8.3591, 8.4511, 8.5892, 8.6297, 8.7619, 8.8552, 8.9836, 9.0236, 9.1169, 9.2825, 9.3886, 9.4183, 9.5143, 9.6862, 9.7333, 9.8875, 9.925, 10.016, 10.1184, 10.2413, 10.3248, 10.4212, 10.5266, 10.6776, 10.7148, 10.8643, 10.9433, 11.0458, 11.1401, 11.2874, 11.3226, 11.4754, 11.5213, 11.6695, 11.7255, 11.8501, 11.9412, 12.0496, 12.1685, 12.23, 12.3322, 12.4383, 12.559, 12.6506, 12.7385, 12.8798, 12.9659, 13.0219, 13.1591, 13.2528, 13.3658, 13.4374, 13.5385, 13.6792, 13.7737, 13.8509, 13.9739, 14.0416, 14.11, 14.2584, 14.3556, 14.4384, 14.5792, 14.683, 14.7447, 14.8388, 14.939]
    """observar o valor de b na função para qual médoto é usado:
    --> b = 1 => metodo = euler_mid
    --> b = 1/2 => metodo = heun
    --> b = 2/3 => metodo = ralston"""
    
    
    # metodo1 = euler(f, x0, y0, h, n)
    # metodo2 = euler_mid(f, x0, y0, h, n)
    # metodo3 = heun(f, x0, y0, h, n)
    # metodo4 = ralston(f, x0, y0, h, n)
    # metodo5 = rk2(g, x0, y0, h, n, b)
    metodo6 = rk2_h_variavel(g, x0, y0, n, b, t_values)

    indice = [i for i in range(n)]
    lista_x, lista_y = zip(*metodo6)

    for i, xi, yi in zip(indice, lista_x, lista_y):
        # print(f'x{i} = {xi} => y{i} = {yi}')
        print(f'{yi},', end='')

 