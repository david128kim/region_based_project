import os
import subprocess
import itertools
import scrapbooking_klee
import time
########       	global initialization section
Region_Text, multilist, permutation, recording, Region_Index, states, dr_num = [], [], [], [], [], [], ""
count, p_count, p_flag, count_src, insert_num, Region_length, t_analyze, t_enumerate, t_verify = 0, 0, 1, 0, 0, 0, 0, 0, 0
########	testing info.
#print ("I_num: ", scrapbooking_klee.I_num)
#print ("p_num: ", scrapbooking_klee.p_num)
#print ("Valid-INPUT: ", scrapbooking_klee.ValidInputs)
#print ("INPUT-index: ", scrapbooking_klee.Inputs_Index)
########
t_start = time.time()
#for i in range(1, int(scrapbooking_klee.num_region)+1):
for i in range(1, 2):
	if int(scrapbooking_klee.I_num) < i:
		break
	#for j in range(1, int(scrapbooking_klee.p_num)+1):
	for j in range(1, 2):
		t_analyzing = time.time()
		testcase = open('testcase.c','w')
		########	only for test _1_2
		#file = open('exe_concurrent/concurrent_'+str(i)+'_'+str(j)+'.c', 'r')
		file = open('exe_concurrent/concurrent_1_3.c', 'r')
		for line in file:
			Region_Text.append(line)
			count_src += 1
			if "mutex_lock" in line or "mutex_unlock" in line or "signal" in line or "wait" in line or "End" in line:
				Region_Text.insert(count_src + insert_num, "tie")
				insert_num += 1
				
		print ("tie:", Region_Text)
		if "tie" in Region_Text:
			if "tie" in Region_Text[len(Region_Text)-1]:
				del Region_Text[len(Region_Text)-1]
			#print ("tie: ", Region_Text)
			Region_Text = " ".join(Region_Text)
			Region_Text = Region_Text.split('tie')
			if Region_Text[len(Region_Text)-1] == "":
				Region_Text.pop()
		print ("untie: ", Region_Text)
		########     update new lengh of each sublist(region)     ########
		for k in range(0, len(Region_Text)):
			if "R1" in Region_Text[k]:
				if  len(Region_Index) == 0:
					Region_Index.insert(0, k+1)
				else:
					del Region_Index[0]
					Region_Index.insert(0, k+1)
			elif "R2" in Region_Text[k]:
				if len(Region_Index) == 1:
					Region_length = k
					Region_Index.insert(1, k+1-Region_length)
				else:
					del Region_Index[1]
					Region_Index.insert(1, k+1-Region_length)
			elif "R3" in Region_Text[k]:
				if len(Region_Index) == 2:
					Region_length = k
					Region_Index.insert(2, k+1-Region_length)
				else:
					del Region_Index[2]
					Region_Index.insert(2, k+1-Region_length)
			elif "R4" in Region_Text[k]:
				if len(Region_Index) == 3:
					Region_length = k
					Region_Index.insert(3, k+1-Region_length)
				else:
					del Region_Index[3]
					Region_Index.insert(3, k+1-Region_length)
		#print (Region_Text[k])
		#print ("Region_Index: ", Region_Index)
		########     divide by index pointer     ########
		for length in Region_Index:
			multilist.append([Region_Text[k+count] for k in range(length)])
			count += length
		print ("Atomic: ", multilist)
		#count = 0
		### ready to enumerate ###
		t_StoE = time.time()
		t_analyze += t_StoE-t_analyzing

		new_order, old_order = (), ()
		inter_permutation = [l for l, group in enumerate(multilist) for j in range(len(group))]
		for new_order in itertools.permutations(inter_permutation):
			if new_order <= old_order:
				continue
			old_order = new_order
			iters = [iter(group) for group in multilist]
			for l in new_order:
				test = next(iters[l])
				permutation.append(test)
				testcase.write(test)
		file.close()
		testcase.close()
		t_EofE = time.time()
		t_enumerate += t_EofE-t_StoE 
		### end of enumeration ###

		while (p_count <= len(Region_Text)):
			if not permutation:
				#print ("Permutation is empty. ")
				break
			os.system('cp sample.c interleave-'+str(p_flag)+'.c')
			generating = open('interleave-'+str(p_flag)+'.c', 'a')
			generating.write(scrapbooking_klee.shared_data+'= '+scrapbooking_klee.ValidInputs[j-1]+'; \n')
			'''
			##########	Insert Valid Inputs here	##########
			if "[" in scrapbooking_klee.shared_data:
				continue
			else:
				generating.write("int "+scrapbooking_klee.shared_data+"="+scrapbooking_klee.ValidInputs[(i-1)*int(scrapbooking_klee.p_num)+j]+"; \n")
			##########
			'''	
			for m in range(0, len(Region_Text)):
				recording.append(permutation.pop())
				p_count += 1
			#if p_count == len(Region_Text):
			p_count = 0
			for n in range(len(Region_Text)-1, -1, -1):
				generating.write(recording[n])
			generating.write('printf("%d", '+scrapbooking_klee.shared_data+'); \n')
			generating.write("return 0; \n}")
			generating.close()

			#time.sleep(0.1)
			DL_filter = subprocess.getoutput('python DL_filter.py')
			#time.sleep(1)
			'''	
			print ("DL_filter: ", DL_filter)
			print ("\n")
			'''
			if "deadlock" in DL_filter and "inexistent" not in DL_filter:
				print ("now detect potential deadlock......")
				print ("===================================================================")
				print ("********Examining interleave", p_flag)
				print ("		 ", DL_filter)
				print ("===================================================================\n")
				#break
			#'''
			elif "inexistent" in DL_filter and "deadlock" not in DL_filter:
				print ("now exclude bug-unrelated interleaving......")
				print ("===================================================================")
				print ("********Examining interleave", p_flag)
				print ("skip the         ", DL_filter)
				print ("===================================================================\n")
			#'''
			else:
				print ("now detect potential data race......")
				os.system('gcc -w interleave-'+str(p_flag)+'.c -o interleave'+str(p_flag)+' -lpthread')
				exe_result = subprocess.getoutput('./interleave'+str(p_flag))
				if (exe_result not in states):
					if states:
						print ("===================================================================")
						print ("********Examining interleave", p_flag)
						print ("		We find a bug!	Error symbolic state: ", exe_result)
						print ("===================================================================\n")
					else:
						print ("===================================================================")
						print ("********Examining interleave", p_flag)
						print ("                It is the first new symbolic state: ", exe_result)
						print ("===================================================================\n")
					states.append(exe_result)
					dr_num += str(p_flag)
					dr_num += ", "	
					os.system('cp interleave-'+str(p_flag)+'.c exe_concurrent/interleaving-'+str(p_flag)+'_'+str(j)+'.c')
				else:
					states.append(exe_result)
					print ("=========================================")
					print ("********Examining interleave", p_flag)
					print ("The latest symbolic state: ", exe_result)
					print ("=========================================\n")
			p_flag += 1
			recording = []
		Region_Text = []
		Region_Index = []
		multilist = []
		states = []
		#dr_num = ""
		p_flag = 1
		count = 0
		### end of verification
		t_EofV = time.time()
		t_verify += t_EofV-t_EofE
		#os.system('rm interleave*')
t_end = time.time()
if len(states) > int(scrapbooking_klee.p_num):
	print ("\n===============================================")
	print ("Please check suspicious "+dr_num+" interleaving")
	print ("===============================================\n")

print ("===============================" )
print (" Total       :", t_end-t_start)
print ("------------------")
print (" Analsis     :", t_analyze)
print ("------------------")
print (" Enumeration :", t_enumerate)
print ("------------------")
print (" Verifation  :", t_verify)
print ("==============================" )

