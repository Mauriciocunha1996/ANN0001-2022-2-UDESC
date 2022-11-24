def lagrange(x,y):
    #retorna yi dividido pelo denominador do polinomio Li
    num=len(x)
    coefs = []
    for i in range(num):
        prod=1
        for j in range(num):
            if i!=j:
                prod*=(x[i] - x[j])
        ci=y[i]/prod
        coefs.append(ci)
    return coefs

def pl(t,x,coefs) -> float:
    soma=0
    num = len(coefs)
    for i in range(num):
        prod=1
        for j in range(num):
            if i!=j:
                prod*=(t-x[j])
        prod*= coefs[i]
        soma+=prod
    return soma


def poly(x, coefs):
    def f(t):
        return pl(t,x, coefs)
    return f


if __name__ == '__main__':
    x=[0.079, 0.808, 1.491, 2.274, 2.64, 3.275, 3.776, 4.602, 4.745, 5.546, 6.127, 6.63]
    y= [4.991, 4.211, 3.188, 2.359, 2.124, 2.009, 2.195, 2.89, 3.033, 3.74, 3.988, 3.94]
    
    # x=[-0.691, 0.247, 0.681]
    # y=[0.07729752396, 0.39600431644 ,0.07940273264]
    
    # x=[1,3]
    # y=[1,-1]
    c = lagrange(x,y)
    print(c)
    lagr=poly(x, c)
    # print(lagrange(x, y))
    #print(lagr(0))

   #import matplotlib.pyplot as plt
    #import numpy as np

    #plt.scatter(x,y)
    #t=np.linspace(min(x), max(x), 100)
    #lt=[lagr(ti) for ti in t]
    #plt.plot(t, lt)
    #plt.savefig('lagrange.png')