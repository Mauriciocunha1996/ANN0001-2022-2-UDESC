#include<stdio.h>
#include<math.h>

#define ROWS 3
#define COLS 3


void print_matrix(double matrix[ROWS][COLS]){
	  for(int i = 0; i < ROWS; i++){
        for(int j = 0; j < COLS; j++){
            printf("%.16f, ", matrix[i][j]);
        }
        printf("\n");
    }
}
void gauss(double E[ROWS][COLS]){
	for(int j = 0; j < COLS - 1; j++){ //COLS - 1 até a antepenultima
		for(int i = j; i < ROWS; i++){
			if(E[i][j] != 0){
				if(i != j){
					// é preciso trocar linhas
					for(int k = 0; k < COLS; k++){
						double temp = E[i][k];
						E[i][k] = E[j][k];
						E[j][k] = temp;
					}
				}
				//aplicar operações elementares em linha
				// a * Lj + Lm -> Lm
				for(int m = j+1; m < COLS; m++){
					double a = -E[m][j]/E[j][j];
					for(int n = j; n < COLS; n++){
						E[m][n] += a * E[j][n];
					}
				}
				print_matrix(E);
				printf("\n");
				break;
			}
		}
	}
}
int main(){
	double E[ROWS][COLS] = {
        {3, 5, -7},
        {5, -8, -8},
        {-2, 6, -6}
    };

	print_matrix(E);
	printf("\n");
	gauss(E);

	//reverse_sub(E);
}