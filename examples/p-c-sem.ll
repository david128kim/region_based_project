; ModuleID = 'p-c-sem.c'
source_filename = "p-c-sem.c"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

%union.sem_t = type { i64, [24 x i8] }
%union.pthread_attr_t = type { i64, [48 x i8] }

@space = common global %union.sem_t zeroinitializer, align 8
@mutex = common global %union.sem_t zeroinitializer, align 8
@.str = private unnamed_addr constant [27 x i8] c"the producer produced: %d\0A\00", align 1
@buffer = common local_unnamed_addr global i32 0, align 4
@items = common global %union.sem_t zeroinitializer, align 8
@.str.1 = private unnamed_addr constant [23 x i8] c"the consumer gets: %d\0A\00", align 1

; Function Attrs: nounwind optsize uwtable
define noalias i8* @producer(i8* nocapture readnone) #0 {
  br label %2

; <label>:2:                                      ; preds = %2, %1
  %3 = phi i32 [ 0, %1 ], [ %10, %2 ]
  %4 = tail call i32 (...) @rand() #4
  %5 = tail call i32 @sem_wait(%union.sem_t* nonnull @space) #4
  %6 = tail call i32 @sem_wait(%union.sem_t* nonnull @mutex) #4
  %7 = tail call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([27 x i8], [27 x i8]* @.str, i64 0, i64 0), i32 %4) #5
  store i32 %4, i32* @buffer, align 4, !tbaa !1
  %8 = tail call i32 @sem_post(%union.sem_t* nonnull @mutex) #4
  %9 = tail call i32 @sem_post(%union.sem_t* nonnull @items) #4
  %10 = add nuw nsw i32 %3, 1
  %11 = icmp eq i32 %10, 10
  br i1 %11, label %12, label %2

; <label>:12:                                     ; preds = %2
  %13 = tail call i32 (i32, ...) bitcast (i32 (...)* @sleep to i32 (i32, ...)*)(i32 1) #4
  ret i8* undef
}

; Function Attrs: argmemonly nounwind
declare void @llvm.lifetime.start(i64, i8* nocapture) #1

; Function Attrs: optsize
declare i32 @rand(...) local_unnamed_addr #2

; Function Attrs: optsize
declare i32 @sem_wait(%union.sem_t*) local_unnamed_addr #2

; Function Attrs: nounwind optsize
declare i32 @printf(i8* nocapture readonly, ...) local_unnamed_addr #3

; Function Attrs: nounwind optsize
declare i32 @sem_post(%union.sem_t*) local_unnamed_addr #3

; Function Attrs: optsize
declare i32 @sleep(...) local_unnamed_addr #2

; Function Attrs: argmemonly nounwind
declare void @llvm.lifetime.end(i64, i8* nocapture) #1

; Function Attrs: nounwind optsize uwtable
define noalias i8* @consumer(i8* nocapture readnone) #0 {
  br label %2

; <label>:2:                                      ; preds = %2, %1
  %3 = phi i32 [ 0, %1 ], [ %10, %2 ]
  %4 = tail call i32 @sem_wait(%union.sem_t* nonnull @items) #4
  %5 = tail call i32 @sem_wait(%union.sem_t* nonnull @mutex) #4
  %6 = load i32, i32* @buffer, align 4, !tbaa !1
  %7 = tail call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([23 x i8], [23 x i8]* @.str.1, i64 0, i64 0), i32 %6) #5
  %8 = tail call i32 @sem_post(%union.sem_t* nonnull @mutex) #4
  %9 = tail call i32 @sem_post(%union.sem_t* nonnull @space) #4
  %10 = add nuw nsw i32 %3, 1
  %11 = icmp eq i32 %10, 10
  br i1 %11, label %12, label %2

; <label>:12:                                     ; preds = %2
  %13 = tail call i32 @putchar(i32 10) #6
  %14 = tail call i32 (i32, ...) bitcast (i32 (...)* @sleep to i32 (i32, ...)*)(i32 1) #4
  ret i8* undef
}

; Function Attrs: nounwind optsize uwtable
define i32 @main() local_unnamed_addr #0 {
  %1 = alloca i64, align 8
  %2 = alloca i64, align 8
  %3 = bitcast i64* %1 to i8*
  call void @llvm.lifetime.start(i64 8, i8* %3) #6
  %4 = bitcast i64* %2 to i8*
  call void @llvm.lifetime.start(i64 8, i8* %4) #6
  %5 = tail call i32 @sem_init(%union.sem_t* nonnull @space, i32 0, i32 3) #4
  %6 = tail call i32 @sem_init(%union.sem_t* nonnull @mutex, i32 0, i32 1) #4
  %7 = tail call i32 @sem_init(%union.sem_t* nonnull @items, i32 0, i32 0) #4
  %8 = call i32 @pthread_create(i64* nonnull %1, %union.pthread_attr_t* null, i8* (i8*)* nonnull @producer, i8* null) #4
  %9 = call i32 @pthread_create(i64* nonnull %2, %union.pthread_attr_t* null, i8* (i8*)* nonnull @consumer, i8* null) #4
  %10 = load i64, i64* %1, align 8, !tbaa !5
  %11 = call i32 @pthread_join(i64 %10, i8** null) #4
  %12 = load i64, i64* %2, align 8, !tbaa !5
  %13 = call i32 @pthread_join(i64 %12, i8** null) #4
  call void @llvm.lifetime.end(i64 8, i8* %4) #6
  call void @llvm.lifetime.end(i64 8, i8* %3) #6
  ret i32 0
}

; Function Attrs: nounwind optsize
declare i32 @sem_init(%union.sem_t*, i32, i32) local_unnamed_addr #3

; Function Attrs: nounwind optsize
declare i32 @pthread_create(i64*, %union.pthread_attr_t*, i8* (i8*)*, i8*) local_unnamed_addr #3

; Function Attrs: optsize
declare i32 @pthread_join(i64, i8**) local_unnamed_addr #2

declare i32 @putchar(i32)

attributes #0 = { nounwind optsize uwtable "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="false" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #1 = { argmemonly nounwind }
attributes #2 = { optsize "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="false" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #3 = { nounwind optsize "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="false" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #4 = { nounwind optsize }
attributes #5 = { optsize }
attributes #6 = { nounwind }

!llvm.ident = !{!0}

!0 = !{!"clang version 3.9.1-4ubuntu3~16.04.2 (tags/RELEASE_391/rc2)"}
!1 = !{!2, !2, i64 0}
!2 = !{!"int", !3, i64 0}
!3 = !{!"omnipotent char", !4, i64 0}
!4 = !{!"Simple C/C++ TBAA"}
!5 = !{!6, !6, i64 0}
!6 = !{!"long", !3, i64 0}
