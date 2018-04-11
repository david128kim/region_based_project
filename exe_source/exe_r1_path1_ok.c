#include <pthread.h>
#include <assert.h>
#include <stdio.h>

#define N 3

int num;
unsigned long total;
int flag;

pthread_mutex_t m;
pthread_cond_t empty, full;

int main() {	pthread_mutex_lock(&m);
     	pthread_cond_wait(&empty, &m);
    	num++;
    	pthread_mutex_unlock(&m);
    	pthread_cond_signal(&full);
return 0; }