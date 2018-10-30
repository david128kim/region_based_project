; ModuleID = 'counter_region1.c'
source_filename = "counter_region1.c"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

%struct.Shared = type { i32, i32, i32* }

; Function Attrs: nounwind optsize uwtable
define i32 @main(i32, i8** nocapture readnone) local_unnamed_addr #0 {
  %3 = tail call i32 (i64, ...) bitcast (i32 (...)* @check_malloc to i32 (i64, ...)*)(i64 16) #2
  %4 = sext i32 %3 to i64
  %5 = inttoptr i64 %4 to %struct.Shared*
  %6 = getelementptr inbounds %struct.Shared, %struct.Shared* %5, i64 0, i32 0
  store i32 0, i32* %6, align 8, !tbaa !1
  %7 = getelementptr inbounds %struct.Shared, %struct.Shared* %5, i64 0, i32 1
  store i32 2, i32* %7, align 4, !tbaa !7
  %8 = tail call i32 (i64, ...) bitcast (i32 (...)* @check_malloc to i32 (i64, ...)*)(i64 8) #2
  %9 = sext i32 %8 to i64
  %10 = inttoptr i64 %9 to i32*
  %11 = getelementptr inbounds %struct.Shared, %struct.Shared* %5, i64 0, i32 2
  store i32* %10, i32** %11, align 8, !tbaa !8
  %12 = load i32, i32* %6, align 8, !tbaa !1
  %13 = sext i32 %12 to i64
  %14 = getelementptr inbounds i32, i32* %10, i64 %13
  %15 = load i32, i32* %14, align 4, !tbaa !9
  %16 = add nsw i32 %15, 1
  store i32 %16, i32* %14, align 4, !tbaa !9
  %17 = load i32, i32* %6, align 8, !tbaa !1
  %18 = add nsw i32 %17, 1
  store i32 %18, i32* %6, align 8, !tbaa !1
  ret i32 0
}

; Function Attrs: optsize
declare i32 @check_malloc(...) local_unnamed_addr #1

attributes #0 = { nounwind optsize uwtable "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="false" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #1 = { optsize "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="false" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #2 = { nounwind optsize }

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
!9 = !{!3, !3, i64 0}
