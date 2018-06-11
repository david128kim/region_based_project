#include "../klee_src/include/klee/klee.h"
#include <pthread.h>
#include <stdio.h>
#include <assert.h>
int Global = 10;
int main(int argc, char **argv) {
klee_make_symbolic(&Global, sizeof(Global), "Global");
	Global *= 3;
	if(Global > 0)
	Global -= 10;
return Global; }
