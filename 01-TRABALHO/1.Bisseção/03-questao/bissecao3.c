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
    return pow(x,4) - 2*(pow(x,3)) - 3*(pow(x,2)) + 3*x + 2;
}

int main() {

    //int vec[100] = {2, 3, 6, 7, 8, 9, 10, 15, 16, 19, 22, 23, 27, 28, 29, 30, 32, 36, 38, 39};
    //int vec[4] = {2, 4, 5, 6};

    double a = -1.83737;
    double b = 1.81492;
    
    //int n = 4;
    //int n = 8;
    //int n = 11;
    //int n = 15;
    int n = 39;
    
    double tol = 0.000000001;

    bissection(f,a,b,n,tol);
    //printf(" \n Valor em vetor: \n");


    return 0;
}