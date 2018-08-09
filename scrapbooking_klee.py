import os
import subprocess
import string

#from app_r1 import execution_path_r1
#from app_r2 import execution_path_r2
import app_r1
import app_r2

ValidInputs, source_line, source_r, ir_line, local_var, program = [], [], [], [], [], []
region_combination, counter_r1, entry_r1, return_r1, counter_r2, entry_r2, return_r2, num_ins, region_flag, entry_region, return_region, counter_region = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
program_name = input("Please key in your program name: \n")
shared_data = input("Please key in your shared data name: \n")
num_region = input("How many regions do you circle: \n")
file = open(program_name)
klee = open('klee_program.c', 'w')
whole = open('whole_program.c', 'w')
#path = open('path.c', 'w')
for line in file:
        if "(" in line:
                break
        source_line.append(line)
for line in file:
        if "(" not in line and "{" not in line and "}" not in line and "+" not in line and "-" not in line and "*" not in line and "/" not in line and "return" not in line and shared_data not in line:
                local_var.append(line)
file.close()

#file = open("region_text/p-c.txt")
for i in range(1, int(num_region)+1):
    file = open("r"+str(i)+"_path.c")
    region = open('region'+str(i)+'.c', 'w')
    for k in range(0, len(source_line)):
            region.write(source_line[k])
    region.write('int main(int argc, char **argv) {\n')
    for j in range(0, len(local_var)):
            region.write(local_var[j])
    for line in file:
            region.write(line)
    region.write('return 0;\n}')
    region.close()
########################################################################
#region = open('region'+str(num_region)+'.c', 'w')
#for k in range(0, len(source_line)):
#    region.write(source_line[k])
#region.write('int main(int argc, char **argv) {\n')
#for line in file:
#    if "region"+str(int(num_region)-1)+"" not in line:
#        region.write(line)
#region.write('return 0;\n}')
#region.close()
#file.close()

for i in range(1, int(num_region)+1):
    os.system('clang -Os -S -emit-llvm region'+str(i)+'.c -o region'+str(i)+'.ll')
    os.system('mv region'+str(i)+'.ll exe_IR/')
#######################################################################
for i in range(1, int(num_region)+1):
    ir_line =[]
    counter_region = 0
    region = open('exe_IR/region'+str(i)+'.ll','r')
    for line in region:
        counter_region += 1 
        ir_line.append(line)
        if "define" in line:
            entry_region = counter_region
        elif "ret" in line:
            return_region = counter_region
    sequential = open('concurrent_program.ll','a')
    sequential.write('region'+str(i)+': \n')
    for k in range(entry_region, return_region-1):
        sequential.write(ir_line[k])
    region.close()
sequential.close()
os.system('mv concurrent_program.ll exe_concurrent/')

region = open("region_text/p-c.txt", 'r')
for line in region:
    if "region" not in line:
        source_r.append(line)

klee.write('#include "klee/klee.h"\n')
for k in range(0, len(source_line)):
    klee.write(source_line[k])
    whole.write(source_line[k])
klee.write('int main(int argc, char **argv) {\n')
whole.write('int main(int argc, char **argv) {\n')
for j in range(0, len(local_var)):
    klee.write(local_var[j])
    whole.write(local_var[j])
klee.write('klee_make_symbolic(&'+shared_data+', sizeof('+shared_data+'), "'+shared_data+'");\n')
for k in range(0, len(source_r)):
    if "pthread_cond_wait" in source_r[k]:
        source_r[k] = source_r[k].replace('pthread_cond_wait(&', 'printf ("')
        source_r[k] = source_r[k].replace(');' , '");')	
    klee.write(source_r[k])
    whole.write(source_r[k])
klee.write('return 0; }\n')
whole.write('printf("%d", '+shared_data+'); \n')
whole.write('return 0; }\n')
klee.close()
whole.close()
os.system('clang -Os -S -emit-llvm klee_program.c -o klee_program.ll')
os.system('clang -Os -S -emit-llvm whole_program.c -o whole_program.ll')
#os.system('mv whole_program.ll program/')
os.system('llvm-as klee_program.ll -o klee_program.bc')
#os.system('klee --libc=uclibc --posix-runtime klee_program.bc')
os.system('klee -search=dfs -write-kqueries -write-paths klee_program.bc')
num = subprocess.getoutput('find klee-last/ -type f |wc -l')
end = (int(num) - 7 + 2) / 2
for i in range(1, int(end)):
        temp = subprocess.getoutput('ktest-tool --write-ints klee-last/test00000'+str(i)+'.ktest')
        tmp = temp.split()
        ValidInputs.append(tmp[len(tmp)-1])
#ValidInputs.insert(0, "0")
print ("valid inputs: ", ValidInputs)

file = open("whole_program.ll", "r")
for line in file:
        program.append(line)
file.close()

for i in range(0, len(ValidInputs)):
        path = open('path.ll', 'w')
        for j in range(0, len(program)):
                if shared_data in program[j] and "global" in program[j] and "common" in program[j]:
                        program[j] = program[j].replace("common global i32 0", "global i32 "+ValidInputs[i]+"")
                elif shared_data in program[j] and "global" in program[j] and "common" not in program[j]:
                        program[j] = program[j].replace(""+ValidInputs[i-1]+"", ""+ValidInputs[i]+"")
                path.write(program[j])
        os.system('mv path.ll path'+str(i+1)+'.ll')
        #os.system('clang -S -emit-llvm path'+str(i+1)+'.c -o path'+str(i+1)+'.ll')
        path.close()
os.system('mv path* program/')
