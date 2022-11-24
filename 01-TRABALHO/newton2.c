#include<stdio.h>
#include<math.h>

#define MAX 700

void newton(double (*f)(double), double (*df)(double), double x0, int n){
	double vetor[MAX];
	 for(int i = 0; i < n; i++){
		double dfx0 = df(x0);
		if(dfx0 == 0){
			break;
			
		}
		double xi = x0 - f(x0) / df(x0);
		printf("x_%d = %.16f\n", i + 1, xi);
		x0 = xi;
	 }
	 /*int size = sizeof(vetor)/sizeof(vetor[0]);
	 	 for(int i = 0; i < size; i++){
			printf("x_%d = %.16f\n", vetor[i + 1]);
			i = i + 25;*/
}

int main(){
	double f(double x){
		return exp(5*x)-2;
	}
	double df (double x){
		return 5*exp(5*x);
	}
	double x0 = -1.16156146;
	int n = 700;
	
	newton(f, df, x0, n); //f = função, x0 = estimativa inicial, n = número de iterações
}