#include<stdio.h>
#include<math.h>

void newton(double (*f)(double), double (*df)(double), double x0, int n){
	 for(int i = 0; i < n; i++){
		double dfx0 = df(x0);
		if(dfx0 == 0){
			break;
			
		}
		double xi = x0 - f(x0) / df(x0);
		printf("x_%d = %.16f\n", i + 1, xi);
		x0 = xi;
	 }
}
int main(){
	double f(double h){
		return (((M_PI*pow(h,2))/3))*(3*7.57-h)-(-(((614.76*((4/3)*M_PI*(pow(7.57,3))))/1000)-((4/3)*M_PI*(pow(7.57,3)))));
	}
	double df (double h){
		return -(M_PI*h*(50*h-757))/50;
	}
	double x0 = 4.75 ;
	int n = 5;
	
	newton(f, df, x0, n); //f = função, x0 = estimativa inicial, n = número de iterações
}