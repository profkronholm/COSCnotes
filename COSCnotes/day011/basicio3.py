# basicio3.py
# 
# Bill Kronholm
# 2015
#
# Demonstrates some basic file input/output in python.
#

# this opens sample.txt for writing.
# If the file doesn't exist, it is created.
# If the file does exists, it is wiped of data and opened as an empty file.
myfile = open('sample.txt', 'a')
line1 = 'I want this text in my file.\n'
line2 = 'Followed by this line of text.\n'
myfile.write(line1)
myfile.write(line2)
myfile.close()

myfile = open('sample.txt', 'w')
line3 = 'But all I get is this.\n'
myfile.write(line3)
myfile.close()

#myfile = open('sample.txt', 'a')
#line4 = 'Then, finally, this.\n'
#myfile.write(line4)
#myfile.close()
