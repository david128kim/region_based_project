import os
import subprocess
import string
import itertools
import time
import scrapbooking_klee

interleaving, a, b, temp, old_order = [], [], [], [], ()
combination = {}
counter_t1, counter_t2, t1_insert_number, t2_insert_number, end_tie = 0, 0, 0, 0, 0
strthread1 = "SVA from thread 1: "
strthread2 = "SVA from thread 2: "
strmerge = "merge two thread function to main: "
strpermutation = "exhaustive representation of interleaving combination ...  "
strwrite = "generate feasible testcase: "

#test region
constraints = [[1, 2], [3, 4], [5, 6]]
recording, filetest, a_tie, b_tie = [] ,[], [], []
counter, path_amount, file_length, temp_exe_result, counter_DL, HasOrder = 0, 0, 0, 0, 0, 0
lock_name, lock_1st = "", ""
'''
for i in range(0, int(scrapbooking_klee.num_region)):
        file = open('exe_IR/exe_r'+str(i+1)+'.ll')
        for line in file:
                lock_split = line.split()
                if "mutex_lock" in line and (lock_1st == ""):
                        print ("length: ", len(lock_split)-2)
                        print (lock_split[len(lock_split)-2])
                        lock_1st = lock_split[len(lock_split)-2]
                        break
                elif "mutex_lock" in line and (lock_1st != ""):
                        if lock_1st == lock_split[len(lock_split)-2]:
                                HasOrder = 1
                        else:
                                HasOrder = 0
                        break
        file.close()
print ("Order?: ", HasOrder)
'''

for k in range(1, 2):
        #testcase = open('testcase'+str(k)+'.ll','w')
        testcase = open('testcase.ll','w')
        file = open('exe_concurrent/concurrent_program.ll')
#def extract_t1():
        counter_t1, t1_insert_number, a_tie, a = 0, 0, [], []
        insert_temp = 0
        for line in file:
                if "region1" not in line and "region2" not in line and "printf" not in line and "llvm.lifetime" not in line: #unnecessary prune
                        a.append(line)
                        counter_t1 += 1
                        temp_split = line.split()
                        #if ("mutex" in line) or ("signal" in line) or ("wait" in line):
                        #if (("load" in line or "store" in line) and scrapbooking_klee.shared_data in line):	
                        #if (("load" in line or "store" in line) and scrapbooking_klee.shared_data in line) or ("mutex" in line) or ("signal" in line):
                        #if ("mutex_unlock" in line) or ("signal" in line) or ("wait" in line):
                        if HasOrder == 1:
                                if "mutex_lock" in line:
                                        if lock_name == "":
                                                lock_name = temp_split[len(lock_split)-2]
                                                '''			
                                                if counter_t1+t1_insert_number-1 == 0:
                                                        continue
                                                else:
                                                        a.insert(counter_t1+t1_insert_number-1, "tie")
                                                        insert_temp += 1
                                                        t1_insert_number += 1
                                                        end_tie = counter_t1+t1_insert_number
                                                '''
                                        else:
                                                continue
                                elif "mutex_unlock" in line or ("signal" in line) or ("wait" in line):
                                        if "mutex_unlock" in line and temp_split[len(lock_split)-2] == lock_name:
                                                lock_name = ""
                                                a.insert(counter_t1+t1_insert_number, "tie")
                                                insert_temp += 1
                                                t1_insert_number += 1
                                                end_tie = counter_t1+t1_insert_number
                                        elif "mutex_unlock" in line and temp_split[len(lock_split)-2] != lock_name:
                                                continue
                                        else:
                                                a.insert(counter_t1+t1_insert_number, "tie")
                                                insert_temp += 1
                                                t1_insert_number += 1
                                                end_tie = counter_t1+t1_insert_number

                        else:
                                #if ("mutex_lock" in line) or ("mutex_unlock" in line) or ("signal" in line) or ("wait" in line):
                                #if "load" in line or "store" in line:
                                if "store" in line:
                                        a.insert(counter_t1+t1_insert_number, "tie")
                                        insert_temp += 1
                                        t1_insert_number += 1
                                        end_tie = counter_t1+t1_insert_number
                        '''
                                        a.insert(counter_t1+t1_insert_number, "tie")
                                        insert_temp += 1
                                        t1_insert_number += 1
                                        end_tie = counter_t1+t1_insert_number
                        '''
                elif "region2" in line:
                       break
        del a[end_tie-1]
        t1_insert_number -= 1
        print ("a: ", a)
        a_tie = " ".join(a)
        a_tie = a_tie.split('tie')
        if a_tie[len(a_tie)-1] == "":
                a_tie.pop()	
        print ("a_tie: ", a_tie)
        print ("a_tie_length: ", len(a_tie))

#def extract_t2():
        counter_t2, t2_insert_number, b_tie, b = 0, 0, [], []	
        insert_temp = 0
        for line in file:
                if "printf" not in line and "llvm.lifetime" not in line: #unnecessary prune	
                        b.append(line)
                        counter_t2 += 1
                        temp_split = line.split()
                        #if ("mutex" in line) or ("signal" in line) or ("wait" in line):
                        #if (("load" in line or "store" in line) and scrapbooking_klee.shared_data in line):
                        #if (("load" in line or "store" in line) and scrapbooking_klee.shared_data in line) or ("mutex" in line) or ("signal" in line):
                        #if ("mutex_unlock" in line) or ("signal" in line) or ("wait" in line):
                        if HasOrder == 1:
                                if "mutex_lock" in line:
                                        if lock_name == "":
                                                lock_name = temp_split[len(lock_split)-2]
                                                '''
                                                if counter_t2+t2_insert_number-1 == 0:
                                                        continue
                                                else:
                                                        b.insert(counter_t2+t2_insert_number-1, "tie")
                                                        insert_temp += 1
                                                        t2_insert_number += 1
                                                        end_tie = counter_t2+t2_insert_number
                                                '''
                                        else:
                                                continue
                                elif "mutex_unlock" in line or ("signal" in line) or ("wait" in line):
                                        if "mutex_unlock" in line and temp_split[len(lock_split)-2] == lock_name:
                                                lock_name = ""
                                                b.insert(counter_t2+t2_insert_number, "tie")
                                                insert_temp += 1
                                                t2_insert_number += 1
                                                end_tie = counter_t2+t2_insert_number
                                        elif "mutex_unlock" in line and temp_split[len(lock_split)-2] != lock_name:
                                                continue
                                        else:
                                                b.insert(counter_t2+t2_insert_number, "tie")
                                                insert_temp += 1
                                                t2_insert_number += 1
                                                end_tie = counter_t2+t2_insert_number
                        else:
                                #if ("mutex_lock" in line) or ("mutex_unlock" in line) or ("signal" in line) or ("wait" in line):
                                #if "load" in line or "store" in line:
                                if "store" in line:
                                        b.insert(counter_t2+t2_insert_number, "tie")
                                        insert_temp += 1
                                        t2_insert_number += 1
                                        end_tie = counter_t2+t2_insert_number
                        '''
                                b.insert(counter_t2+t2_insert_number, "tie")
                                insert_temp += 1
                                t2_insert_number += 1
                                end_tie = counter_t2+t2_insert_number
                        '''
        del b[end_tie-1]
        t2_insert_number -= 1
        #b.insert(len(b), "tie")
        print ("b: ", b)
        b_tie = " ".join(b)
        b_tie = b_tie.split('tie')
        if b_tie[len(b_tie)-1] == "":
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
                        #print (test)
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
        #temp.pop()
        print ("temp_length: ", len(temp))
        file_length =  len(temp)
        file.close()
        print ("a_l, b_l: ", len(a), len(b))
        print ("t1_i, t2_i: ", t1_insert_number, t2_insert_number)	
        path_amount = file_length/(len(a)+len(b)-t1_insert_number-t2_insert_number)
        print ("total path amount: ", file_length/(len(a)+len(b)-t1_insert_number-t2_insert_number))
####################################################################################################
#for i in range(1, len(scrapbooking_klee.ValidInputs)+1):
for i in range(1, 2):
	#while(counter < file_length):
	while(counter <= (len(a)+len(b)-t1_insert_number-t2_insert_number)):
		if not temp:
			print ("temp is empty. ")
			break
		generating = open('answer.ll', 'w')
		for i in range(0,len(a)+len(b)-t1_insert_number-t2_insert_number):
			#if not temp:
				#print ("temp is empty. ")
				#break
			#else:
			recording.append(temp.pop())
			counter += 1
		if counter == (len(a)+len(b)-t1_insert_number-t2_insert_number):
			counter = 0
		for i in range(len(a)+len(b)-t1_insert_number-t2_insert_number-1, -1, -1):
			#if "store" in recording[i] and scrapbooking_klee.shared_data not in recording[i]:
				#continue
			#else:
			generating.write(recording[i])
		#generating.write('  %4 = sext i32 %3 to i64 \n  %5 = inttoptr i64 %4 to i8* \n')
		#generating.write('  %6 = tail call i32 (i8*, ...)* @printf(i8* %5) #2 \n')
		#generating.write('  %7 = load i32* @Global, align 4, !tbaa !1 \n')
		#generating.write('  %4 = tail call i32 (i8*, ...)* @printf(i8* getelementptr inbounds ([3 x i8]* @.str, i64 0, i64 0), i32 %3) #2 \n  %5 = load i32* @Global, align 4, !tbaa !1 \n')
		generating.close()
		
		os.system('python scrapbooking_IR.py')
		
		temp_filter = subprocess.getoutput('python filter.py')
		if "deadlock" in temp_filter:
			counter_DL += 1
			print ("error "+str(flag)+" : "+str(temp_filter)+" accumulated error: "+str(counter_DL))
			#continue
		else:
			temp_llc = subprocess.getoutput('llc -O3 -march=x86-64 answer_ok.ll -o answer_ok.s')
			if "error" in temp_llc:
				print ("error at number of file, and its cause: ", flag, temp_llc)
				break
			
		
		os.system('llc -O3 -march=x86-64 answer_ok.ll -o answer_ok.s')
		os.system('gcc -o answer_ok answer_ok.s -lpthread')
		#os.system('timeout 3 ./answer_ok')
		exe_result = subprocess.getoutput('timeout 0.1 ./answer_ok \n')
		os.system('cp answer.ll answer_'+str(flag)+'.ll')
		os.system('cp answer_ok.ll answer_ok_'+str(flag)+'.ll')
		#exe_result = subprocess.getoutput('./answer_ok \n')
		#temp_result = exe_result
		if (flag > 1) and (temp_result != exe_result):
			print ("now: ", exe_result)
			print ("We find a bug!")
			break
		else:
			temp_result = exe_result
			print ("last: ", temp_result)
		#os.system('rm -r klee-last && rm -r klee-out-* && rm answer*')
		
		flag += 1
		recording = []
		file_length -= (len(a)+len(b)-t1_insert_number-t2_insert_number)
		print ("verifying path",flag-1)
	#os.system('rm testcase.ll')
print ("deadlock(DL) number: ", counter_DL)
