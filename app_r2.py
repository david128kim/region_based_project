import os
import subprocess
import string
#from app_r1 import temp_name
from tree import Tree
#from app_r1 import execution_path_r1

(_ROOT, _DEPTH, _BREADTH) = range(3)

tree = Tree()

file = open("region_text/deadlock.txt")
region_path = open("r2_path.c", "w")
treeID, height, brackets_match, branch_boundrary, counter_if, execution_path_r2, counter_bp = 0, 0, 0, 0, 0, 0, 0
info, info_bottom, branch_layer, branch_point, branch_leaf, breakpoint, dfs, cond_num, if_layer, branch_type = [], [], [], [], [], [], [], [], [], []
start, end, counter_r2, r2_flag, main_flag, temp_pop = 1, 0, 0, 0, 0, 0
constrain, constrain_state, path_cond_state, path_cond, cond_text, p_num, path, cond_list, cond_dfs, cond_final_list = "", [], [], [], [], [], [], [], [], []
temp_layer, temp_branch, temp_brackets, branch_end, info_length, loop_flag, gap, temp_i = 0, 0, 0, 0, 0, 0, 0, 0
loop_body, loop_start, loop_end, loop_brackets, temp_info, temp_body, branch_start, branch_finish = [], [], [], [], [], [], [], []

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

#############       loop heuristic reduction AND printing instead pthread_cond_wait      ##############        
for i in range(1, len(info)):
        if "{" in info[i]:
                brackets_match += 1
                if "while" in info[i]:
                        constrain = info[i].replace("while", "if")
                        del info[i]
                        info.insert(i, constrain)
                        loop_start.append(i)
                        loop_brackets.append(brackets_match)
        elif "}" in info[i]:
                brackets_match -= 1
                if (loop_brackets != []) and (brackets_match == loop_brackets[len(loop_brackets)-1] - 1):
                        loop_end.append(i)
                        loop_brackets.pop()
'''
        elif "pthread_cond_wait" in info[i]:
                constrain = info[i].replace('pthread_cond_wait(&', 'printf ("')
                constrain = constrain.replace(');' , '");')
                del info[i]
                info.insert(i, constrain)
'''
#############   eliminate while statement and implement loop heuristic reduction
loop_end.reverse()
info_length = len(info)
for i in range(len(loop_start)-1, -1, -1):
        for j in range(loop_start[i] + 1, loop_end[i] + gap):
                #if "while" not in info[j]:
                temp_body.append(info[j])
#        for j in range(loop_start[i], loop_end[i] + 1 + gap):
#                del info[loop_start[i]]
#        print ("temp_body: ", temp_body)
#        if i == 0:
#                loop_body.extend(temp_body)
##                print ("loop_body: ", loop_body)
#        temp_body = temp_body * 2
        temp_i = loop_start[i] + 1
        if "pthread_cond" in temp_body[0]:
                #print ("+++++++")
                break
        else:
                for j in range(0, len(temp_body)):
                        info.insert(temp_i, temp_body[j])
                        temp_i += 1
       
        gap = len(info) - info_length
        temp_body = []
#print ("fixing info: ", info)

tree.add_node(info[treeID])
for i  in range(1, len(info)):
        #info[i] = info[i] + "/*R2 line:" + str(treeID) + "*/"
        info[i] = "/*R2 line:" + str(treeID) + "*/" + info[i]
        if (("if" in info[i]) and ("else" not in info[i])):
                brackets_match += 1
                cond_num.append(brackets_match)
                branch_layer.append(brackets_match)
                branch_point.append(treeID)
#                if ("else" not in  info[i-1]):
                if cond_num[len(cond_num)-1] == cond_num[len(cond_num)-2]:
                        temp = branch_point[brackets_match-1]
                        tree.add_node(info[i], info[temp])
                        p_num.append(temp)
                        cond_list.append(temp)
                        cond_final_list.append(temp)
                        if branch_start == []:
                                branch_start.append(temp + 1)
                        else: 
                                branch_start.append(i)
                else:
                        tree.add_node(info[i], info[treeID])
                        p_num.append(treeID)
                        cond_list.append(treeID)
                        cond_final_list.append(treeID)

#                constrain = info[i].replace("if", "")
#                constrain = constrain.replace("(", "", 1)
#                constrain = constrain.replace(")", "", 1)
#                constrain = constrain.replace("{", "")
#                constrain = constrain.replace("/*R2 line:" + str(treeID) + "*/", "")
#                constrain_state.append(constrain)
#                path_cond_state.append(constrain)
#                cond_text.append(constrain)


        elif (("else" in info[i]) and ("if" in info[i])):
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

#                constrain = info[i].replace("else if", "")
#                constrain = constrain.replace("(", "", 1)
#                constrain = constrain.replace(")", "", 1)
#                constrain = constrain.replace("{", "")
#                constrain_state.append("null")
#                path_cond_state.append(constrain)
#                cond_text.append(constrain)

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

#                constrain_state.append("null")
#                constrain = " !(" + constrain_state[temp] + ") "
#                path_cond_state.append(constrain)
#                cond_text.append(constrain)

#        elif "while" in info[i]:
#                brackets_match += 1
#                cond_num.append(brackets_match)
#                branch_layer.append(brackets_match)
#                branch_point.append(treeID)
#                if cond_num[len(cond_num)-1] == cond_num[len(cond_num)-2]:
#                        temp = branch_point[brackets_match-1]
#                        tree.add_node(info[i], info[temp])
#                        p_num.append(temp)
#                        cond_list.append(temp)
#                        cond_final_list.append(temp)
##                        print ("info, i, temp: ", info[i], i, temp)
#                else:                                                           ################ else/while then "while" appear ################
#                        tree.add_node(info[i], info[treeID])
#                        p_num.append(treeID)
#                        cond_list.append(treeID)
#                        cond_final_list.append(treeID)
##                        print ("info, i, treeID: ", info[i], i, treeID)
#
#                constrain = info[i].replace("while", "")
#                constrain = constrain.replace("(", "", 1)
#                constrain = constrain.replace(")", "", 1)
#                constrain = constrain.replace("{", "")
#                constrain = constrain.replace("/*R2 line:" + str(treeID) + "*/", "")
#                constrain_state.append(constrain)
#                path_cond_state.append(constrain)
#                cond_text.append(constrain)

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
#print ("branch_layer: ", branch_layer)
        
###########     record every branch type    ############
#for i in range(1, len(info)):
#        if "if" in info[i] and "else" not in info[i]:
#                branch_type.append("if")
#        elif "else" in info[i] and "if" in info[i]:
#                branch_type.append("else if")
#        elif "else" in info[i] and "if" not in info[i]:
#                branch_type.append("else")
#        elif "while" in info[i]:
#                branch_type.append("while")
#
#temp = len(cond_list)
#for i in range(0, temp-1):
#        cond_dfs.append(cond_text[i])
##        if (cond_final_list[i+1] <= cond_final_list[i]):
#        if (cond_final_list[i+1] <= cond_final_list[i]) and "else" in branch_type[i+1]:
#                constrain = "1"
#                for j in range(0, len(cond_dfs)):
#                        constrain = constrain + " && " + path_cond_state[j]
#                path_cond.append(constrain)
#                temp_state_pop = 0
#                temp_cond_dfs_length = len(cond_dfs)
#                for k in range(len(cond_dfs)-1, -1, -1):
#                        if cond_list[temp_cond_dfs_length] <= cond_list[k]:
#                                cond_dfs.pop()
#                                temp_state_pop += 1
#                                temp_del = k
#                        else:
#                                break
#                for l in range(0, temp_state_pop):
#                        del cond_list[temp_del]
#                        del path_cond_state[temp_del]
#constrain = "1"
#for i in range(0, len(path_cond_state)):
#        constrain = constrain + " && " + path_cond_state[i]
#path_cond.append(constrain)
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
for i in range(0, len(dfs)):
        region_path.write(dfs[i])
region_path.close()

"""
#print (dfs)
for i in range(0, len(p_num)-1):
        #if (p_num[i+1] < p_num[i]) and ("}" in dfs[i+1]):
        if (p_num[i+1] < p_num[i]) and ("{" not in dfs[i+1]):
                p_num.insert(i+1, 99)
#print ("parents: ", p_num)
for i in range(0, len(p_num)-1):
        path.append(dfs[i])
#        if ("}" in dfs[i]) and ("}" not in dfs[i+1]) and (("else" in dfs[i+1]) or ("if" in dfs[i+1]) or ("while" in dfs[i+1])):
        if ("}" in dfs[i]) and ("}" not in dfs[i+1]) and ("{" in dfs[i+1]):
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
#partition.write("}\n")
partition.close()
#print ("last path: ", path)
os.system("mv partition.c exe_r2_path"+str(execution_path_r2)+".c")


###########     forking each false condition without other choose ("elif", "else"): for "if" only
for i in range(1, len(info)):
        if (("if" in info[i] ) and "else" not in info[i]) or "while" in info[i]:
                temp_layer += 1
                if "while" in info[i]:
                        temp_branch = -1
                else:
                    for j in range(0, len(branch_layer)):
                            if (branch_layer[j] == temp_layer) and ("else" in branch_type[j]) and ("if" not in branch_type[j]):
                                    temp_branch += 1
                if temp_branch >= 1:
                        continue
                else:
                        temp_brackets = 0
                        #temp_brackets = temp_layer - 1
#                        print ("if start location: ", i)
                        for k in range(i, len(info)):
                                if "{" in info[k]:
                                        temp_brackets += 1
                                elif "}" in info[k]:
                                        temp_brackets -= 1
                                        #if k == len(info)-2:
                                                #temp_brackets -= 1
                                        if (temp_brackets == 0):
                                                #if k < len(info)-2 and "else if" not in info[k+1]:
                                                if k != len(info) -1 and "else if" not in info[k+1]:
                                                        branch_end = k
                                                        break
                                                #elif k == len(info)-2 and "}" in info[k+1]:
                                                elif k == len(info)-1:
                                                        branch_end = len(info)
                                                        break
                                                else:
                                                        continue
#                        print ("branch_end: ", branch_end)
#                        branch_start.append(i)
                        if i in branch_start:
                                branch_finish.append(branch_end + 1)
                        partition = open("partition.c", "w")
                        execution_path_r2 += 1
                        temp_brackets = 0
                        for l in range(1, i):
                                if "{" in info[l]:
                                        temp_brackets += 1
                                elif "}" in info[l]:
                                        temp_brackets -= 1
                                partition.write(info[l])
#                                print ("upper part: ",info[l])
                       
                        for l in range(branch_end+1, len(info)):
                                if "{" in info[l]:
                                        temp_brackets += 1
                                elif "}" in info[l]:
                                        temp_brackets -= 1
                                if temp_brackets >= 0:
                                        partition.write(info[l])
#                                print ("down part: ", info[l])
                                
                        if temp_brackets > 0:
                                for m in range(0, temp_brackets):
                                        partition.write("}\n")                                      
                        partition.close()
                        os.system("mv partition.c exe_r2_path"+str(execution_path_r2)+".c")
info_length = len(info)
if len(branch_finish) > 1:
        partition = open("partition.c", "w")
        execution_path_r2 += 1
        for i in range(0, len(branch_start)):
                gap = info_length - len(info)
                for j in range(0, branch_finish[i] - branch_start[i]):
                        del info[branch_start[i] - gap]
        for i in range(1, len(info)):
                partition.write(info[i])
#                print ("All False Path: ", info[i])
        partition.close()
        os.system("mv partition.c exe_r2_path"+str(execution_path_r2)+".c")                
"""                     
                
