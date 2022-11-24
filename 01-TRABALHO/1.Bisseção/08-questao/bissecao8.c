/*Encontre o menor inteiro positivo n para o qual
	|bn−an|<2.27683⋅10−08,
onde [an,bn] é o intervalo usado, no método da bisseção, para encontrar a n-ésima aproximação para a raiz da função
	f(x)=x3−7x2+14x−7
no intervalo [3.382848,4.25091]*/
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
    return (pow(x,3))-7*(pow(x,2))+14*x-7;
}

int main() {


    double a = 3.382848;
    double b = 4.25091;
    
    int n = 70;
    
    double tol = 2.27683e-08;

    bissection(f,a,b,n,tol);


    return 0;
}