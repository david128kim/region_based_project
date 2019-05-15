import os
import subprocess
#from src_interleaving import p_flag
#import src_interleaving
ins, sig_wait, lock_usage, length = [], [], [], []
cir_wait, check_cond_to_end = 0, 0
condition, region_num = "", ""

interleaving = subprocess.getoutput('find -name "interleave-*" -type f |wc -l')
#print ("interleaving: ", interleaving)
#file = open('interleave-1.c', 'r')
file = open('interleave-'+str(interleaving)+'.c', 'r')
for line in file:
	length.append(line)
file.close()
#file = open('interleave-1.c', 'r')
file = open('interleave-'+str(interleaving)+'.c', 'r')

for line in file:
	ins.append(line) 
	temp_split = line.split()
	#print ("lock_usage: ", lock_usage)
	#print ("sig_wait: ", sig_wait)
	if "cond_wait" in line:			#########      pthread_mutex_unlock(&m);	// cond_wait &full R2
		if temp_split[0].lstrip('pthread_mutex_unlock(').rstrip(');') in lock_usage:
			lock_usage.remove(temp_split[0].lstrip('pthread_mutex_unlock(').rstrip(');'))
		'''
		else:
			print ("4. error lock releasing")
		'''
		sig_wait.append(temp_split[3])
		region_num = temp_split[len(temp_split)-1]
		'''
		if condition == "":
			condition = temp_split[len(temp_split)-1]
		else:
			print ("1. wait: inexistent enumeration")
			break
		'''
	elif "pthread_cond_signal" in line:		#########       %11 = tail call i32 @pthread_cond_signal(%union.pthread_cond_t* nonnull @full) #3 ;R?
		if temp_split[0].lstrip('pthread_cond_signal(').rstrip(');') in sig_wait:
			sig_wait.remove(temp_split[0].lstrip('pthread_cond_signal(').rstrip(');'))
			#region_num = ""
		#else:	
			#if region_num != "":
				#print ("1. wait: inexistent enumeration")
				#break
			#region_num = ""
			#condition = ""
			#check_cond_to_end = 0
		#print (temp_split[len(temp_split)-1].lstrip('//'))
		'''	
		if region_num in temp_split[len(temp_split)-1] and sig_wait:
			print ("1. wait: inexistent enumeration")
			#### only for avoiding the last branch: if sig_wait: => not good ####
			#sig_wait = []
			####
			break
		else:
			region_num = ""
		'''
		'''
		if condition != "":
			if condition not in line:
				continue
			else:
				check_cond_to_end = 1
				if len(length) == len(ins):
					check_cond_to_end = 0
		'''
	elif "mutex_lock" in line:			########	type 2: %9 = call i32 @pthread_mutex_lock(%union.pthread_mutex_t* %8) #5
		if temp_split[0].lstrip('pthread_mutex_lock(').rstrip(');') in lock_usage:
			if len(lock_usage) >= 2:
				print ("deadlock: circular waitting same lock ", temp_split[0].lstrip('pthread_mutex_lock(&').rstrip(');'))	
				break
			
			else:
				print ("2. lock: inexistent enumeration")
				break
			
		else:
			lock_usage.append(temp_split[0].lstrip('pthread_mutex_lock(').rstrip(');'))
	elif "mutex_unlock" in line:
		if temp_split[0].lstrip('pthread_mutex_unlock(').rstrip(');') in lock_usage:
			lock_usage.remove(temp_split[0].lstrip('pthread_mutex_unlock(').rstrip(');'))
		'''
		if condition != "":
			if condition not in line:
				continue
			else:
				check_cond_to_end = 1
				if len(length) == len(ins):
					check_cond_to_end = 0
		'''
	else:
		'''
		if condition != "":
			if condition not in line:
				continue
			else:   #### too early to check condition
				#print ("3. normal op.: inexistent enumeration")
				#break
				check_cond_to_end = 1
				if len(length) == len(ins):
					check_cond_to_end = 0
		'''
		continue
	#print (line)
	#print ("SIG: ", sig_wait)
	#print ("region_num: ", region_num)
file.close()
#if ";R2" in ins[0]:
	#print ("different thread order")
#else:
'''
if check_cond_to_end == 1:
	print ("3. normal op.: inexistent enumeration")
else:
'''
if sig_wait:
	print ("deadlock: condition variable order violation. ")
'''
if len(lock_usage) > 0:
	print ("error: incomplete lock usage. ")
'''
