import os
import subprocess
import string
#import scrapbooking_klee
#print (scrapbooking_klee.ValidInputs)
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
file = open('program/path1.ll')
scrap = open('answer_o.ll','w')
scrapping = []
for line in file:
	if "define" in line:
		scrapping.append(line)
		break
	else:
		scrapping.append(line)

for i in range(0, len(scrapping)):
	scrap.write(scrapping[i])

#scrap.write("entry: \n")
file.close()
scrap.close()
#################  1st time replacing part #####################
file = open('answer.ll')
booking = open('answer_o.ll','a')
counter_ins, counter_load, before_1stBB, counter_temp, counter_call, label_point, counter_store = 0, 1, 0, -1, 0, 0, 0
load_number, operation_name, assert_answer, temp = "", "", "", ""
instruction, label, re_instruction = [], [], []

for line in file:
	if "load" in line:
		counter_ins += 1
		instruction.append(line)
		temp = line
		temp_1 = temp.split()
		load_number = str(temp_1[0])
		temp = temp.replace(str(load_number), "%"+str(counter_ins))
		instruction.pop()
		instruction.append(temp)
		temp = ""
	elif ("store" in line):
		if before_1stBB == 0:
			counter_ins += 1
		else:
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
		instruction.pop()
		instruction.append(temp)
	elif ("call" in line):
		counter_ins += 1
		instruction.append(line)
		temp = line
		temp_1 = temp.split()
		load_number = str(temp_1[0])
		temp = temp.replace(str(load_number), "%"+str(counter_ins))
		'''
		load_number = str(temp_1[2])
		if "%" not in load_number:
			i = 3
			while ("%" not in load_number) and (i < len(temp_1)-1) :
				load_number = str(temp_1[i])
				if "%" in load_number:
					temp = temp.replace(str(load_number), str(operation_name)+')')
					break
				i += 1
		else:
			temp = temp.replace(str(load_number), str(operation_name))
		'''
		instruction.pop()
		instruction.append(temp)

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
					instruction.pop()
					instruction.append(temp)
					temp = ""
				else:						
					temp = temp.replace(str(temp_split[2]), '%'+str(counter_ins-1)+',')
					instruction.pop()
					instruction.append(temp)
					temp = ""
			else:
				temp = line
				temp_split = line.split()
				temp = temp.replace(str(temp_split[1]), '<label>:'+str(counter_ins)+':')
				instruction.pop()
				instruction.append(temp)
				temp = ""
				label.append(counter_ins)
				before_1stBB = 1
			continue
		else:
			counter_ins += 1
			temp = line
			temp_1 = temp.split()
			load_number = str(temp_1[0])
			temp = temp.replace(str(load_number), "%"+str(counter_ins))
			load_number = str(temp_1[1])
			if "%" not in load_number:
				i = 1
				while (("%" not in load_number) and ("mutex" not in load_number) and i < len(temp_1)):
					load_number = str(temp_1[i])
					if "%" in load_number:
						#print "load_number", load_number
						if "sext" in line or "inttoptr" in line:
							temp = temp.replace(str(load_number), "%"+str(counter_ins-1))
							break
						else:	
							#print (instruction[counter_ins-2])
							if "label" in instruction[counter_ins-1]:
								print ("???, ", temp)
								#temp = temp.replace(str(load_number), "%"+str(counter_ins-2)+",")
							else:
								temp = temp.replace(str(load_number), "%"+str(counter_ins-1)+",")
							break
					i += 1
			else:
				temp = temp.replace(str(load_number), "%"+str(counter_ins-1)+",")
			temp_1 = temp.split()
			operation_name = str(temp_1[0])
			instruction.pop()
			instruction.append(temp)
			temp = ""
file.close()
for i in range(0, len(instruction)):
	booking.write(instruction[i])
booking.close()

############  2nd time replacing part  ####################
#print ("label: ", label)
file = open('answer_o.ll','r')
scrapbooking = open('answer_ok.ll','w')
for line in file:
	temp = line
	temp_split = temp.split()
	#print ("there")
	if "br" in line and temp_split[1] != 'label':
		#print (temp_split)
		temp = temp.replace(str(temp_split[4]), '%'+str(label[label_point])+',')
		temp = temp.replace(str(temp_split[6]), '%'+str(label[label_point+1]))
		label_point += 2
		re_instruction.append(temp)
	else:
		re_instruction.append(line)
file.close()
for i in range(0, len(re_instruction)):
	scrapbooking.write(re_instruction[i])
scrapbooking.close()

###########  ending part of scapbooking  ##################
file = open('program/path1.ll')
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

file = open('program/path1.ll')
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
