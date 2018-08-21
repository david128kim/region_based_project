import os
import subprocess

sig_wait = []
#counter_line = 0

file = open('answer.ll', 'r')

for line in file:
	#counter_line += 1
	temp_split = line.split()
	if "pthread_cond_wait" in line:			#########       %6 = tail call i32 @pthread_cond_wait(%union.pthread_cond_t* nonnull @empty, %union.pthread_mutex_t* nonnull @m) #3
		sig_wait.append(temp_split[7].lstrip('@').rstrip(','))
		#print ("wait: ", sig_wait)
	elif "pthread_cond_signal" in line:		#########       %11 = tail call i32 @pthread_cond_signal(%union.pthread_cond_t* nonnull @full) #3
		#print (temp_split[7].lstrip('@').rstrip(')'))
		if temp_split[7].lstrip('@').rstrip(')') in sig_wait:
			sig_wait.remove(temp_split[7].lstrip('@').rstrip(')'))
			#print ("signal: ", sig_wait)
		else: 
			print ("deadlock: condition variable order violation. ")
			break
