; ModuleID = 'program/path_1_6.c'
source_filename = "program/path_1_6.c"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

%union.pthread_cond_t = type { %struct.anon }
%struct.anon = type { i32, i32, i64, i64, i64, i8*, i32, i32 }
%union.pthread_mutex_t = type { %struct.__pthread_mutex_s }
%struct.__pthread_mutex_s = type { i32, i32, i32, i32, i32, i16, i16, %struct.__pthread_internal_list }
%struct.__pthread_internal_list = type { %struct.__pthread_internal_list*, %struct.__pthread_internal_list* }

@flag = common local_unnamed_addr global i32 0, align 4
@total = common local_unnamed_addr global i32 0, align 4
@empty = common global %union.pthread_cond_t zeroinitializer, align 8
@m = common global %union.pthread_mutex_t zeroinitializer, align 8
@num = global i32 16777216, align 4
@.str = private unnamed_addr constant [16 x i8] c"produce ....%d\0A\00", align 1
@full = common global %union.pthread_cond_t zeroinitializer, align 8
@.str.1 = private unnamed_addr constant [15 x i8] c"total ....%ld\0A\00", align 1
@.str.2 = private unnamed_addr constant [16 x i8] c"consume ....%d\0A\00", align 1

; Function Attrs: nounwind optsize uwtable
define i32 @main(i32, i8** nocapture readnone) local_unnamed_addr #0 {
  store i32 1, i32* @flag, align 4, !tbaa !1
  store i32 0, i32* @total, align 4, !tbaa !1
  %3 = tail call i32 @pthread_cond_wait(%union.pthread_cond_t* nonnull @empty, %union.pthread_mutex_t* nonnull @m) #3
  %4 = load i32, i32* @num, align 4, !tbaa !1
  %5 = add nsw i32 %4, 1
  store i32 %5, i32* @num, align 4, !tbaa !1
  %6 = tail call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([16 x i8], [16 x i8]* @.str, i64 0, i64 0), i32 0) #4
  %7 = tail call i32 @pthread_cond_signal(%union.pthread_cond_t* nonnull @full) #3
  %8 = tail call i32 @pthread_cond_wait(%union.pthread_cond_t* nonnull @empty, %union.pthread_mutex_t* nonnull @m) #3
  %9 = load i32, i32* @num, align 4, !tbaa !1
  %10 = add nsw i32 %9, 1
  store i32 %10, i32* @num, align 4, !tbaa !1
  %11 = tail call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([16 x i8], [16 x i8]* @.str, i64 0, i64 0), i32 1) #4
  %12 = tail call i32 @pthread_cond_signal(%union.pthread_cond_t* nonnull @full) #3
  %13 = load i32, i32* @total, align 4, !tbaa !1
  %14 = tail call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([15 x i8], [15 x i8]* @.str.1, i64 0, i64 0), i32 %13) #4
  %15 = load i32, i32* @num, align 4, !tbaa !1
  %16 = add nsw i32 %15, -1
  store i32 %16, i32* @num, align 4, !tbaa !1
  %17 = tail call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([16 x i8], [16 x i8]* @.str.2, i64 0, i64 0), i32 0) #4
  %18 = tail call i32 @pthread_cond_signal(%union.pthread_cond_t* nonnull @empty) #3
  %19 = load i32, i32* @total, align 4, !tbaa !1
  %20 = add nsw i32 %19, 1
  store i32 %20, i32* @total, align 4, !tbaa !1
  %21 = tail call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([15 x i8], [15 x i8]* @.str.1, i64 0, i64 0), i32 %20) #4
  %22 = load i32, i32* @num, align 4, !tbaa !1
  %23 = add nsw i32 %22, -1
  store i32 %23, i32* @num, align 4, !tbaa !1
  %24 = tail call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([16 x i8], [16 x i8]* @.str.2, i64 0, i64 0), i32 1) #4
  %25 = tail call i32 @pthread_cond_signal(%union.pthread_cond_t* nonnull @empty) #3
  ret i32 0
}

; Function Attrs: optsize
declare i32 @pthread_cond_wait(%union.pthread_cond_t*, %union.pthread_mutex_t*) local_unnamed_addr #1

; Function Attrs: nounwind optsize
declare i32 @printf(i8* nocapture readonly, ...) local_unnamed_addr #2

; Function Attrs: nounwind optsize
declare i32 @pthread_cond_signal(%union.pthread_cond_t*) local_unnamed_addr #2

attributes #0 = { nounwind optsize uwtable "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="false" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #1 = { optsize "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="false" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #2 = { nounwind optsize "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="false" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #3 = { nounwind optsize }
attributes #4 = { optsize }

!llvm.ident = !{!0}

!0 = !{!"clang version 3.9.1-4ubuntu3~16.04.2 (tags/RELEASE_391/rc2)"}
!1 = !{!2, !2, i64 0}
!2 = !{!"int", !3, i64 0}
!3 = !{!"omnipotent char", !4, i64 0}
!4 = !{!"Simple C/C++ TBAA"}
