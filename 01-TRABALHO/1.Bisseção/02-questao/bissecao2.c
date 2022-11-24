#include <stdio.h>
#include <math.h>

int bissection(double (*f)(double),double a,double b, int n, double tol) {
    double fa = f(a);
    double fb = f(b);

    if(fa*fb >=0) {
        printf("voce nao pode usar esse intervalo");
        return 0;
    } else {
        for(int i=0;i<n;i++) {
            double m = 0.5*(a+b);
            double fm = f(m);

            if(fabs(fm) ==0) {
                printf("voce encontrou uma raiz r= %.16f",fm);
                return 0;
            }

            printf("x_%d = %.16f\n",i+1,m);

            if(fabs(fm)<tol) {
                printf("atingiu a tolerancia => x_%d = %.16f\n",i+1,m);
                return 0;
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
    return sqrt(x) - cos(x);
}

int main() {

    //int vec[100] = {2, 3, 6, 7, 8, 9, 10, 15, 16, 19, 22, 23, 27, 28, 29, 30, 32, 36, 38, 39};
    //int vec[4] = {2, 4, 5, 6};

    double a =  0.41806;
    double b = 1.11057;

    int n = 18;
    
    double tol = 0.0000000000001;

    bissection(f,a,b,n,tol);
    //printf(" \n Valor em vetor: \n");

    //bissectionvec(f,a,b,n,tol,vec);

    return 0;
}