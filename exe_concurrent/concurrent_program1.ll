region1: 
  %1 = tail call i32 @pthread_mutex_lock(%union.pthread_mutex_t* @m) #3
  %2 = tail call i32 @pthread_cond_wait(%union.pthread_cond_t* @empty, %union.pthread_mutex_t* @m) #3
  %3 = load i32* @num, align 4, !tbaa !1
  %4 = add nsw i32 %3, 1
  store i32 %4, i32* @num, align 4, !tbaa !1
  %5 = tail call i32 @pthread_mutex_unlock(%union.pthread_mutex_t* @m) #3
  %6 = tail call i32 @pthread_cond_signal(%union.pthread_cond_t* @full) #3
region2: 
  %1 = tail call i32 @pthread_mutex_lock(%union.pthread_mutex_t* @m) #3
  %2 = tail call i32 @pthread_cond_wait(%union.pthread_cond_t* @full, %union.pthread_mutex_t* @m) #3
  %3 = load i32* @num, align 4, !tbaa !1
  %4 = add nsw i32 %3, -1
  store i32 %4, i32* @num, align 4, !tbaa !1
  %5 = tail call i32 @pthread_mutex_unlock(%union.pthread_mutex_t* @m) #3
  %6 = tail call i32 @pthread_cond_signal(%union.pthread_cond_t* @empty) #3
