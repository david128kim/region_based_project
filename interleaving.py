import os
#import commands
import subprocess
import string
import itertools
import time
from app_r1 import execution_path_r1
from app_r2 import execution_path_r2
import scrapbooking_source

interleaving, a, b, temp, old_order = [], [], [], [], ()
combination = {}
counter_t1, counter_t2, t1_insert_number, t2_insert_number = 0, 0, 0, 0
strthread1 = "SVA from thread 1: "
strthread2 = "SVA from thread 2: "
strmerge = "merge two thread function to main: "
strpermutation = "exhaustive representation of interleaving combination ...  "
strwrite = "generate feasible testcase: "

#test region
constraints = [[1, 2], [3, 4], [5, 6]]
recording, filetest, a_tie, b_tie = [] ,[], [], []
counter, path_amount, file_length, temp_exe_result = 0, 0, 0, 0

for k in range(1, scrapbooking_source.region_combination+1):
        #testcase = open('testcase'+str(k)+'.ll','w')
        testcase = open('testcase.ll','w')
        file = open('exe_concurrent/concurrent_program'+str(k)+'.ll')


#def extract_t1():
        counter_t1, t1_insert_number, a_tie, a = 0, 0, [], []
        insert_temp = 0
        for line in file:
                if "region1" not in line and "region2" not in line: #unnecessary prune
                        a.append(line)
                        counter_t1 += 1
                        if (("load" in line) or ("store" in line) or ("mutex" in line) or ("signal" in line)):
                                a.insert(counter_t1+insert_temp, "tie")
                                insert_temp += 1
                                t1_insert_number += 1
	
                elif "region2" in line:
                       break
        print ("a: ", a)
        a_tie = " ".join(a)
        a_tie = a_tie.split('tie')
        a_tie.pop()	
        print ("a_tie: ", a_tie)
        print ("a_tie_length: ", len(a_tie))

#def extract_t2():
        counter_t2, t2_insert_number, b_tie, b = 0, 0, [], []	
        insert_temp = 0
        for line in file:
                b.append(line)
                counter_t2 += 1
                if (("load" in line) or ("store" in line)) or ("mutex" in line) or ("signal" in line):
                        b.insert(counter_t2+insert_temp, "tie")
                        insert_temp += 1
                        t2_insert_number += 1
			#print strthread2
			#print b
                elif "main" in line:
                        break
	
        print ("b: ", b)
        b_tie = " ".join(b)
        b_tie = b_tie.split('tie')
        b_tie.pop()
        print ("b_tie: ", b_tie)
        print ("b_tie length: ", len(b_tie))

        print ("##################################################################")


#for k in range(1, region_combination+1):
	#testcase = open('testcase'+str(k)+'.ll','w')
	#file = open('exe_concurrent/concurrent_program'+str(k)+'.ll')
	
	#extract_t1()
	#extract_t2()

	#	divide to two sublist. depends on list length
        if(len(a_tie) >= len(b_tie)):
                combination = a_tie + b_tie
                interleaving = [combination[i:i+len(a_tie)] for i in range(0, len(combination), len(a_tie))]
                print ("interleaving: ", interleaving)
        else:
                combination = b_tie + a_tie
                interleaving =  [combination[i:i+len(b_tie)] for i in range(0, len(combination), len(b_tie))]
                print ("interleaving: ", interleaving)

	#	list permutation
        print (strpermutation)
        new_order, old_order = (), ()
        inter_permutation = [i for i, group in enumerate(interleaving) for j in range(len(group))]
        for new_order in itertools.permutations(inter_permutation):
                if new_order <= old_order:
                        continue
                old_order = new_order
                iters = [iter(group) for group in interleaving]
                for i in new_order:
                        test = next(iters[i])
                        testcase.write(test)
        file.close()
        testcase.close()

        print ("##################################################################")
	#file = open('testcase'+str(k)+'.ll')
        file = open('testcase.ll')
        flag = 1
        for line in file:
                 temp.append(line)
	#print temp
        temp.pop()
	#print "temp_length: ", len(temp)
        file_length =  len(temp)
        file.close()
	
        path_amount = file_length/(len(a)+len(b)-t1_insert_number-t2_insert_number)
        print ("total path amount: ", file_length/(len(a)+len(b)-t1_insert_number-t2_insert_number))

        while(counter < file_length):
                generating = open('answer.ll', 'w')
                for i in range(0,len(a)+len(b)-t1_insert_number-t2_insert_number):
                        recording.append(temp.pop())
                        counter += 1
                if counter == (len(a)+len(b)-t1_insert_number-t2_insert_number):
                        counter = 0
		
                for i in range(len(a)+len(b)-t1_insert_number-t2_insert_number-1, -1, -1):
                        generating.write(recording[i])
                generating.close()
                os.system('python scrapbooking_IR.py')
                os.system('llvm-as answer_ok.ll -o answer_ok.bc')
                os.chdir('/home/klee/')
                os.system('cp region_based/answer_ok.bc .')
                os.system('klee --libc=uclibc --posix-runtime answer_ok.bc')
                os.system('klee answer_ok.bc')
                os.system('ktest-tool --write-ints klee-last/test000001.ktest')
                os.system('export LD_LIBRARY_PATH=klee_build/klee/Release+Asserts/lib/:$LD_LIBRARY_PATH')
                os.system('cp region_based/answer_ok.ll .')
                os.system('llc -O3 -march=x86-64 answer_ok.ll -o answer_ok.s')
                os.system('gcc -L klee_build/klee/Release+Asserts/lib/ -o answer_ok answer_ok.s -lpthread -lkleeRuntest')
                os.system('KTEST_FILE=klee-last/test000001.ktest ./answer_ok')
                exe_result = subprocess.getoutput('echo $?')
                print ("result: ", exe_result)
		
		#os.system('llc -O3 -march=x86-64 answer_ok.ll -o answer_ok.s')
        	#os.system('gcc -o answer_ok answer_ok.s -lpthread')
        	#os.system('./answer_ok')
		#exe_result = commands.getoutput('./answer_ok')
		#temp_result = exe_result
                
                if (flag > 1) and (temp_result != exe_result):
                        print ("We find a bug!")
                        break
                else:
                        temp_result = exe_result
		
		#if "failed" in exe_result:
			#break

                #os.system('rm -r klee-last && rm -r klee-out* && rm answer*')
                os.chdir('/home/klee/region_based')
                #os.system('rm answer*')

                flag += 1
                recording = []
                file_length -= (len(a)+len(b)-t1_insert_number-t2_insert_number)
                print ("verifying path",flag-1)
	#os.system('mv testcase'+str(k)+'.ll testcase_set/')
        os.system('rm testcase.ll')	
