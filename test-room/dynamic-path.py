import os
import subprocess

ValidInputs, kquery, ins, exe_path = [], [], [], []
k_point, appendable, brackets = 0, 1, 0

os.system('clang -Os -S -emit-llvm region1.c -o region1.ll')
os.system('llvm-as region1.ll -o region1.bc')
os.system('klee -search=dfs -write-kqueries -write-paths region1.bc')
num = subprocess.getoutput('find klee-last/ -type f |wc -l')
end = (int(num) - 7 + 2) / 2
for i in range(1, int(end)):
	temp = subprocess.getoutput('ktest-tool --write-ints klee-last/test00000'+str(i)+'.ktest')
	tmp = temp.split()
	if "found" not in tmp[len(tmp)-1]:
		ValidInputs.append(tmp[len(tmp)-1])
print ("valid inputs: ", ValidInputs)

file = open('region1.c')
for line in file:
	ins.append(line)
file.close()
p_num = subprocess.getoutput('find klee-last/ -name *.path -type f |wc -l')
print (p_num)
for i in range(1, int(p_num)+1):
	file = open('klee-last/test00000'+str(i)+'.path')
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
			exe_path.append(ins[j])
			#print (ins[j])
		else:	
			continue
	path = open("path_r1.c", "w")
	for j in range(0, len(exe_path)):
		path.write(exe_path[j])
	path.close()
	os.system('mv path_r1.c path_r1_'+str(i)+'.c')
	k_point = 0	
	kquery = []
	exe_path = []
