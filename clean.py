import os

os.system('rm answer*')
os.system('rm exe_r*')
os.system('rm r1_path*')
os.system('rm r2_path*')
os.system('rm interleave*')
os.system('rm region1_klee*')
os.system('rm region2_klee*')
os.system('cd exe_IR && rm r*')
os.system('cd exe_concurrent && rm c*')
os.system('cd exe_source && rm exe_r* && rm region*')
os.system('rm whole*')
os.system('rm -r klee-out-*')
os.system('cd program && rm path* && rm e*')
