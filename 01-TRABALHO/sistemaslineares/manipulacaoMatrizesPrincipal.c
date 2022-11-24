#include <stdio.h>
#include <math.h>

#define ROW 4
#define COL 3

void imprimeMatriz(double matriz[ROW][COL]){
    for(int row = 0; row < ROW; row++){
        for(int col = 0; col < COL; col++){
            printf("%.16f ", matriz[row][col]);
        }
        printf("\n");
    }
}

void trocaLinha(double matriz[ROW][COL], int r1, int r2){
        for(int k=0;k<COL;k++){
        double temp = matriz[r1][k];
        matriz[r1][k] = matriz[r2][k];
        matriz[r2][k] = temp;
    }
}

void operacaoEmLinha(double matriz[ROW][COL], int row, double num){
    for(int i = 0; i < COL; i++){
        matriz[row][i] *= num; 
    }
}

void opercaoEmDuasLinhas(double matriz[ROW][COL], int target, int r2, double num){
    for(int i = 0; i < COL; i++){
        matriz[target][i] = (num*matriz[r2][i]) + matriz[target][i];
    }
}

void operacoes(double matriz[ROW][COL]){
    //L1 0
    //L2 1
    //L3 2
	//L4 3

	//-3/2.L4 → L4
	operacaoEmLinha(matriz, 3, (-3.0/2.0));
	//7/9.L3 → L3
	operacaoEmLinha(matriz, 2, (7.0/9.0));
    // −4/7⋅L4+L2→L2
    opercaoEmDuasLinhas(matriz, 1, 3, (-4.0/7.0));
	//-3/7.L1 + L4 → L4
	opercaoEmDuasLinhas(matriz, 3, 0, (-3.0/7.0));

    imprimeMatriz(matriz);
}

int main(){
    double matriz[ROW][COL] = {
		{-3.0, -4.5, -1.4},
        {-4.5, 5.0, 0.14285714285714285},
		{-0.75, -0.25, -0.4},
		{1.3333333333333333, 0.8, -0.625}
    };

    printf("Matriz Original:\n");
    imprimeMatriz(matriz);
    printf("Resultado:\n");
    operacoes(matriz);
    return 0;
}