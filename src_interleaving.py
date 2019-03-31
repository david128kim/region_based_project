import os
import subprocess
import itertools
import scrapbooking_klee

########       	global initialization section
Region_Text, multilist, permutation, recording, Region_Index = [], [], [], [], []
count, p_count, p_flag, count_src, insert_num, Region_length = 0, 0, 1, 0, 0, 0
########	testing info.
print ("I_num: ", scrapbooking_klee.I_num)
print ("p_num: ", scrapbooking_klee.p_num)
print ("Valid-INPUT: ", scrapbooking_klee.ValidInputs)
print ("INPUT-index: ", scrapbooking_klee.Inputs_Index)
########
for i in range(1, int(scrapbooking_klee.num_region)+1):
	if int(scrapbooking_klee.I_num) < i:
		break
	for j in range(1, int(scrapbooking_klee.p_num)+1):
		testcase = open('testcase.c','w')
		file = open('exe_concurrent/concurrent_'+str(i)+'_'+str(j)+'.c', 'r')
		for line in file:
			Region_Text.append(line)
			count_src += 1
			if "mutex_lock" in line or "mutex_unlock" in line or "signal" in line or "wait" in line:
				Region_Text.insert(count_src + insert_num, "tie")
				insert_num += 1
		if "tie" in Region_Text:
			if "tie" in Region_Text[len(Region_Text)-1]:
				del Region_Text[len(Region_Text)-1]
			print ("tie: ", Region_Text)
			Region_Text = " ".join(Region_Text)
			Region_Text = Region_Text.split('tie')
			if Region_Text[len(Region_Text)-1] == "":
				Region_Text.pop()
		print ("atomic: ", Region_Text)
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
		print ("multi-list: ", multilist)
		new_order, old_order = (), ()
		inter_permutation = [i for i, group in enumerate(multilist) for j in range(len(group))]
		for new_order in itertools.permutations(inter_permutation):
			if new_order <= old_order:
				continue
			old_order = new_order
			iters = [iter(group) for group in multilist]
			for i in new_order:
				test = next(iters[i])
				permutation.append(test)
				testcase.write(test)
		file.close()
		testcase.close()
		while (p_count <= len(Region_Text)):
			if not permutation:
				print ("Permutation is empty. ")
				break
			os.system('cp sample.c interleave'+str(p_flag)+'.c')
			generating = open('interleave'+str(p_flag)+'.c', 'a')
			'''
			##########	Insert Valid Inputs here	##########
			if "[" in scrapbooking_klee.shared_data:
				continue
			else:
				generating.write("int "+scrapbooking_klee.shared_data+"="+scrapbooking_klee.ValidInputs[(i-1)*int(scrapbooking_klee.p_num)+j]+"; \n")
			##########
			'''	
			for i in range(0, len(Region_Text)):
				recording.append(permutation.pop())
				p_count += 1
			#if p_count == len(Region_Text):
			p_count = 0
			for i in range(len(Region_Text)-1, -1, -1):
				generating.write(recording[i])
			generating.write('printf("%d", '+scrapbooking_klee.shared_data+'); \n')
			generating.write("return 0; \n}")
			generating.close()
			os.system('gcc interleave'+str(p_flag)+'.c -o interleave'+str(p_flag)+' -lpthread')
			exe_result = subprocess.getoutput('./interleave'+str(p_flag))
			if (p_flag > 1) and (prev_result != exe_result):
				print ("We find a bug! \n Error state: ", exe_result)
				break
			else:
				prev_result = exe_result
				print ("The latest state: ", prev_result)
			p_flag += 1
			recording = []	
		Region_Text = []
		
