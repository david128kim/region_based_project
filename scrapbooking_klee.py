import os
import subprocess
import string
import app_r1
import app_r2

ValidInputs, global_line, function_line, source_r, ir_line, local_var, program, source_path, ins, kquery, exe_path, exe_r1_path, exe_r2_path = [], [], [], [], [], [], [], [], [], [], [], [], []
region_combination, counter_r1, entry_r1, return_r1, counter_r2, entry_r2, return_r2, num_ins, region_flag, entry_region, return_region, counter_region, k_point, appendable = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1
program_name = input("Please key in your program name: \n")
shared_data = input("Please key in your shared data name: \n")
num_region = input("How many regions do you circle: \n")
file = open(program_name)
klee = open('klee_program.c', 'w')
whole = open('whole_program.c', 'w')

for line in file:
        if "(" in line:
                break
        global_line.append(line)
for line in file:
        if "(" not in line and "{" not in line and "}" not in line and "+" not in line and "-" not in line and "*" not in line and "/" not in line and "return" not in line and shared_data not in line:
        #if "(" not in line and "{" not in line and "}" not in line and "=" not in line and "return" not in line:
                local_var.append(line)
        elif "struct" in line:
                local_var.append(line)
        elif "main" in line:
                break
        
file.close()
############ acquire instruction-level interleaving #############
for i in range(1, int(num_region)+1):
        file = open("r"+str(i)+"_path.c")
        region = open('region'+str(i)+'.c', 'w')
        for k in range(0, len(global_line)):
                region.write(global_line[k])
        region.write('int main(int argc, char **argv) {\n')
        for j in range(0, len(local_var)):
                region.write(local_var[j])
        for line in file:
                region.write(line)
        region.write('return 0;\n}')
        region.close()
        os.system('clang -Os -S -emit-llvm region'+str(i)+'.c -o region'+str(i)+'.ll')
        os.system('mv region'+str(i)+'.c exe_source/')
        os.system('mv region'+str(i)+'.ll exe_IR/')

############ calculate valid inputs #############
for i in range(1, int(num_region)+1):
        file = open("r"+str(i)+"_path.c")
        region_klee = open('region'+str(i)+'_klee.c', 'w')
        for k in range(0, len(global_line)):
                region_klee.write(global_line[k])
        region_klee.write('int main(int argc, char **argv) {\n')
        for j in range(0, len(local_var)):
                region_klee.write(local_var[j])
        region_klee.write('klee_make_symbolic(&'+shared_data+', sizeof('+shared_data+'), "'+shared_data+'");\n')
        for line in file:
                source_path.append(line)
        for l in range(0, len(source_path)):
                if "pthread_cond_wait" in source_path[l]:
                        source_path[l] = source_path[l].replace('pthread_cond_wait(&', 'printf ("')
                        source_path[l] = source_path[l].replace(');' , 'wait");')
                region_klee.write(source_path[l])
        source_path = []
        region_klee.write('return 0;\n}')
        region_klee.close()
        os.system('clang -emit-llvm -g -c region'+str(i)+'_klee.c -o region'+str(i)+'_klee.bc')
        os.system('klee -search=dfs region'+str(i)+'_klee.bc')
        os.system('mv region'+str(i)+'_klee.c exe_source/')
        num = subprocess.getoutput('find klee-last/ -type f |wc -l')
        end = (int(num) - 7 + 2)
        print (end)
        for j in range(1, int(end)):
                temp = subprocess.getoutput('ktest-tool --write-ints klee-last/test00000'+str(j)+'.ktest')
                tmp = temp.split()
                if "found" not in tmp and tmp[len(tmp)-1] not in ValidInputs:
                        ValidInputs.append(tmp[len(tmp)-1])
print ("valid inputs: ", ValidInputs)
'''
########################################################################
dy_path = open("Itrigger.c", "w")
for j in range(0, len(global_line)):
	dy_path.write(global_line[j])
dy_path.write('int main(int argc, char **argv) {\n')
for k in range(0, len(local_var)):
	dy_path.write(local_var[k])
dy_path.write('klee_make_symbolic(&'+shared_data+', sizeof('+shared_data+'), "'+shared_data+'");\n')
#os.system('cp Itrigger_1.c Itrigger_2.c')
for i in range(0, int(num_region)):						##### two region: need to be dynamic (ex: find r?_path.c number) #####
	file = open("r"+str(i+1)+"_path.c")
	dy_path = open("Itrigger.c", "a")
	for line in file:
		source_path.append(line)
	for l in range(0, len(source_path)):
		if "pthread_cond_wait" in source_path[l]:
			source_path[l] = source_path[l].replace('pthread_cond_wait(&', 'printf ("')
			source_path[l] = source_path[l].replace(');' , 'wait");')
		dy_path.write(source_path[l])
	source_path = []
dy_path.write('return 0; }\n')
dy_path.close()

os.system('clang -Os -S -emit-llvm Itrigger.c -o Itrigger.ll')
os.system('llvm-as Itrigger.ll -o Itrigger.bc')
os.system('klee -search=dfs -write-paths Itrigger.bc')
num = subprocess.getoutput('find klee-last/ -type f |wc -l')
end = (int(num) - 7 + 2) / 2
print (end)
for j in range(1, int(end)):
	temp = subprocess.getoutput('ktest-tool --write-ints klee-last/test00000'+str(j)+'.ktest')
	tmp = temp.split()
	if "found" not in tmp:
		ValidInputs.append(tmp[len(tmp)-1])
	print ("valid inputs: ", ValidInputs)

#for i in range(0, int(num_region)):
file = open('Itrigger.c')
for line in file:
	ins.append(line)
file.close()
p_num = subprocess.getoutput('find klee-last/ -name *.path -type f |wc -l')
for k in range(1, int(p_num)+1):
	file = open('klee-last/test00000'+str(k)+'.path')
	for line in file:
		kquery.append(line)
	file.close()
	for j in range(0, len(ins)):
		if shared_data in ins[j] and "if" in ins[j]:	# num => shared_data
			if "0" in kquery[k_point]:
				appendable = 0
			k_point += 1
		elif "}" in ins[j]:
			appendable = 1
		if appendable == 1 and "}" not in ins[j] and "if" not in ins[j]:
			if "klee" not in ins[j]:                      	
				exe_path.append(ins[j])
			#print (ins[j])
		else:
			continue
	path = open("path.c", "w")
	for j in range(0, len(exe_path)):
		if "wait" in exe_path[j]:
			exe_path[j] = exe_path[j].replace('printf ("', 'pthread_cond_wait(&')
			exe_path[j] = exe_path[j].replace('wait");', ');')
		path.write(exe_path[j])
	path.write('return 0;\n}')
	path.close()
	os.system('mv path.c program/path_'+str(k)+'.c')
	os.system('clang -Os -S -emit-llvm program/path_'+str(k)+'.c -o program/path_'+str(k)+'.ll')
	k_point = 0
	kquery = []
	exe_path = []
ins = []

file = open('program/path_1.c')
for line in file:
        if "R1" in line:
                exe_r1_path.append(line)
                #print ("exe_r1: \n", line)
        elif "R2" in line:
                exe_r2_path.append(line)
        else:
                if "klee" not in line:
                        exe_r1_path.append(line)
                        exe_r2_path.append(line)
file.close()
#print ("exe_r1: \n", exe_r1_path)
for i in range(1 , int(num_region)+1):
        executions = open("exe_r"+str(i)+".c", "w")
        if i == 1:
                for j in range(0 , len(exe_r1_path)):
                        executions.write(exe_r1_path[j])
        else:
                for j in range(0 , len(exe_r2_path)):
                        executions.write(exe_r2_path[j])
        executions.close()
        os.system('clang -Os -S -emit-llvm exe_r'+str(i)+'.c -o exe_r'+str(i)+'.ll')
        os.system('mv exe_r'+str(i)+'.ll exe_IR/')
        os.system('mv exe_r'+str(i)+'.c exe_source/')	
'''
##################	produce concurrent_program.ll	###################
for i in range(1, int(num_region)+1):
    ir_line =[]
    counter_region = 0
    region = open('exe_IR/region'+str(i)+'.ll','r')
    for line in region:
        counter_region += 1
        #print (''.join(line+';R'+str(i)))
        ir_line.append(line)
        if "define" in line:
            entry_region = counter_region
        elif "ret" in line:
            return_region = counter_region
    sequential = open('concurrent_program.ll','a')
    sequential.write('region'+str(i)+': \n')
    for k in range(entry_region, return_region-1):
        sequential.write(ir_line[k].rstrip('\n')+' ;R'+str(i)+'\n')
    region.close()
sequential.close()
os.system('mv concurrent_program.ll exe_concurrent/')

#################	verify each combination possibility ( Input )	##################
os.system('cp exe_IR/region1.ll program/')
for j in range(0, len(ValidInputs)):
	#file = open("program/path_"+str(j+1)+".ll", "r")
	file = open("program/region1.ll", "r")
	for line in file:
		program.append(line)
	file.close()
	path = open('exe_path'+str(j+1)+'.ll', 'w')
	for k in range(0, len(program)):
		if shared_data in program[k] and "global" in program[k] and "common" in program[k]:
			program[k] = program[k].replace("common local_unnamed_addr global i32 0", "global i32 "+ValidInputs[j]+"")
		elif shared_data in program[k] and "global" in program[k] and "common" not in program[k]:
			program[k] = program[k].replace(""+ValidInputs[j-1]+"", ""+ValidInputs[j]+"")
		path.write(program[k])
	path.close()
	program = []
os.system('mv exe_path* program/')
