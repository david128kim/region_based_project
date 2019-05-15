#include <pthread.h>
#include <stdio.h>
#include <assert.h>
int Global = 10;
pthread_mutex_t a;
void *Thread1(void *x) {
  //Global *= 2;
  pthread_mutex_lock(NULL);
  Global += 10;
  pthread_mutex_unlock(NULL);
  return x;
}
void *Thread2(void *y) {
  pthread_mutex_lock(NULL);
  Global -= 10;
  pthread_mutex_unlock(NULL);
  return y;
}
int main() {
  pthread_t t1, t2;
  
  pthread_mutex_init(&a, NULL); 

  pthread_create(&t1, NULL, Thread1, NULL);
  pthread_create(&t2, NULL, Thread2, NULL);

  pthread_join(t1, NULL);
  pthread_join(t2, NULL);
  
  printf("%d\n", Global);
  return Global;
}
