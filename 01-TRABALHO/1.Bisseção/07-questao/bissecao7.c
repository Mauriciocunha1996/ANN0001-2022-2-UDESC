/*Encontre o menor inteiro positivo n para o qual
	|bn−an|<1.81116⋅10−13,
onde [an,bn] é o intervalo usado, no método da bisseção, para encontrar a n-ésima aproximação para a raiz da função
	f(x)=ex−2x2+x−1.5
no intervalo [0.975692,1.750452].*/
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

            if(fabs(b - a) < tol) {
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
    return exp(x)-2*(pow(x,2))+x-1.5;
}

int main() {


    double a = 0.946184;
    double b = 1.84076;
    
    int n = 70;
    
    double tol = 1.74739e-09;

    bissection(f,a,b,n,tol);


    return 0;
}