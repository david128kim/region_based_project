#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>


int array[10];
int counter = 0;

int main (int argc, char **argv) {
	klee_make_symbolic(&array, sizeof(array), "array");
	array[counter]++; 		//R1
	counter++;			//R1
	array[counter]++;		//R2
        counter++;			//R2
	array[counter]++;               //R3
        counter++;                      //R3
	printf("%d\n", array[counter]);
	return 0;
}
