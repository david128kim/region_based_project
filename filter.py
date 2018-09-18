import os
import subprocess

sig_wait, lock_usage = [], []

file = open('answer.ll', 'r')

for line in file:
	temp_split = line.split()
	if "pthread_cond_wait" in line:			#########       %6 = tail call i32 @pthread_cond_wait(%union.pthread_cond_t* nonnull @empty, %union.pthread_mutex_t* nonnull @m) #3
		sig_wait.append(temp_split[7].lstrip('@').rstrip(','))
	elif "pthread_cond_signal" in line:		#########       %11 = tail call i32 @pthread_cond_signal(%union.pthread_cond_t* nonnull @full) #3
		if temp_split[7].lstrip('@').rstrip(')') in sig_wait:
			sig_wait.remove(temp_split[7].lstrip('@').rstrip(')'))
#		else: 
#			print ("deadlock: condition variable order violation. ")
#			break
	
	elif "mutex_lock" in line:
		if temp_split[7].lstrip('@').rstrip(')') in lock_usage:
			print ("deadlock: circular waitting same lock. ")
			break
		else:
			lock_usage.append(temp_split[7].lstrip('@').rstrip(')'))
			#print ("lock usage: ", lock_usage)
	elif "mutex_unlock" in line:
		if temp_split[7].lstrip('@').rstrip(')') in lock_usage:
			lock_usage.remove(temp_split[7].lstrip('@').rstrip(')'))
	
	else:
		continue
if len(sig_wait) > 0:
	print ("deadlock: condition variable order violation. ")
'''
if len(lock_usage) > 0:
	print ("error: incomplete lock usage. ")
'''
