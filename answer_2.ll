  %3 = tail call i32 @pthread_mutex_lock(%union.pthread_mutex_t* nonnull @m) #2 ;R1
   %4 = load i32, i32* @num, align 4, !tbaa !1 ;R1
   %5 = add nsw i32 %4, 1 ;R1
   store i32 %5, i32* @num, align 4, !tbaa !1 ;R1
   %7 = tail call i32 @pthread_mutex_unlock(%union.pthread_mutex_t* nonnull @m) #2 ;R1
   %3 = tail call i32 @pthread_cond_wait(%union.pthread_cond_t* nonnull @full, %union.pthread_mutex_t* nonnull @m) #3 ;R2
    %8 = tail call i32 @pthread_cond_signal(%union.pthread_cond_t* nonnull @full) #2 ;R1
   %5 = tail call i32 @pthread_mutex_lock(%union.pthread_mutex_t* nonnull @m) #3 ;R2
   %6 = load i32, i32* @num, align 4, !tbaa !1 ;R2
   %7 = add nsw i32 %6, -1 ;R2
   store i32 %7, i32* @num, align 4, !tbaa !1 ;R2
   %9 = tail call i32 @pthread_mutex_unlock(%union.pthread_mutex_t* nonnull @m) #3 ;R2
    %10 = tail call i32 @pthread_cond_signal(%union.pthread_cond_t* nonnull @empty) #3 ;R2
