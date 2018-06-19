import os
import subprocess
import string

from tree import Tree
from tree import depth_list

(_ROOT, _DEPTH, _BREADTH) = range(3)

tree = Tree()

file = open("region_text/while.txt")
treeID, height, brackets_match, branch_boundrary, counter_if, execution_path_r1, counter_bp, fork = 0, 0, 0, 0, 0, 0, 0, 0
info, node_height, branch_layer, branch_point, branch_leaf, breakpoint, dfs, dfs_temp, cond_num, if_layer, branch_type = [], [], [], [], [], [], [], [], [], [], []
start, end, counter_r2, r2_flag, main_flag, temp_node_length, temp_dfs, temp_pop = 1, 0, 0, 0, 0, 0, 0, 0
constrain, constrain_state, path_cond_state, path_cond, cond_text, p_num, path, cond_list, cond_dfs, cond_final_list = "", [], [], [], [], [], [], [], [], []
temp_layer, temp_branch, temp_brackets, branch_end, info_length, loop_flag, loop_brackets = 0, 0, 0, 0, 0, 0, 0
loop_body = []

def extract_branch(a,b):
        a = b.replace("if", "")
        a = a.replace("(", "", 1)
        a = a.replace(")", "", 1)
        a = a.replace("{", "")
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
                brackets_match += 1
                cond_num.append(brackets_match)
                branch_layer.append(brackets_match)
                branch_point.append(treeID)
                if cond_num[len(cond_num)-1] == cond_num[len(cond_num)-2]:      ################ same depth #################################
                        temp = branch_point[brackets_match-1]
                        tree.add_node(info[i], info[temp])
                        p_num.append(temp)
                        cond_list.append(temp)
                        cond_final_list.append(temp)
                else:                                                           ################ else/while/if/elif then "if" appear ################
                        tree.add_node(info[i], info[treeID])
                        p_num.append(treeID)
                        cond_list.append(treeID)
                        cond_final_list.append(treeID)

                constrain = info[i].replace("if", "")
                constrain = constrain.replace("(", "", 1)
                constrain = constrain.replace(")", "", 1)
                constrain = constrain.replace("{", "")
                constrain_state.append(constrain)
                path_cond_state.append(constrain)
                cond_text.append(constrain)
		
                if (brackets_match != loop_brackets - 1) and (loop_flag == 1):
                        loop_body.append(info[i])
                else:
                        loop_flag = 0		

        elif ("else if" in info[i]):
                brackets_match += 1
                cond_num.append(brackets_match)
                branch_layer.append(brackets_match)
                if (branch_layer[len(branch_layer)-1] < branch_layer[len(branch_layer)-2]):
                        branch_point.pop()
                temp = branch_point[brackets_match-1]
                tree.add_node(info[i], info[temp])

                p_num.append(temp)
                cond_list.append(temp)
                cond_final_list.append(temp)

                constrain = info[i].replace("else if", "")
                constrain = constrain.replace("(", "", 1)
                constrain = constrain.replace(")", "", 1)
                constrain = constrain.replace("{", "")
                constrain_state.append("null")
                path_cond_state.append(constrain)
                cond_text.append(constrain)

                if (brackets_match != loop_brackets - 1) and (loop_flag == 1):
                        loop_body.append(info[i])
                else:
                        loop_flag = 0

        elif (("else" in info[i]) and ("if" not in info[i])):
                brackets_match += 1
                cond_num.append(brackets_match)
                branch_layer.append(brackets_match)

                if (branch_layer[len(branch_layer)-1] < branch_layer[len(branch_layer)-2]):
                        branch_point.pop()
                temp = branch_point[brackets_match-1]
                tree.add_node(info[i], info[temp])

                p_num.append(temp)
                cond_list.append(temp)
                cond_final_list.append(temp)

                constrain_state.append("null")
                constrain = " !(" + constrain_state[temp] + ") "
                path_cond_state.append(constrain)
                cond_text.append(constrain)

                if (brackets_match != loop_brackets - 1) and (loop_flag == 1):
                        loop_body.append(info[i])
                else:
                        loop_flag = 0

        elif "while" in info[i]:
                brackets_match += 1
                cond_num.append(brackets_match)
                branch_layer.append(brackets_match)
                branch_point.append(treeID)
                if cond_num[len(cond_num)-1] == cond_num[len(cond_num)-2]:
                        temp = branch_point[brackets_match-1]
                        tree.add_node(info[i], info[temp])
                        p_num.append(temp)
                        cond_list.append(temp)
                        cond_final_list.append(temp)
                else:                                                           ################ else/while then "while" appear ################
                        tree.add_node(info[i], info[treeID])
                        p_num.append(treeID)
                        cond_list.append(treeID)
                        cond_final_list.append(treeID)

                constrain = info[i].replace("while", "")
                constrain = constrain.replace("(", "", 1)
                constrain = constrain.replace(")", "", 1)
                constrain = constrain.replace("{", "")
                constrain_state.append(constrain)
                path_cond_state.append(constrain)
                cond_text.append(constrain)

                loop_brackets = brackets_match
                loop_flag = 1

        else:
                if "end of branch" in info[i]:
                        branch_boundrary = i
                        break
                else:
                        tree.add_node(info[i], info[treeID])
                        p_num.append(treeID)
                        constrain_state.append("null")

                if("}" in info[i]):
                ######## layer problem #########
                        brackets_match -= 1
                        if brackets_match == 0:
                                branch_leaf.append(i)

                if (brackets_match != loop_brackets - 1) and (loop_flag == 1):
                        loop_body.append(info[i])
                else:
                        loop_flag = 0
                        

        treeID += 1
print ("loop_body: ", loop_body)
temp = len(cond_list)
print ("branch_layer: ", branch_layer)
for i in range(0, temp-1):
        cond_dfs.append(cond_text[i])
        if (cond_final_list[i+1] <= cond_final_list[i]):
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
                for l in range(0, temp_state_pop):
                        del cond_list[temp_del]
                        del path_cond_state[temp_del]
constrain = "1"
for i in range(0, len(path_cond_state)):
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
                        else:
                                tree.add_node(info[j], info[j-1])
                        counter += 1

tree.display(info[0])

#print("***** DEPTH-FIRST ITERATION *****"), '\n'
for node in tree.traverse(info[0]):                                                     #  calculate path amount
        if "region" not in node:
                dfs.append(node)

for i in range(0, len(p_num)-1):
        if (p_num[i+1] < p_num[i]) and ("{" not in dfs[i+1]):
                p_num.insert(i+1, 99)

#print ("parents: \n", p_num)

for i in range(0, len(p_num)-1):
        path.append(dfs[i])
        #if ("}" in dfs[i]) and ("}" not in dfs[i+1]) and (("else" in dfs[i+1]) or ("else if" in dfs[i+1]) or ("while" in dfs[i+1])):
        if ("}" in dfs[i]) and ("}" not in dfs[i+1]) and ("{" in dfs[i+1]):
                partition = open("partition.c", "w")
                execution_path_r1 += 1
                for i in range(0, len(path)):
                        #if ("if" not in dfs[i]) and ("elif" not in dfs[i]) and ("else" not in dfs[i]) and ("}" not in dfs[i]):
                        partition.write(path[i])
                partition.close()
                os.system("mv partition.c exe_r1_path"+str(execution_path_r1)+".c")
                temp_pop = 0
                temp_path = len(path)
                #print ("p_num: ", p_num[temp_path])
                for j in range(len(path)-1, -1, -1):
                        if (p_num[temp_path] <= p_num[j]):
                                path.pop()
                                temp_pop += 1
                                temp_del = j
                                #print ("temp_del: ", temp_del)
                        else:
                                break
                for k in range(0, temp_pop):
                        del p_num[temp_del]
                #print ("after del p_num: ", p_num)
                #print ("after pop: ", path)

partition = open("partition.c", "w")
execution_path_r1 += 1
for i in range(0, len(path)):
        partition.write(path[i])
partition.write("}\n")
partition.close()
os.system("mv partition.c exe_r1_path"+str(execution_path_r1)+".c")

info_length = len(info)
for i in range(1, len(info)):
        if "if" in info[i] and "else" not in info[i]:
                branch_type.append("if")
        elif "else" in info[i] and "if" in info[i]:
                branch_type.append("else if")
        elif "else" in info[i] and "if" not in info[i]:
                branch_type.append("else")
print ("branch_type: ", branch_type)

for i in range(1, len(info)):
        if "if" in info[i] and "else" not in info[i]:
                temp_layer += 1
                for j in range(0, len(branch_layer)):
                        if (branch_layer[j] == temp_layer) and ("else" in branch_type[j]) and ("if" not in branch_type[j]):
                                temp_branch += 1
                if temp_branch > 1:
                        continue
                else:
                        temp_brackets = 0
                        #temp_brackets = temp_layer - 1
                        for k in range(i, len(info)-1):
                                if "{" in info[k]:
                                        temp_brackets += 1
                                elif "}" in info[k]:
                                        temp_brackets -= 1
                                        if k == len(info)-2:
                                                temp_brackets -= 1
                                        if (temp_brackets == 0):
                                                if "else if" not in info[k+1] and k != len(info)-2:
                                                        branch_end = k
                                                        break
                                                elif "}" in info[k+1] and k == len(info)-2:
                                                        branch_end = len(info)
                                                        break
                                                else:
                                                        continue
                        #print ("branch_end: ", branch_end)
                        partition = open("partition.c", "w")
                        execution_path_r1 += 1
                        temp_brackets = 0
                        for l in range(1, i):
                                if "{" in info[l]:
                                        temp_brackets += 1
                                elif "}" in info[l]:
                                        temp_brackets -= 1
                                partition.write(info[l])
                                #print ("upper part: ",info[l])
                        for l in range(branch_end+1, info_length):
                                if "{" in info[l]:
                                        temp_brackets += 1
                                elif "}" in info[l]:
                                        temp_brackets -= 1
                                partition.write(info[l])
                                #print ("down part: ", info[l])
                        for l in range(0, temp_brackets):
                                partition.write("}\n")
                        partition.close()
                        os.system("mv partition.c exe_r1_path"+str(execution_path_r1)+".c")
