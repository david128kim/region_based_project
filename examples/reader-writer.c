#include <stdio.h>

/* starvation */

  void reader_function(void);
  void writer_function(void);
  
  int buffer = 0;
  int buffer_has_item = 0;
  pthread_mutex_t mutex;
  
  int  main()
  {
     pthread_t reader;
  
     pthread_mutex_init(&mutex, pthread_mutexattr_default);
     pthread_create( &reader, pthread_attr_default, (void*)&reader_function,
                    NULL);
     writer_function();
  }
  
  void writer_function(void)
  {
     while(1)
     {
          pthread_mutex_lock( &mutex );
          if ( buffer_has_item == 0 )
          {
               buffer += 1;
               buffer_has_item = 1;
	       printf("w-buffer: %d", buffer);
          }
          pthread_mutex_unlock( &mutex );
     }
  }
  
  void reader_function(void)
  {
     while(1)
     {
          pthread_mutex_lock( &mutex );
          if ( buffer_has_item == 1)
          {
               buffer -= 1;
               buffer_has_item = 0;
	       printf("r-buffer: %d", buffer);
          }
          pthread_mutex_unlock( &mutex );
     }
  }
