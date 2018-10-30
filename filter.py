import os
import subprocess

ins, sig_wait, lock_usage, length = [], [], [], []
cir_wait, check_cond_to_end = 0, 0
condition = ""

file = open('answer.ll', 'r')
for line in file:
	length.append(line)
file.close()

file = open('answer.ll', 'r')

for line in file:
	ins.append(line) 
	temp_split = line.split()
	if "pthread_cond_wait" in line:			#########       %6 = tail call i32 @pthread_cond_wait(%union.pthread_cond_t* nonnull @empty, %union.pthread_mutex_t* nonnull @m) #3 ;R?
		sig_wait.append(temp_split[7].lstrip('@').rstrip(','))
		
		#if temp_split[len(temp_split)-3].lstrip('@').rstrip(')') in lock_usage:
			#lock_usage.remove(temp_split[len(temp_split)-3].lstrip('@').rstrip(')'))
		
		if condition == "":
			condition = temp_split[len(temp_split)-1]
		else:
			print ("1. wait: inexistent enumeration")
			break
		
	elif "pthread_cond_signal" in line:		#########       %11 = tail call i32 @pthread_cond_signal(%union.pthread_cond_t* nonnull @full) #3 ;R?
		if temp_split[7].lstrip('@').rstrip(')') in sig_wait:
			sig_wait.remove(temp_split[7].lstrip('@').rstrip(')'))
			condition = ""
			check_cond_to_end = 0
		
		if condition != "":
			if condition not in line:
				continue
			else:
				check_cond_to_end = 1
				if len(length) == len(ins):
					check_cond_to_end = 0
		
	elif "mutex_lock" in line:			########	type 2: %9 = call i32 @pthread_mutex_lock(%union.pthread_mutex_t* %8) #5
		if temp_split[len(temp_split)-3].lstrip('@').rstrip(')') in lock_usage:
			if len(lock_usage) >= 2:
				print ("deadlock: circular waitting same lock. ")	
				break
			
			else:
				print ("2. lock: inexistent enumeration")
				break
			
		else:
			lock_usage.append(temp_split[len(temp_split)-3].lstrip('@').rstrip(')'))
			#print ("lock usage: ", lock_usage)
	elif "mutex_unlock" in line:
		if temp_split[len(temp_split)-3].lstrip('@').rstrip(')') in lock_usage:
			lock_usage.remove(temp_split[len(temp_split)-3].lstrip('@').rstrip(')'))
		
		if condition != "":
			if condition not in line:
				continue
			else:
				check_cond_to_end = 1
				if len(length) == len(ins):
					check_cond_to_end = 0
		
	else:
		
		if condition != "":
			if condition not in line:
				continue
			else:   #### too early to check condition
				#print ("3. normal op.: inexistent enumeration")
				#break
				check_cond_to_end = 1
				if len(length) == len(ins):
					check_cond_to_end = 0
		
		continue
	#print (line)
	#print (sig_wait)
file.close()
#if ";R2" in ins[0]:
	#print ("different thread order")
#else:
if check_cond_to_end == 1:
	print ("3. normal op.: inexistent enumeration")
else:
	if (len(sig_wait) > 0):
		print ("deadlock: condition variable order violation. ")
'''
if len(lock_usage) > 0:
	print ("error: incomplete lock usage. ")
'''
