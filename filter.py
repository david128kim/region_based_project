import os
import subprocess

ins, sig_wait, lock_usage = [], [], []
cir_wait = 0

file = open('answer.ll', 'r')

for line in file:
	ins.append(line) 
	temp_split = line.split()
	'''
	if ";R2" in ins[0]:
		print ("wrong data dependency")
		break
	'''
	#else:
	if "pthread_cond_wait" in line:			#########       %6 = tail call i32 @pthread_cond_wait(%union.pthread_cond_t* nonnull @empty, %union.pthread_mutex_t* nonnull @m) #3 ;R?
		sig_wait.append(temp_split[7].lstrip('@').rstrip(','))
	elif "pthread_cond_signal" in line:		#########       %11 = tail call i32 @pthread_cond_signal(%union.pthread_cond_t* nonnull @full) #3 ;R?
		if temp_split[7].lstrip('@').rstrip(')') in sig_wait:
			sig_wait.remove(temp_split[7].lstrip('@').rstrip(')'))
#		else: 
#			print ("deadlock: condition variable order violation. ")
#			break
	
	elif "mutex_lock" in line:
#type 1:
#type 2: %9 = call i32 @pthread_mutex_lock(%union.pthread_mutex_t* %8) #5

		if temp_split[len(lock_split)-3].lstrip('@').rstrip(')') in lock_usage:
			'''
			print ("deadlock: circular waitting same lock. ")
			break
			'''
			#cir_wait += 1
			#if cir_wait > 1:
			#print ("deadlock: circular waitting same lock. ")
		
			if len(lock_usage) >= 2:
				#cir_wait += 1
				#if cir_wait > 1:
				print ("deadlock: circular waitting same lock. ")	
				break
			
			else:
				print ("inexistent enumeration")
			
		else:
			lock_usage.append(temp_split[len(lock_split)-3].lstrip('@').rstrip(')'))
			#print ("lock usage: ", lock_usage)
	elif "mutex_unlock" in line:
		if temp_split[len(lock_split)-3].lstrip('@').rstrip(')') in lock_usage:
			lock_usage.remove(temp_split[len(lock_split)-3].lstrip('@').rstrip(')'))
			#cir_wait -= 1
		'''
		else:
			print ("wrong lock match")
			break
		'''
	else:
		continue
file.close()
'''
for i in range(0, len(ins)):
	temp_split = ins[i]
	if "pthread_cond_wait" in ins[i]:
		temp_region = temp_split[9]
		if temp_region in ins[i+1]:
			print ("inexistent enumeration (wait)")
			break
'''
if (len(sig_wait) > 0):
	print ("deadlock: condition variable order violation. ")
'''
if len(lock_usage) > 0:
	print ("error: incomplete lock usage. ")
'''
