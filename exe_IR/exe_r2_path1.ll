; ModuleID = 'exe_r2_path1_ok.c'
target datalayout = "e-p:64:64:64-i1:8:8-i8:8:8-i16:16:16-i32:32:32-i64:64:64-f32:32:32-f64:64:64-v64:64:64-v128:128:128-a0:0:64-s0:64:64-f80:128:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

%union.pthread_mutex_t = type { %struct.__pthread_mutex_s }
%struct.__pthread_mutex_s = type { i32, i32, i32, i32, i32, i16, i16, %struct.__pthread_internal_list }
%struct.__pthread_internal_list = type { %struct.__pthread_internal_list*, %struct.__pthread_internal_list* }
%union.pthread_cond_t = type { %struct.anon }
%struct.anon = type { i32, i32, i64, i64, i64, i8*, i32, i32 }

@m = common global %union.pthread_mutex_t zeroinitializer, align 8
@full = common global %union.pthread_cond_t zeroinitializer, align 8
@num = common global i32 0, align 4
@empty = common global %union.pthread_cond_t zeroinitializer, align 8
@total = common global i64 0, align 8
@flag = common global i32 0, align 4

; Function Attrs: nounwind optsize uwtable
define i32 @main() #0 {
  %1 = tail call i32 @pthread_mutex_lock(%union.pthread_mutex_t* @m) #3
  %2 = tail call i32 @pthread_cond_wait(%union.pthread_cond_t* @full, %union.pthread_mutex_t* @m) #3
  %3 = load i32* @num, align 4, !tbaa !1
  %4 = add nsw i32 %3, -1
  store i32 %4, i32* @num, align 4, !tbaa !1
  %5 = tail call i32 @pthread_mutex_unlock(%union.pthread_mutex_t* @m) #3
  %6 = tail call i32 @pthread_cond_signal(%union.pthread_cond_t* @empty) #3
  ret i32 0
}

; Function Attrs: nounwind optsize
declare i32 @pthread_mutex_lock(%union.pthread_mutex_t*) #1

; Function Attrs: optsize
declare i32 @pthread_cond_wait(%union.pthread_cond_t*, %union.pthread_mutex_t*) #2

; Function Attrs: nounwind optsize
declare i32 @pthread_mutex_unlock(%union.pthread_mutex_t*) #1

; Function Attrs: nounwind optsize
declare i32 @pthread_cond_signal(%union.pthread_cond_t*) #1

attributes #0 = { nounwind optsize uwtable "less-precise-fpmad"="false" "no-frame-pointer-elim"="false" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "stack-protector-buffer-size"="8" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #1 = { nounwind optsize "less-precise-fpmad"="false" "no-frame-pointer-elim"="false" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "stack-protector-buffer-size"="8" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #2 = { optsize "less-precise-fpmad"="false" "no-frame-pointer-elim"="false" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "stack-protector-buffer-size"="8" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #3 = { nounwind optsize }

!llvm.ident = !{!0}

!0 = metadata !{metadata !"Ubuntu clang version 3.4-1ubuntu3 (tags/RELEASE_34/final) (based on LLVM 3.4)"}
!1 = metadata !{metadata !2, metadata !2, i64 0}
!2 = metadata !{metadata !"int", metadata !3, i64 0}
!3 = metadata !{metadata !"omnipotent char", metadata !4, i64 0}
!4 = metadata !{metadata !"Simple C/C++ TBAA"}
