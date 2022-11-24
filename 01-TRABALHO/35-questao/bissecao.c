#include <stdio.h>
#include <math.h>

#define V 143.35
#define L 7.19
#define r 4.9

void bissection(double (*f)(double),double a,double b, int n) {
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

            /*if(fabs(fm)<tol) {
                printf("atingiu a tolerancia => x_%d = %.16f\n",i+1,m);
                return;
            }*/
            if(fa*fm<0) {
                b = m;
            } else {
                a = m;
            }

            

        }
    }
}

int main() {

	//exemplo crescimento populacional
	//taxa de natalidade
	double f(double h)
	{
    return L*((0.5*M_PI*pow(r,2)) - pow(r,2)*asin(h/r)- h*(sqrt(pow(r,2)-pow(h,2))))-V;
	}

	double a = 0;
	double b = 4.9;
	int n = 12;

	bissection(f, a, b,n);


    return 0;
}