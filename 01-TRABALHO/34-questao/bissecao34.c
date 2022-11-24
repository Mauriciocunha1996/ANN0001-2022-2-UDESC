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
	double f(double h)
	{
    double r1 = 2.33;
    double r2 = 5.71;
    double pt = 470.47;
    double pw = 1000.0;
    double H = 7.63;
    double x = H*r1/(r2-r1);

    return pt * ((H) * (pow(r2, 2) + pow(r1, 2) + r1 * r2)) - pw * (H - h) * ((pow(r1, 2) + (2* (pow(r1, 2) * h)/ x) + pow(h,2)*pow(r1,2)/pow(x,2)+ pow(r2,2) + r2*r1 + h*r2*r1/x));
	}

	double a = 0;
	double b = 7.63;
	int n = 12;

	bissection(f, a, b,n);


    return 0;
}