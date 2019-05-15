#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>
#include <string.h>
#include <assert.h>

pthread_mutex_t *mut;
int count = 2;

int main () {
pthread_mutex_init(mut, 0);
