//Matrix Chain Multiplication

#include<stdio.h>
#include<conio.h>

int main(){
	int i, j, k, d, min, x;
	int n = 5;
	int p[] = {5, 4, 6, 2, 7};
	int m[n][n], s[n][n];
	
	for(i=0 ; i<n ; i++){
		m[i][i] = 0;
		s[i][i] = 0;
	}
	
	for(d=1 ; d<n-1 ; d++){
		for(i=1 ; i<n-d ; i++){
			j = i + d;
			min = 99999;
			for(k=i ; k<=j-1 ; k++){
				x = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j];
				if(x < min){
					min = x;
					s[i][j] = k;
				}
			}
			m[i][j] = min;
		}
	}
	
	printf("\n\n\nM-Table: \n");
	for(i=1 ; i<=n-1 ; i++){
		for(j=i ; j<=n-1 ; j++){
			printf("%d\t", m[i][j]);
		}
		printf("\n");
		for(j=1 ; j<=i ; j++){
			printf("\t");
		}	
	}
	
	printf("\nS-Table: \n");
	for(i=1 ; i<=n-1 ; i++){
		for(j=i ; j<=n-1 ; j++){
			printf("%d\t", s[i][j]);
		}
		printf("\n");
		for(j=1 ; j<=i ; j++){
			printf("\t");
		}
	}
}
