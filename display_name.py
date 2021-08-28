import os, glob

os.chdir('/home/akk/Music/')
for file in glob.glob('*.py'):
    print(file)
    
    
# Fibonacci Sequence
# a, b = 0, 1
# for i in xrange(0, 10):
#     print(a)
#     a, b = b, a + b
