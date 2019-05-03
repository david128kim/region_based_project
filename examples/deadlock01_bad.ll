; ModuleID = 'deadlock01_bad.c'
source_filename = "deadlock01_bad.c"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

%union.pthread_mutex_t = type { %struct.__pthread_mutex_s }
%struct.__pthread_mutex_s = type { i32, i32, i32, i32, i32, i16, i16, %struct.__pthread_internal_list }
%struct.__pthread_internal_list = type { %struct.__pthread_internal_list*, %struct.__pthread_internal_list* }
%union.pthread_mutexattr_t = type { i32 }
%union.pthread_attr_t = type { i64, [48 x i8] }

@counter = local_unnamed_addr global i32 1, align 4
@a = common global %union.pthread_mutex_t zeroinitializer, align 8
@b = common global %union.pthread_mutex_t zeroinitializer, align 8

; Function Attrs: nounwind optsize uwtable
define noalias i8* @thread1(i8* nocapture readnone) #0 {
  %2 = tail call i32 @pthread_mutex_lock(%union.pthread_mutex_t* nonnull @a) #4
  %3 = tail call i32 (i32, ...) bitcast (i32 (...)* @usleep to i32 (i32, ...)*)(i32 200) #4
  %4 = tail call i32 @pthread_mutex_lock(%union.pthread_mutex_t* nonnull @b) #4
  %5 = load i32, i32* @counter, align 4, !tbaa !1
  %6 = add nsw i32 %5, 1
  store i32 %6, i32* @counter, align 4, !tbaa !1
  %7 = tail call i32 @pthread_mutex_unlock(%union.pthread_mutex_t* nonnull @b) #4
  %8 = tail call i32 @pthread_mutex_unlock(%union.pthread_mutex_t* nonnull @a) #4
  ret i8* null
}

; Function Attrs: nounwind optsize
declare i32 @pthread_mutex_lock(%union.pthread_mutex_t*) local_unnamed_addr #1

; Function Attrs: optsize
declare i32 @usleep(...) local_unnamed_addr #2

; Function Attrs: nounwind optsize
declare i32 @pthread_mutex_unlock(%union.pthread_mutex_t*) local_unnamed_addr #1

; Function Attrs: nounwind optsize uwtable
define noalias i8* @thread2(i8* nocapture readnone) #0 {
  %2 = tail call i32 @pthread_mutex_lock(%union.pthread_mutex_t* nonnull @b) #4
  %3 = tail call i32 (i32, ...) bitcast (i32 (...)* @usleep to i32 (i32, ...)*)(i32 200) #4
  %4 = tail call i32 @pthread_mutex_lock(%union.pthread_mutex_t* nonnull @a) #4
  %5 = load i32, i32* @counter, align 4, !tbaa !1
  %6 = add nsw i32 %5, -1
  store i32 %6, i32* @counter, align 4, !tbaa !1
  %7 = tail call i32 @pthread_mutex_unlock(%union.pthread_mutex_t* nonnull @a) #4
  %8 = tail call i32 @pthread_mutex_unlock(%union.pthread_mutex_t* nonnull @b) #4
  ret i8* null
}

; Function Attrs: nounwind optsize uwtable
define i32 @main() local_unnamed_addr #0 {
  %1 = alloca i64, align 8
  %2 = alloca i64, align 8
  %3 = bitcast i64* %1 to i8*
  call void @llvm.lifetime.start(i64 8, i8* %3) #5
  %4 = bitcast i64* %2 to i8*
  call void @llvm.lifetime.start(i64 8, i8* %4) #5
  %5 = tail call i32 @pthread_mutex_init(%union.pthread_mutex_t* nonnull @a, %union.pthread_mutexattr_t* null) #4
  %6 = tail call i32 @pthread_mutex_init(%union.pthread_mutex_t* nonnull @b, %union.pthread_mutexattr_t* null) #4
  %7 = call i32 @pthread_create(i64* nonnull %1, %union.pthread_attr_t* null, i8* (i8*)* nonnull @thread1, i8* null) #4
  %8 = call i32 @pthread_create(i64* nonnull %2, %union.pthread_attr_t* null, i8* (i8*)* nonnull @thread2, i8* null) #4
  %9 = load i64, i64* %1, align 8, !tbaa !5
  %10 = call i32 @pthread_join(i64 %9, i8** null) #4
  %11 = load i64, i64* %2, align 8, !tbaa !5
  %12 = call i32 @pthread_join(i64 %11, i8** null) #4
  call void @llvm.lifetime.end(i64 8, i8* %4) #5
  call void @llvm.lifetime.end(i64 8, i8* %3) #5
  ret i32 0
}

; Function Attrs: argmemonly nounwind
declare void @llvm.lifetime.start(i64, i8* nocapture) #3

; Function Attrs: nounwind optsize
declare i32 @pthread_mutex_init(%union.pthread_mutex_t*, %union.pthread_mutexattr_t*) local_unnamed_addr #1

; Function Attrs: nounwind optsize
declare i32 @pthread_create(i64*, %union.pthread_attr_t*, i8* (i8*)*, i8*) local_unnamed_addr #1

; Function Attrs: optsize
declare i32 @pthread_join(i64, i8**) local_unnamed_addr #2

; Function Attrs: argmemonly nounwind
declare void @llvm.lifetime.end(i64, i8* nocapture) #3

attributes #0 = { nounwind optsize uwtable "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="false" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #1 = { nounwind optsize "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="false" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #2 = { optsize "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="false" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #3 = { argmemonly nounwind }
attributes #4 = { nounwind optsize }
attributes #5 = { nounwind }

!llvm.ident = !{!0}

!0 = !{!"clang version 3.9.1-4ubuntu3~16.04.2 (tags/RELEASE_391/rc2)"}
!1 = !{!2, !2, i64 0}
!2 = !{!"int", !3, i64 0}
!3 = !{!"omnipotent char", !4, i64 0}
!4 = !{!"Simple C/C++ TBAA"}
!5 = !{!6, !6, i64 0}
!6 = !{!"long", !3, i64 0}
