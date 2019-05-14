#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>

#define N 3
int num;
int total;
int flag;
pthread_mutex_t m;
pthread_cond_t empty, full;

int main(){
int i,j;
i = 0;
j = 0;

