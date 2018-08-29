#include "klee/klee.h"
#include <pthread.h>
#include <assert.h>
#include <stdio.h>

#define N 1

int num;
int total;
int flag;

pthread_mutex_t m;
pthread_cond_t empty, full;

int main(int argc, char **argv) {
  int i;

  i = 0;
    




  int j;

  j = 0;

    
  flag=1;


  pthread_t  t1, t2;

  total = 0;

  


  


klee_make_symbolic(&num, sizeof(num), "num");
    	while (i < N){
    		if (num > 0) {
      			printf ("empty, &m");
      		}
    		num++;
    		printf ("produce ....%d\n", i);
    		pthread_cond_signal(&full);
    		i++;
      	}
  	while (j < N){  		
    		if (num == 0) {
      			printf ("full, &m");
      		}
    		total=total+j;
    		printf("total ....%ld\n",total);
    		num--;
    		printf("consume ....%d\n",j);
    		pthread_cond_signal(&empty);
    		j++;
  	}
return 0; }
