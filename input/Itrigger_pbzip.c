#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>
#include <string.h>
#include <assert.h>

/* global variable initialization */
pthread_mutex_t *mut;
int count = 2;
/* end of initialization */

int main (int argc, char **argv) {
/* local variable initialization */

/* end of initialization */

/* KLEE setting section */
	klee_make_symbolic(&count, sizeof(count), "count");
	//klee_assume(array[2] == '\0');
/* end KLEE section */

/* put circled region here */
	/* region 1 */
	pthread_mutex_lock(mut);		//R1
	count *= 11;				//R1
	printf ("Steven, i'm here.");		//R1
	pthread_mutex_unlock(mut);		//R1
	/* region 2 */
	pthread_mutex_destroy(mut);           	//R2
	mut = NULL;				//R2
	/* region 3 */


	/* region 4 */


/* end of circled region */

return 0;
}
