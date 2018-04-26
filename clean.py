import os

os.system('cd exe_IR && rm e*')
os.system('cd exe_concurrent && rm c*')
os.system('cd exe_source && rm e*')
os.system('rm whole*')
os.system('rm -r klee-out-*')
