import os
#import commands
import subprocess
import string

from tree import Tree
from tree import depth_list

(_ROOT, _DEPTH, _BREADTH) = range(3)

tree = Tree()

file = open("region_text/branch.txt")
treeID, height, brackets_match, branch_boundrary, counter_if, execution_path_r1, counter_bp = 0, 0, 0, 0, 0, 0, 0
info, node_height, brackets_match_record, branch_point, branch_point_record, branch_leaf, breakpoint, dfs, dfs_temp = [], [], [], [], [], [], [], [], []
start, end, counter_r2, r2_flag, main_flag, temp_node_length, temp_dfs, temp_pop = 1, 0, 0, 0, 0, 0, 0, 0
constrain, constrain_state, path_cond_state, path_cond, c_num, p_num, path, cond_list, cond_dfs, cond_final_list = "", [], [], [], [], [], [], [], [], []

def extract_branch(a,b):
	a = b.replace("if", "")
	a = a.replace("(", "", 1)
	a = a.replace(")", "", 1)
	a = a.replace("{", "")
	#print ("a :", a)
	#print ("b :", b)
	return a
	return b

for line in file:
	counter_r2 += 1
	if "region2" in line:
		r2_flag = counter_r2
		break
	info.append(line)

tree.add_node(info[treeID])

for i  in range(1, len(info)):
	if (("if" in info[i]) and ("else" not in info[i])):
		height += 1
		counter_if += 1		
		brackets_match += 1
		brackets_match_record.append(brackets_match)
		branch_point.append(treeID)
		branch_point_record.append(treeID)
		node_height.append(height)
		if ("else" not in  info[i-1]):
			temp = branch_point[brackets_match-1]
			tree.add_node(info[i], info[temp])
			c_num.append(i)
			p_num.append(temp)
			cond_list.append(temp)
			cond_final_list.append(temp)
			#print ("if: child, parents: ", (i, temp))
		else:
			tree.add_node(info[i], info[treeID])
			#print ("if: child, parents: ", (i, treeID))
			c_num.append(i)
			p_num.append(treeID)
			cond_list.append(treeID)
			cond_final_list.append(treeID)
		
		constrain = info[i].replace("if", "")
		constrain = constrain.replace("(", "", 1)
		constrain = constrain.replace(")", "", 1)
		constrain = constrain.replace("{", "")
		constrain_state.append(constrain)
		path_cond_state.append(constrain)
		
		#extract_branch(constrain, info[i])
		#print ("constrain: ", constrain)

		"""
		if (len(brackets_match_record) > 1) and (brackets_match_record[len(brackets_match_record)-2] < brackets_match_record[len(brackets_match_record)-1]):
			constrain_state.append(constrain)
			constrain = constrain_state[len(constrain_state)-2] + " && " + constrain
			#constrain_state.pop()
			constrain_state.append(constrain)
			#path_cond.append(constrain)
		else:
			constrain_state.append(constrain)
		
		print ("extract and combine: \n", constrain)
		print ("state:(if) \n", constrain_state)
		#print ("path condition: \n", path_cond)
		"""
	elif ("else if" in info[i]):
		brackets_match += 1
		brackets_match_record.append(brackets_match)
		if (brackets_match_record[len(brackets_match_record)-1] < brackets_match_record[len(brackets_match_record)-2]):
			branch_point.pop()
		height = brackets_match
		temp = branch_point[brackets_match-1]
		tree.add_node(info[i], info[temp])
		#print ("elif: child, parents: ", (i, temp))

		c_num.append(i)
		p_num.append(temp)
		cond_list.append(temp)
		cond_final_list.append(temp)

		constrain = info[i].replace("else if", "")
		constrain = constrain.replace("(", "", 1)
		constrain = constrain.replace(")", "", 1)
		constrain = constrain.replace("{", "")
		constrain_state.append("null")
		path_cond_state.append(constrain)
		#print ("constrain: ", constrain)

		node_height.append(height)
		temp_node_length = len(node_height)


	elif (("else" in info[i]) and ("if" not in info[i])):
		brackets_match += 1
		brackets_match_record.append(brackets_match)
		if (brackets_match_record[len(brackets_match_record)-1] < brackets_match_record[len(brackets_match_record)-2]):
                        branch_point.pop()
		height = brackets_match
		temp = branch_point[brackets_match-1]
		tree.add_node(info[i], info[temp])
		#print ("else: child, parents: ", (i, temp))

		c_num.append(i)
		p_num.append(temp)
		cond_list.append(temp)
		cond_final_list.append(temp)

		constrain_state.append("null")
		constrain = " !(" + constrain_state[temp] + ") "
		path_cond_state.append(constrain)

		node_height.append(height)
		temp_node_length = len(node_height)

		"""
		constrain = "! (" + constrain_state[len(constrain_state)-1] + ") && " + constrain_state[len(constrain_state)-2]			
		constrain_state.append(constrain)
		"""
	else:	
		if "end of branch" in info[i]:
			branch_boundrary = i
			#print "branch_boundrary: ", branch_boundrary
			break
		else: 
			height += 1
			#print height
			tree.add_node(info[i], info[treeID])
			#print ("others: child, parents: ", (i, treeID))
			c_num.append(i)
			p_num.append(treeID)
			#cond_list.append(treeID)
			constrain_state.append("null")

			node_height.append(height)

		if("}" in info[i]):
		######## layer problem #########
			brackets_match -= 1			
			if brackets_match == 0:
				branch_leaf.append(i)
	treeID += 1
print ("original cond_list: ", cond_list)
print ("constrain_state: ", constrain_state)
print ("path_cond_state: ", path_cond_state)
temp = len(cond_list)
for i in range(0, temp-1):
	cond_dfs.append(path_cond_state[i])
	if (cond_final_list[i+1] <= cond_final_list[i]):
		#print ("temp_cond_list: ", cond_final_list)
		#print ("(i, temp_cond_list[i]): ", (i, cond_final_list[i]))	
		constrain = "1"
		for j in range(0, len(cond_dfs)):
			constrain = constrain + " && " + path_cond_state[j]
		path_cond.append(constrain)
		temp_state_pop = 0
		temp_cond_dfs_length = len(cond_dfs)
		for k in range(len(cond_dfs)-1, -1, -1):
			if cond_list[temp_cond_dfs_length] <= cond_list[k]:	
				cond_dfs.pop()
				temp_state_pop += 1
				temp_del = k
			else:
				break
		print (temp_state_pop)
		for l in range(0, temp_state_pop):
			#del path_cond_state[temp_del]
			del cond_list[temp_del]
		print ("cond_list state: ", cond_list)
#print ("path_cond: ", path_cond)
constrain = "1"
for i in range(0, len(cond_dfs)):
	constrain = constrain + " && " + path_cond_state[i]
path_cond.append(constrain)
print ("path_cond: ", path_cond)

if branch_boundrary > 0:
	for i in range(0, 1):
		counter = 0
		for j in range(branch_boundrary, len(info)):
			temp = branch_leaf[i]
			branch_leaf.append(j)
			if counter == 0:
				tree.add_node(info[j], info[temp])
				#print "j, temp: ", (j, temp)
			else:
				tree.add_node(info[j], info[j-1])
				#print "j, j-1: ", (j, j-1)
			counter += 1

tree.display(info[0])

#print("***** DEPTH-FIRST ITERATION *****"), '\n'
for node in tree.traverse(info[0]):							#  calculate path amount
	if "region" not in node:
		dfs.append(node)

for i in range(0, len(p_num)-1):
	if (p_num[i+1] < p_num[i]) and ("}" in dfs[i+1]):
		p_num.insert(i+1, 99)

print ("parents: \n", p_num)

for i in range(0, len(p_num)-1):
	path.append(dfs[i])
	if ("}" in dfs[i]) and ("}" not in dfs[i+1]):
		#print (dfs[i+1])
		partition = open("partition.c", "w")
		execution_path_r1 += 1
		for i in range(0, len(path)):
			#if ("if" not in dfs[i]) and ("elif" not in dfs[i]) and ("else" not in dfs[i]) and ("}" not in dfs[i]):
			partition.write(path[i])
		partition.close()
		os.system("mv partition.c exe_r1_path"+str(execution_path_r1)+".c")
		temp_pop = 0
		temp_path = len(path)
		for j in range(len(path)-1, -1, -1):
			if (p_num[temp_path] <= p_num[j]):
				#print ("(p_num[temp_path], p_num[j]): ", (p_num[temp_path], p_num[j]))
				path.pop()
				temp_pop += 1
				temp_del = j
				#print ("(p_num[temp_path], p_num_stat[j]): ", (p_num[temp_path], p_num_stat[j]))
			else: 
				break
		for k in range(0, temp_pop):
			del p_num[temp_del]
		print ("after del p_num: ", p_num)
		#print ("after del p_num_stat: ", p_num_stat)
		#print ("after path.pop(): ", path)

partition = open("partition.c", "w")
execution_path_r1 += 1
for i in range(0, len(path)):
	partition.write(path[i])
partition.write("}\n")
partition.close()
os.system("mv partition.c exe_r1_path"+str(execution_path_r1)+".c")
	
	





	
