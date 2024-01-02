// Selection Sort

#include<stdio.h>
#include<conio.h>

int main() {
	
	int i, j, temp, n;
	printf("\e[1;1H\e[2J");
	
	printf("Enter size of array: ");
	scanf("%d", &n);

	int a[n];
	printf("Enter elements of array:\n");
	for(i=0 ; i<n ; i++) {
		scanf("%d", &a[i]);
	}
	
	for(i=0 ; i<n-1 ; i++){
		int least = i;
		for(j=i+1 ; j<n ; j++){
			if(a[j] < a[least]){
				least = j;
			}
		}
		if(least != i){
			temp = a[i];
			a[i] = a[least];
			a[least] = temp;
		}
	}
	
	printf("\nSorted Array:\n");
	for(i=0 ; i<n ; i++){
		printf("%d ", a[i]);
	}
	
	return 0;
}
