#include <stdio.h>
#include <math.h>


void false_position(double (*f)(double),double a,double b,int n){
    double fa = f(a);
    double fb = f(b);
    if(fa * fb >= 0){
        printf("O Teorema de Bolzano não sabe dizer se existe raiz para f no intervalo [%.16f, %.16f]",a,b);
        return;
    }else {
        double x;
        for(int i =0;i<n;i++){
            x = (a *fb - b * fa) / (fb - fa);
            printf("x_%d = %.16lf\n", i+1,x);
            double fx = f(x);
            if(fx == 0){
                printf("Encontramos uma raiz para f, ela é x = %.16lf",x);
                return;
            }
            if(fa * fx < 0){
                b = x;
                fb = fx;
            }else{
                a = x;
                fa = fx;
            }
        }
    }
}

int main(){
    ouble f(double h)
	{
    double r1 = 2.33;
    double r2 = 5.71;
    double pt = 470.47;
    double pw = 1000.0;
    double H = 7.63;
    double x = H*r1/(r2-r1);

    return pt * ((H) * (pow(r2, 2) + pow(r1, 2) + r1 * r2)) - pw * (H - h) * ((pow(r1, 2) + (2* (pow(r1, 2) * h)/ x) + pow(h,2)*pow(r1,2)/pow(x,2)+ pow(r2,2) + r2*r1 + h*r2*r1/x));
	}
    //intervalo iniial
    double a = 0;
    double b = 7.63;

    int n =11; // número de iterações

    false_position(f,a,b,n);
}