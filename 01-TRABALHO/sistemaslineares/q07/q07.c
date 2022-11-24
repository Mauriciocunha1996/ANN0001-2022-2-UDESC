#include <stdio.h>
#include <math.h>
#define L 4
#define C 4

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
    double A[L][C]={{-10.22, 4.38, -0.51, 4.12}, {-3.85, 12.39, -4.36, -2.98}, {1.21, 1.81, -8.7, 4.48}, {-4.22, 2.16, 3.37, 10.96}};
    double B[L]={4.53, -0.53, -1.78, 2.5}; // result

    double chute[L]= {-3.63, -2.56, -4.59, 0.79}; //x0
    int n=25;

    jacobi(A, B, chute, n);

    return 0;
}