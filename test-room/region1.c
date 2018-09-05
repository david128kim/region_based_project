#include "klee/klee.h"
#include <pthread.h>
#include <assert.h>
#include <stdio.h>

#define N 3

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
  


//klee_assume(num >= 0);
klee_make_symbolic(&num, sizeof(num), "num");
//klee_assume(num >= 0);
    	//if (i < N){
/*R1 line:0*/    		if (num > 0) {
/*R1 line:1*/      			//pthread_cond_wait(&empty, &m);
					printf("wait");
/*R1 line:2*/      		}
/*R1 line:3*/    		num++;
/*R1 line:4*/    		printf ("produce ....%d\n", i);
/*R1 line:5*/    		pthread_cond_signal(&full);
/*R1 line:6*/    		i++;
/*R1 line:7*/    		if (num > 0) {
/*R1 line:8*/      			//pthread_cond_wait(&empty, &m);
					printf("wait");
/*R1 line:9*/      		}
/*R1 line:10*/    		num++;
/*R1 line:11*/    		printf ("produce ....%d\n", i);
/*R1 line:12*/    		pthread_cond_signal(&full);
/*R1 line:13*/    		i++;
/*R1 line:14*/      	//}
/*R1 line:15*/return 0;
}
