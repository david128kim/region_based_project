import os
import subprocess
import string
import app_r1
import app_r2

ValidInputs_1, ValidInputs_2, source_line, source_r, ir_line, local_var, program, source_path, ins, kquery, exe_path, exe_r1_path, exe_r2_path = [], [], [], [], [], [], [], [], [], [], [], [], []
region_combination, counter_r1, entry_r1, return_r1, counter_r2, entry_r2, return_r2, num_ins, region_flag, entry_region, return_region, counter_region, k_point, appendable = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1
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
    os.system('mv region'+str(i)+'.c exe_source/')
########################################################################

region = open("region_text/p-c.txt", 'r')
for line in region:
    if "region" not in line:
        source_r.append(line)

dy_path_r1 = open("Itrigger_1.c", "w")
dy_path_r2 = open("Itrigger_2.c", "w")
for j in range(0, len(source_line)):
	dy_path_r1.write(source_line[j])
	dy_path_r2.write(source_line[j])
dy_path_r1.write('int main(int argc, char **argv) {\n')
dy_path_r2.write('int main(int argc, char **argv) {\n')
for k in range(0, len(local_var)):
	dy_path_r1.write(local_var[k])
	dy_path_r2.write(local_var[k])
dy_path_r1.write('klee_make_symbolic(&'+shared_data+', sizeof('+shared_data+'), "'+shared_data+'");\n')
dy_path_r2.write('klee_make_symbolic(&'+shared_data+', sizeof('+shared_data+'), "'+shared_data+'");\n')
#os.system('cp Itrigger_1.c Itrigger_2.c')
for i in range(0, int(num_region)):						##### two region: need to be dynamic (ex: find r?_path.c number) #####
	file = open("r"+str(i+1)+"_path.c")
	dy_path_r1 = open("Itrigger_1.c", "a")
	for line in file:
		source_path.append(line)
	for l in range(0, len(source_path)):
		if "pthread_cond_wait" in source_path[l]:
			source_path[l] = source_path[l].replace('pthread_cond_wait(&', 'printf ("')
			source_path[l] = source_path[l].replace(');' , 'wait");')
		dy_path_r1.write(source_path[l])
	source_path = []
for i in range(int(num_region), 0, -1):
	file = open("r"+str(i)+"_path.c")
	dy_path_r2 = open("Itrigger_2.c", "a")
	for line in file:
		source_path.append(line)
	for l in range(0, len(source_path)):
		if "pthread_cond_wait" in source_path[l]:
			source_path[l] = source_path[l].replace('pthread_cond_wait(&', 'printf ("')
			source_path[l] = source_path[l].replace(');' , 'wait");')
		dy_path_r2.write(source_path[l])
	source_path = []
dy_path_r1.write('return 0; }\n')
dy_path_r1.close()
dy_path_r2.write('return 0; }\n')
dy_path_r2.close()

for i in range(0, int(num_region)):
	os.system('clang -Os -S -emit-llvm Itrigger_'+str(i+1)+'.c -o Itrigger_'+str(i+1)+'.ll')
	os.system('llvm-as Itrigger_'+str(i+1)+'.ll -o Itrigger_'+str(i+1)+'.bc')
	os.system('klee -search=dfs -write-paths Itrigger_'+str(i+1)+'.bc')
	num = subprocess.getoutput('find klee-last/ -type f |wc -l')
	end = (int(num) - 7 + 2) / 2
	print (end)
	for j in range(1, int(end)):
		temp = subprocess.getoutput('ktest-tool --write-ints klee-last/test00000'+str(j)+'.ktest')
		tmp = temp.split()
		#if "found" not in tmp:
		if i == 0:
			ValidInputs_1.append(tmp[len(tmp)-1])
		else:
			ValidInputs_2.append(tmp[len(tmp)-1])
	#ValidInputs.insert(0, "0")
	print ("valid inputs: ", ValidInputs_1)
	print ("valid inputs: ", ValidInputs_2)

#for i in range(0, int(num_region)):
	file = open('Itrigger_'+str(i+1)+'.c')
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
			if "num" in ins[j] and "if" in ins[j]:
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
		os.system('mv path.c program/path_'+str(i+1)+'_'+str(k)+'.c')
		os.system('clang -Os -S -emit-llvm program/path_'+str(i+1)+'_'+str(k)+'.c -o program/path_'+str(i+1)+'_'+str(k)+'.ll')
		k_point = 0
		kquery = []
		exe_path = []
	ins = []

file = open('program/path_2_6.c')
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

for i in range(1, int(num_region)+1):
    ir_line =[]
    counter_region = 0
    region = open('exe_IR/exe_r'+str(i)+'.ll','r')
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

for i in range(1, int(num_region)+1):
	if i == 1:
		for j in range(0, len(ValidInputs_1)):
			file = open("program/path_"+str(i)+"_"+str(j+1)+".ll", "r")
			for line in file:
				program.append(line)
			file.close()
			path = open('exe_path'+str(i)+'_'+str(j+1)+'.ll', 'w')
			for k in range(0, len(program)):
				if shared_data in program[k] and "global" in program[k] and "common" in program[k]:
					program[k] = program[k].replace("common local_unnamed_addr global i32 0", "global i32 "+ValidInputs_1[j]+"")
				elif shared_data in program[k] and "global" in program[k] and "common" not in program[k]:
					program[k] = program[k].replace(""+ValidInputs_1[j-1]+"", ""+ValidInputs_1[j]+"")
				path.write(program[k])
			path.close()
			program = []
	elif i == 2:
		for j in range(0, len(ValidInputs_2)):
			file = open("program/path_"+str(i)+"_"+str(j+1)+".ll", "r")
			for line in file:
				program.append(line)
			file.close()
			path = open('exe_path'+str(i)+'_'+str(j+1)+'.ll', 'w')
			for k in range(0, len(program)):
				if shared_data in program[k] and "global" in program[k] and "common" in program[k]:
					program[k] = program[k].replace("common local_unnamed_addr global i32 0", "global i32 "+ValidInputs_2[j]+"")
				elif shared_data in program[k] and "global" in program[k] and "common" not in program[k]:
					program[k] = program[k].replace(""+ValidInputs_2[j-1]+"", ""+ValidInputs_2[j]+"")
				path.write(program[k])
			path.close()
			program = []
os.system('mv exe_path* program/')
#os.system('mv path* program/')

