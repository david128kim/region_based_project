import os
#import commands
import subprocess
import string

from app_r1 import execution_path_r1
from app_r2 import execution_path_r2

source_line, source_r1, source_r2, ir_r1, ir_r2, ir_line, = [], [], [], [], [], [] 
counter_r1, entry_r1, return_r1, counter_r2, entry_r2, return_r2, region_combination, brackets = 0, 0, 0, 0, 0, 0, 0, 0
program_name = input("Please key in your program name: \n")
shared_data = input("Please key in your shared data name: \n")
file = open(program_name)
whole = open('whole_program.c', 'w')

for line in file:
        if "{" in line:
                brackets += 1
        elif "}" in line:
                brackets -= 1
        elif "(" not in line and "{" not in line and "}" not in line:
#                break
                if brackets <= 1 and "return" not in line and "+" not in line:
                        source_line.append(line)
                        print (line)
                else:
                        continue
        
file.close()

for i in range(1, execution_path_r1+1):
	source_r1 =[]
	region1 = open('exe_r1_path'+str(i)+'.c','r')
	for line in region1:
		source_r1.append(line)
	region1.close()
	sequential = open('exe_r1_path'+str(i)+'_ok.c','a')
	for k in range(0, len(source_line)):
		sequential.write(source_line[k])
	sequential.write("int main() {")
	for k in range(0, len(source_r1)):
		sequential.write(source_r1[k])
	sequential.write("return 0; }")
	sequential.close()
	os.system('clang -Os -S -emit-llvm exe_r1_path'+str(i)+'_ok.c -o exe_r1_path'+str(i)+'.ll')
	os.system('mv exe_r1_path'+str(i)+'_ok.c exe_source/')
	os.system('mv exe_r1_path'+str(i)+'.ll exe_IR/')
	os.system('rm exe_r1_path'+str(i)+'.c')

for i in range(1, execution_path_r2+1):
        source_r2 =[]
        region2 = open('exe_r2_path'+str(i)+'.c','r')
        for line in region2:
                source_r2.append(line)
        region2.close()
        sequential = open('exe_r2_path'+str(i)+'_ok.c','a')
        for k in range(0, len(source_line)):
                sequential.write(source_line[k])
        sequential.write("int main() {")
        for k in range(0, len(source_r2)):
                sequential.write(source_r2[k])
        sequential.write("return 0; }")
        sequential.close()
        os.system('clang -Os -S -emit-llvm exe_r2_path'+str(i)+'_ok.c -o exe_r2_path'+str(i)+'.ll')
        os.system('mv exe_r2_path'+str(i)+'_ok.c exe_source/')
        os.system('mv exe_r2_path'+str(i)+'.ll exe_IR/')
        os.system('rm exe_r2_path'+str(i)+'.c')

whole.write('#include "../klee_src/include/klee/klee.h"\n')
for k in range(0, len(source_line)):
	whole.write(source_line[k])
whole.write('int main(int argc, char **argv) {\n')
whole.write('klee_make_symbolic(&'+shared_data+', sizeof('+shared_data+'), "'+shared_data+'");\n')
for k in range(0, len(source_r1)):
        whole.write(source_r1[k])
for k in range(0, len(source_r2)):
        whole.write(source_r2[k])
whole.write('return '+shared_data+'; }\n')
whole.close()
os.system('clang -Os -S -emit-llvm whole_program.c -o whole_program.ll')

for i in range(1, execution_path_r1+1):
	ir_r1 =[]
	counter_r1 = 0
	region1 = open('exe_IR/exe_r1_path'+str(i)+'.ll','r')
	for line in region1:
		counter_r1 += 1 
		ir_r1.append(line)
		if "define" in line:
			entry_r1 = counter_r1
		elif "ret" in line:
			return_r1 = counter_r1
	region1.close()
	for j in range(1, execution_path_r2+1):
		ir_r2 = []
		counter_r2 = 0
		region2 = open('exe_IR/exe_r2_path'+str(j)+'.ll','r')
		for line in region2:
			counter_r2 += 1
			ir_r2.append(line)
			if "define" in line:
				entry_r2 = counter_r2
			elif "ret" in line:
                        	return_r2 = counter_r2
		region2.close()
		region_combination += 1
		sequential = open('concurrent_program'+str(region_combination)+'.ll','a')
		#for k in range(0, len(ir_line)):
			#sequential.write(ir_line[k])
		sequential.write("region1: \n")
		for k in range(entry_r1, return_r1-1):
			sequential.write(ir_r1[k])
		sequential.write("region2: \n")
		for k in range(entry_r2, return_r2-1):
			sequential.write(ir_r2[k])
		sequential.close()
		os.system('mv concurrent_program'+str(region_combination)+'.ll exe_concurrent/')	

