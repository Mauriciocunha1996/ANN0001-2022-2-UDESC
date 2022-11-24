#include <stdio.h>
#include <math.h>
#define L 3
#define C 3

void jacobi(double A[L][C], double B[L], double chute[L], int n){
    for(int k=0;k<n;k++){
        for(int i=0;i<L;i++){
            double bi=B[i];
            for(int j=0;j<C;j++){
                if(j!=i) bi-=A[i][j]*chute[j];
            }
            bi/=A[i][i];
            printf("x_%d(%d) = %.16f | ", i+1, k+1, bi);
            chute[i]=bi;
        }
        printf("\n");
    }
}


// INSERIR O TAMANHO DA MATRIZ EM DEFINE
//***************************************************************************

int main(){
    double A[L][C]={{-4.28, -1.15, -1.16},{2.01, 7.81, -3.83},{-0.65, 1.43, -4.05}};
    double B[L]={1.08, 2.65, 1.26}; // result

    double chute[L]= {-3.19, 4.28, 0.93}; //x0
    int n=19;

    jacobi(A, B, chute, n);

    return 0;
}