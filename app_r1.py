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
start, end, counter_r2, r2_flag, main_flag, temp_node_length= 1, 0, 0, 0, 0, 0
constrain, constrain_state, path_cond, c_num, p_num = "", [], [], [], []

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
			print ("if: child, parents: ", (i, temp))
		else:
			tree.add_node(info[i], info[treeID])
			print ("if: child, parents: ", (i, treeID))
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
		print ("elif: child, parents: ", (i, temp))
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
		print ("else: child, parents: ", (i, temp))
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
			print ("others: child, parents: ", (i, treeID))
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

print ("parents: \n", p_num)
print ("child: \n", c_num)

#print("***** DEPTH-FIRST ITERATION *****"), '\n'
print ("region1: ")
for node in tree.traverse(info[0]):							#  calculate path amount
	if "region" not in node:
		dfs.append(node)
		if node == info[len(info)-1]: 
			partition = open("partition.c", "w")
			execution_path_r1 += 1
			array_site = 0
			for i in range(1, len(dfs)):
				array_site += 1
				if ("if" not in dfs[i]) and ("elif" not in dfs[i]) and ("else" not in dfs[i]) and ("}" not in dfs[i]):
					partition.write(dfs[i])
			partition.close()
			os.system("mv partition.c exe_r1_path"+str(execution_path_r1)+".c")
			#os.system('clang -Os -S -emit-llvm exe_r1_path'+str(execution_path_r1)+'.c -o exe_r1_path'+str(execution_path_r1)+'.ll')
			"""
			brackets_match = 0
			for i in range(len(dfs)-1, -1, -1):
				if "{" in dfs[i]:
					brackets_match += 1
				if ("if" in dfs[i]) and ("elif" in dfs[i]) and ("else" in dfs[i]) or brackets_match < 1:
					dfs.pop()
			"""
			dfs.pop()
			print ("length of dfs: ", len(dfs))
			print ("dfs: ", dfs)
			
			"""
			for i in range(len(dfs)-1, -1, -1):
				if p_num[len(dfs)-1] >= p_num[i]:
						dfs.pop()
				elif ("if" in dfs[i]) and ("elif" in dfs[i]) and ("else" in dfs[i]) and ("}" in dfs[i]):
						dfs.pop()
			"""

