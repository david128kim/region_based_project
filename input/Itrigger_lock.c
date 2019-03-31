#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>


pthread_mutex_t a,b;
int counter = 1;

int main (int argc, char **argv) {
	klee_make_symbolic(&counter, sizeof(counter), "counter");
	pthread_mutex_lock(&a);	//R1
  	usleep(200);		//R1
  	pthread_mutex_lock(&b); //R1
  	counter++;		//R1
  	pthread_mutex_unlock(&b);	//R1
  	pthread_mutex_unlock(&a);	//R1
	pthread_mutex_lock(&b);	//R2
  	usleep(200);		//R2
  	pthread_mutex_lock(&a); //R2
  	counter--;		//R2
  	pthread_mutex_unlock(&a);	//R2
  	pthread_mutex_unlock(&b);	//R2
	return 0;
}
