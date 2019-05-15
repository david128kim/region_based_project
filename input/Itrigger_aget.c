#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>
#include <string.h>
#include <assert.h>

/* global variable initialization */
pthread_mutex_t mut;
int total = 0;
int bwritten = 0;
/* end of initialization */

int main (int argc, char **argv) {
/* local variable initialization */
int dw = 15473;
/* end of initialization */

/* KLEE setting section */
	klee_make_symbolic(&total, sizeof(total), "total");
	//klee_assume(array[2] == '\0');
/* end KLEE section */

/* put circled region here */
	/* region 1 */
	pthread_mutex_lock(&mut);		//R1
	bwritten += dw;				//R1
	pthread_mutex_unlock(&mut);		//R1
	/* region 2 */
	total = bwritten;			//R2
	/* region 3 */


	/* region 4 */


/* end of circled region */

return 0;
}
