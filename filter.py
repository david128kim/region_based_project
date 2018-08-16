import os
import subprocess

filter_phi = []
counter_line = 0

file = open('answer_ok.ll', 'r')

for line in file:
	counter_line += 1
	temp_split = line.split()
	if ("br" in line) and temp_split[1] == "label":
		filter_phi.append(counter_line)
	elif "phi" in line:
		if counter_line - 1 in filter_phi:
			print ("inexistent enumeration")
