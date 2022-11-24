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
    double f(double h){
        //double e = exp(x); 
        //return 1-((pow(130.65,2))/(9.81*(pow(8.09*x,3)+((pow(0.5*x,2))*(pow(0.5*x,2))*(pow(0.5*x,2))))))*(8.09+x);
        //return 1-((pow(130.65,2))/(9.81*pow((8.09*x+((pow(x,2))/2)),3)))*8.09+x;
        //return (sqrt(2*9.81*h)*(tanh(((sqrt(2*9.81*h))/(2*3.03))*5.16)))-10.18;
		/*double V = 213.02;
		double R = 7.33;
		return M_PI*pow(h,2)*((3*R-h)/3);*/
		return (((9.81*m)/21.09)*(1-exp(-((21.09/m)*8.58))))-30.93;
    }
    //intervalo iniial
    double a = 29.33;
    double b = 197.3;

    int n = 9; // número de iterações

    false_position(f,a,b,n);
}