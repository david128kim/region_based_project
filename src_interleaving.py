import os
import subprocess
import itertools
import scrapbooking_klee

########       	global initialization section
Region_Text, multilist, permutation, recording = [], [], [], []
count, p_count, p_flag = 0, 0, 0
########	testing info.
print ("I_num: ", scrapbooking_klee.I_num)
print ("p_num: ", scrapbooking_klee.p_num)
########
for i in range(1, int(scrapbooking_klee.num_region)+1):
	if int(scrapbooking_klee.I_num) < i:
		break
	for j in range(1, int(scrapbooking_klee.p_num)+1):
		testcase = open('testcase.c','w')
		file = open('exe_concurrent/concurrent_'+str(i)+'_'+str(j)+'.c', 'r')
		for line in file:
			Region_Text.append(line)
		for length in scrapbooking_klee.Region_Index:
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
			os.system('cp sample.c interleaving'+str(p_flag)+'.c')
			generating = open('interleaving'+str(p_flag)+'.c', 'a')
			for i in range(0, len(Region_Text)):
				recording.append(permutation.pop())
				p_count += 1
			if p_count == len(Region_Text):
				p_count = 0
			for i in range(len(Region_Text)-1, -1, -1):
				generating.write(recording[i])
			generating.write("printf("+scrapbooking_klee.shared_data+"); \n")
			generating.write("return 0; \n}")
			generating.close()
			p_flag += 1
			recording = []	
		Region_Text = []
		
