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
scrap = open('answer_ok.ll','w')
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
#################  replace part #####################
file = open('answer.ll')
booking = open('answer_ok.ll','a')
counter_ins, counter_load, counter_operation, counter_temp, counter_store, counter_call = 0, 1, 0, -1, 0, 0
load_number, load_number_1, operation_name, second_operation, assert_answer, temp, first_number, instruction = "", "", "", "", "", "", "", []

for line in file:
	if "load" in line:
		#counter_load += 1
		counter_ins += 1
		instruction.append(line)
		#if counter_load >= 1:
		temp = line
		temp_1 = temp.split()
		load_number = str(temp_1[0])
			#print "old: ", temp
			#temp = temp.replace(str(load_number), "%"+str(counter_load))
		temp = temp.replace(str(load_number), "%"+str(counter_ins))
			#print "new: ", temp
		instruction.pop()
		instruction.append(temp)
		temp = ""
	elif ("store" in line):
		instruction.append(line)
		#counter_store += 1
		temp = line
		#temp = temp.split()
		#second_operation = str(temp[2])
		#print (operation_name)
		#if "%" not in second_operation:
			#second_operation = str(temp[3])
		#if counter_store >= 2:
			#temp = line
		temp_assert_answer = temp.split()
			#print "length: ", len(temp_assert_answer)
		assert_answer = str(temp_assert_answer[2])
		if "%" not in assert_answer:
			i = 3
			while ("%" not in assert_answer) and (i < len(temp_assert_answer)-1) : 
				assert_answer = str(temp_assert_answer[i])
				if "%" in assert_answer:
					temp = temp.replace(str(assert_answer), str(operation_name)+',')
					break
				i += 1
					#print "i: ", i
		else:
			temp = temp.replace(str(assert_answer), str(operation_name)+',')
		instruction.pop()
		instruction.append(temp)
                        #temp_assert_answer = temp.split()
                        #assert_answer = str(temp_assert_answer[2])
                        #if "%" not in assert_answer:
                                #assert_answer = str(temp_assert_answer[3])
	elif ("call" in line):
		counter_ins += 1
		instruction.append(line)
		temp = line
		temp_1 = temp.split()
		load_number = str(temp_1[0])
		temp = temp.replace(str(load_number), "%"+str(counter_ins))
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
		instruction.pop()
		instruction.append(temp)
		#if counter_call > 0:
			#temp = line
                        #print "old: ", temp
			#temp_1 = temp.split()
			#call_number = str(temp_1[0])
			#temp = temp.replace(call_number, "%call"+str(counter_call))
                        #print "new: ", temp
			#instruction.append(temp)
                        #temp = ""
		#else:
			#instruction.append(line)
		#counter_call += 1

	else:
		counter_ins += 1
		counter_operation += 1
		instruction.append(line)
		if "=" not in line and "%" not in line:
			continue	
		else:
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
							temp = temp.replace(str(load_number), "%"+str(counter_ins-1)+",")
							break
					i += 1
			else:
				temp = temp.replace(str(load_number), "%"+str(counter_ins-1)+",")
			#temp = temp.replace(str(load_number), "%"+str(counter_load)+",")
			#temp = line
			temp_1 = temp.split()
			operation_name = str(temp_1[0])
			#print (operation_name)
			instruction.pop()
			instruction.append(temp)
			temp = ""
		# 20180327
		#if counter_operation >= 2:
			#temp = line
			#temp_1 = temp.split()
			#if "%" not in load_number:
				#i = 1
				#while (("%" not in load_number) and ("mutex" not in load_number) and i < len(temp_1)):
					#load_number = str(temp_1[i])
					#if "%" in load_number:
                                        	#print "load_number", load_number
						#temp = temp.replace(str(load_number), "%"+str(counter_load)+",")
						#break
					#i += 1
			#else:
				#temp = temp.replace(str(load_number), "%"+str(counter_load)+",")


			#load_number_back = str(temp_1[1])
			#load_number_front = str(temp_1[0])
			#i = 1
			#while (("%" not in load_number_back) and ("mutex" not in load_number_back) and i < len(temp_1)):
                        	#load_number_back = str(temp_1[i])
                        	#i += 1
                       	#temp = temp.replace(str(load_number_back), str(second_operation))
			#temp_1 = temp.split()
			#load_number_back = str(temp_1[1])
			#i = 1
                        #while (("%" not in load_number_back) and ("mutex" not in load_number_back) and i < len(temp_1)):
                                #load_number_back = str(temp_1[i])
                                #i += 1
                        #load_number_front = str(temp_1[0])
			#if str(load_number_front)+"," == str(load_number_back):
				#temp = temp.replace(str(load_number_front), str(load_number_front)+str(counter_operation), 1)
				#temp_1 = temp.split()

			#operation_name = str(temp_1[0])
			#instruction.pop()
			#instruction.append(temp)
			#temp = ""

for i in range(0, len(instruction)):
	booking.write(instruction[i])
file.close()
booking.close()

###########  ending part of scapbooking  ##################
file = open('program/path1.ll')
scrapbooking = open('answer_ok.ll','a')
counter_store, counter, temp_cut, cut = 0, 0, 0, 0
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
		#print ("temp: ", temp )
		#print ("temp_ret: ", temp_ret)
		#print ("counter_ins: ",counter_ins )
		break
file.close()

file = open('program/path1.ll')
for line in file:
	counter += 1
		
cut = len(temp_2)	 							#before 20171121
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
for i in range(cut, counter):	# include cmp ( before conv )
	scrapbooking.write(ending[i])

file.close()
scrapbooking.close()	 
