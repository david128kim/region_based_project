; ModuleID = 'counter.bc'
source_filename = "counter.c"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

%struct.Shared = type { i32, i32, i32* }

@.str = private unnamed_addr constant [16 x i8] c"shared->counter\00", align 1
@.str.1 = private unnamed_addr constant [12 x i8] c"klee_choose\00", align 1
@.str.1.2 = private unnamed_addr constant [60 x i8] c"/home/kim-llvm/klee/runtime/Intrinsic/klee_div_zero_check.c\00", align 1
@.str.1.2.3 = private unnamed_addr constant [15 x i8] c"divide by zero\00", align 1
@.str.2 = private unnamed_addr constant [8 x i8] c"div.err\00", align 1
@.str.3 = private unnamed_addr constant [8 x i8] c"IGNORED\00", align 1
@.str.1.4 = private unnamed_addr constant [16 x i8] c"overshift error\00", align 1
@.str.2.5 = private unnamed_addr constant [14 x i8] c"overshift.err\00", align 1
@.str.6 = private unnamed_addr constant [51 x i8] c"/home/kim-llvm/klee/runtime/Intrinsic/klee_range.c\00", align 1
@.str.1.7 = private unnamed_addr constant [14 x i8] c"invalid range\00", align 1
@.str.2.8 = private unnamed_addr constant [5 x i8] c"user\00", align 1

; Function Attrs: nounwind uwtable
define i32 @main(i32, i8**) #0 !dbg !26 {
  %3 = alloca i32, align 4
  %4 = alloca i32, align 4
  %5 = alloca i8**, align 8
  %6 = alloca i32, align 4
  %7 = alloca %struct.Shared*, align 8
  store i32 0, i32* %3, align 4
  store i32 %0, i32* %4, align 4
  store i8** %1, i8*** %5, align 8
  store i32 2, i32* %6, align 4, !dbg !33
  %8 = call i32 (i64, ...) bitcast (i32 (...)* @check_malloc to i32 (i64, ...)*)(i64 16), !dbg !34
  %9 = sext i32 %8 to i64, !dbg !34
  %10 = inttoptr i64 %9 to %struct.Shared*, !dbg !34
  store %struct.Shared* %10, %struct.Shared** %7, align 8, !dbg !35
  %11 = load %struct.Shared*, %struct.Shared** %7, align 8, !dbg !36
  %12 = getelementptr inbounds %struct.Shared, %struct.Shared* %11, i32 0, i32 0, !dbg !37
  store i32 0, i32* %12, align 8, !dbg !38
  %13 = load i32, i32* %6, align 4, !dbg !39
  %14 = load %struct.Shared*, %struct.Shared** %7, align 8, !dbg !40
  %15 = getelementptr inbounds %struct.Shared, %struct.Shared* %14, i32 0, i32 1, !dbg !41
  store i32 %13, i32* %15, align 4, !dbg !42
  %16 = load %struct.Shared*, %struct.Shared** %7, align 8, !dbg !43
  %17 = getelementptr inbounds %struct.Shared, %struct.Shared* %16, i32 0, i32 1, !dbg !44
  %18 = load i32, i32* %17, align 4, !dbg !44
  %19 = sext i32 %18 to i64, !dbg !43
  %20 = mul i64 %19, 4, !dbg !45
  %21 = call i32 (i64, ...) bitcast (i32 (...)* @check_malloc to i32 (i64, ...)*)(i64 %20), !dbg !46
  %22 = sext i32 %21 to i64, !dbg !46
  %23 = inttoptr i64 %22 to i32*, !dbg !46
  %24 = load %struct.Shared*, %struct.Shared** %7, align 8, !dbg !47
  %25 = getelementptr inbounds %struct.Shared, %struct.Shared* %24, i32 0, i32 2, !dbg !48
  store i32* %23, i32** %25, align 8, !dbg !49
  %26 = load %struct.Shared*, %struct.Shared** %7, align 8, !dbg !50
  %27 = getelementptr inbounds %struct.Shared, %struct.Shared* %26, i32 0, i32 0, !dbg !51
  %28 = call i32 (i32*, i64, i8*, ...) bitcast (i32 (...)* @klee_make_symbolic to i32 (i32*, i64, i8*, ...)*)(i32* %27, i64 4, i8* getelementptr inbounds ([16 x i8], [16 x i8]* @.str, i32 0, i32 0)), !dbg !52
  %29 = load %struct.Shared*, %struct.Shared** %7, align 8, !dbg !53
  %30 = getelementptr inbounds %struct.Shared, %struct.Shared* %29, i32 0, i32 0, !dbg !54
  %31 = load i32, i32* %30, align 8, !dbg !54
  %32 = sext i32 %31 to i64, !dbg !55
  %33 = load %struct.Shared*, %struct.Shared** %7, align 8, !dbg !55
  %34 = getelementptr inbounds %struct.Shared, %struct.Shared* %33, i32 0, i32 2, !dbg !56
  %35 = load i32*, i32** %34, align 8, !dbg !56
  %36 = getelementptr inbounds i32, i32* %35, i64 %32, !dbg !55
  %37 = load i32, i32* %36, align 4, !dbg !57
  %38 = add nsw i32 %37, 1, !dbg !57
  store i32 %38, i32* %36, align 4, !dbg !57
  %39 = load %struct.Shared*, %struct.Shared** %7, align 8, !dbg !58
  %40 = getelementptr inbounds %struct.Shared, %struct.Shared* %39, i32 0, i32 0, !dbg !59
  %41 = load i32, i32* %40, align 8, !dbg !60
  %42 = add nsw i32 %41, 1, !dbg !60
  store i32 %42, i32* %40, align 8, !dbg !60
  %43 = load %struct.Shared*, %struct.Shared** %7, align 8, !dbg !61
  %44 = getelementptr inbounds %struct.Shared, %struct.Shared* %43, i32 0, i32 0, !dbg !62
  %45 = load i32, i32* %44, align 8, !dbg !62
  %46 = sext i32 %45 to i64, !dbg !63
  %47 = load %struct.Shared*, %struct.Shared** %7, align 8, !dbg !63
  %48 = getelementptr inbounds %struct.Shared, %struct.Shared* %47, i32 0, i32 2, !dbg !64
  %49 = load i32*, i32** %48, align 8, !dbg !64
  %50 = getelementptr inbounds i32, i32* %49, i64 %46, !dbg !63
  %51 = load i32, i32* %50, align 4, !dbg !65
  %52 = add nsw i32 %51, 1, !dbg !65
  store i32 %52, i32* %50, align 4, !dbg !65
  %53 = load %struct.Shared*, %struct.Shared** %7, align 8, !dbg !66
  %54 = getelementptr inbounds %struct.Shared, %struct.Shared* %53, i32 0, i32 0, !dbg !67
  %55 = load i32, i32* %54, align 8, !dbg !68
  %56 = add nsw i32 %55, 1, !dbg !68
  store i32 %56, i32* %54, align 8, !dbg !68
  ret i32 0, !dbg !69
}

; Function Attrs: nounwind readnone
declare void @llvm.dbg.declare(metadata, metadata, metadata) #1

declare i32 @check_malloc(...) #2

declare i32 @klee_make_symbolic(...) #2

; Function Attrs: nounwind uwtable
define i64 @klee_choose(i64) local_unnamed_addr #3 !dbg !70 {
  %2 = alloca i64, align 8
  %3 = bitcast i64* %2 to i8*, !dbg !79
  call void bitcast (i32 (...)* @klee_make_symbolic to void (i8*, i64, i8*)*)(i8* %3, i64 8, i8* getelementptr inbounds ([12 x i8], [12 x i8]* @.str.1, i64 0, i64 0)) #7, !dbg !80
  %4 = load i64, i64* %2, align 8, !dbg !81, !tbaa !83
  %5 = icmp ult i64 %4, %0, !dbg !87
  br i1 %5, label %7, label %6, !dbg !88

; <label>:6:                                      ; preds = %1
  call void @klee_silent_exit(i32 0) #8, !dbg !89
  unreachable, !dbg !89

; <label>:7:                                      ; preds = %1
  ret i64 %4, !dbg !90
}

; Function Attrs: nounwind readnone
declare void @llvm.dbg.value(metadata, i64, metadata, metadata) #1

; Function Attrs: argmemonly nounwind
declare void @llvm.lifetime.start(i64, i8* nocapture) #4

; Function Attrs: noreturn
declare void @klee_silent_exit(i32) local_unnamed_addr #5

; Function Attrs: argmemonly nounwind
declare void @llvm.lifetime.end(i64, i8* nocapture) #4

; Function Attrs: nounwind uwtable
define void @klee_div_zero_check(i64) local_unnamed_addr #3 !dbg !91 {
  %2 = icmp eq i64 %0, 0, !dbg !97
  br i1 %2, label %3, label %4, !dbg !99

; <label>:3:                                      ; preds = %1
  tail call void @klee_report_error(i8* getelementptr inbounds ([60 x i8], [60 x i8]* @.str.1.2, i64 0, i64 0), i32 14, i8* getelementptr inbounds ([15 x i8], [15 x i8]* @.str.1.2.3, i64 0, i64 0), i8* getelementptr inbounds ([8 x i8], [8 x i8]* @.str.2, i64 0, i64 0)) #8, !dbg !100
  unreachable, !dbg !100

; <label>:4:                                      ; preds = %1
  ret void, !dbg !101
}

; Function Attrs: noreturn
declare void @klee_report_error(i8*, i32, i8*, i8*) local_unnamed_addr #5

; Function Attrs: nounwind uwtable
define i32 @klee_int(i8*) local_unnamed_addr #3 !dbg !102 {
  %2 = alloca i32, align 4
  %3 = bitcast i32* %2 to i8*, !dbg !110
  call void bitcast (i32 (...)* @klee_make_symbolic to void (i8*, i64, i8*)*)(i8* %3, i64 4, i8* %0) #7, !dbg !111
  %4 = load i32, i32* %2, align 4, !dbg !112, !tbaa !113
  ret i32 %4, !dbg !115
}

; Function Attrs: nounwind uwtable
define void @klee_overshift_check(i64, i64) local_unnamed_addr #3 !dbg !116 {
  %3 = icmp ult i64 %1, %0, !dbg !123
  br i1 %3, label %5, label %4, !dbg !125

; <label>:4:                                      ; preds = %2
  tail call void @klee_report_error(i8* getelementptr inbounds ([8 x i8], [8 x i8]* @.str.3, i64 0, i64 0), i32 0, i8* getelementptr inbounds ([16 x i8], [16 x i8]* @.str.1.4, i64 0, i64 0), i8* getelementptr inbounds ([14 x i8], [14 x i8]* @.str.2.5, i64 0, i64 0)) #8, !dbg !126
  unreachable, !dbg !126

; <label>:5:                                      ; preds = %2
  ret void, !dbg !128
}

; Function Attrs: nounwind uwtable
define i32 @klee_range(i32, i32, i8*) local_unnamed_addr #3 !dbg !129 {
  %4 = alloca i32, align 4
  %5 = bitcast i32* %4 to i8*, !dbg !137
  %6 = icmp slt i32 %0, %1, !dbg !138
  br i1 %6, label %8, label %7, !dbg !140

; <label>:7:                                      ; preds = %3
  tail call void @klee_report_error(i8* getelementptr inbounds ([51 x i8], [51 x i8]* @.str.6, i64 0, i64 0), i32 17, i8* getelementptr inbounds ([14 x i8], [14 x i8]* @.str.1.7, i64 0, i64 0), i8* getelementptr inbounds ([5 x i8], [5 x i8]* @.str.2.8, i64 0, i64 0)) #8, !dbg !141
  unreachable, !dbg !141

; <label>:8:                                      ; preds = %3
  %9 = add nsw i32 %0, 1, !dbg !142
  %10 = icmp eq i32 %9, %1, !dbg !144
  br i1 %10, label %25, label %11, !dbg !145

; <label>:11:                                     ; preds = %8
  call void bitcast (i32 (...)* @klee_make_symbolic to void (i8*, i64, i8*)*)(i8* %5, i64 4, i8* %2) #7, !dbg !146
  %12 = icmp eq i32 %0, 0, !dbg !148
  %13 = load i32, i32* %4, align 4, !dbg !150, !tbaa !113
  br i1 %12, label %14, label %17, !dbg !152

; <label>:14:                                     ; preds = %11
  %15 = icmp ult i32 %13, %1, !dbg !153
  %16 = zext i1 %15 to i64, !dbg !154
  call void @klee_assume(i64 %16) #7, !dbg !155
  br label %23, !dbg !156

; <label>:17:                                     ; preds = %11
  %18 = icmp sge i32 %13, %0, !dbg !157
  %19 = zext i1 %18 to i64, !dbg !159
  call void @klee_assume(i64 %19) #7, !dbg !160
  %20 = load i32, i32* %4, align 4, !dbg !161, !tbaa !113
  %21 = icmp slt i32 %20, %1, !dbg !162
  %22 = zext i1 %21 to i64, !dbg !161
  call void @klee_assume(i64 %22) #7, !dbg !163
  br label %23

; <label>:23:                                     ; preds = %17, %14
  %24 = load i32, i32* %4, align 4, !dbg !164, !tbaa !113
  br label %25, !dbg !165

; <label>:25:                                     ; preds = %8, %23
  %26 = phi i32 [ %24, %23 ], [ %0, %8 ]
  ret i32 %26, !dbg !166
}

declare void @klee_assume(i64) local_unnamed_addr #6

; Function Attrs: nounwind uwtable
define weak i8* @memcpy(i8*, i8*, i64) local_unnamed_addr #3 !dbg !167 {
  %4 = icmp eq i64 %2, 0, !dbg !181
  br i1 %4, label %148, label %5, !dbg !183

; <label>:5:                                      ; preds = %3
  %6 = icmp ult i64 %2, 16, !dbg !184
  br i1 %6, label %96, label %7, !dbg !184

; <label>:7:                                      ; preds = %5
  %8 = and i64 %2, -16, !dbg !184
  %9 = icmp eq i64 %8, 0, !dbg !184
  br i1 %9, label %96, label %10, !dbg !184

; <label>:10:                                     ; preds = %7
  %11 = getelementptr i8, i8* %0, i64 %2, !dbg !184
  %12 = getelementptr i8, i8* %1, i64 %2, !dbg !184
  %13 = icmp ugt i8* %12, %0, !dbg !184
  %14 = icmp ugt i8* %11, %1, !dbg !184
  %15 = and i1 %13, %14, !dbg !184
  %16 = getelementptr i8, i8* %1, i64 %8, !dbg !184
  %17 = getelementptr i8, i8* %0, i64 %8, !dbg !184
  %18 = sub i64 %2, %8, !dbg !184
  br i1 %15, label %96, label %19, !dbg !184

; <label>:19:                                     ; preds = %10
  %20 = add i64 %8, -16
  %21 = lshr exact i64 %20, 4
  %22 = add nuw nsw i64 %21, 1
  %23 = and i64 %22, 7
  %24 = icmp ult i64 %20, 112
  br i1 %24, label %80, label %25

; <label>:25:                                     ; preds = %19
  %26 = sub nsw i64 %22, %23
  br label %27

; <label>:27:                                     ; preds = %27, %25
  %28 = phi i64 [ 0, %25 ], [ %77, %27 ]
  %29 = phi i64 [ %26, %25 ], [ %78, %27 ]
  %30 = getelementptr i8, i8* %1, i64 %28
  %31 = getelementptr i8, i8* %0, i64 %28
  %32 = bitcast i8* %30 to <16 x i8>*, !dbg !185
  %33 = load <16 x i8>, <16 x i8>* %32, align 1, !dbg !185, !tbaa !186, !alias.scope !187
  %34 = bitcast i8* %31 to <16 x i8>*, !dbg !190
  store <16 x i8> %33, <16 x i8>* %34, align 1, !dbg !190, !tbaa !186, !alias.scope !191, !noalias !187
  %35 = or i64 %28, 16, !dbg !184
  %36 = getelementptr i8, i8* %1, i64 %35
  %37 = getelementptr i8, i8* %0, i64 %35
  %38 = bitcast i8* %36 to <16 x i8>*, !dbg !185
  %39 = load <16 x i8>, <16 x i8>* %38, align 1, !dbg !185, !tbaa !186, !alias.scope !187
  %40 = bitcast i8* %37 to <16 x i8>*, !dbg !190
  store <16 x i8> %39, <16 x i8>* %40, align 1, !dbg !190, !tbaa !186, !alias.scope !191, !noalias !187
  %41 = or i64 %28, 32, !dbg !184
  %42 = getelementptr i8, i8* %1, i64 %41
  %43 = getelementptr i8, i8* %0, i64 %41
  %44 = bitcast i8* %42 to <16 x i8>*, !dbg !185
  %45 = load <16 x i8>, <16 x i8>* %44, align 1, !dbg !185, !tbaa !186, !alias.scope !187
  %46 = bitcast i8* %43 to <16 x i8>*, !dbg !190
  store <16 x i8> %45, <16 x i8>* %46, align 1, !dbg !190, !tbaa !186, !alias.scope !191, !noalias !187
  %47 = or i64 %28, 48, !dbg !184
  %48 = getelementptr i8, i8* %1, i64 %47
  %49 = getelementptr i8, i8* %0, i64 %47
  %50 = bitcast i8* %48 to <16 x i8>*, !dbg !185
  %51 = load <16 x i8>, <16 x i8>* %50, align 1, !dbg !185, !tbaa !186, !alias.scope !187
  %52 = bitcast i8* %49 to <16 x i8>*, !dbg !190
  store <16 x i8> %51, <16 x i8>* %52, align 1, !dbg !190, !tbaa !186, !alias.scope !191, !noalias !187
  %53 = or i64 %28, 64, !dbg !184
  %54 = getelementptr i8, i8* %1, i64 %53
  %55 = getelementptr i8, i8* %0, i64 %53
  %56 = bitcast i8* %54 to <16 x i8>*, !dbg !185
  %57 = load <16 x i8>, <16 x i8>* %56, align 1, !dbg !185, !tbaa !186, !alias.scope !187
  %58 = bitcast i8* %55 to <16 x i8>*, !dbg !190
  store <16 x i8> %57, <16 x i8>* %58, align 1, !dbg !190, !tbaa !186, !alias.scope !191, !noalias !187
  %59 = or i64 %28, 80, !dbg !184
  %60 = getelementptr i8, i8* %1, i64 %59
  %61 = getelementptr i8, i8* %0, i64 %59
  %62 = bitcast i8* %60 to <16 x i8>*, !dbg !185
  %63 = load <16 x i8>, <16 x i8>* %62, align 1, !dbg !185, !tbaa !186, !alias.scope !187
  %64 = bitcast i8* %61 to <16 x i8>*, !dbg !190
  store <16 x i8> %63, <16 x i8>* %64, align 1, !dbg !190, !tbaa !186, !alias.scope !191, !noalias !187
  %65 = or i64 %28, 96, !dbg !184
  %66 = getelementptr i8, i8* %1, i64 %65
  %67 = getelementptr i8, i8* %0, i64 %65
  %68 = bitcast i8* %66 to <16 x i8>*, !dbg !185
  %69 = load <16 x i8>, <16 x i8>* %68, align 1, !dbg !185, !tbaa !186, !alias.scope !187
  %70 = bitcast i8* %67 to <16 x i8>*, !dbg !190
  store <16 x i8> %69, <16 x i8>* %70, align 1, !dbg !190, !tbaa !186, !alias.scope !191, !noalias !187
  %71 = or i64 %28, 112, !dbg !184
  %72 = getelementptr i8, i8* %1, i64 %71
  %73 = getelementptr i8, i8* %0, i64 %71
  %74 = bitcast i8* %72 to <16 x i8>*, !dbg !185
  %75 = load <16 x i8>, <16 x i8>* %74, align 1, !dbg !185, !tbaa !186, !alias.scope !187
  %76 = bitcast i8* %73 to <16 x i8>*, !dbg !190
  store <16 x i8> %75, <16 x i8>* %76, align 1, !dbg !190, !tbaa !186, !alias.scope !191, !noalias !187
  %77 = add i64 %28, 128, !dbg !184
  %78 = add i64 %29, -8, !dbg !184
  %79 = icmp eq i64 %78, 0, !dbg !184
  br i1 %79, label %80, label %27, !dbg !184, !llvm.loop !193

; <label>:80:                                     ; preds = %27, %19
  %81 = phi i64 [ 0, %19 ], [ %77, %27 ]
  %82 = icmp eq i64 %23, 0
  br i1 %82, label %94, label %83

; <label>:83:                                     ; preds = %80, %83
  %84 = phi i64 [ %91, %83 ], [ %81, %80 ]
  %85 = phi i64 [ %92, %83 ], [ %23, %80 ]
  %86 = getelementptr i8, i8* %1, i64 %84
  %87 = getelementptr i8, i8* %0, i64 %84
  %88 = bitcast i8* %86 to <16 x i8>*, !dbg !185
  %89 = load <16 x i8>, <16 x i8>* %88, align 1, !dbg !185, !tbaa !186, !alias.scope !187
  %90 = bitcast i8* %87 to <16 x i8>*, !dbg !190
  store <16 x i8> %89, <16 x i8>* %90, align 1, !dbg !190, !tbaa !186, !alias.scope !191, !noalias !187
  %91 = add i64 %84, 16, !dbg !184
  %92 = add i64 %85, -1, !dbg !184
  %93 = icmp eq i64 %92, 0, !dbg !184
  br i1 %93, label %94, label %83, !dbg !184, !llvm.loop !197

; <label>:94:                                     ; preds = %83, %80
  %95 = icmp eq i64 %8, %2
  br i1 %95, label %148, label %96, !dbg !184

; <label>:96:                                     ; preds = %94, %10, %7, %5
  %97 = phi i8* [ %1, %10 ], [ %1, %7 ], [ %1, %5 ], [ %16, %94 ]
  %98 = phi i8* [ %0, %10 ], [ %0, %7 ], [ %0, %5 ], [ %17, %94 ]
  %99 = phi i64 [ %2, %10 ], [ %2, %7 ], [ %2, %5 ], [ %18, %94 ]
  %100 = add i64 %99, -1, !dbg !184
  %101 = and i64 %99, 7, !dbg !184
  %102 = icmp ult i64 %100, 7, !dbg !184
  br i1 %102, label %135, label %103, !dbg !184

; <label>:103:                                    ; preds = %96
  %104 = sub i64 %99, %101, !dbg !184
  br label %105, !dbg !184

; <label>:105:                                    ; preds = %105, %103
  %106 = phi i8* [ %97, %103 ], [ %130, %105 ]
  %107 = phi i8* [ %98, %103 ], [ %132, %105 ]
  %108 = phi i64 [ %104, %103 ], [ %133, %105 ]
  %109 = getelementptr inbounds i8, i8* %106, i64 1, !dbg !199
  %110 = load i8, i8* %106, align 1, !dbg !185, !tbaa !186
  %111 = getelementptr inbounds i8, i8* %107, i64 1, !dbg !200
  store i8 %110, i8* %107, align 1, !dbg !190, !tbaa !186
  %112 = getelementptr inbounds i8, i8* %106, i64 2, !dbg !199
  %113 = load i8, i8* %109, align 1, !dbg !185, !tbaa !186
  %114 = getelementptr inbounds i8, i8* %107, i64 2, !dbg !200
  store i8 %113, i8* %111, align 1, !dbg !190, !tbaa !186
  %115 = getelementptr inbounds i8, i8* %106, i64 3, !dbg !199
  %116 = load i8, i8* %112, align 1, !dbg !185, !tbaa !186
  %117 = getelementptr inbounds i8, i8* %107, i64 3, !dbg !200
  store i8 %116, i8* %114, align 1, !dbg !190, !tbaa !186
  %118 = getelementptr inbounds i8, i8* %106, i64 4, !dbg !199
  %119 = load i8, i8* %115, align 1, !dbg !185, !tbaa !186
  %120 = getelementptr inbounds i8, i8* %107, i64 4, !dbg !200
  store i8 %119, i8* %117, align 1, !dbg !190, !tbaa !186
  %121 = getelementptr inbounds i8, i8* %106, i64 5, !dbg !199
  %122 = load i8, i8* %118, align 1, !dbg !185, !tbaa !186
  %123 = getelementptr inbounds i8, i8* %107, i64 5, !dbg !200
  store i8 %122, i8* %120, align 1, !dbg !190, !tbaa !186
  %124 = getelementptr inbounds i8, i8* %106, i64 6, !dbg !199
  %125 = load i8, i8* %121, align 1, !dbg !185, !tbaa !186
  %126 = getelementptr inbounds i8, i8* %107, i64 6, !dbg !200
  store i8 %125, i8* %123, align 1, !dbg !190, !tbaa !186
  %127 = getelementptr inbounds i8, i8* %106, i64 7, !dbg !199
  %128 = load i8, i8* %124, align 1, !dbg !185, !tbaa !186
  %129 = getelementptr inbounds i8, i8* %107, i64 7, !dbg !200
  store i8 %128, i8* %126, align 1, !dbg !190, !tbaa !186
  %130 = getelementptr inbounds i8, i8* %106, i64 8, !dbg !199
  %131 = load i8, i8* %127, align 1, !dbg !185, !tbaa !186
  %132 = getelementptr inbounds i8, i8* %107, i64 8, !dbg !200
  store i8 %131, i8* %129, align 1, !dbg !190, !tbaa !186
  %133 = add i64 %108, -8, !dbg !183
  %134 = icmp eq i64 %133, 0, !dbg !183
  br i1 %134, label %135, label %105, !dbg !183, !llvm.loop !201

; <label>:135:                                    ; preds = %105, %96
  %136 = phi i8* [ %97, %96 ], [ %130, %105 ]
  %137 = phi i8* [ %98, %96 ], [ %132, %105 ]
  %138 = icmp eq i64 %101, 0, !dbg !202
  br i1 %138, label %148, label %139, !dbg !202

; <label>:139:                                    ; preds = %135, %139
  %140 = phi i8* [ %143, %139 ], [ %136, %135 ]
  %141 = phi i8* [ %145, %139 ], [ %137, %135 ]
  %142 = phi i64 [ %146, %139 ], [ %101, %135 ]
  %143 = getelementptr inbounds i8, i8* %140, i64 1, !dbg !199
  %144 = load i8, i8* %140, align 1, !dbg !185, !tbaa !186
  %145 = getelementptr inbounds i8, i8* %141, i64 1, !dbg !200
  store i8 %144, i8* %141, align 1, !dbg !190, !tbaa !186
  %146 = add i64 %142, -1, !dbg !183
  %147 = icmp eq i64 %146, 0, !dbg !183
  br i1 %147, label %148, label %139, !dbg !183, !llvm.loop !203

; <label>:148:                                    ; preds = %135, %139, %94, %3
  ret i8* %0, !dbg !202
}

; Function Attrs: nounwind uwtable
define weak i8* @memmove(i8*, i8*, i64) local_unnamed_addr #3 !dbg !204 {
  %4 = icmp eq i8* %1, %0, !dbg !211
  br i1 %4, label %246, label %5, !dbg !213

; <label>:5:                                      ; preds = %3
  %6 = icmp ugt i8* %1, %0, !dbg !214
  br i1 %6, label %7, label %139, !dbg !216

; <label>:7:                                      ; preds = %5
  %8 = icmp eq i64 %2, 0, !dbg !217
  br i1 %8, label %246, label %9, !dbg !217

; <label>:9:                                      ; preds = %7
  %10 = icmp ult i64 %2, 16, !dbg !220
  br i1 %10, label %100, label %11, !dbg !220

; <label>:11:                                     ; preds = %9
  %12 = and i64 %2, -16, !dbg !220
  %13 = icmp eq i64 %12, 0, !dbg !220
  br i1 %13, label %100, label %14, !dbg !220

; <label>:14:                                     ; preds = %11
  %15 = getelementptr i8, i8* %0, i64 %2, !dbg !220
  %16 = getelementptr i8, i8* %1, i64 %2, !dbg !220
  %17 = icmp ugt i8* %16, %0, !dbg !220
  %18 = icmp ugt i8* %15, %1, !dbg !220
  %19 = and i1 %17, %18, !dbg !220
  %20 = getelementptr i8, i8* %1, i64 %12, !dbg !220
  %21 = getelementptr i8, i8* %0, i64 %12, !dbg !220
  %22 = sub i64 %2, %12, !dbg !220
  br i1 %19, label %100, label %23, !dbg !220

; <label>:23:                                     ; preds = %14
  %24 = add i64 %12, -16
  %25 = lshr exact i64 %24, 4
  %26 = add nuw nsw i64 %25, 1
  %27 = and i64 %26, 7
  %28 = icmp ult i64 %24, 112
  br i1 %28, label %84, label %29

; <label>:29:                                     ; preds = %23
  %30 = sub nsw i64 %26, %27
  br label %31

; <label>:31:                                     ; preds = %31, %29
  %32 = phi i64 [ 0, %29 ], [ %81, %31 ]
  %33 = phi i64 [ %30, %29 ], [ %82, %31 ]
  %34 = getelementptr i8, i8* %1, i64 %32
  %35 = getelementptr i8, i8* %0, i64 %32
  %36 = bitcast i8* %34 to <16 x i8>*, !dbg !221
  %37 = load <16 x i8>, <16 x i8>* %36, align 1, !dbg !221, !tbaa !186, !alias.scope !223
  %38 = bitcast i8* %35 to <16 x i8>*, !dbg !226
  store <16 x i8> %37, <16 x i8>* %38, align 1, !dbg !226, !tbaa !186, !alias.scope !227, !noalias !223
  %39 = or i64 %32, 16, !dbg !220
  %40 = getelementptr i8, i8* %1, i64 %39
  %41 = getelementptr i8, i8* %0, i64 %39
  %42 = bitcast i8* %40 to <16 x i8>*, !dbg !221
  %43 = load <16 x i8>, <16 x i8>* %42, align 1, !dbg !221, !tbaa !186, !alias.scope !223
  %44 = bitcast i8* %41 to <16 x i8>*, !dbg !226
  store <16 x i8> %43, <16 x i8>* %44, align 1, !dbg !226, !tbaa !186, !alias.scope !227, !noalias !223
  %45 = or i64 %32, 32, !dbg !220
  %46 = getelementptr i8, i8* %1, i64 %45
  %47 = getelementptr i8, i8* %0, i64 %45
  %48 = bitcast i8* %46 to <16 x i8>*, !dbg !221
  %49 = load <16 x i8>, <16 x i8>* %48, align 1, !dbg !221, !tbaa !186, !alias.scope !223
  %50 = bitcast i8* %47 to <16 x i8>*, !dbg !226
  store <16 x i8> %49, <16 x i8>* %50, align 1, !dbg !226, !tbaa !186, !alias.scope !227, !noalias !223
  %51 = or i64 %32, 48, !dbg !220
  %52 = getelementptr i8, i8* %1, i64 %51
  %53 = getelementptr i8, i8* %0, i64 %51
  %54 = bitcast i8* %52 to <16 x i8>*, !dbg !221
  %55 = load <16 x i8>, <16 x i8>* %54, align 1, !dbg !221, !tbaa !186, !alias.scope !223
  %56 = bitcast i8* %53 to <16 x i8>*, !dbg !226
  store <16 x i8> %55, <16 x i8>* %56, align 1, !dbg !226, !tbaa !186, !alias.scope !227, !noalias !223
  %57 = or i64 %32, 64, !dbg !220
  %58 = getelementptr i8, i8* %1, i64 %57
  %59 = getelementptr i8, i8* %0, i64 %57
  %60 = bitcast i8* %58 to <16 x i8>*, !dbg !221
  %61 = load <16 x i8>, <16 x i8>* %60, align 1, !dbg !221, !tbaa !186, !alias.scope !223
  %62 = bitcast i8* %59 to <16 x i8>*, !dbg !226
  store <16 x i8> %61, <16 x i8>* %62, align 1, !dbg !226, !tbaa !186, !alias.scope !227, !noalias !223
  %63 = or i64 %32, 80, !dbg !220
  %64 = getelementptr i8, i8* %1, i64 %63
  %65 = getelementptr i8, i8* %0, i64 %63
  %66 = bitcast i8* %64 to <16 x i8>*, !dbg !221
  %67 = load <16 x i8>, <16 x i8>* %66, align 1, !dbg !221, !tbaa !186, !alias.scope !223
  %68 = bitcast i8* %65 to <16 x i8>*, !dbg !226
  store <16 x i8> %67, <16 x i8>* %68, align 1, !dbg !226, !tbaa !186, !alias.scope !227, !noalias !223
  %69 = or i64 %32, 96, !dbg !220
  %70 = getelementptr i8, i8* %1, i64 %69
  %71 = getelementptr i8, i8* %0, i64 %69
  %72 = bitcast i8* %70 to <16 x i8>*, !dbg !221
  %73 = load <16 x i8>, <16 x i8>* %72, align 1, !dbg !221, !tbaa !186, !alias.scope !223
  %74 = bitcast i8* %71 to <16 x i8>*, !dbg !226
  store <16 x i8> %73, <16 x i8>* %74, align 1, !dbg !226, !tbaa !186, !alias.scope !227, !noalias !223
  %75 = or i64 %32, 112, !dbg !220
  %76 = getelementptr i8, i8* %1, i64 %75
  %77 = getelementptr i8, i8* %0, i64 %75
  %78 = bitcast i8* %76 to <16 x i8>*, !dbg !221
  %79 = load <16 x i8>, <16 x i8>* %78, align 1, !dbg !221, !tbaa !186, !alias.scope !223
  %80 = bitcast i8* %77 to <16 x i8>*, !dbg !226
  store <16 x i8> %79, <16 x i8>* %80, align 1, !dbg !226, !tbaa !186, !alias.scope !227, !noalias !223
  %81 = add i64 %32, 128, !dbg !220
  %82 = add i64 %33, -8, !dbg !220
  %83 = icmp eq i64 %82, 0, !dbg !220
  br i1 %83, label %84, label %31, !dbg !220, !llvm.loop !229

; <label>:84:                                     ; preds = %31, %23
  %85 = phi i64 [ 0, %23 ], [ %81, %31 ]
  %86 = icmp eq i64 %27, 0
  br i1 %86, label %98, label %87

; <label>:87:                                     ; preds = %84, %87
  %88 = phi i64 [ %95, %87 ], [ %85, %84 ]
  %89 = phi i64 [ %96, %87 ], [ %27, %84 ]
  %90 = getelementptr i8, i8* %1, i64 %88
  %91 = getelementptr i8, i8* %0, i64 %88
  %92 = bitcast i8* %90 to <16 x i8>*, !dbg !221
  %93 = load <16 x i8>, <16 x i8>* %92, align 1, !dbg !221, !tbaa !186, !alias.scope !223
  %94 = bitcast i8* %91 to <16 x i8>*, !dbg !226
  store <16 x i8> %93, <16 x i8>* %94, align 1, !dbg !226, !tbaa !186, !alias.scope !227, !noalias !223
  %95 = add i64 %88, 16, !dbg !220
  %96 = add i64 %89, -1, !dbg !220
  %97 = icmp eq i64 %96, 0, !dbg !220
  br i1 %97, label %98, label %87, !dbg !220, !llvm.loop !231

; <label>:98:                                     ; preds = %87, %84
  %99 = icmp eq i64 %12, %2
  br i1 %99, label %246, label %100, !dbg !220

; <label>:100:                                    ; preds = %98, %14, %11, %9
  %101 = phi i8* [ %1, %14 ], [ %1, %11 ], [ %1, %9 ], [ %20, %98 ]
  %102 = phi i8* [ %0, %14 ], [ %0, %11 ], [ %0, %9 ], [ %21, %98 ]
  %103 = phi i64 [ %2, %14 ], [ %2, %11 ], [ %2, %9 ], [ %22, %98 ]
  %104 = add i64 %103, -1, !dbg !220
  %105 = and i64 %103, 7, !dbg !220
  %106 = icmp ult i64 %104, 7, !dbg !220
  br i1 %106, label %220, label %107, !dbg !220

; <label>:107:                                    ; preds = %100
  %108 = sub i64 %103, %105, !dbg !220
  br label %109, !dbg !220

; <label>:109:                                    ; preds = %109, %107
  %110 = phi i8* [ %101, %107 ], [ %134, %109 ]
  %111 = phi i8* [ %102, %107 ], [ %136, %109 ]
  %112 = phi i64 [ %108, %107 ], [ %137, %109 ]
  %113 = getelementptr inbounds i8, i8* %110, i64 1, !dbg !232
  %114 = load i8, i8* %110, align 1, !dbg !221, !tbaa !186
  %115 = getelementptr inbounds i8, i8* %111, i64 1, !dbg !233
  store i8 %114, i8* %111, align 1, !dbg !226, !tbaa !186
  %116 = getelementptr inbounds i8, i8* %110, i64 2, !dbg !232
  %117 = load i8, i8* %113, align 1, !dbg !221, !tbaa !186
  %118 = getelementptr inbounds i8, i8* %111, i64 2, !dbg !233
  store i8 %117, i8* %115, align 1, !dbg !226, !tbaa !186
  %119 = getelementptr inbounds i8, i8* %110, i64 3, !dbg !232
  %120 = load i8, i8* %116, align 1, !dbg !221, !tbaa !186
  %121 = getelementptr inbounds i8, i8* %111, i64 3, !dbg !233
  store i8 %120, i8* %118, align 1, !dbg !226, !tbaa !186
  %122 = getelementptr inbounds i8, i8* %110, i64 4, !dbg !232
  %123 = load i8, i8* %119, align 1, !dbg !221, !tbaa !186
  %124 = getelementptr inbounds i8, i8* %111, i64 4, !dbg !233
  store i8 %123, i8* %121, align 1, !dbg !226, !tbaa !186
  %125 = getelementptr inbounds i8, i8* %110, i64 5, !dbg !232
  %126 = load i8, i8* %122, align 1, !dbg !221, !tbaa !186
  %127 = getelementptr inbounds i8, i8* %111, i64 5, !dbg !233
  store i8 %126, i8* %124, align 1, !dbg !226, !tbaa !186
  %128 = getelementptr inbounds i8, i8* %110, i64 6, !dbg !232
  %129 = load i8, i8* %125, align 1, !dbg !221, !tbaa !186
  %130 = getelementptr inbounds i8, i8* %111, i64 6, !dbg !233
  store i8 %129, i8* %127, align 1, !dbg !226, !tbaa !186
  %131 = getelementptr inbounds i8, i8* %110, i64 7, !dbg !232
  %132 = load i8, i8* %128, align 1, !dbg !221, !tbaa !186
  %133 = getelementptr inbounds i8, i8* %111, i64 7, !dbg !233
  store i8 %132, i8* %130, align 1, !dbg !226, !tbaa !186
  %134 = getelementptr inbounds i8, i8* %110, i64 8, !dbg !232
  %135 = load i8, i8* %131, align 1, !dbg !221, !tbaa !186
  %136 = getelementptr inbounds i8, i8* %111, i64 8, !dbg !233
  store i8 %135, i8* %133, align 1, !dbg !226, !tbaa !186
  %137 = add i64 %112, -8, !dbg !217
  %138 = icmp eq i64 %137, 0, !dbg !217
  br i1 %138, label %220, label %109, !dbg !217, !llvm.loop !234

; <label>:139:                                    ; preds = %5
  %140 = add i64 %2, -1, !dbg !235
  %141 = icmp eq i64 %2, 0, !dbg !237
  br i1 %141, label %246, label %142, !dbg !237

; <label>:142:                                    ; preds = %139
  %143 = getelementptr inbounds i8, i8* %1, i64 %140, !dbg !239
  %144 = getelementptr inbounds i8, i8* %0, i64 %140, !dbg !240
  %145 = icmp ult i64 %2, 32, !dbg !241
  br i1 %145, label %181, label %146, !dbg !241

; <label>:146:                                    ; preds = %142
  %147 = and i64 %2, 31, !dbg !241
  %148 = sub i64 %2, %147, !dbg !241
  %149 = icmp eq i64 %148, 0, !dbg !241
  br i1 %149, label %181, label %150, !dbg !241

; <label>:150:                                    ; preds = %146
  %151 = getelementptr i8, i8* %0, i64 %2, !dbg !241
  %152 = getelementptr i8, i8* %1, i64 %2, !dbg !241
  %153 = icmp ugt i8* %152, %0, !dbg !241
  %154 = icmp ugt i8* %151, %1, !dbg !241
  %155 = and i1 %153, %154, !dbg !241
  %156 = sub i64 %147, %2, !dbg !241
  %157 = getelementptr i8, i8* %143, i64 %156, !dbg !241
  %158 = getelementptr i8, i8* %144, i64 %156, !dbg !241
  br i1 %155, label %181, label %159, !dbg !241

; <label>:159:                                    ; preds = %150, %159
  %160 = phi i64 [ %177, %159 ], [ 0, %150 ]
  %161 = sub i64 0, %160, !dbg !241
  %162 = getelementptr i8, i8* %143, i64 %161
  %163 = sub i64 0, %160, !dbg !241
  %164 = getelementptr i8, i8* %144, i64 %163
  %165 = getelementptr i8, i8* %162, i64 -15, !dbg !242
  %166 = bitcast i8* %165 to <16 x i8>*, !dbg !242
  %167 = load <16 x i8>, <16 x i8>* %166, align 1, !dbg !242, !tbaa !186, !alias.scope !244
  %168 = getelementptr i8, i8* %162, i64 -16, !dbg !242
  %169 = getelementptr i8, i8* %168, i64 -15, !dbg !242
  %170 = bitcast i8* %169 to <16 x i8>*, !dbg !242
  %171 = load <16 x i8>, <16 x i8>* %170, align 1, !dbg !242, !tbaa !186, !alias.scope !244
  %172 = getelementptr i8, i8* %164, i64 -15, !dbg !247
  %173 = bitcast i8* %172 to <16 x i8>*, !dbg !247
  store <16 x i8> %167, <16 x i8>* %173, align 1, !dbg !247, !tbaa !186, !alias.scope !248, !noalias !244
  %174 = getelementptr i8, i8* %164, i64 -16, !dbg !247
  %175 = getelementptr i8, i8* %174, i64 -15, !dbg !247
  %176 = bitcast i8* %175 to <16 x i8>*, !dbg !247
  store <16 x i8> %171, <16 x i8>* %176, align 1, !dbg !247, !tbaa !186, !alias.scope !248, !noalias !244
  %177 = add i64 %160, 32, !dbg !241
  %178 = icmp eq i64 %177, %148, !dbg !241
  br i1 %178, label %179, label %159, !dbg !241, !llvm.loop !250

; <label>:179:                                    ; preds = %159
  %180 = icmp eq i64 %147, 0
  br i1 %180, label %246, label %181, !dbg !241

; <label>:181:                                    ; preds = %179, %150, %146, %142
  %182 = phi i8* [ %143, %150 ], [ %143, %146 ], [ %143, %142 ], [ %157, %179 ]
  %183 = phi i8* [ %144, %150 ], [ %144, %146 ], [ %144, %142 ], [ %158, %179 ]
  %184 = phi i64 [ %2, %150 ], [ %2, %146 ], [ %2, %142 ], [ %147, %179 ]
  %185 = add i64 %184, -1, !dbg !241
  %186 = and i64 %184, 7, !dbg !241
  %187 = icmp ult i64 %185, 7, !dbg !241
  br i1 %187, label %233, label %188, !dbg !241

; <label>:188:                                    ; preds = %181
  %189 = sub i64 %184, %186, !dbg !241
  br label %190, !dbg !241

; <label>:190:                                    ; preds = %190, %188
  %191 = phi i8* [ %182, %188 ], [ %215, %190 ]
  %192 = phi i8* [ %183, %188 ], [ %217, %190 ]
  %193 = phi i64 [ %189, %188 ], [ %218, %190 ]
  %194 = getelementptr inbounds i8, i8* %191, i64 -1, !dbg !252
  %195 = load i8, i8* %191, align 1, !dbg !242, !tbaa !186
  %196 = getelementptr inbounds i8, i8* %192, i64 -1, !dbg !253
  store i8 %195, i8* %192, align 1, !dbg !247, !tbaa !186
  %197 = getelementptr inbounds i8, i8* %191, i64 -2, !dbg !252
  %198 = load i8, i8* %194, align 1, !dbg !242, !tbaa !186
  %199 = getelementptr inbounds i8, i8* %192, i64 -2, !dbg !253
  store i8 %198, i8* %196, align 1, !dbg !247, !tbaa !186
  %200 = getelementptr inbounds i8, i8* %191, i64 -3, !dbg !252
  %201 = load i8, i8* %197, align 1, !dbg !242, !tbaa !186
  %202 = getelementptr inbounds i8, i8* %192, i64 -3, !dbg !253
  store i8 %201, i8* %199, align 1, !dbg !247, !tbaa !186
  %203 = getelementptr inbounds i8, i8* %191, i64 -4, !dbg !252
  %204 = load i8, i8* %200, align 1, !dbg !242, !tbaa !186
  %205 = getelementptr inbounds i8, i8* %192, i64 -4, !dbg !253
  store i8 %204, i8* %202, align 1, !dbg !247, !tbaa !186
  %206 = getelementptr inbounds i8, i8* %191, i64 -5, !dbg !252
  %207 = load i8, i8* %203, align 1, !dbg !242, !tbaa !186
  %208 = getelementptr inbounds i8, i8* %192, i64 -5, !dbg !253
  store i8 %207, i8* %205, align 1, !dbg !247, !tbaa !186
  %209 = getelementptr inbounds i8, i8* %191, i64 -6, !dbg !252
  %210 = load i8, i8* %206, align 1, !dbg !242, !tbaa !186
  %211 = getelementptr inbounds i8, i8* %192, i64 -6, !dbg !253
  store i8 %210, i8* %208, align 1, !dbg !247, !tbaa !186
  %212 = getelementptr inbounds i8, i8* %191, i64 -7, !dbg !252
  %213 = load i8, i8* %209, align 1, !dbg !242, !tbaa !186
  %214 = getelementptr inbounds i8, i8* %192, i64 -7, !dbg !253
  store i8 %213, i8* %211, align 1, !dbg !247, !tbaa !186
  %215 = getelementptr inbounds i8, i8* %191, i64 -8, !dbg !252
  %216 = load i8, i8* %212, align 1, !dbg !242, !tbaa !186
  %217 = getelementptr inbounds i8, i8* %192, i64 -8, !dbg !253
  store i8 %216, i8* %214, align 1, !dbg !247, !tbaa !186
  %218 = add i64 %193, -8, !dbg !237
  %219 = icmp eq i64 %218, 0, !dbg !237
  br i1 %219, label %233, label %190, !dbg !237, !llvm.loop !254

; <label>:220:                                    ; preds = %109, %100
  %221 = phi i8* [ %101, %100 ], [ %134, %109 ]
  %222 = phi i8* [ %102, %100 ], [ %136, %109 ]
  %223 = icmp eq i64 %105, 0, !dbg !255
  br i1 %223, label %246, label %224, !dbg !255

; <label>:224:                                    ; preds = %220, %224
  %225 = phi i8* [ %228, %224 ], [ %221, %220 ]
  %226 = phi i8* [ %230, %224 ], [ %222, %220 ]
  %227 = phi i64 [ %231, %224 ], [ %105, %220 ]
  %228 = getelementptr inbounds i8, i8* %225, i64 1, !dbg !232
  %229 = load i8, i8* %225, align 1, !dbg !221, !tbaa !186
  %230 = getelementptr inbounds i8, i8* %226, i64 1, !dbg !233
  store i8 %229, i8* %226, align 1, !dbg !226, !tbaa !186
  %231 = add i64 %227, -1, !dbg !217
  %232 = icmp eq i64 %231, 0, !dbg !217
  br i1 %232, label %246, label %224, !dbg !217, !llvm.loop !256

; <label>:233:                                    ; preds = %190, %181
  %234 = phi i8* [ %182, %181 ], [ %215, %190 ]
  %235 = phi i8* [ %183, %181 ], [ %217, %190 ]
  %236 = icmp eq i64 %186, 0, !dbg !255
  br i1 %236, label %246, label %237, !dbg !255

; <label>:237:                                    ; preds = %233, %237
  %238 = phi i8* [ %241, %237 ], [ %234, %233 ]
  %239 = phi i8* [ %243, %237 ], [ %235, %233 ]
  %240 = phi i64 [ %244, %237 ], [ %186, %233 ]
  %241 = getelementptr inbounds i8, i8* %238, i64 -1, !dbg !252
  %242 = load i8, i8* %238, align 1, !dbg !242, !tbaa !186
  %243 = getelementptr inbounds i8, i8* %239, i64 -1, !dbg !253
  store i8 %242, i8* %239, align 1, !dbg !247, !tbaa !186
  %244 = add i64 %240, -1, !dbg !237
  %245 = icmp eq i64 %244, 0, !dbg !237
  br i1 %245, label %246, label %237, !dbg !237, !llvm.loop !257

; <label>:246:                                    ; preds = %233, %237, %220, %224, %179, %98, %139, %7, %3
  ret i8* %0, !dbg !255
}

; Function Attrs: nounwind uwtable
define weak i8* @mempcpy(i8*, i8*, i64) local_unnamed_addr #3 !dbg !258 {
  %4 = icmp eq i64 %2, 0, !dbg !265
  br i1 %4, label %150, label %5, !dbg !267

; <label>:5:                                      ; preds = %3
  %6 = icmp ult i64 %2, 16, !dbg !268
  br i1 %6, label %96, label %7, !dbg !268

; <label>:7:                                      ; preds = %5
  %8 = and i64 %2, -16, !dbg !268
  %9 = icmp eq i64 %8, 0, !dbg !268
  br i1 %9, label %96, label %10, !dbg !268

; <label>:10:                                     ; preds = %7
  %11 = getelementptr i8, i8* %0, i64 %2, !dbg !268
  %12 = getelementptr i8, i8* %1, i64 %2, !dbg !268
  %13 = icmp ugt i8* %12, %0, !dbg !268
  %14 = icmp ugt i8* %11, %1, !dbg !268
  %15 = and i1 %13, %14, !dbg !268
  %16 = getelementptr i8, i8* %1, i64 %8, !dbg !268
  %17 = getelementptr i8, i8* %0, i64 %8, !dbg !268
  %18 = sub i64 %2, %8, !dbg !268
  br i1 %15, label %96, label %19, !dbg !268

; <label>:19:                                     ; preds = %10
  %20 = add i64 %8, -16
  %21 = lshr exact i64 %20, 4
  %22 = add nuw nsw i64 %21, 1
  %23 = and i64 %22, 7
  %24 = icmp ult i64 %20, 112
  br i1 %24, label %80, label %25

; <label>:25:                                     ; preds = %19
  %26 = sub nsw i64 %22, %23
  br label %27

; <label>:27:                                     ; preds = %27, %25
  %28 = phi i64 [ 0, %25 ], [ %77, %27 ]
  %29 = phi i64 [ %26, %25 ], [ %78, %27 ]
  %30 = getelementptr i8, i8* %1, i64 %28
  %31 = getelementptr i8, i8* %0, i64 %28
  %32 = bitcast i8* %30 to <16 x i8>*, !dbg !269
  %33 = load <16 x i8>, <16 x i8>* %32, align 1, !dbg !269, !tbaa !186, !alias.scope !270
  %34 = bitcast i8* %31 to <16 x i8>*, !dbg !273
  store <16 x i8> %33, <16 x i8>* %34, align 1, !dbg !273, !tbaa !186, !alias.scope !274, !noalias !270
  %35 = or i64 %28, 16, !dbg !268
  %36 = getelementptr i8, i8* %1, i64 %35
  %37 = getelementptr i8, i8* %0, i64 %35
  %38 = bitcast i8* %36 to <16 x i8>*, !dbg !269
  %39 = load <16 x i8>, <16 x i8>* %38, align 1, !dbg !269, !tbaa !186, !alias.scope !270
  %40 = bitcast i8* %37 to <16 x i8>*, !dbg !273
  store <16 x i8> %39, <16 x i8>* %40, align 1, !dbg !273, !tbaa !186, !alias.scope !274, !noalias !270
  %41 = or i64 %28, 32, !dbg !268
  %42 = getelementptr i8, i8* %1, i64 %41
  %43 = getelementptr i8, i8* %0, i64 %41
  %44 = bitcast i8* %42 to <16 x i8>*, !dbg !269
  %45 = load <16 x i8>, <16 x i8>* %44, align 1, !dbg !269, !tbaa !186, !alias.scope !270
  %46 = bitcast i8* %43 to <16 x i8>*, !dbg !273
  store <16 x i8> %45, <16 x i8>* %46, align 1, !dbg !273, !tbaa !186, !alias.scope !274, !noalias !270
  %47 = or i64 %28, 48, !dbg !268
  %48 = getelementptr i8, i8* %1, i64 %47
  %49 = getelementptr i8, i8* %0, i64 %47
  %50 = bitcast i8* %48 to <16 x i8>*, !dbg !269
  %51 = load <16 x i8>, <16 x i8>* %50, align 1, !dbg !269, !tbaa !186, !alias.scope !270
  %52 = bitcast i8* %49 to <16 x i8>*, !dbg !273
  store <16 x i8> %51, <16 x i8>* %52, align 1, !dbg !273, !tbaa !186, !alias.scope !274, !noalias !270
  %53 = or i64 %28, 64, !dbg !268
  %54 = getelementptr i8, i8* %1, i64 %53
  %55 = getelementptr i8, i8* %0, i64 %53
  %56 = bitcast i8* %54 to <16 x i8>*, !dbg !269
  %57 = load <16 x i8>, <16 x i8>* %56, align 1, !dbg !269, !tbaa !186, !alias.scope !270
  %58 = bitcast i8* %55 to <16 x i8>*, !dbg !273
  store <16 x i8> %57, <16 x i8>* %58, align 1, !dbg !273, !tbaa !186, !alias.scope !274, !noalias !270
  %59 = or i64 %28, 80, !dbg !268
  %60 = getelementptr i8, i8* %1, i64 %59
  %61 = getelementptr i8, i8* %0, i64 %59
  %62 = bitcast i8* %60 to <16 x i8>*, !dbg !269
  %63 = load <16 x i8>, <16 x i8>* %62, align 1, !dbg !269, !tbaa !186, !alias.scope !270
  %64 = bitcast i8* %61 to <16 x i8>*, !dbg !273
  store <16 x i8> %63, <16 x i8>* %64, align 1, !dbg !273, !tbaa !186, !alias.scope !274, !noalias !270
  %65 = or i64 %28, 96, !dbg !268
  %66 = getelementptr i8, i8* %1, i64 %65
  %67 = getelementptr i8, i8* %0, i64 %65
  %68 = bitcast i8* %66 to <16 x i8>*, !dbg !269
  %69 = load <16 x i8>, <16 x i8>* %68, align 1, !dbg !269, !tbaa !186, !alias.scope !270
  %70 = bitcast i8* %67 to <16 x i8>*, !dbg !273
  store <16 x i8> %69, <16 x i8>* %70, align 1, !dbg !273, !tbaa !186, !alias.scope !274, !noalias !270
  %71 = or i64 %28, 112, !dbg !268
  %72 = getelementptr i8, i8* %1, i64 %71
  %73 = getelementptr i8, i8* %0, i64 %71
  %74 = bitcast i8* %72 to <16 x i8>*, !dbg !269
  %75 = load <16 x i8>, <16 x i8>* %74, align 1, !dbg !269, !tbaa !186, !alias.scope !270
  %76 = bitcast i8* %73 to <16 x i8>*, !dbg !273
  store <16 x i8> %75, <16 x i8>* %76, align 1, !dbg !273, !tbaa !186, !alias.scope !274, !noalias !270
  %77 = add i64 %28, 128, !dbg !268
  %78 = add i64 %29, -8, !dbg !268
  %79 = icmp eq i64 %78, 0, !dbg !268
  br i1 %79, label %80, label %27, !dbg !268, !llvm.loop !276

; <label>:80:                                     ; preds = %27, %19
  %81 = phi i64 [ 0, %19 ], [ %77, %27 ]
  %82 = icmp eq i64 %23, 0
  br i1 %82, label %94, label %83

; <label>:83:                                     ; preds = %80, %83
  %84 = phi i64 [ %91, %83 ], [ %81, %80 ]
  %85 = phi i64 [ %92, %83 ], [ %23, %80 ]
  %86 = getelementptr i8, i8* %1, i64 %84
  %87 = getelementptr i8, i8* %0, i64 %84
  %88 = bitcast i8* %86 to <16 x i8>*, !dbg !269
  %89 = load <16 x i8>, <16 x i8>* %88, align 1, !dbg !269, !tbaa !186, !alias.scope !270
  %90 = bitcast i8* %87 to <16 x i8>*, !dbg !273
  store <16 x i8> %89, <16 x i8>* %90, align 1, !dbg !273, !tbaa !186, !alias.scope !274, !noalias !270
  %91 = add i64 %84, 16, !dbg !268
  %92 = add i64 %85, -1, !dbg !268
  %93 = icmp eq i64 %92, 0, !dbg !268
  br i1 %93, label %94, label %83, !dbg !268, !llvm.loop !278

; <label>:94:                                     ; preds = %83, %80
  %95 = icmp eq i64 %8, %2
  br i1 %95, label %148, label %96, !dbg !268

; <label>:96:                                     ; preds = %94, %10, %7, %5
  %97 = phi i8* [ %1, %10 ], [ %1, %7 ], [ %1, %5 ], [ %16, %94 ]
  %98 = phi i8* [ %0, %10 ], [ %0, %7 ], [ %0, %5 ], [ %17, %94 ]
  %99 = phi i64 [ %2, %10 ], [ %2, %7 ], [ %2, %5 ], [ %18, %94 ]
  %100 = add i64 %99, -1, !dbg !268
  %101 = and i64 %99, 7, !dbg !268
  %102 = icmp ult i64 %100, 7, !dbg !268
  br i1 %102, label %135, label %103, !dbg !268

; <label>:103:                                    ; preds = %96
  %104 = sub i64 %99, %101, !dbg !268
  br label %105, !dbg !268

; <label>:105:                                    ; preds = %105, %103
  %106 = phi i8* [ %97, %103 ], [ %130, %105 ]
  %107 = phi i8* [ %98, %103 ], [ %132, %105 ]
  %108 = phi i64 [ %104, %103 ], [ %133, %105 ]
  %109 = getelementptr inbounds i8, i8* %106, i64 1, !dbg !279
  %110 = load i8, i8* %106, align 1, !dbg !269, !tbaa !186
  %111 = getelementptr inbounds i8, i8* %107, i64 1, !dbg !280
  store i8 %110, i8* %107, align 1, !dbg !273, !tbaa !186
  %112 = getelementptr inbounds i8, i8* %106, i64 2, !dbg !279
  %113 = load i8, i8* %109, align 1, !dbg !269, !tbaa !186
  %114 = getelementptr inbounds i8, i8* %107, i64 2, !dbg !280
  store i8 %113, i8* %111, align 1, !dbg !273, !tbaa !186
  %115 = getelementptr inbounds i8, i8* %106, i64 3, !dbg !279
  %116 = load i8, i8* %112, align 1, !dbg !269, !tbaa !186
  %117 = getelementptr inbounds i8, i8* %107, i64 3, !dbg !280
  store i8 %116, i8* %114, align 1, !dbg !273, !tbaa !186
  %118 = getelementptr inbounds i8, i8* %106, i64 4, !dbg !279
  %119 = load i8, i8* %115, align 1, !dbg !269, !tbaa !186
  %120 = getelementptr inbounds i8, i8* %107, i64 4, !dbg !280
  store i8 %119, i8* %117, align 1, !dbg !273, !tbaa !186
  %121 = getelementptr inbounds i8, i8* %106, i64 5, !dbg !279
  %122 = load i8, i8* %118, align 1, !dbg !269, !tbaa !186
  %123 = getelementptr inbounds i8, i8* %107, i64 5, !dbg !280
  store i8 %122, i8* %120, align 1, !dbg !273, !tbaa !186
  %124 = getelementptr inbounds i8, i8* %106, i64 6, !dbg !279
  %125 = load i8, i8* %121, align 1, !dbg !269, !tbaa !186
  %126 = getelementptr inbounds i8, i8* %107, i64 6, !dbg !280
  store i8 %125, i8* %123, align 1, !dbg !273, !tbaa !186
  %127 = getelementptr inbounds i8, i8* %106, i64 7, !dbg !279
  %128 = load i8, i8* %124, align 1, !dbg !269, !tbaa !186
  %129 = getelementptr inbounds i8, i8* %107, i64 7, !dbg !280
  store i8 %128, i8* %126, align 1, !dbg !273, !tbaa !186
  %130 = getelementptr inbounds i8, i8* %106, i64 8, !dbg !279
  %131 = load i8, i8* %127, align 1, !dbg !269, !tbaa !186
  %132 = getelementptr inbounds i8, i8* %107, i64 8, !dbg !280
  store i8 %131, i8* %129, align 1, !dbg !273, !tbaa !186
  %133 = add i64 %108, -8, !dbg !267
  %134 = icmp eq i64 %133, 0, !dbg !267
  br i1 %134, label %135, label %105, !dbg !267, !llvm.loop !281

; <label>:135:                                    ; preds = %105, %96
  %136 = phi i8* [ %97, %96 ], [ %130, %105 ]
  %137 = phi i8* [ %98, %96 ], [ %132, %105 ]
  %138 = icmp eq i64 %101, 0, !dbg !268
  br i1 %138, label %148, label %139, !dbg !268

; <label>:139:                                    ; preds = %135, %139
  %140 = phi i8* [ %143, %139 ], [ %136, %135 ]
  %141 = phi i8* [ %145, %139 ], [ %137, %135 ]
  %142 = phi i64 [ %146, %139 ], [ %101, %135 ]
  %143 = getelementptr inbounds i8, i8* %140, i64 1, !dbg !279
  %144 = load i8, i8* %140, align 1, !dbg !269, !tbaa !186
  %145 = getelementptr inbounds i8, i8* %141, i64 1, !dbg !280
  store i8 %144, i8* %141, align 1, !dbg !273, !tbaa !186
  %146 = add i64 %142, -1, !dbg !267
  %147 = icmp eq i64 %146, 0, !dbg !267
  br i1 %147, label %148, label %139, !dbg !267, !llvm.loop !282

; <label>:148:                                    ; preds = %135, %139, %94
  %149 = getelementptr i8, i8* %0, i64 %2, !dbg !268
  br label %150, !dbg !283

; <label>:150:                                    ; preds = %148, %3
  %151 = phi i8* [ %0, %3 ], [ %149, %148 ]
  ret i8* %151, !dbg !283
}

; Function Attrs: nounwind uwtable
define weak i8* @memset(i8*, i32, i64) local_unnamed_addr #3 !dbg !284 {
  %4 = icmp eq i64 %2, 0, !dbg !294
  br i1 %4, label %34, label %5, !dbg !296

; <label>:5:                                      ; preds = %3
  %6 = trunc i32 %1 to i8, !dbg !297
  %7 = add i64 %2, -1, !dbg !296
  %8 = and i64 %2, 7, !dbg !296
  %9 = icmp ult i64 %7, 7, !dbg !296
  br i1 %9, label %25, label %10, !dbg !296

; <label>:10:                                     ; preds = %5
  %11 = sub i64 %2, %8, !dbg !296
  br label %12, !dbg !296

; <label>:12:                                     ; preds = %12, %10
  %13 = phi i8* [ %0, %10 ], [ %22, %12 ]
  %14 = phi i64 [ %11, %10 ], [ %23, %12 ]
  %15 = getelementptr inbounds i8, i8* %13, i64 1, !dbg !298
  store volatile i8 %6, i8* %13, align 1, !dbg !299, !tbaa !186
  %16 = getelementptr inbounds i8, i8* %13, i64 2, !dbg !298
  store volatile i8 %6, i8* %15, align 1, !dbg !299, !tbaa !186
  %17 = getelementptr inbounds i8, i8* %13, i64 3, !dbg !298
  store volatile i8 %6, i8* %16, align 1, !dbg !299, !tbaa !186
  %18 = getelementptr inbounds i8, i8* %13, i64 4, !dbg !298
  store volatile i8 %6, i8* %17, align 1, !dbg !299, !tbaa !186
  %19 = getelementptr inbounds i8, i8* %13, i64 5, !dbg !298
  store volatile i8 %6, i8* %18, align 1, !dbg !299, !tbaa !186
  %20 = getelementptr inbounds i8, i8* %13, i64 6, !dbg !298
  store volatile i8 %6, i8* %19, align 1, !dbg !299, !tbaa !186
  %21 = getelementptr inbounds i8, i8* %13, i64 7, !dbg !298
  store volatile i8 %6, i8* %20, align 1, !dbg !299, !tbaa !186
  %22 = getelementptr inbounds i8, i8* %13, i64 8, !dbg !298
  store volatile i8 %6, i8* %21, align 1, !dbg !299, !tbaa !186
  %23 = add i64 %14, -8, !dbg !296
  %24 = icmp eq i64 %23, 0, !dbg !296
  br i1 %24, label %25, label %12, !dbg !296, !llvm.loop !300

; <label>:25:                                     ; preds = %12, %5
  %26 = phi i8* [ %0, %5 ], [ %22, %12 ]
  %27 = icmp eq i64 %8, 0, !dbg !302
  br i1 %27, label %34, label %28, !dbg !302

; <label>:28:                                     ; preds = %25, %28
  %29 = phi i8* [ %31, %28 ], [ %26, %25 ]
  %30 = phi i64 [ %32, %28 ], [ %8, %25 ]
  %31 = getelementptr inbounds i8, i8* %29, i64 1, !dbg !298
  store volatile i8 %6, i8* %29, align 1, !dbg !299, !tbaa !186
  %32 = add i64 %30, -1, !dbg !296
  %33 = icmp eq i64 %32, 0, !dbg !296
  br i1 %33, label %34, label %28, !dbg !296, !llvm.loop !303

; <label>:34:                                     ; preds = %25, %28, %3
  ret i8* %0, !dbg !302
}

attributes #0 = { nounwind uwtable "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #1 = { nounwind readnone }
attributes #2 = { "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #3 = { nounwind uwtable "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="false" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #4 = { argmemonly nounwind }
attributes #5 = { noreturn "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="false" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #6 = { "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="false" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #7 = { nobuiltin nounwind }
attributes #8 = { nobuiltin noreturn nounwind }

!llvm.dbg.cu = !{!0, !3, !5, !7, !9, !11, !15, !17, !19, !21}
!llvm.module.flags = !{!23, !24}
!llvm.ident = !{!25, !25, !25, !25, !25, !25, !25, !25, !25, !25}

!0 = distinct !DICompileUnit(language: DW_LANG_C99, file: !1, producer: "clang version 3.9.1-4ubuntu3~16.04.2 (tags/RELEASE_391/rc2)", isOptimized: false, runtimeVersion: 0, emissionKind: FullDebug, enums: !2)
!1 = !DIFile(filename: "counter.c", directory: "/home/kim-llvm/region_based_project/test-room")
!2 = !{}
!3 = distinct !DICompileUnit(language: DW_LANG_C89, file: !4, producer: "clang version 3.9.1-4ubuntu3~16.04.2 (tags/RELEASE_391/rc2)", isOptimized: true, runtimeVersion: 0, emissionKind: FullDebug, enums: !2)
!4 = !DIFile(filename: "/home/kim-llvm/klee/runtime/Intrinsic/klee_choose.c", directory: "/home/kim-llvm/klee/klee_build_dir/runtime/Intrinsic")
!5 = distinct !DICompileUnit(language: DW_LANG_C89, file: !6, producer: "clang version 3.9.1-4ubuntu3~16.04.2 (tags/RELEASE_391/rc2)", isOptimized: true, runtimeVersion: 0, emissionKind: FullDebug, enums: !2)
!6 = !DIFile(filename: "/home/kim-llvm/klee/runtime/Intrinsic/klee_div_zero_check.c", directory: "/home/kim-llvm/klee/klee_build_dir/runtime/Intrinsic")
!7 = distinct !DICompileUnit(language: DW_LANG_C89, file: !8, producer: "clang version 3.9.1-4ubuntu3~16.04.2 (tags/RELEASE_391/rc2)", isOptimized: true, runtimeVersion: 0, emissionKind: FullDebug, enums: !2)
!8 = !DIFile(filename: "/home/kim-llvm/klee/runtime/Intrinsic/klee_int.c", directory: "/home/kim-llvm/klee/klee_build_dir/runtime/Intrinsic")
!9 = distinct !DICompileUnit(language: DW_LANG_C89, file: !10, producer: "clang version 3.9.1-4ubuntu3~16.04.2 (tags/RELEASE_391/rc2)", isOptimized: true, runtimeVersion: 0, emissionKind: FullDebug, enums: !2)
!10 = !DIFile(filename: "/home/kim-llvm/klee/runtime/Intrinsic/klee_overshift_check.c", directory: "/home/kim-llvm/klee/klee_build_dir/runtime/Intrinsic")
!11 = distinct !DICompileUnit(language: DW_LANG_C89, file: !12, producer: "clang version 3.9.1-4ubuntu3~16.04.2 (tags/RELEASE_391/rc2)", isOptimized: true, runtimeVersion: 0, emissionKind: FullDebug, enums: !2, retainedTypes: !13)
!12 = !DIFile(filename: "/home/kim-llvm/klee/runtime/Intrinsic/klee_range.c", directory: "/home/kim-llvm/klee/klee_build_dir/runtime/Intrinsic")
!13 = !{!14}
!14 = !DIBasicType(name: "unsigned int", size: 32, align: 32, encoding: DW_ATE_unsigned)
!15 = distinct !DICompileUnit(language: DW_LANG_C89, file: !16, producer: "clang version 3.9.1-4ubuntu3~16.04.2 (tags/RELEASE_391/rc2)", isOptimized: true, runtimeVersion: 0, emissionKind: FullDebug, enums: !2)
!16 = !DIFile(filename: "/home/kim-llvm/klee/runtime/Intrinsic/memcpy.c", directory: "/home/kim-llvm/klee/klee_build_dir/runtime/Intrinsic")
!17 = distinct !DICompileUnit(language: DW_LANG_C89, file: !18, producer: "clang version 3.9.1-4ubuntu3~16.04.2 (tags/RELEASE_391/rc2)", isOptimized: true, runtimeVersion: 0, emissionKind: FullDebug, enums: !2)
!18 = !DIFile(filename: "/home/kim-llvm/klee/runtime/Intrinsic/memmove.c", directory: "/home/kim-llvm/klee/klee_build_dir/runtime/Intrinsic")
!19 = distinct !DICompileUnit(language: DW_LANG_C89, file: !20, producer: "clang version 3.9.1-4ubuntu3~16.04.2 (tags/RELEASE_391/rc2)", isOptimized: true, runtimeVersion: 0, emissionKind: FullDebug, enums: !2)
!20 = !DIFile(filename: "/home/kim-llvm/klee/runtime/Intrinsic/mempcpy.c", directory: "/home/kim-llvm/klee/klee_build_dir/runtime/Intrinsic")
!21 = distinct !DICompileUnit(language: DW_LANG_C89, file: !22, producer: "clang version 3.9.1-4ubuntu3~16.04.2 (tags/RELEASE_391/rc2)", isOptimized: true, runtimeVersion: 0, emissionKind: FullDebug, enums: !2)
!22 = !DIFile(filename: "/home/kim-llvm/klee/runtime/Intrinsic/memset.c", directory: "/home/kim-llvm/klee/klee_build_dir/runtime/Intrinsic")
!23 = !{i32 2, !"Dwarf Version", i32 4}
!24 = !{i32 2, !"Debug Info Version", i32 3}
!25 = !{!"clang version 3.9.1-4ubuntu3~16.04.2 (tags/RELEASE_391/rc2)"}
!26 = distinct !DISubprogram(name: "main", scope: !1, file: !1, line: 14, type: !27, isLocal: false, isDefinition: true, scopeLine: 14, flags: DIFlagPrototyped, isOptimized: false, unit: !0, variables: !2)
!27 = !DISubroutineType(types: !28)
!28 = !{!29, !29, !30}
!29 = !DIBasicType(name: "int", size: 32, align: 32, encoding: DW_ATE_signed)
!30 = !DIDerivedType(tag: DW_TAG_pointer_type, baseType: !31, size: 64, align: 64)
!31 = !DIDerivedType(tag: DW_TAG_pointer_type, baseType: !32, size: 64, align: 64)
!32 = !DIBasicType(name: "char", size: 8, align: 8, encoding: DW_ATE_signed_char)
!33 = !DILocation(line: 16, column: 7, scope: !26)
!34 = !DILocation(line: 17, column: 20, scope: !26)
!35 = !DILocation(line: 17, column: 11, scope: !26)
!36 = !DILocation(line: 18, column: 3, scope: !26)
!37 = !DILocation(line: 18, column: 11, scope: !26)
!38 = !DILocation(line: 18, column: 19, scope: !26)
!39 = !DILocation(line: 19, column: 17, scope: !26)
!40 = !DILocation(line: 19, column: 3, scope: !26)
!41 = !DILocation(line: 19, column: 11, scope: !26)
!42 = !DILocation(line: 19, column: 15, scope: !26)
!43 = !DILocation(line: 20, column: 33, scope: !26)
!44 = !DILocation(line: 20, column: 41, scope: !26)
!45 = !DILocation(line: 20, column: 45, scope: !26)
!46 = !DILocation(line: 20, column: 19, scope: !26)
!47 = !DILocation(line: 20, column: 3, scope: !26)
!48 = !DILocation(line: 20, column: 11, scope: !26)
!49 = !DILocation(line: 20, column: 17, scope: !26)
!50 = !DILocation(line: 23, column: 21, scope: !26)
!51 = !DILocation(line: 23, column: 29, scope: !26)
!52 = !DILocation(line: 23, column: 1, scope: !26)
!53 = !DILocation(line: 24, column: 32, scope: !26)
!54 = !DILocation(line: 24, column: 40, scope: !26)
!55 = !DILocation(line: 24, column: 18, scope: !26)
!56 = !DILocation(line: 24, column: 26, scope: !26)
!57 = !DILocation(line: 24, column: 48, scope: !26)
!58 = !DILocation(line: 25, column: 18, scope: !26)
!59 = !DILocation(line: 25, column: 26, scope: !26)
!60 = !DILocation(line: 25, column: 33, scope: !26)
!61 = !DILocation(line: 26, column: 32, scope: !26)
!62 = !DILocation(line: 26, column: 40, scope: !26)
!63 = !DILocation(line: 26, column: 18, scope: !26)
!64 = !DILocation(line: 26, column: 26, scope: !26)
!65 = !DILocation(line: 26, column: 48, scope: !26)
!66 = !DILocation(line: 27, column: 18, scope: !26)
!67 = !DILocation(line: 27, column: 26, scope: !26)
!68 = !DILocation(line: 27, column: 33, scope: !26)
!69 = !DILocation(line: 28, column: 1, scope: !26)
!70 = distinct !DISubprogram(name: "klee_choose", scope: !4, file: !4, line: 12, type: !71, isLocal: false, isDefinition: true, scopeLine: 12, flags: DIFlagPrototyped, isOptimized: true, unit: !3, variables: !76)
!71 = !DISubroutineType(types: !72)
!72 = !{!73, !73}
!73 = !DIDerivedType(tag: DW_TAG_typedef, name: "uintptr_t", file: !74, line: 122, baseType: !75)
!74 = !DIFile(filename: "/usr/include/stdint.h", directory: "/home/kim-llvm/klee/klee_build_dir/runtime/Intrinsic")
!75 = !DIBasicType(name: "long unsigned int", size: 64, align: 64, encoding: DW_ATE_unsigned)
!76 = !{!77, !78}
!77 = !DILocalVariable(name: "n", arg: 1, scope: !70, file: !4, line: 12, type: !73)
!78 = !DILocalVariable(name: "x", scope: !70, file: !4, line: 13, type: !73)
!79 = !DILocation(line: 13, column: 3, scope: !70)
!80 = !DILocation(line: 14, column: 3, scope: !70)
!81 = !DILocation(line: 17, column: 6, scope: !82)
!82 = distinct !DILexicalBlock(scope: !70, file: !4, line: 17, column: 6)
!83 = !{!84, !84, i64 0}
!84 = !{!"long", !85, i64 0}
!85 = !{!"omnipotent char", !86, i64 0}
!86 = !{!"Simple C/C++ TBAA"}
!87 = !DILocation(line: 17, column: 8, scope: !82)
!88 = !DILocation(line: 17, column: 6, scope: !70)
!89 = !DILocation(line: 18, column: 5, scope: !82)
!90 = !DILocation(line: 19, column: 3, scope: !70)
!91 = distinct !DISubprogram(name: "klee_div_zero_check", scope: !6, file: !6, line: 12, type: !92, isLocal: false, isDefinition: true, scopeLine: 12, flags: DIFlagPrototyped, isOptimized: true, unit: !5, variables: !95)
!92 = !DISubroutineType(types: !93)
!93 = !{null, !94}
!94 = !DIBasicType(name: "long long int", size: 64, align: 64, encoding: DW_ATE_signed)
!95 = !{!96}
!96 = !DILocalVariable(name: "z", arg: 1, scope: !91, file: !6, line: 12, type: !94)
!97 = !DILocation(line: 13, column: 9, scope: !98)
!98 = distinct !DILexicalBlock(scope: !91, file: !6, line: 13, column: 7)
!99 = !DILocation(line: 13, column: 7, scope: !91)
!100 = !DILocation(line: 14, column: 5, scope: !98)
!101 = !DILocation(line: 15, column: 1, scope: !91)
!102 = distinct !DISubprogram(name: "klee_int", scope: !8, file: !8, line: 13, type: !103, isLocal: false, isDefinition: true, scopeLine: 13, flags: DIFlagPrototyped, isOptimized: true, unit: !7, variables: !107)
!103 = !DISubroutineType(types: !104)
!104 = !{!29, !105}
!105 = !DIDerivedType(tag: DW_TAG_pointer_type, baseType: !106, size: 64, align: 64)
!106 = !DIDerivedType(tag: DW_TAG_const_type, baseType: !32)
!107 = !{!108, !109}
!108 = !DILocalVariable(name: "name", arg: 1, scope: !102, file: !8, line: 13, type: !105)
!109 = !DILocalVariable(name: "x", scope: !102, file: !8, line: 14, type: !29)
!110 = !DILocation(line: 14, column: 3, scope: !102)
!111 = !DILocation(line: 15, column: 3, scope: !102)
!112 = !DILocation(line: 16, column: 10, scope: !102)
!113 = !{!114, !114, i64 0}
!114 = !{!"int", !85, i64 0}
!115 = !DILocation(line: 16, column: 3, scope: !102)
!116 = distinct !DISubprogram(name: "klee_overshift_check", scope: !10, file: !10, line: 20, type: !117, isLocal: false, isDefinition: true, scopeLine: 20, flags: DIFlagPrototyped, isOptimized: true, unit: !9, variables: !120)
!117 = !DISubroutineType(types: !118)
!118 = !{null, !119, !119}
!119 = !DIBasicType(name: "long long unsigned int", size: 64, align: 64, encoding: DW_ATE_unsigned)
!120 = !{!121, !122}
!121 = !DILocalVariable(name: "bitWidth", arg: 1, scope: !116, file: !10, line: 20, type: !119)
!122 = !DILocalVariable(name: "shift", arg: 2, scope: !116, file: !10, line: 20, type: !119)
!123 = !DILocation(line: 21, column: 13, scope: !124)
!124 = distinct !DILexicalBlock(scope: !116, file: !10, line: 21, column: 7)
!125 = !DILocation(line: 21, column: 7, scope: !116)
!126 = !DILocation(line: 27, column: 5, scope: !127)
!127 = distinct !DILexicalBlock(scope: !124, file: !10, line: 21, column: 26)
!128 = !DILocation(line: 29, column: 1, scope: !116)
!129 = distinct !DISubprogram(name: "klee_range", scope: !12, file: !12, line: 13, type: !130, isLocal: false, isDefinition: true, scopeLine: 13, flags: DIFlagPrototyped, isOptimized: true, unit: !11, variables: !132)
!130 = !DISubroutineType(types: !131)
!131 = !{!29, !29, !29, !105}
!132 = !{!133, !134, !135, !136}
!133 = !DILocalVariable(name: "start", arg: 1, scope: !129, file: !12, line: 13, type: !29)
!134 = !DILocalVariable(name: "end", arg: 2, scope: !129, file: !12, line: 13, type: !29)
!135 = !DILocalVariable(name: "name", arg: 3, scope: !129, file: !12, line: 13, type: !105)
!136 = !DILocalVariable(name: "x", scope: !129, file: !12, line: 14, type: !29)
!137 = !DILocation(line: 14, column: 3, scope: !129)
!138 = !DILocation(line: 16, column: 13, scope: !139)
!139 = distinct !DILexicalBlock(scope: !129, file: !12, line: 16, column: 7)
!140 = !DILocation(line: 16, column: 7, scope: !129)
!141 = !DILocation(line: 17, column: 5, scope: !139)
!142 = !DILocation(line: 19, column: 12, scope: !143)
!143 = distinct !DILexicalBlock(scope: !129, file: !12, line: 19, column: 7)
!144 = !DILocation(line: 19, column: 14, scope: !143)
!145 = !DILocation(line: 19, column: 7, scope: !129)
!146 = !DILocation(line: 22, column: 5, scope: !147)
!147 = distinct !DILexicalBlock(scope: !143, file: !12, line: 21, column: 10)
!148 = !DILocation(line: 25, column: 14, scope: !149)
!149 = distinct !DILexicalBlock(scope: !147, file: !12, line: 25, column: 9)
!150 = !DILocation(line: 26, column: 30, scope: !151)
!151 = distinct !DILexicalBlock(scope: !149, file: !12, line: 25, column: 19)
!152 = !DILocation(line: 25, column: 9, scope: !147)
!153 = !DILocation(line: 26, column: 32, scope: !151)
!154 = !DILocation(line: 26, column: 19, scope: !151)
!155 = !DILocation(line: 26, column: 7, scope: !151)
!156 = !DILocation(line: 27, column: 5, scope: !151)
!157 = !DILocation(line: 28, column: 25, scope: !158)
!158 = distinct !DILexicalBlock(scope: !149, file: !12, line: 27, column: 12)
!159 = !DILocation(line: 28, column: 19, scope: !158)
!160 = !DILocation(line: 28, column: 7, scope: !158)
!161 = !DILocation(line: 29, column: 19, scope: !158)
!162 = !DILocation(line: 29, column: 21, scope: !158)
!163 = !DILocation(line: 29, column: 7, scope: !158)
!164 = !DILocation(line: 32, column: 12, scope: !147)
!165 = !DILocation(line: 32, column: 5, scope: !147)
!166 = !DILocation(line: 34, column: 1, scope: !129)
!167 = distinct !DISubprogram(name: "memcpy", scope: !16, file: !16, line: 12, type: !168, isLocal: false, isDefinition: true, scopeLine: 12, flags: DIFlagPrototyped, isOptimized: true, unit: !15, variables: !175)
!168 = !DISubroutineType(types: !169)
!169 = !{!170, !170, !171, !173}
!170 = !DIDerivedType(tag: DW_TAG_pointer_type, baseType: null, size: 64, align: 64)
!171 = !DIDerivedType(tag: DW_TAG_pointer_type, baseType: !172, size: 64, align: 64)
!172 = !DIDerivedType(tag: DW_TAG_const_type, baseType: null)
!173 = !DIDerivedType(tag: DW_TAG_typedef, name: "size_t", file: !174, line: 62, baseType: !75)
!174 = !DIFile(filename: "/usr/lib/llvm-3.9/bin/../lib/clang/3.9.1/include/stddef.h", directory: "/home/kim-llvm/klee/klee_build_dir/runtime/Intrinsic")
!175 = !{!176, !177, !178, !179, !180}
!176 = !DILocalVariable(name: "destaddr", arg: 1, scope: !167, file: !16, line: 12, type: !170)
!177 = !DILocalVariable(name: "srcaddr", arg: 2, scope: !167, file: !16, line: 12, type: !171)
!178 = !DILocalVariable(name: "len", arg: 3, scope: !167, file: !16, line: 12, type: !173)
!179 = !DILocalVariable(name: "dest", scope: !167, file: !16, line: 13, type: !31)
!180 = !DILocalVariable(name: "src", scope: !167, file: !16, line: 14, type: !105)
!181 = !DILocation(line: 16, column: 16, scope: !182)
!182 = !DILexicalBlockFile(scope: !167, file: !16, discriminator: 1)
!183 = !DILocation(line: 16, column: 3, scope: !182)
!184 = !DILocation(line: 16, column: 13, scope: !182)
!185 = !DILocation(line: 17, column: 15, scope: !167)
!186 = !{!85, !85, i64 0}
!187 = !{!188}
!188 = distinct !{!188, !189}
!189 = distinct !{!189, !"LVerDomain"}
!190 = !DILocation(line: 17, column: 13, scope: !167)
!191 = !{!192}
!192 = distinct !{!192, !189}
!193 = distinct !{!193, !194, !195, !196}
!194 = !DILocation(line: 16, column: 3, scope: !167)
!195 = !{!"llvm.loop.vectorize.width", i32 1}
!196 = !{!"llvm.loop.interleave.count", i32 1}
!197 = distinct !{!197, !198}
!198 = !{!"llvm.loop.unroll.disable"}
!199 = !DILocation(line: 17, column: 19, scope: !167)
!200 = !DILocation(line: 17, column: 10, scope: !167)
!201 = distinct !{!201, !194, !195, !196}
!202 = !DILocation(line: 18, column: 3, scope: !167)
!203 = distinct !{!203, !198}
!204 = distinct !DISubprogram(name: "memmove", scope: !18, file: !18, line: 12, type: !168, isLocal: false, isDefinition: true, scopeLine: 12, flags: DIFlagPrototyped, isOptimized: true, unit: !17, variables: !205)
!205 = !{!206, !207, !208, !209, !210}
!206 = !DILocalVariable(name: "dst", arg: 1, scope: !204, file: !18, line: 12, type: !170)
!207 = !DILocalVariable(name: "src", arg: 2, scope: !204, file: !18, line: 12, type: !171)
!208 = !DILocalVariable(name: "count", arg: 3, scope: !204, file: !18, line: 12, type: !173)
!209 = !DILocalVariable(name: "a", scope: !204, file: !18, line: 13, type: !31)
!210 = !DILocalVariable(name: "b", scope: !204, file: !18, line: 14, type: !105)
!211 = !DILocation(line: 16, column: 11, scope: !212)
!212 = distinct !DILexicalBlock(scope: !204, file: !18, line: 16, column: 7)
!213 = !DILocation(line: 16, column: 7, scope: !204)
!214 = !DILocation(line: 19, column: 10, scope: !215)
!215 = distinct !DILexicalBlock(scope: !204, file: !18, line: 19, column: 7)
!216 = !DILocation(line: 19, column: 7, scope: !204)
!217 = !DILocation(line: 20, column: 5, scope: !218)
!218 = !DILexicalBlockFile(scope: !219, file: !18, discriminator: 1)
!219 = distinct !DILexicalBlock(scope: !215, file: !18, line: 19, column: 16)
!220 = !DILocation(line: 20, column: 17, scope: !218)
!221 = !DILocation(line: 20, column: 28, scope: !222)
!222 = !DILexicalBlockFile(scope: !219, file: !18, discriminator: 2)
!223 = !{!224}
!224 = distinct !{!224, !225}
!225 = distinct !{!225, !"LVerDomain"}
!226 = !DILocation(line: 20, column: 26, scope: !222)
!227 = !{!228}
!228 = distinct !{!228, !225}
!229 = distinct !{!229, !230, !195, !196}
!230 = !DILocation(line: 20, column: 5, scope: !219)
!231 = distinct !{!231, !198}
!232 = !DILocation(line: 20, column: 30, scope: !222)
!233 = !DILocation(line: 20, column: 23, scope: !222)
!234 = distinct !{!234, !230, !195, !196}
!235 = !DILocation(line: 22, column: 13, scope: !236)
!236 = distinct !DILexicalBlock(scope: !215, file: !18, line: 21, column: 10)
!237 = !DILocation(line: 24, column: 5, scope: !238)
!238 = !DILexicalBlockFile(scope: !236, file: !18, discriminator: 1)
!239 = !DILocation(line: 23, column: 6, scope: !236)
!240 = !DILocation(line: 22, column: 6, scope: !236)
!241 = !DILocation(line: 24, column: 17, scope: !238)
!242 = !DILocation(line: 24, column: 28, scope: !243)
!243 = !DILexicalBlockFile(scope: !236, file: !18, discriminator: 2)
!244 = !{!245}
!245 = distinct !{!245, !246}
!246 = distinct !{!246, !"LVerDomain"}
!247 = !DILocation(line: 24, column: 26, scope: !243)
!248 = !{!249}
!249 = distinct !{!249, !246}
!250 = distinct !{!250, !251, !195, !196}
!251 = !DILocation(line: 24, column: 5, scope: !236)
!252 = !DILocation(line: 24, column: 30, scope: !243)
!253 = !DILocation(line: 24, column: 23, scope: !243)
!254 = distinct !{!254, !251, !195, !196}
!255 = !DILocation(line: 28, column: 1, scope: !204)
!256 = distinct !{!256, !198}
!257 = distinct !{!257, !198}
!258 = distinct !DISubprogram(name: "mempcpy", scope: !20, file: !20, line: 11, type: !168, isLocal: false, isDefinition: true, scopeLine: 11, flags: DIFlagPrototyped, isOptimized: true, unit: !19, variables: !259)
!259 = !{!260, !261, !262, !263, !264}
!260 = !DILocalVariable(name: "destaddr", arg: 1, scope: !258, file: !20, line: 11, type: !170)
!261 = !DILocalVariable(name: "srcaddr", arg: 2, scope: !258, file: !20, line: 11, type: !171)
!262 = !DILocalVariable(name: "len", arg: 3, scope: !258, file: !20, line: 11, type: !173)
!263 = !DILocalVariable(name: "dest", scope: !258, file: !20, line: 12, type: !31)
!264 = !DILocalVariable(name: "src", scope: !258, file: !20, line: 13, type: !105)
!265 = !DILocation(line: 15, column: 16, scope: !266)
!266 = !DILexicalBlockFile(scope: !258, file: !20, discriminator: 1)
!267 = !DILocation(line: 15, column: 3, scope: !266)
!268 = !DILocation(line: 15, column: 13, scope: !266)
!269 = !DILocation(line: 16, column: 15, scope: !258)
!270 = !{!271}
!271 = distinct !{!271, !272}
!272 = distinct !{!272, !"LVerDomain"}
!273 = !DILocation(line: 16, column: 13, scope: !258)
!274 = !{!275}
!275 = distinct !{!275, !272}
!276 = distinct !{!276, !277, !195, !196}
!277 = !DILocation(line: 15, column: 3, scope: !258)
!278 = distinct !{!278, !198}
!279 = !DILocation(line: 16, column: 19, scope: !258)
!280 = !DILocation(line: 16, column: 10, scope: !258)
!281 = distinct !{!281, !277, !195, !196}
!282 = distinct !{!282, !198}
!283 = !DILocation(line: 17, column: 3, scope: !258)
!284 = distinct !DISubprogram(name: "memset", scope: !22, file: !22, line: 11, type: !285, isLocal: false, isDefinition: true, scopeLine: 11, flags: DIFlagPrototyped, isOptimized: true, unit: !21, variables: !287)
!285 = !DISubroutineType(types: !286)
!286 = !{!170, !170, !29, !173}
!287 = !{!288, !289, !290, !291}
!288 = !DILocalVariable(name: "dst", arg: 1, scope: !284, file: !22, line: 11, type: !170)
!289 = !DILocalVariable(name: "s", arg: 2, scope: !284, file: !22, line: 11, type: !29)
!290 = !DILocalVariable(name: "count", arg: 3, scope: !284, file: !22, line: 11, type: !173)
!291 = !DILocalVariable(name: "a", scope: !284, file: !22, line: 12, type: !292)
!292 = !DIDerivedType(tag: DW_TAG_pointer_type, baseType: !293, size: 64, align: 64)
!293 = !DIDerivedType(tag: DW_TAG_volatile_type, baseType: !32)
!294 = !DILocation(line: 13, column: 20, scope: !295)
!295 = !DILexicalBlockFile(scope: !284, file: !22, discriminator: 1)
!296 = !DILocation(line: 13, column: 5, scope: !295)
!297 = !DILocation(line: 14, column: 14, scope: !284)
!298 = !DILocation(line: 14, column: 9, scope: !284)
!299 = !DILocation(line: 14, column: 12, scope: !284)
!300 = distinct !{!300, !301}
!301 = !DILocation(line: 13, column: 5, scope: !284)
!302 = !DILocation(line: 15, column: 5, scope: !284)
!303 = distinct !{!303, !198}
