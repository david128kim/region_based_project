import os
#import commands
import subprocess
import string

from tree import Tree
from tree import depth_list

(_ROOT, _DEPTH, _BREADTH) = range(3)

tree = Tree()

file = open("region_text/p-c.txt")
treeID = 0
info = []
height = 0
node_height = []
brackets_match_record = []
brackets_match = 0
branch_point = []
branch_point_record = []
branch_boundrary = 0
branch_leaf = []
counter_if = 0
execution_path_r1 = 0
breakpoint = []
counter_bp = 0
dfs = []
dfs_temp = []
start, end, counter_r2, r2_flag, main_flag, temp_node_length= 1, 0, 0, 0, 0, 0
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
		else:
			tree.add_node(info[i], info[treeID])

	elif ("else if" in info[i]):
		brackets_match += 1
		brackets_match_record.append(brackets_match)
		if (brackets_match_record[len(brackets_match_record)-1] < brackets_match_record[len(brackets_match_record)-2]):
			branch_point.pop()
		height = brackets_match
		temp = branch_point[brackets_match-1]
		tree.add_node(info[i], info[temp])
		node_height.append(height)
		temp_node_length = len(node_height)


	elif (("else" in info[i]) and ("if" not in info[i])):
		brackets_match += 1
		brackets_match_record.append(brackets_match)
		if (brackets_match_record[len(brackets_match_record)-1] < brackets_match_record[len(brackets_match_record)-2]):
                        branch_point.pop()
		height = brackets_match
		#print height
		#print "branch_point(else): ", branch_point[1]
		temp = branch_point[brackets_match-1]
		#temp = branch_point[len(branch_point)-1]
		#print "branch_point(else): ", temp
		tree.add_node(info[i], info[temp])
		#print "else = i, temp: ", (i, temp)
		node_height.append(height)
		temp_node_length = len(node_height)
                #print "length of node_height: ", temp_node_length
                #if (node_height[temp_node_length-1] < node_height[temp_node_length-2]):
			#branch_leaf.append(i-1)

	else:	
		if "end of branch" in info[i]:
			branch_boundrary = i
			#print "branch_boundrary: ", branch_boundrary
			break
		else: 
			height += 1
			#print height
			tree.add_node(info[i], info[treeID])
			#print "others = i, treeID: ", (i, treeID)
			node_height.append(height)

		if("}" in info[i]):
		######## layer problem #########
			brackets_match -= 1			
			if brackets_match == 0:
				branch_leaf.append(i)
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

#print("***** DEPTH-FIRST ITERATION *****"), '\n'
for node in tree.traverse(info[0]):							#  calculate path amount
	dfs.append(node)
	if node == info[len(info)-1]: 
		partition = open("partition.c", "w")
		execution_path_r1 += 1
		for i in range(1, len(dfs)):
			if ("if" not in dfs[i]) and ("elif" not in dfs[i]) and ("else" not in dfs[i]) and ("}" not in dfs[i]):
				partition.write(dfs[i])
		partition.close()
		os.system("mv partition.c exe_r1_path"+str(execution_path_r1)+".c")
		#os.system('clang -Os -S -emit-llvm exe_r1_path'+str(execution_path_r1)+'.c -o exe_r1_path'+str(execution_path_r1)+'.ll')
		for i in range(len(dfs)-1, -1, -1):
			if ("if" not in dfs[i]) and ("elif" not in dfs[i]) and ("else" not in dfs[i]):
				dfs.pop()
	
















