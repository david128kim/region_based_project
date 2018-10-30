#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>

#define NUM_CHILDREN 2

typedef struct {
  int counter;
  int end;
  int *array;
} Shared;

int main(int argc, char **argv) {

  int end = 2; 										//make_shared(int end)
  Shared *shared = check_malloc (sizeof (Shared));
  shared->counter = 0;
  shared->end = end;
  shared->array = check_malloc (shared->end * sizeof(int));


/*R1 line:0*/    shared->array[shared->counter]++;
/*R1 line:1*/    shared->counter++;
/*R2 line:0*/    shared->array[shared->counter]++;
/*R2 line:1*/    shared->counter++;
return 0; }
