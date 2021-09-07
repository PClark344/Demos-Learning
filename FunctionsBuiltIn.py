import math
from math import sqrt
import os
import random

# math functions

print('Pi = ',math.pi)
print('e = ',math.e)
print('Ceiling of 8.1 = ',math.ceil(8.1))
print('Floor of 8.1 = ',math.ceil(8.1))
print('2 to power of 4 = ',math.pow(2,4))
print('Sqr root of 8 = ',sqrt(8))

# os functions

path = os.environ['PATH']
print('system path = ',path)

curr_dir = os.getcwd()
print('Current dir path = ',curr_dir)
#print('DICT OF ENVIRONMENT VARIABLES = ',os.environ)

user = os.environ['USER']
print('user = ',user)

curr_files = os.listdir(curr_dir)
print('Current dir files = ',curr_files)

cmd = os.mkdir('testdir')
print('Creating dir testdir')

cmd = os.rename('testdir','newtestdir')
print('renaming dir testdir')

# random functions

