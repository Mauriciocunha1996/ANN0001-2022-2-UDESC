/*Encontre o menor inteiro positivo n para o qual
	|f(xn)|<2.12273⋅10−13 ,
onde xn é a n-ésima aproximação para a raiz da função
	f(x)=πx−e^x
obtida pelo método da bisseção usando [0.087385,0.968294] como intervalo inicial.
Dica: Se você encontrar n≥64, insira 64 no campo de respostas.*/

/*Encontre o menor inteiro positivo n para o qual
	|f(xn)|<3.33897⋅10−08,
onde xn é a n-ésima aproximação para a raiz da função
	f(x)=2(x+1)(x−0.5)(x−1)
obtida pelo método da bisseção usando [−1.721694,1.490945] como intervalo inicial.*/

#include <stdio.h>
#include <math.h>

void bissection(double (*f)(double),double a,double b, int n, double tol) {
    double fa = f(a);
    double fb = f(b);

    if(fa*fb >=0) {
        printf("voce nao pode usar esse intervalo");
        return;
    } else {
        for(int i=0;i<n;i++) {
            double m = 0.5*(a+b);
            double fm = f(m);

            if(fabs(fm) ==0) {
                printf("voce encontrou uma raiz r= %.16f",fm);
                return;
            }

            printf("x_%d = %.16f\n",i+1,m);

            if(fabs(fm)<tol) {
                printf("atingiu a tolerancia => x_%d = %.16f\n",i+1,m);
                return;
            }
            if(fa*fm<0) {
                b = m;
            } else {
                a = m;
            }

            

        }
    }
}

double f(double x) {
    return M_PI * x - exp(x);
}

int main() {


    double a = 0.087385;
    double b = 0.968294;
    
    int n = 70;
    
    double tol = 2.12273e-13;

    bissection(f,a,b,n,tol);


    return 0;
}