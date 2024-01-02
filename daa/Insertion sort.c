// Insertion Sort 
#include<stdio.h>
#include<conio.h>

int main() {
	
	printf("\e[1;1H\e[2J");
	int n, i, j, p;
	
	printf("Enter the size of array: ");
	scanf("%d", &n);
	
	int a[n];
	printf("Enter the elements of array:\n");
	for(i=0 ; i<n ; i++){
		scanf("%d", &a[i]);
	}
	
	for(i=1 ; i<n ; i++){
		p = a[i];
		j = i - 1;
		while (j>=0 && a[j]>p){
			a[j+1] = a[j];
			j--;
		}
		a[j+1] = p;
	}
	
	printf("\nSorted array is:\n");
	for(i=0 ; i<n ; i++){
		printf("%d ", a[i]);
	}
	
	return 0;
}
