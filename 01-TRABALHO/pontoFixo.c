#include<stdio.h>
#include<math.h>

/*
Provar que sequencia converge para o ponto fixo da função
como usar a tecnica do ponto fixo:
1- Use o metodo do ponto fixo para encontar uma raiz poara funçao:
              f(x) = x^2 - 2
solução: encontre ums raiz para f, significa resolver f(x)  = 0
tentativa e erro
f(x)=0 <==> x^2-2=0 <==> x^2+x^2-2 = x^2
       <==> (2x^2)/2 -2 = x^2 <=> (2x^2)/2 = x^2*/

void fixed_point(double(*f)(double), double x0, int n){
    for(int i=0; i <n; i++){
      x0 = f(x0);
      printf("x_%d = %.16f \n", i+1, x0);
    }
}
double f(double x){
    return pow(x,2) - 2;
}
double g(double x){
    return ((3*(pow(x,4))+2*(pow(x,2))+3)/(4 * pow(x, 3) + 4 * x - 1));
}
int main(){
  int n = 8;
  double x0 = 1.85682;

  fixed_point(g, x0, n);
	return 0;
  
}
 