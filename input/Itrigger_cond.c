#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>

/* global variable initialization */
#define N 3
int num;
int total;
int flag;
pthread_mutex_t m;
pthread_cond_t empty, full;
/* end of initialization */

int main (int argc, char **argv) {
/* local variable initialization */
int i,j;
i = 0;
j = 0;
/* end of initialization */

/* KLEE setting section */
	klee_make_symbolic(&num, sizeof(num), "num");
	//klee_assume(array[2] == '\0');
/* end KLEE section */

/* put circled region here */
	/* region 1 */
    	while (num > 0) 			//R1
      		pthread_cond_wait(&empty, &m);	//R1
    	num++;					//R1
    	printf ("produce ....%d\n", i);		//R1
    	pthread_cond_signal(&full);		//R1
    	i++;					//R1
	/* region 2 */
    	while (num == 0) 			//R2
      		pthread_cond_wait(&full, &m);	//R2
    	total=total+j;				//R2
    	printf("total ....%ld\n",total);	//R2
    	num--;					//R2
    	printf("consume ....%d\n",j);		//R2
    	pthread_cond_signal(&empty);		//R2
    	j++;    				//R2
	/* region 3 */


	/* region 4 */



/* end of circled region */

return 0;
}