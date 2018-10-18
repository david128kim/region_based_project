import os

os.system('rm answer*')
os.system('rm exe_r*')
os.system('cd exe_IR && rm e*')
os.system('cd exe_concurrent && rm c*')
os.system('cd exe_source && rm exe_r* && rm region*')
os.system('rm whole*')
os.system('rm -r klee-out-*')
os.system('cd program && rm path* && rm e*')
