#include <stdio.h>

#define L 3
#define C 3


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
    double A[L][C]={{-6.54, 3.85, 1.48},{1.24, -6.2, -3.76},{3.72, -3.12, 8.04}};
    double B[L]={-0.96, -1.71, 3.26}; // result

    double chute[L]={-3.42, -1.53, 1.37}; // x0
    int n=19;

    jacobi(A, B, chute, n);

    return 0;
}