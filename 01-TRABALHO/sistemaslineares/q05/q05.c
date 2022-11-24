#include <stdio.h>

#define L 4
#define C 4


//so funciona para sistemas nxn
void jacobi(double A[L][C], double B[L], double chute[L], int n){
    double next[L];
    for(int k=0;k<n;k++){
        for(int i=0;i<L;i++){
            double bi=B[i];
            for(int j=0;j<C;j++){
                if(j!=i) bi-=A[i][j]*chute[j];
            }
            bi/=A[i][i];
            printf("x_%d(%d) = %.16f | ", i+1, k+1, bi);
            next[i]=bi;
        }
        printf("\n");
        //atualizar o chute
        for(int i=0;i<L;i++) chute[i]=next[i];
    }
}

int main(){
    double A[L][C]={{-7.82, -0.13, 1.06, -4.85},{1.4, -11.18, -4.28, 3.73},{0.59, -3.23, -8.19, -2.6},{0.59, -1.22, 3.89, -7.47}};
    double B[L]={4.24, -0.4, -0.93, 2.05}; // result

    double chute[L]={2.46, 4.95, -3.68, -3.09}; // x0
    int n=26;

    jacobi(A, B, chute, n);

    return 0;
}