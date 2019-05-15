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

