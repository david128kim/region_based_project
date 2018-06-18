import os
import subprocess
import string
#from app_r1 import temp_name
from tree import Tree
#from app_r1 import execution_path_r1

(_ROOT, _DEPTH, _BREADTH) = range(3)

tree = Tree()

file = open("region_text/branch.txt")
treeID, height, brackets_match, branch_boundrary, counter_if, execution_path_r2, counter_bp = 0, 0, 0, 0, 0, 0, 0
info, info_bottom, branch_layer, branch_point, branch_leaf, breakpoint, dfs, if_layer = [], [], [], [], [], [], [], []
start, end, counter_r2, r2_flag, main_flag, temp_pop = 1, 0, 0, 0, 0, 0
constrain, constrain_state, path_cond_state, path_cond, cond_text, p_num, path, cond_list, cond_dfs, cond_final_list = "", [], [], [], [], [], [], [], [], []

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
                brackets_match += 1
                branch_layer.append(brackets_match)
                branch_point.append(treeID)
                if ("else" not in  info[i-1]):
                        temp = branch_point[brackets_match-1]
                        tree.add_node(info[i], info[temp])
                        p_num.append(temp)
                        cond_list.append(temp)
                        cond_final_list.append(temp)
                else:
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


        elif (("else" in info[i]) and ("if" in info[i])):
                brackets_match += 1
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

        elif (("else" in info[i]) and ("if" not in info[i])):
                brackets_match += 1
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
        treeID += 1
#print ("branch_point: ", branch_point)
print ("branch_layer: ", branch_layer)
temp = len(cond_list)
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
#print ("path_cond: ", path_cond)


if branch_boundrary > 0:
        for i in range(0, 1):
                counter = 0
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
#print (dfs)
for i in range(0, len(p_num)-1):
        #if (p_num[i+1] < p_num[i]) and ("}" in dfs[i+1]):
        if (p_num[i+1] < p_num[i]) and ("else" not in dfs[i+1]):
                p_num.insert(i+1, 99)
#print ("parents: ", p_num)
for i in range(0, len(p_num)-1):
        path.append(dfs[i])
        if ("}" in dfs[i]) and ("}" not in dfs[i+1]) and (("else" in dfs[i+1]) or ("if" in dfs[i+1]) or ("while" in dfs[i+1])):
                partition = open("partition.c", "w")
                execution_path_r2 += 1
                for i in range(0, len(path)):
                        #if ("if" not in dfs[i]) and ("elif" not in dfs[i]) and ("else" not in dfs[i]) and ("}" not in dfs[i]):
                        partition.write(path[i])
                partition.close()
                #print ("path: ", path)
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
                #print (p_num)
partition = open("partition.c", "w")
execution_path_r2 += 1
for i in range(0, len(path)):
        partition.write(path[i])
partition.write("}\n")
partition.close()
#print ("last path: ", path)
os.system("mv partition.c exe_r2_path"+str(execution_path_r2)+".c")
