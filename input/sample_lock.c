#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>

pthread_mutex_t a,b;
counter = 0;

int main(){
pthread_mutex_init(&a, 0);
pthread_mutex_init(&b, 0);
