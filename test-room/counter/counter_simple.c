#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>

#define NUM_CHILDREN 2

int counter = 0;
int end = 2;
int *array;
int main(int argc, char **argv) {
int *array = malloc(end * sizeof(int));
/*R1 line:0*/    array[counter]++;
/*R1 line:1*/    counter++;
/*R2 line:0*/    array[counter]++;
/*R2 line:1*/    counter++;
return 0; }
