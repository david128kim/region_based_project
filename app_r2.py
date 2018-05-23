import os
#import commands
import subprocess
import string
#from app_r1 import temp_name
#reload(app_r1)
#print temp_name
#print app_r1.program_name
from tree import Tree
from app_r1 import execution_path_r1

(_ROOT, _DEPTH, _BREADTH) = range(3)

tree = Tree()

#file = open("select_region1.c")
file = open("region_text/branch.txt")
treeID, height, brackets_match, branch_boundrary, counter_if, execution_path_r2, counter_bp = 0, 0, 0, 0, 0, 0, 0
info, info_bottom, brackets_match_record, branch_point, branch_leaf, breakpoint, dfs = [], [], [], [], [], [], []
start, end, counter_r2, r2_flag, main_flag, temp_pop = 1, 0, 0, 0, 0, 0
p_num, path = [], []
for line in file:
	counter_r2 += 1
	if "region2" in line:
		r2_flag = counter_r2
	info.append(line)
main_flag = len(info)
### set "region2: " into info_bottom ######
for i in range(0, main_flag-r2_flag+1):
	info_bottom.append(info.pop())
info = []
for i in range(main_flag-r2_flag, -1, -1):
	info.append(info_bottom[i])


tree.add_node(info[treeID])
for i  in range(1, len(info)):
	if (("if" in info[i]) and ("else" not in info[i])):
		counter_if += 1
		brackets_match += 1
		brackets_match_record.append(brackets_match)
		branch_point.append(treeID)
		if ("else" not in  info[i-1]):
			temp = branch_point[brackets_match-1]
			tree.add_node(info[i], info[temp])
			p_num.append(temp)
		else: 
			tree.add_node(info[i], info[treeID])
			p_num.append(treeID)
	
	elif (("else" in info[i]) and ("if" in info[i])):
		brackets_match += 1
		brackets_match_record.append(brackets_match)                                        
		if (brackets_match_record[len(brackets_match_record)-1] < brackets_match_record[len(brackets_match_record)-2]):
			branch_point.pop()
		temp = branch_point[brackets_match-1]
		tree.add_node(info[i], info[temp])
		p_num.append(temp)
	elif (("else" in info[i]) and ("if" not in info[i])):
		brackets_match += 1
		brackets_match_record.append(brackets_match)                                        
		if (brackets_match_record[len(brackets_match_record)-1] < brackets_match_record[len(brackets_match_record)-2]):
                	branch_point.pop()
		temp = branch_point[brackets_match-1]
		tree.add_node(info[i], info[temp])
		p_num.append(temp)
	else:	
		if "end of branch" in info[i]:
			branch_boundrary = i
			break
		else: 
			tree.add_node(info[i], info[treeID])
			p_num.append(treeID)
		if("}" in info[i]):
		######## layer problem #########
			brackets_match -= 1
			if brackets_match == 0:
				#print i
				branch_leaf.append(i)
	treeID += 1
if branch_boundrary > 0:
	for i in range(0, 1): 
		counter = 0
		#print "i: ",  i
		for j in range(branch_boundrary, len(info)):
			temp = branch_leaf[i]
			if counter == 0:
				tree.add_node(info[j], info[temp])
			else:
				tree.add_node(info[j], info[j-1])
			counter += 1
tree.display(info[0])

#print("***** DEPTH-FIRST ITERATION *****"), '\n'
#print ("region2:\n")
for node in tree.traverse(info[0]):
	if "region" not in node:
		dfs.append(node)
for i in range(0, len(p_num)-1):
	if (p_num[i+1] < p_num[i]) and ("}" in dfs[i+1]):
		p_num.insert(i+1, 99)
print ("parents: ", p_num)
for i in range(0, len(p_num)-1):
	path.append(dfs[i])
	if ("}" in dfs[i]) and ("}" not in dfs[i+1]):
		partition = open("partition.c", "w")
		execution_path_r2 += 1
		for i in range(0, len(path)):
			#if ("if" not in dfs[i]) and ("elif" not in dfs[i]) and ("else" not in dfs[i]) and ("}" not in dfs[i]):
			partition.write(path[i])
		partition.close()
		os.system("mv partition.c exe_r2_path"+str(execution_path_r2)+".c")
		temp_pop = 0
		temp_path = len(path)
		for j in range(len(path)-1, -1, -1):
			if (p_num[temp_path] <= p_num[j]):
				path.pop()
				temp_pop += 1
				temp_del = j
			else:
				break
		for k in range(0, temp_pop):
			del p_num[temp_del]
		print (p_num)
partition = open("partition.c", "w")
execution_path_r2 += 1
for i in range(0, len(path)):
	partition.write(path[i])
partition.write("}\n")
partition.close()
os.system("mv partition.c exe_r2_path"+str(execution_path_r2)+".c")













