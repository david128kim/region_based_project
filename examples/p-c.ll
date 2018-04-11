; ModuleID = 'p-c.c'
target datalayout = "e-p:64:64:64-i1:8:8-i8:8:8-i16:16:16-i32:32:32-i64:64:64-f32:32:32-f64:64:64-v64:64:64-v128:128:128-a0:0:64-s0:64:64-f80:128:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

%union.pthread_mutex_t = type { %struct.__pthread_mutex_s }
%struct.__pthread_mutex_s = type { i32, i32, i32, i32, i32, i16, i16, %struct.__pthread_internal_list }
%struct.__pthread_internal_list = type { %struct.__pthread_internal_list*, %struct.__pthread_internal_list* }
%union.pthread_cond_t = type { %struct.anon }
%struct.anon = type { i32, i32, i64, i64, i64, i8*, i32, i32 }
%union.pthread_mutexattr_t = type { i32 }
%union.pthread_condattr_t = type { i32 }
%union.pthread_attr_t = type { i64, [48 x i8] }

@m = common global %union.pthread_mutex_t zeroinitializer, align 8
@num = common global i32 0, align 4
@empty = common global %union.pthread_cond_t zeroinitializer, align 8
@.str = private unnamed_addr constant [16 x i8] c"produce ....%d\0A\00", align 1
@full = common global %union.pthread_cond_t zeroinitializer, align 8
@total = common global i64 0, align 8
@.str1 = private unnamed_addr constant [15 x i8] c"total ....%ld\0A\00", align 1
@.str2 = private unnamed_addr constant [16 x i8] c"consume ....%d\0A\00", align 1
@flag = common global i32 0, align 4
@.str3 = private unnamed_addr constant [21 x i8] c"total!=((3*(3+1))/2)\00", align 1
@.str4 = private unnamed_addr constant [6 x i8] c"p-c.c\00", align 1
@__PRETTY_FUNCTION__.main = private unnamed_addr constant [11 x i8] c"int main()\00", align 1

; Function Attrs: nounwind optsize uwtable
define noalias i8* @thread1(i8* nocapture readnone %arg) #0 {
  br label %1

; <label>:1                                       ; preds = %._crit_edge, %0
  %i.01 = phi i32 [ 0, %0 ], [ %12, %._crit_edge ]
  %2 = tail call i32 @pthread_mutex_lock(%union.pthread_mutex_t* @m) #4
  %3 = load i32* @num, align 4, !tbaa !1
  %4 = icmp sgt i32 %3, 0
  br i1 %4, label %.lr.ph, label %._crit_edge

.lr.ph:                                           ; preds = %1, %.lr.ph
  %5 = tail call i32 @pthread_cond_wait(%union.pthread_cond_t* @empty, %union.pthread_mutex_t* @m) #4
  %6 = load i32* @num, align 4, !tbaa !1
  %7 = icmp sgt i32 %6, 0
  br i1 %7, label %.lr.ph, label %._crit_edge

._crit_edge:                                      ; preds = %.lr.ph, %1
  %.lcssa = phi i32 [ %3, %1 ], [ %6, %.lr.ph ]
  %8 = add nsw i32 %.lcssa, 1
  store i32 %8, i32* @num, align 4, !tbaa !1
  %9 = tail call i32 (i8*, ...)* @printf(i8* getelementptr inbounds ([16 x i8]* @.str, i64 0, i64 0), i32 %i.01) #4
  %10 = tail call i32 @pthread_mutex_unlock(%union.pthread_mutex_t* @m) #4
  %11 = tail call i32 @pthread_cond_signal(%union.pthread_cond_t* @full) #4
  %12 = add nsw i32 %i.01, 1
  %exitcond = icmp eq i32 %12, 3
  br i1 %exitcond, label %13, label %1

; <label>:13                                      ; preds = %._crit_edge
  ret i8* undef
}

; Function Attrs: nounwind optsize
declare i32 @pthread_mutex_lock(%union.pthread_mutex_t*) #1

; Function Attrs: optsize
declare i32 @pthread_cond_wait(%union.pthread_cond_t*, %union.pthread_mutex_t*) #2

; Function Attrs: nounwind optsize
declare i32 @printf(i8* nocapture readonly, ...) #1

; Function Attrs: nounwind optsize
declare i32 @pthread_mutex_unlock(%union.pthread_mutex_t*) #1

; Function Attrs: nounwind optsize
declare i32 @pthread_cond_signal(%union.pthread_cond_t*) #1

; Function Attrs: nounwind optsize uwtable
define noalias i8* @thread2(i8* nocapture readnone %arg) #0 {
  br label %1

; <label>:1                                       ; preds = %._crit_edge, %0
  %indvars.iv = phi i64 [ 0, %0 ], [ %indvars.iv.next, %._crit_edge ]
  %2 = tail call i32 @pthread_mutex_lock(%union.pthread_mutex_t* @m) #4
  %3 = load i32* @num, align 4, !tbaa !1
  %4 = icmp eq i32 %3, 0
  br i1 %4, label %.lr.ph, label %._crit_edge

.lr.ph:                                           ; preds = %1, %.lr.ph
  %5 = tail call i32 @pthread_cond_wait(%union.pthread_cond_t* @full, %union.pthread_mutex_t* @m) #4
  %6 = load i32* @num, align 4, !tbaa !1
  %7 = icmp eq i32 %6, 0
  br i1 %7, label %.lr.ph, label %._crit_edge

._crit_edge:                                      ; preds = %.lr.ph, %1
  %8 = load i64* @total, align 8, !tbaa !5
  %9 = add i64 %8, %indvars.iv
  store i64 %9, i64* @total, align 8, !tbaa !5
  %10 = tail call i32 (i8*, ...)* @printf(i8* getelementptr inbounds ([15 x i8]* @.str1, i64 0, i64 0), i64 %9) #4
  %11 = load i32* @num, align 4, !tbaa !1
  %12 = add nsw i32 %11, -1
  store i32 %12, i32* @num, align 4, !tbaa !1
  %13 = trunc i64 %indvars.iv to i32
  %14 = tail call i32 (i8*, ...)* @printf(i8* getelementptr inbounds ([16 x i8]* @.str2, i64 0, i64 0), i32 %13) #4
  %15 = tail call i32 @pthread_mutex_unlock(%union.pthread_mutex_t* @m) #4
  %16 = tail call i32 @pthread_cond_signal(%union.pthread_cond_t* @empty) #4
  %indvars.iv.next = add nuw nsw i64 %indvars.iv, 1
  %exitcond = icmp eq i64 %indvars.iv.next, 3
  br i1 %exitcond, label %17, label %1

; <label>:17                                      ; preds = %._crit_edge
  %18 = load i64* @total, align 8, !tbaa !5
  %19 = add i64 %18, 3
  store i64 %19, i64* @total, align 8, !tbaa !5
  %20 = tail call i32 (i8*, ...)* @printf(i8* getelementptr inbounds ([15 x i8]* @.str1, i64 0, i64 0), i64 %19) #4
  store i32 1, i32* @flag, align 4, !tbaa !1
  ret i8* undef
}

; Function Attrs: nounwind optsize uwtable
define i32 @main() #0 {
  %t1 = alloca i64, align 8
  %t2 = alloca i64, align 8
  store i32 0, i32* @num, align 4, !tbaa !1
  store i64 0, i64* @total, align 8, !tbaa !5
  %1 = call i32 @pthread_mutex_init(%union.pthread_mutex_t* @m, %union.pthread_mutexattr_t* null) #4
  %2 = call i32 @pthread_cond_init(%union.pthread_cond_t* @empty, %union.pthread_condattr_t* null) #4
  %3 = call i32 @pthread_cond_init(%union.pthread_cond_t* @full, %union.pthread_condattr_t* null) #4
  %4 = call i32 @pthread_create(i64* %t1, %union.pthread_attr_t* null, i8* (i8*)* @thread1, i8* null) #4
  %5 = call i32 @pthread_create(i64* %t2, %union.pthread_attr_t* null, i8* (i8*)* @thread2, i8* null) #4
  %6 = load i64* %t1, align 8, !tbaa !5
  %7 = call i32 @pthread_join(i64 %6, i8** null) #4
  %8 = load i64* %t2, align 8, !tbaa !5
  %9 = call i32 @pthread_join(i64 %8, i8** null) #4
  %10 = load i32* @flag, align 4, !tbaa !1
  %11 = icmp eq i32 %10, 0
  %12 = load i64* @total, align 8, !tbaa !5
  %13 = icmp ne i64 %12, 6
  %or.cond = or i1 %11, %13
  br i1 %or.cond, label %15, label %14

; <label>:14                                      ; preds = %0
  call void @__assert_fail(i8* getelementptr inbounds ([21 x i8]* @.str3, i64 0, i64 0), i8* getelementptr inbounds ([6 x i8]* @.str4, i64 0, i64 0), i32 79, i8* getelementptr inbounds ([11 x i8]* @__PRETTY_FUNCTION__.main, i64 0, i64 0)) #5
  unreachable

; <label>:15                                      ; preds = %0
  ret i32 0
}

; Function Attrs: nounwind optsize
declare i32 @pthread_mutex_init(%union.pthread_mutex_t*, %union.pthread_mutexattr_t*) #1

; Function Attrs: nounwind optsize
declare i32 @pthread_cond_init(%union.pthread_cond_t*, %union.pthread_condattr_t*) #1

; Function Attrs: nounwind optsize
declare i32 @pthread_create(i64*, %union.pthread_attr_t*, i8* (i8*)*, i8*) #1

; Function Attrs: optsize
declare i32 @pthread_join(i64, i8**) #2

; Function Attrs: noreturn nounwind optsize
declare void @__assert_fail(i8*, i8*, i32, i8*) #3

attributes #0 = { nounwind optsize uwtable "less-precise-fpmad"="false" "no-frame-pointer-elim"="false" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "stack-protector-buffer-size"="8" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #1 = { nounwind optsize "less-precise-fpmad"="false" "no-frame-pointer-elim"="false" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "stack-protector-buffer-size"="8" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #2 = { optsize "less-precise-fpmad"="false" "no-frame-pointer-elim"="false" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "stack-protector-buffer-size"="8" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #3 = { noreturn nounwind optsize "less-precise-fpmad"="false" "no-frame-pointer-elim"="false" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "stack-protector-buffer-size"="8" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #4 = { nounwind optsize }
attributes #5 = { noreturn nounwind optsize }

!llvm.ident = !{!0}

!0 = metadata !{metadata !"Ubuntu clang version 3.4-1ubuntu3 (tags/RELEASE_34/final) (based on LLVM 3.4)"}
!1 = metadata !{metadata !2, metadata !2, i64 0}
!2 = metadata !{metadata !"int", metadata !3, i64 0}
!3 = metadata !{metadata !"omnipotent char", metadata !4, i64 0}
!4 = metadata !{metadata !"Simple C/C++ TBAA"}
!5 = metadata !{metadata !6, metadata !6, i64 0}
!6 = metadata !{metadata !"long", metadata !3, i64 0}
