; ModuleID = 'counter.c'
source_filename = "counter.c"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

%union.sem_t = type { i64, [24 x i8] }
%struct.Shared = type { i32, i32, i32* }
%union.pthread_attr_t = type { i64, [48 x i8] }

@.str = private unnamed_addr constant [14 x i8] c"malloc failed\00", align 1
@.str.1 = private unnamed_addr constant [16 x i8] c"sem_init failed\00", align 1
@.str.2 = private unnamed_addr constant [22 x i8] c"pthread_create failed\00", align 1
@.str.3 = private unnamed_addr constant [20 x i8] c"pthread_join failed\00", align 1
@.str.4 = private unnamed_addr constant [30 x i8] c"Starting child at counter %d\0A\00", align 1
@.str.5 = private unnamed_addr constant [4 x i8] c"%d\0A\00", align 1
@.str.8 = private unnamed_addr constant [12 x i8] c"%d errors.\0A\00", align 1
@str = private unnamed_addr constant [12 x i8] c"Child done.\00"
@str.9 = private unnamed_addr constant [12 x i8] c"Checking...\00"

; Function Attrs: noreturn nounwind optsize uwtable
define void @perror_exit(i8* nocapture readonly) local_unnamed_addr #0 {
  tail call void @perror(i8* %0) #8
  tail call void @exit(i32 -1) #9
  unreachable
}

; Function Attrs: nounwind optsize
declare void @perror(i8* nocapture readonly) local_unnamed_addr #1

; Function Attrs: noreturn nounwind optsize
declare void @exit(i32) local_unnamed_addr #2

; Function Attrs: nounwind optsize uwtable
define noalias i8* @check_malloc(i32) local_unnamed_addr #3 {
  %2 = sext i32 %0 to i64
  %3 = tail call noalias i8* @malloc(i64 %2) #10
  %4 = icmp eq i8* %3, null
  br i1 %4, label %5, label %6

; <label>:5:                                      ; preds = %1
  tail call void @perror_exit(i8* getelementptr inbounds ([14 x i8], [14 x i8]* @.str, i64 0, i64 0)) #11
  unreachable

; <label>:6:                                      ; preds = %1
  ret i8* %3
}

; Function Attrs: argmemonly nounwind
declare void @llvm.lifetime.start(i64, i8* nocapture) #4

; Function Attrs: nounwind optsize
declare noalias i8* @malloc(i64) local_unnamed_addr #1

; Function Attrs: argmemonly nounwind
declare void @llvm.lifetime.end(i64, i8* nocapture) #4

; Function Attrs: nounwind optsize uwtable
define %union.sem_t* @make_semaphore(i32) local_unnamed_addr #3 {
  %2 = tail call i8* @check_malloc(i32 32) #11
  %3 = bitcast i8* %2 to %union.sem_t*
  %4 = tail call i32 @sem_init(%union.sem_t* %3, i32 0, i32 %0) #10
  %5 = icmp eq i32 %4, -1
  br i1 %5, label %6, label %7

; <label>:6:                                      ; preds = %1
  tail call void @perror_exit(i8* getelementptr inbounds ([16 x i8], [16 x i8]* @.str.1, i64 0, i64 0)) #11
  unreachable

; <label>:7:                                      ; preds = %1
  ret %union.sem_t* %3
}

; Function Attrs: nounwind optsize
declare i32 @sem_init(%union.sem_t*, i32, i32) local_unnamed_addr #1

; Function Attrs: nounwind optsize uwtable
define i32 @sem_signal(%union.sem_t*) local_unnamed_addr #3 {
  %2 = tail call i32 @sem_post(%union.sem_t* %0) #10
  ret i32 %2
}

; Function Attrs: nounwind optsize
declare i32 @sem_post(%union.sem_t*) local_unnamed_addr #1

; Function Attrs: nounwind optsize uwtable
define noalias %struct.Shared* @make_shared(i32) local_unnamed_addr #3 {
  %2 = tail call i8* @check_malloc(i32 16) #11
  %3 = bitcast i8* %2 to %struct.Shared*
  %4 = bitcast i8* %2 to i32*
  store i32 0, i32* %4, align 8, !tbaa !1
  %5 = getelementptr inbounds i8, i8* %2, i64 4
  %6 = bitcast i8* %5 to i32*
  store i32 %0, i32* %6, align 4, !tbaa !7
  %7 = shl i32 %0, 2
  %8 = tail call i8* @check_malloc(i32 %7) #11
  %9 = getelementptr inbounds i8, i8* %2, i64 8
  %10 = bitcast i8* %9 to i8**
  store i8* %8, i8** %10, align 8, !tbaa !8
  %11 = icmp sgt i32 %0, 0
  br i1 %11, label %12, label %17

; <label>:12:                                     ; preds = %1
  %13 = add i32 %0, -1
  %14 = zext i32 %13 to i64
  %15 = shl nuw nsw i64 %14, 2
  %16 = add nuw nsw i64 %15, 4
  call void @llvm.memset.p0i8.i64(i8* %8, i8 0, i64 %16, i32 4, i1 false)
  br label %17

; <label>:17:                                     ; preds = %12, %1
  ret %struct.Shared* %3
}

; Function Attrs: nounwind optsize uwtable
define i64 @make_thread(i8* (i8*)*, %struct.Shared*) local_unnamed_addr #3 {
  %3 = alloca i64, align 8
  %4 = bitcast i64* %3 to i8*
  call void @llvm.lifetime.start(i64 8, i8* %4) #7
  %5 = bitcast %struct.Shared* %1 to i8*
  %6 = call i32 @pthread_create(i64* nonnull %3, %union.pthread_attr_t* null, i8* (i8*)* %0, i8* %5) #10
  %7 = icmp eq i32 %6, 0
  br i1 %7, label %9, label %8

; <label>:8:                                      ; preds = %2
  call void @perror_exit(i8* getelementptr inbounds ([22 x i8], [22 x i8]* @.str.2, i64 0, i64 0)) #11
  unreachable

; <label>:9:                                      ; preds = %2
  %10 = load i64, i64* %3, align 8, !tbaa !9
  call void @llvm.lifetime.end(i64 8, i8* %4) #7
  ret i64 %10
}

; Function Attrs: nounwind optsize
declare i32 @pthread_create(i64*, %union.pthread_attr_t*, i8* (i8*)*, i8*) local_unnamed_addr #1

; Function Attrs: nounwind optsize uwtable
define void @join_thread(i64) local_unnamed_addr #3 {
  %2 = tail call i32 @pthread_join(i64 %0, i8** null) #10
  %3 = icmp eq i32 %2, -1
  br i1 %3, label %4, label %5

; <label>:4:                                      ; preds = %1
  tail call void @perror_exit(i8* getelementptr inbounds ([20 x i8], [20 x i8]* @.str.3, i64 0, i64 0)) #11
  unreachable

; <label>:5:                                      ; preds = %1
  ret void
}

; Function Attrs: optsize
declare i32 @pthread_join(i64, i8**) local_unnamed_addr #5

; Function Attrs: nounwind optsize uwtable
define void @child_code(%struct.Shared* nocapture) local_unnamed_addr #3 {
  %2 = getelementptr inbounds %struct.Shared, %struct.Shared* %0, i64 0, i32 0
  %3 = load i32, i32* %2, align 8, !tbaa !1
  %4 = tail call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([30 x i8], [30 x i8]* @.str.4, i64 0, i64 0), i32 %3) #11
  %5 = bitcast %struct.Shared* %0 to i64*
  %6 = load i64, i64* %5, align 8
  %7 = trunc i64 %6 to i32
  %8 = lshr i64 %6, 32
  %9 = trunc i64 %8 to i32
  %10 = icmp slt i32 %7, %9
  br i1 %10, label %11, label %14

; <label>:11:                                     ; preds = %1
  %12 = getelementptr inbounds %struct.Shared, %struct.Shared* %0, i64 0, i32 2
  br label %15

; <label>:13:                                     ; preds = %31
  br label %14

; <label>:14:                                     ; preds = %13, %1
  ret void

; <label>:15:                                     ; preds = %11, %31
  %16 = phi i32 [ %7, %11 ], [ %33, %31 ]
  %17 = sext i32 %16 to i64
  %18 = load i32*, i32** %12, align 8, !tbaa !8
  %19 = getelementptr inbounds i32, i32* %18, i64 %17
  %20 = load i32, i32* %19, align 4, !tbaa !11
  %21 = add nsw i32 %20, 1
  store i32 %21, i32* %19, align 4, !tbaa !11
  %22 = load i64, i64* %5, align 8
  %23 = trunc i64 %22 to i32
  %24 = add nsw i32 %23, 1
  store i32 %24, i32* %2, align 8, !tbaa !1
  %25 = srem i32 %24, 10000
  %26 = icmp eq i32 %25, 0
  br i1 %26, label %27, label %31

; <label>:27:                                     ; preds = %15
  %28 = tail call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.str.5, i64 0, i64 0), i32 %24) #11
  %29 = load i64, i64* %5, align 8
  %30 = trunc i64 %29 to i32
  br label %31

; <label>:31:                                     ; preds = %27, %15
  %32 = phi i64 [ %29, %27 ], [ %22, %15 ]
  %33 = phi i32 [ %30, %27 ], [ %24, %15 ]
  %34 = lshr i64 %32, 32
  %35 = trunc i64 %34 to i32
  %36 = icmp slt i32 %33, %35
  br i1 %36, label %15, label %13
}

; Function Attrs: nounwind optsize
declare i32 @printf(i8* nocapture readonly, ...) local_unnamed_addr #1

; Function Attrs: noreturn nounwind optsize uwtable
define noalias nonnull i8* @entry(i8* nocapture) #0 {
  %2 = bitcast i8* %0 to %struct.Shared*
  tail call void @child_code(%struct.Shared* %2) #11
  %3 = tail call i32 @puts(i8* getelementptr inbounds ([12 x i8], [12 x i8]* @str, i64 0, i64 0))
  tail call void @pthread_exit(i8* null) #9
  unreachable
}

; Function Attrs: noreturn optsize
declare void @pthread_exit(i8*) local_unnamed_addr #6

; Function Attrs: nounwind optsize uwtable
define void @check_array(%struct.Shared* nocapture readonly) local_unnamed_addr #3 {
  %2 = tail call i32 @puts(i8* getelementptr inbounds ([12 x i8], [12 x i8]* @str.9, i64 0, i64 0))
  %3 = getelementptr inbounds %struct.Shared, %struct.Shared* %0, i64 0, i32 1
  %4 = load i32, i32* %3, align 4, !tbaa !7
  %5 = icmp sgt i32 %4, 0
  br i1 %5, label %6, label %67

; <label>:6:                                      ; preds = %1
  %7 = getelementptr inbounds %struct.Shared, %struct.Shared* %0, i64 0, i32 2
  %8 = load i32*, i32** %7, align 8, !tbaa !8
  %9 = sext i32 %4 to i64
  %10 = add nsw i64 %9, -1
  %11 = and i64 %9, 3
  %12 = icmp ult i64 %10, 3
  br i1 %12, label %46, label %13

; <label>:13:                                     ; preds = %6
  %14 = sub nsw i64 %9, %11
  br label %15

; <label>:15:                                     ; preds = %15, %13
  %16 = phi i64 [ 0, %13 ], [ %42, %15 ]
  %17 = phi i32 [ 0, %13 ], [ %41, %15 ]
  %18 = phi i64 [ %14, %13 ], [ %43, %15 ]
  %19 = getelementptr inbounds i32, i32* %8, i64 %16
  %20 = load i32, i32* %19, align 4, !tbaa !11
  %21 = icmp ne i32 %20, 1
  %22 = zext i1 %21 to i32
  %23 = add nsw i32 %22, %17
  %24 = or i64 %16, 1
  %25 = getelementptr inbounds i32, i32* %8, i64 %24
  %26 = load i32, i32* %25, align 4, !tbaa !11
  %27 = icmp ne i32 %26, 1
  %28 = zext i1 %27 to i32
  %29 = add nsw i32 %28, %23
  %30 = or i64 %16, 2
  %31 = getelementptr inbounds i32, i32* %8, i64 %30
  %32 = load i32, i32* %31, align 4, !tbaa !11
  %33 = icmp ne i32 %32, 1
  %34 = zext i1 %33 to i32
  %35 = add nsw i32 %34, %29
  %36 = or i64 %16, 3
  %37 = getelementptr inbounds i32, i32* %8, i64 %36
  %38 = load i32, i32* %37, align 4, !tbaa !11
  %39 = icmp ne i32 %38, 1
  %40 = zext i1 %39 to i32
  %41 = add nsw i32 %40, %35
  %42 = add nsw i64 %16, 4
  %43 = add i64 %18, -4
  %44 = icmp eq i64 %43, 0
  br i1 %44, label %45, label %15

; <label>:45:                                     ; preds = %15
  br label %46

; <label>:46:                                     ; preds = %45, %6
  %47 = phi i32 [ undef, %6 ], [ %41, %45 ]
  %48 = phi i64 [ 0, %6 ], [ %42, %45 ]
  %49 = phi i32 [ 0, %6 ], [ %41, %45 ]
  %50 = icmp eq i64 %11, 0
  br i1 %50, label %65, label %51

; <label>:51:                                     ; preds = %46
  br label %52

; <label>:52:                                     ; preds = %52, %51
  %53 = phi i64 [ %48, %51 ], [ %61, %52 ]
  %54 = phi i32 [ %49, %51 ], [ %60, %52 ]
  %55 = phi i64 [ %11, %51 ], [ %62, %52 ]
  %56 = getelementptr inbounds i32, i32* %8, i64 %53
  %57 = load i32, i32* %56, align 4, !tbaa !11
  %58 = icmp ne i32 %57, 1
  %59 = zext i1 %58 to i32
  %60 = add nsw i32 %59, %54
  %61 = add nuw nsw i64 %53, 1
  %62 = add i64 %55, -1
  %63 = icmp eq i64 %62, 0
  br i1 %63, label %64, label %52, !llvm.loop !12

; <label>:64:                                     ; preds = %52
  br label %65

; <label>:65:                                     ; preds = %46, %64
  %66 = phi i32 [ %47, %46 ], [ %60, %64 ]
  br label %67

; <label>:67:                                     ; preds = %65, %1
  %68 = phi i32 [ 0, %1 ], [ %66, %65 ]
  %69 = tail call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([12 x i8], [12 x i8]* @.str.8, i64 0, i64 0), i32 %68) #11
  ret void
}

; Function Attrs: nounwind optsize uwtable
define i32 @main() local_unnamed_addr #3 {
  %1 = alloca [2 x i64], align 16
  %2 = bitcast [2 x i64]* %1 to i8*
  call void @llvm.lifetime.start(i64 16, i8* %2) #7
  %3 = tail call i8* @check_malloc(i32 16) #10
  %4 = bitcast i8* %3 to %struct.Shared*
  %5 = bitcast i8* %3 to i32*
  store i32 0, i32* %5, align 8, !tbaa !1
  %6 = getelementptr inbounds i8, i8* %3, i64 4
  %7 = bitcast i8* %6 to i32*
  store i32 100000000, i32* %7, align 4, !tbaa !7
  %8 = tail call i8* @check_malloc(i32 400000000) #10
  %9 = getelementptr inbounds i8, i8* %3, i64 8
  %10 = bitcast i8* %9 to i8**
  store i8* %8, i8** %10, align 8, !tbaa !8
  tail call void @llvm.memset.p0i8.i64(i8* %8, i8 0, i64 400000000, i32 4, i1 false) #7
  br label %11

; <label>:11:                                     ; preds = %11, %0
  %12 = phi i64 [ 0, %0 ], [ %15, %11 ]
  %13 = tail call i64 @make_thread(i8* (i8*)* nonnull @entry, %struct.Shared* %4) #11
  %14 = getelementptr inbounds [2 x i64], [2 x i64]* %1, i64 0, i64 %12
  store i64 %13, i64* %14, align 8, !tbaa !9
  %15 = add nuw nsw i64 %12, 1
  %16 = icmp eq i64 %15, 2
  br i1 %16, label %17, label %11

; <label>:17:                                     ; preds = %11
  br label %18

; <label>:18:                                     ; preds = %17, %18
  %19 = phi i64 [ %22, %18 ], [ 0, %17 ]
  %20 = getelementptr inbounds [2 x i64], [2 x i64]* %1, i64 0, i64 %19
  %21 = load i64, i64* %20, align 8, !tbaa !9
  tail call void @join_thread(i64 %21) #11
  %22 = add nuw nsw i64 %19, 1
  %23 = icmp eq i64 %22, 2
  br i1 %23, label %24, label %18

; <label>:24:                                     ; preds = %18
  tail call void @check_array(%struct.Shared* %4) #11
  call void @llvm.lifetime.end(i64 16, i8* nonnull %2) #7
  ret i32 0
}

; Function Attrs: nounwind
declare i32 @puts(i8* nocapture readonly) #7

; Function Attrs: argmemonly nounwind
declare void @llvm.memset.p0i8.i64(i8* nocapture writeonly, i8, i64, i32, i1) #4

attributes #0 = { noreturn nounwind optsize uwtable "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="false" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #1 = { nounwind optsize "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="false" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #2 = { noreturn nounwind optsize "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="false" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #3 = { nounwind optsize uwtable "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="false" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #4 = { argmemonly nounwind }
attributes #5 = { optsize "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="false" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #6 = { noreturn optsize "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="false" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #7 = { nounwind }
attributes #8 = { cold optsize }
attributes #9 = { noreturn nounwind optsize }
attributes #10 = { nounwind optsize }
attributes #11 = { optsize }

!llvm.ident = !{!0}

!0 = !{!"clang version 3.9.1-4ubuntu3~16.04.2 (tags/RELEASE_391/rc2)"}
!1 = !{!2, !3, i64 0}
!2 = !{!"", !3, i64 0, !3, i64 4, !6, i64 8}
!3 = !{!"int", !4, i64 0}
!4 = !{!"omnipotent char", !5, i64 0}
!5 = !{!"Simple C/C++ TBAA"}
!6 = !{!"any pointer", !4, i64 0}
!7 = !{!2, !3, i64 4}
!8 = !{!2, !6, i64 8}
!9 = !{!10, !10, i64 0}
!10 = !{!"long", !4, i64 0}
!11 = !{!3, !3, i64 0}
!12 = distinct !{!12, !13}
!13 = !{!"llvm.loop.unroll.disable"}
