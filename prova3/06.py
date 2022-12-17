import math


p0 = 0.00123
birth_rate = 0.01512
death_rate = 0.00794
rebel_rate = 0.13203

def rk4(f, x0, y0,x_values, n):
    r = []
    h = x_values[0] - x0
    for _ in range(n):
        #realizar as iterações
        if (_>=1):
            h = x_values[_] - x_values[_-1]
        m1 = f(x0, y0)
        m2 = f(x0 + h/2, y0 + (h/2)*m1)
        m3 = f(x0 + h/2, y0 + (h/2)*m2)
        m4 = f(x0 + h, y0 + h *m3)
        yk = y0 + h * (m1+2*m2+2*m3+m4)/6
        #atualizando os valores
        x0 = x_values[_]
        y0 = yk
        #colocando valores na lista
        r.append((x0, y0))
    return r
    
# modificar valores de r e lambd    
def f(p, t):
    #rebel_rate = 0.16784
    #birth_rate = 0.01721
    k = rebel_rate * birth_rate
    return k * (1 - t)

# modificar valor de p0

''''
t0 = 0
p0 = 0.00179




'''
t0 = 0
#p0 = 0.00123



t_values = [0.11299, 0.79692, 1.44614, 2.13831, 3.1643, 3.52778, 4.37931, 4.80898, 5.43523, 6.49985, 6.79306, 7.46289, 8.46815, 8.95532, 9.89185, 10.27977, 10.96731, 11.60364, 12.22769, 12.91282, 13.69941, 14.34958, 15.15249, 15.64235, 16.30494, 16.77002, 17.69033, 18.35911, 19.10617, 19.71142, 20.086, 21.14492, 21.5311, 22.41854, 23.07331, 23.59597, 24.10593, 25.22186, 25.82023, 26.08354, 26.84278, 27.83018, 28.16116, 28.81803, 29.61537, 30.23223, 30.76192, 31.90512, 32.42889, 32.96142, 33.59157, 34.30236, 35.17178, 35.51891, 36.1029, 37.14641, 37.50453, 38.3654, 39.17469, 39.80424, 40.38057, 41.26631, 41.87749, 42.11748, 43.0662, 43.79445, 44.30646, 44.99278, 45.66898, 46.10849, 46.8194, 47.8849, 48.43862, 48.9386, 49.44803, 50.50545, 50.87362, 51.54435, 52.32843, 53.00588, 53.88319, 54.44973, 54.81631, 55.86476, 56.16838, 57.22611, 57.87289, 58.22361, 58.82238, 59.45339, 60.32982, 61.1098, 61.42005, 62.49162, 63.07638, 63.91254, 64.5515, 65.2012, 65.46532, 66.56272, 67.21792, 67.516, 68.47043, 68.92154, 69.60362, 70.25811, 70.76688, 71.57111, 72.31864, 73.22181, 73.83436, 74.44609, 75.22923, 75.68126, 76.45251, 76.82756, 77.56613, 78.2478, 79.18068, 79.65957, 80.57015, 80.79752, 81.69623, 82.16059, 83.03721, 83.57147, 84.15768, 84.98003, 85.80055, 86.48318, 87.15007, 87.69015, 88.42008, 88.93117, 89.91879, 90.12591, 90.84564, 91.53455, 92.54039, 93.13224, 93.72865, 94.44441, 94.91976, 95.7949, 96.37128, 96.9601, 97.72388, 98.37842, 99.0895, 99.70887]
n = 150

r = rk4(f, t0, p0, t_values, n)

runge = []
for yi in r:
    runge.append(yi[1])


''''
t0 = 0





'''
# solução exata:
# modificar valores de r, lambd e coef 

''''Considerando p(t0)=p0, com t0=0, p0=0.00159, λ=0.01046, μ=0.006 e r=0.11114, use o método de Runge-Kutta de ordem 4 para encontrar aproximações para a solução p(t) nos instantes'''
def p(t):
    #rebel_rate = 0.16784
    #birth_rate = 0.01721
    k = rebel_rate * birth_rate
    # resolver:
    # solve p'(t) = k * (1 - p(t)), p(0) = p0
    # no wolfram, substituindo o valor de p0 dado na questao, então:
    #solve p'(t) = k * (1 - p(t)), p(0) = 0.00179
    #death_rate = 0.00507

    #result em wolpram alpha, apos fazer "solve p'(t) = k * (1 - p(t)), p(0) = 0.00159"
    return 1 - death_rate * math.exp(-k*t)
    
for i in range(n):
    print(f"{runge[i]}, {abs(0)},")



''''
obs: dp(t)dt=rλ(1−p(t)). <<-- isso é o que é dado no enunciado

onde r = rebel_rate

lambda = birth_rate

sendo assim, k = r * lambda
k = rebel_rate * birth_rate

assim, dp(t)dt=k * (1−p(t)), simplificando: 
p'(t) = k * ( - p(t)), p(0) = p0 
'''




''''
t0 = 0



'''