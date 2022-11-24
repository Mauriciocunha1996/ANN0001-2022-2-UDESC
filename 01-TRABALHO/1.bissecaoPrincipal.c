#include <stdio.h>
#include <math.h>

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
	double f(double m){
		return (((9.81*m)/21.09)*(1-exp(-((21.09/m)*8.58))))-30.93;
	}
	double a = 31.92;
	double b = 201.07;
	int n = 12;

	bissection(f, a, b,n);


    return 0;
}