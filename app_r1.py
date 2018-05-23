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
constrain, constrain_state, path_cond, c_num, p_num, path, p_num_stat = "", [], [], [], [], [], []

def extract_branch(a,b):
	a = b.replace("if", "")
	a = a.replace("(", "", 1)
	a = a.replace(")", "", 1)
	a = a.replace("{", "")
	print ("a :", a)
	print ("b :", b)
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
			#print ("if: child, parents: ", (i, temp))
		else:
			tree.add_node(info[i], info[treeID])
			#print ("if: child, parents: ", (i, treeID))
			c_num.append(i)
			p_num.append(treeID)
		constrain = info[i].replace("if", "")
		constrain = constrain.replace("(", "", 1)
		constrain = constrain.replace(")", "", 1)
		constrain = constrain.replace("{", "")
		"""
		if (len(brackets_match_record) > 1) and (brackets_match_record[len(brackets_match_record)-2] < brackets_match_record[len(brackets_match_record)-1]):
			constrain_state.append(constrain)
			constrain = constrain_state[len(constrain_state)-2] + " && " + constrain
			#constrain_state.pop()
			constrain_state.append(constrain)
			#path_cond.append(constrain)
		else:
			constrain_state.append(constrain)
		
		#constrain = extract_branch
		#extract_branch(constrain, info[i])
		
		print ("brackets_match: \n", brackets_match)
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
		node_height.append(height)
		temp_node_length = len(node_height)
                #if (node_height[temp_node_length-1] < node_height[temp_node_length-2]):
			#branch_leaf.append(i-1)
		"""
		print ("brackets_match:(else) \n", brackets_match)
			
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
			node_height.append(height)

		if("}" in info[i]):
		######## layer problem #########
			brackets_match -= 1			
			if brackets_match == 0:
				branch_leaf.append(i)
				"""
				constrain = constrain_state.pop()
				path_cond.append(constrain)
				print ("path condition: \n", path_cond)
				print ("state:(leaf) \n", constrain_state)
				"""
	#print "b-m: ", brackets_match
	#print "info[i]: ", info[i]
	treeID += 1
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

#print ("parents: \n", p_num)
#print ("child: \n", c_num)
#print (len(info))
#print("***** DEPTH-FIRST ITERATION *****"), '\n'
#print ("region1: ")
for node in tree.traverse(info[0]):							#  calculate path amount
	if "region" not in node:
		dfs.append(node)
#print ("dfs: ", dfs)
for i in range(0, len(p_num)-1):
	if (p_num[i+1] < p_num[i]) and ("}" in dfs[i+1]):
		p_num.insert(i+1, 99)
p_num_stat = p_num
#print (p_num_stat)
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
		#temp_path = len(p_num)
		#temp_path = len(path) + temp_pop
		temp_pop = 0
		temp_path = len(path)
		#print ("path length: ", temp_path)
		#print ("len(path): ", len(path))
		#print ("path: ", path)
		for j in range(len(path)-1, -1, -1):
			if (p_num[temp_path] <= p_num[j]):
				#print ("(p_num[temp_path], p_num[j]): ", (p_num[temp_path], p_num[j]))
				path.pop()
				temp_pop += 1
				temp_del = j
				#del p_num[j]
				#p_num.pop()
				#print ("(p_num[temp_path], p_num_stat[j]): ", (p_num[temp_path], p_num_stat[j]))
			#elif "}" in path[j]:
				#path.pop()
				#temp_pop += 1
		
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
	
	





	
