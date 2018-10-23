import os
import subprocess
import string
#import scrapbooking_klee
#print (scrapbooking_klee.ValidInputs)

def replaceIR(instruction_list, new_list):
	instruction_list.pop()
	instruction_list.append(new_list)
	new_list = ""

def splitIR(original_line, temp_line, line_split):
	temp_line = original_line
	print ("temp_r: ", temp_line)
	line_split = temp_line.split()
	print ("split: ", line_split)

###############  initialization  ##############################
temp_testcase, temp_path1 = [], []
file = open('testcase.ll')
for line in file:
	temp_testcase.append(line)
testcase_length = len(temp_testcase)
file.close()
file = open('answer.ll')
for line in file:
	temp_path1.append(line)
path_length = len(temp_path1)
file.close()
###############  start point of scapbooking  ##################
file = open('program/exe_path1_2.ll')
scrap = open('answer_o.ll','w')
scrapping = []
start_counter = 0
for line in file:
	if "define" in line:
		scrapping.append(line)
		break
	else:
		scrapping.append(line)
		if "common local_unnamed_addr" in line or "common global" in line:
			start_counter += 1

for i in range(0, len(scrapping)):
	scrap.write(scrapping[i])

#scrap.write("entry: \n")
file.close()
scrap.close()
#################  1st time replacing part #####################
file = open('answer.ll')
booking = open('answer_o.ll','a')
counter_ins, counter_load, before_1stBB, counter_temp, counter_call, label_point, phi_point, counter_store, opening_load, counter_re = 0, 1, 0, -1, 0, 0, 0, 0, 0, -1
load_number, operation_name, assert_answer, temp = "", "", "", ""
instruction, label, re_instruction, cmp_point, br_label, br_value = [], [], [], [], [], []
#counter_ins += start_counter
counter_ins += 2 
for line in file:
	if "load" in line:
		counter_ins += 1
		#if opening_load == 0:
			#opening_load = counter_ins
		instruction.append(line)
		temp = line
		temp_1 = temp.split()
		load_number = str(temp_1[0])
		temp = temp.replace(str(load_number), "%"+str(counter_ins))
		"""
		instruction.pop()
		instruction.append(temp)
		temp = ""
		"""
		replaceIR(instruction, temp)
		#before_1stBB = 1	##### special case to increase program counter

	elif ("store" in line):
		#if before_1stBB == 0:
			#counter_ins += 1
		#else:
		counter_store += 1
		instruction.append(line)
		temp = line
		temp_assert_answer = temp.split()
		assert_answer = str(temp_assert_answer[2])
		if "%" not in assert_answer:
			i = 3
			while ("%" not in assert_answer) and (i < len(temp_assert_answer)-1) : 
				assert_answer = str(temp_assert_answer[i])
				if "%" in assert_answer:
					temp = temp.replace(str(assert_answer), str(operation_name)+',')
					break
				i += 1
		else:
			temp = temp.replace(str(assert_answer), str(operation_name)+',')
		'''
		instruction.pop()
		instruction.append(temp)
		'''
		replaceIR(instruction, temp)
	elif ("call" in line) and ("pthread_cond" not in line):
			
		counter_ins += 1
		instruction.append(line)
		temp = line
		temp_1 = temp.split()
		load_number = str(temp_1[0])
		temp = temp.replace(str(load_number), "%"+str(counter_ins))
		replaceIR(instruction, temp)
		
		#before_1stBB = 1							############## special reason about local variable initialization ##############
	elif ("call" in line) and ("pthread_cond" in line):
		continue
	else:
		instruction.append(line)
		if "=" not in line and "%" not in line:
			continue
		elif "label" in line:
			if ";" not in line:						############## br instruction ###############
				counter_ins += 1
				temp = line
				temp_split = line.split()
				#print (temp_split[1])
				if temp_split[1] == 'label':
					temp = temp.replace(str(temp_split[2]), '%'+str(counter_ins))
					replaceIR(instruction, temp)
				else:						
					temp = temp.replace(str(temp_split[2]), '%'+str(counter_ins-1)+',')
					replaceIR(instruction, temp)
			else:
				temp = line
				temp_split = line.split()
				temp = temp.replace(str(temp_split[1]), '<label>:'+str(counter_ins)+':')
				replaceIR(instruction, temp)
				label.append(counter_ins)
				before_1stBB = 1
			continue
		elif "phi" in line:							################ phi instruction (ex:%8 = phi i32 [ %7, %5 ], [ 0, %2 ]): format of [ %7, %5 ] => [ BB last line -1, label ]  #################
			counter_ins += 1
			
			temp = line
			temp_split = line.split()
			
			load_number = str(temp_split[0])
			temp = temp.replace(str(load_number), "%"+str(counter_ins), 1)
			replaceIR(instruction, temp)
		else:
			counter_ins += 1
			temp = line
			if "cmp" in line:
				cmp_point.append(counter_ins)
			temp_1 = temp.split()
			load_number = str(temp_1[0])
			temp = temp.replace(str(load_number), "%"+str(counter_ins))
			load_number = str(temp_1[1])
			if "%" not in load_number:
				i = 1
				while (("%" not in load_number) and ("mutex" not in load_number) and i < len(temp_1)):
					load_number = str(temp_1[i])
					if "%" in load_number and "mutex" not in load_number:
						#print "load_number", load_number
						if "sext" in line or "inttoptr" in line:
							temp = temp.replace(str(load_number), "%"+str(counter_ins-1))
							break
						else:
							temp = temp.replace(str(load_number), "%"+str(counter_ins-1)+",")
							break
					i += 1
			else:
				temp = temp.replace(str(load_number), "%"+str(counter_ins-1)+",")
			temp_1 = temp.split()
			operation_name = str(temp_1[0])
			replaceIR(instruction, temp)
file.close()
for i in range(0, len(instruction)):
	booking.write(instruction[i])
booking.close()

############  2nd time replacing part  ####################
label_point = 0
file = open('answer_o.ll','r')
scrapbooking = open('answer_ok.ll','w')
for line in file:
	counter_re += 1
	temp = line
	temp_split = temp.split()
	if "br" in line and temp_split[1] != 'label':				#############  br i1 %14, label %15, label %18  #############
		temp = temp.replace('label '+str(temp_split[6])+'', 'label %'+str(label[label_point+1]))
		temp = temp.replace('label '+str(temp_split[4]), 'label %'+str(label[label_point])+',')
		#print (temp)
		label_point += 2
		re_instruction.append(temp)
	elif "phi" in line:			################ phi instruction (ex:%8 = phi i32 [ %7, %5 ], [ 0, %2 ]): format of [ %7, %5 ] => [ BB last line -1, label ]  #################
		for i in range(counter_re-1, 0, -1):
			if 'label %'+str(int(temp_split[0].strip('%'))-1) in str(re_instruction[i]):
				#print ("ins[i]: ", re_instruction[i])
				for j in range(i-1, 0, -1):
					if "cmp" not in re_instruction[j] and "=" in re_instruction[j]:
						#print ("ins[j]: ", re_instruction[j])
						temp_value = re_instruction[j].split()
						br_value.append(temp_value[0]) 
						break
				for j in range(i-1, 0, -1):
					if "; <label>" in re_instruction[j]:
						temp_label = re_instruction[j].split()
						br_label.append(temp_label[1].lstrip('; <label>:').rstrip(':'))
						break	
		#print ("brv: ", br_value)
		#print ("brl: ", br_label)
		if len(br_label) < len(br_value):
			br_label.append(str(opening_load-1))
		temp = temp.replace(temp_split[5], str(br_value[0])+',')
		temp = temp.replace(temp_split[6]+' ]', "%"+str(br_label[0])+' ]')
		'''
		if str(temp_split[5]) == str(temp_split[6])+',':
			temp = temp.replace(temp_split[5], "%"+str(label[label_point]-3)+',')
			temp = temp.replace(temp_split[6]+' ]', "%"+str(label[label_point-2])+' ]')
		'''
		temp = temp.replace('[ '+temp_split[9], "[ "+str(br_value[1])+',')
		temp = temp.replace(temp_split[10]+' ]', "%"+str(br_label[1])+' ]')

		for i in range(0, len(br_value)):
			br_value.pop()
			br_label.pop()

				

		re_instruction.append(temp)	
	else:
		re_instruction.append(line)
file.close()
for i in range(0, len(re_instruction)):
	scrapbooking.write(re_instruction[i])
scrapbooking.close()

###########  ending part of scapbooking  ##################
file = open('program/exe_path1_2.ll')
scrapbooking = open('answer_ok.ll','a')
counter, temp_cut, cut = 0, 0, 0
ending, temp_2 = [], []

for line in file:
	temp_2.append(line)
	if ("ret" in line):
		temp = line
		temp_1 = temp.split()
		temp_ret = str(temp_1[2])
		temp = temp.replace(str(temp_ret), "%"+str(counter_ins))
		temp_2.pop()
		temp_2.append(temp)
		break
file.close()

file = open('program/exe_path1_2.ll')
for line in file:
	counter += 1
	ending.append(line)
		
cut = len(temp_2)	 							#before 20171121
#print ("\nlength: ", counter)
'''		
	if ("cmp" in line) and ("br" not in line):	# not good
		temp_cut = counter
		temp = line
		temp_1 = temp.split()
		assert_source = str(temp_1[5])
		temp = temp.replace(str(assert_source), str(assert_answer))

		#print temp_cut
		ending.append(temp)
	else:	
		ending.append(line)

if (temp_cut < cut) and (temp_cut != 0):
	cut = temp_cut
scrapbooking.write(temp)
'''
#print ("cut: ", ending[cut])
for i in range(cut-1, counter):	# include cmp ( before conv )
	scrapbooking.write(ending[i])

file.close()
scrapbooking.close()	 
