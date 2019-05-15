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
pthread_mutex_init(&mut, 0);
/* end of initialization */
