#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>
#include <string.h>
#include <assert.h>

/* global variable initialization */
char *value;
int value_length = 16;
int count = 4;
char null_buffer[16] = "null";
char sb[16] = "";
int len = 0;
/* end of initialization */

int main (int argc, char **argv) {
/* local variable initialization */
int end = 3;
int start = 0;
/* end of initialization */

/* KLEE setting section */
	klee_make_symbolic(&len, sizeof(len), "len");
	//klee_assume(array[2] == '\0');
/* end KLEE section */

/* put circled region here */
	/* region 1 */
  	if (sb == NULL) 			//R1
    		strcpy(sb, null_buffer);	//R1
	len = strlen(sb);			//R1
  	int newcount = count + len;		//R1
	if (len > count)			//R1
		printf("deadlock");		//R1
  	count = newcount;			//R1
	/* region 2 */
	int len = end - start;			//R2
  	if (len > 0) {				//R2
    		count -= len;			//R2
  	}					//R2
	/* region 3 */


	/* region 4 */


/* end of circled region */

return 0;
}
